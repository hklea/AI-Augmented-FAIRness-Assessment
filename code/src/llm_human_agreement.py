import argparse
import re
import csv
import math
import sys
from pathlib import Path

# models.py lives in code/web/backend, not next to this script — add that
# folder to the import path so "from models import ..." can find it.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "web" / "backend"))

from models import LLAMA, QWEN, MODELS, model_config, result_filename

DIMS = [
    "D1_installation",
    "D2_usage",
    "D3_purpose",
    "D4_dependencies",
    "D5_examples",
    "D6_contribution",
]

DIM_TO_LLM_COL = {
    "D1_installation": "D1_score",
    "D2_usage": "D2_score",
    "D3_purpose": "D3_score",
    "D4_dependencies": "D4_score",
    "D5_examples": "D5_score",
    "D6_contribution": "D6_score",
}

PILOT_REPOS = {
    "OpenMS_OpenMS",
    "astropy_astropy",
    "biopython_biopython",
    "healpy_healpy",
    "jupyter_nbconvert",
    "networkx_networkx",
    "nilearn_nilearn",
    "numpy_numpy",
    "scikit-learn_scikit-learn",
    "sunpy_sunpy",
}


def normalize_repo_id(repo_id):
    return repo_id.strip().replace("/", "_")


def parse_score(value):
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    try:
        score = int(float(value))
    except ValueError:
        return None
    return score if score in {0, 1, 2} else None


def parse_manual_annotation(filepath):
    text = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    scores = {}
    for dim in DIMS:
        short = dim.split("_")[0]
        match = re.search(rf"{short}_[^:]+:\s*([012])", text)
        scores[dim] = int(match.group(1)) if match else None
    return scores


def cohen_kappa_weighted(y1, y2, max_score=2):
    n = len(y1)
    if n == 0:
        return None
    categories = list(range(max_score + 1))
    k = len(categories)
    weights = [[1 - abs(i - j) / max_score for j in categories] for i in categories]
    counts = [[0] * k for _ in range(k)]
    for a, b in zip(y1, y2):
        counts[a][b] += 1
    row_totals = [sum(row) for row in counts]
    col_totals = [sum(counts[i][j] for i in range(k)) for j in range(k)]
    po = sum(weights[i][j] * counts[i][j]
             for i in range(k) for j in range(k)) / n
    pe = sum(weights[i][j] * row_totals[i] * col_totals[j]
             for i in range(k) for j in range(k)) / (n * n)
    if abs(1.0 - pe) < 1e-12:
        return None
    return (po - pe) / (1.0 - pe)


def sklearn_kappa_weighted(y1, y2):
    try:
        from sklearn.metrics import cohen_kappa_score
        return cohen_kappa_score(y1, y2, weights="linear")
    except ImportError:
        return None


def print_contingency(name, y_human, y_llm, labels=[0, 1, 2]):
    table = {a: {b: 0 for b in labels} for a in labels}
    for a, b in zip(y_human, y_llm):
        table[a][b] += 1
    print(f"\n{name} contingency (human=rows, LLM=cols):")
    print("          " + "  ".join(f"LLM={l}" for l in labels))
    for a in labels:
        print(f"Human={a}  " + "  ".join(f"{table[a][b]:5d}" for b in labels))


def run_agreement(ground_truth_dir, llm_csv_path, output_path, label="primary annotator",
                   exclude_repos=None, model_name=""):
    with open(llm_csv_path, encoding="utf-8") as f:
        llm_rows = {normalize_repo_id(r["repo"]): r for r in csv.DictReader(f)}

    repos = sorted([d.name for d in Path(ground_truth_dir).iterdir()
                    if d.is_dir() and not d.name.startswith(".")])
    if exclude_repos:
        repos = [r for r in repos if r not in exclude_repos]

    human_scores = {d: [] for d in DIMS}
    llm_scores = {d: [] for d in DIMS}
    repo_rows = []
    skipped = []

    for repo in repos:
        annotation_path = Path(ground_truth_dir) / repo / "annotation.md"
        if not annotation_path.exists():
            skipped.append((repo, "missing annotation"))
            continue
        if repo not in llm_rows:
            skipped.append((repo, "missing LLM row"))
            continue

        manual = parse_manual_annotation(annotation_path)
        llm = llm_rows[repo]

        row = {"repo": repo}
        for dim in DIMS:
            h = manual.get(dim)
            l = parse_score(llm.get(DIM_TO_LLM_COL[dim]))
            row[f"human_{dim}"] = h
            row[f"llm_{dim}"] = l
            row[f"diff_{dim}"] = (l - h) if h is not None and l is not None else None
            row[f"agree_{dim}"] = int(h == l) if h is not None and l is not None else None
            if h is not None and l is not None:
                human_scores[dim].append(h)
                llm_scores[dim].append(l)
        repo_rows.append(row)

    print(f"\n=== LLM ({model_name}) vs {label} ===")
    print(f"Compared {len(repo_rows)} repos, skipped {len(skipped)}")
    if skipped:
        for repo, reason in skipped:
            print(f"  Skipped {repo}: {reason}")

    print("\n--- Weighted Kappa per dimension ---")
    kappa_results = {}
    for dim in DIMS:
        y_h = human_scores[dim]
        y_l = llm_scores[dim]
        if len(y_h) < 2:
            continue
        exact = sum(1 for a, b in zip(y_h, y_l) if a == b) / len(y_h)
        mae = sum(abs(a - b) for a, b in zip(y_h, y_l)) / len(y_h)
        kappa = cohen_kappa_weighted(y_h, y_l)
        sk = sklearn_kappa_weighted(y_h, y_l)
        kappa_results[dim] = kappa
        kappa_str = f"{kappa:.3f}" if kappa is not None else "undefined"
        sk_str = f", sklearn={sk:.3f}" if sk is not None else ""
        print(f"  {dim}: Kappa={kappa_str}, Exact={exact:.3f}, "
              f"MAE={mae:.3f}{sk_str} (n={len(y_h)})")

        higher = sum(1 for a, b in zip(y_h, y_l) if b > a)
        lower = sum(1 for a, b in zip(y_h, y_l) if b < a)
        major = sum(1 for a, b in zip(y_h, y_l) if abs(a - b) == 2)
        print(f"    LLM higher={higher}, LLM lower={lower}, major diff={major}")

    valid_kappas = [v for v in kappa_results.values() if v is not None]
    if valid_kappas:
        print(f"\nMacro-avg LLM-Human Kappa: {sum(valid_kappas)/len(valid_kappas):.3f}")

    for dim in DIMS:
        print_contingency(dim, human_scores[dim], llm_scores[dim])

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if repo_rows:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=repo_rows[0].keys())
            writer.writeheader()
            writer.writerows(repo_rows)
        print(f"\nResults saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Compute LLM-vs-human agreement for a chosen model. "
                     "Run once per model (e.g. --model llama3.1:8b and again "
                     "--model Qwen3.6-35B-A3B-MLX-8bit) so each model's files "
                     "get their own correctly-suffixed output, instead of "
                     "maintaining a separate hardcoded script per model."
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()),
                         help="Model key as registered in models.py (e.g. llama3.1:8b or "
                              "Qwen3.6-35B-A3B-MLX-8bit).")
    args = parser.parse_args()

    model = args.model
    model_config(model)  # raises ValueError early if the model key is unknown

    project_root = Path(__file__).resolve().parents[2]
    llm_csv = project_root / "data" / "results" / result_filename("llm_scores_ground_truth", model)

    run_agreement(
        ground_truth_dir=project_root / "data" / "ground_truth",
        llm_csv_path=llm_csv,
        output_path=project_root / "data" / "results" / result_filename("llm_human_agreement_annotator1", model),
        label="primary annotator",
        model_name=model,
    )

    print("\n" + "=" * 60 + "\n")

    run_agreement(
        ground_truth_dir=project_root / "data" / "second_annotator" / "completed_annotations",
        llm_csv_path=llm_csv,
        output_path=project_root / "data" / "results" / result_filename("llm_human_agreement_annotator2", model),
        label="second annotator",
        model_name=model,
    )

    print("\n" + "=" * 60 + "\n")

    run_agreement(
        ground_truth_dir=project_root / "data" / "ground_truth",
        llm_csv_path=llm_csv,
        output_path=project_root / "data" / "results" / result_filename("llm_human_agreement_holdout", model),
        label="primary annotator (20-repo holdout)",
        exclude_repos=PILOT_REPOS,
        model_name=model,
    )


if __name__ == "__main__":
    main()
