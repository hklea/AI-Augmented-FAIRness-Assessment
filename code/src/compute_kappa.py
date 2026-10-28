import re
import csv
import math
import json
import argparse
from pathlib import Path


def parse_annotation(filepath):
    text = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    scores = {}
    for indicator in ["F1_persistent_id", "F2_metadata_file", "A1_license",
                      "I1_dependency_file", "R1_readme_present", "R2_citation"]:
        match = re.search(rf"{indicator}:\s*([01])", text)
        scores[indicator] = int(match.group(1)) if match else None
    for dim in ["D1_installation", "D2_usage", "D3_purpose",
                "D4_dependencies", "D5_examples", "D6_contribution"]:
        short = dim.split("_")[0]
        match = re.search(rf"{short}_[^:]+:\s*([012])", text)
        scores[dim] = int(match.group(1)) if match else None
    return scores


def cohen_kappa_binary(y1, y2):
    n = len(y1)
    if n == 0:
        return None
    po = sum(1 for a, b in zip(y1, y2) if a == b) / n
    p1 = (sum(y1) / n) * (sum(y2) / n)
    p0 = ((n - sum(y1)) / n) * ((n - sum(y2)) / n)
    pe = p1 + p0
    if abs(1.0 - pe) < 1e-12:
        return None
    return (po - pe) / (1.0 - pe)


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


def print_contingency(name, y1, y2, labels):
    table = {a: {b: 0 for b in labels} for a in labels}
    for a, b in zip(y1, y2):
        table[a][b] += 1
    print(f"\n{name} contingency table (A1=rows, A2=cols):")
    print("       " + "  ".join(f"A2={l}" for l in labels))
    for a in labels:
        print(f"A1={a}  " + "  ".join(f"{table[a][b]:5d}" for b in labels))


def sklearn_kappa(y1, y2, weighted=False):
    try:
        from sklearn.metrics import cohen_kappa_score
        weights = "linear" if weighted else None
        return cohen_kappa_score(y1, y2, weights=weights)
    except ImportError:
        print("  sklearn not available — skipping cross-check")
        return None


def compute_agreement(annotator1_dir, annotator2_dir, output_path, diagnostics=False):
    repos = sorted([d.name for d in Path(annotator1_dir).iterdir()
                    if d.is_dir() and not d.name.startswith(".")])

    rule_indicators = ["F1_persistent_id", "F2_metadata_file", "A1_license",
                       "I1_dependency_file", "R1_readme_present", "R2_citation"]
    ai_dims = ["D1_installation", "D2_usage", "D3_purpose",
               "D4_dependencies", "D5_examples", "D6_contribution"]

    all1 = {k: [] for k in rule_indicators + ai_dims}
    all2 = {k: [] for k in rule_indicators + ai_dims}
    repo_data = {}
    repo_rows = []
    skipped = []

    for repo in repos:
        p1 = Path(annotator1_dir) / repo / "annotation.md"
        p2 = Path(annotator2_dir) / repo / "annotation.md"
        if not p1.exists() or not p2.exists():
            skipped.append(repo)
            continue
        s1 = parse_annotation(p1)
        s2 = parse_annotation(p2)
        repo_data[repo] = (s1, s2)

        row = {"repo": repo}
        for k in rule_indicators + ai_dims:
            score1 = s1.get(k)
            score2 = s2.get(k)
            row[f"annotator1_{k}"] = score1
            row[f"annotator2_{k}"] = score2
            row[f"agree_{k}"] = (
                int(score1 == score2)
                if score1 is not None and score2 is not None
                else None
            )
            if score1 is not None and score2 is not None:
                all1[k].append(score1)
                all2[k].append(score2)
        repo_rows.append(row)

    print(f"\nCompared {len(repo_rows)} repos, skipped {len(skipped)}")

    if diagnostics:
        print("\n--- Sample sizes per dimension ---")
        for k in rule_indicators + ai_dims:
            print(f"  {k}: n={len(all1[k])}")

        print_contingency("A1_license", all1["A1_license"],
                          all2["A1_license"], [0, 1])
        print_contingency("I1_dependency_file", all1["I1_dependency_file"],
                          all2["I1_dependency_file"], [0, 1])

        print("\nI1 disagreements:")
        for repo, (s1, s2) in repo_data.items():
            if s1.get("I1_dependency_file") != s2.get("I1_dependency_file"):
                fair_path = Path(annotator1_dir) / repo / "fair_file_checks.json"
                dep_files = []
                if fair_path.exists():
                    with fair_path.open(encoding="utf-8") as f:
                        checks = json.load(f)
                    dep_files = [fname for fname in [
                        "requirements.txt", "pyproject.toml", "environment.yml",
                        "setup.py", "Cargo.toml", "go.mod", "pom.xml",
                        "Project.toml", "package.json"] if checks.get(fname)]
                print(f"  {repo}: A1={s1['I1_dependency_file']}, "
                      f"A2={s2['I1_dependency_file']}, files={dep_files}")

    print("\n--- Rule-Based Indicators (Unweighted Kappa) ---")
    kappa_results = {}
    for ind in rule_indicators:
        y1, y2 = all1[ind], all2[ind]
        if len(y1) < 2:
            continue
        exact = sum(1 for a, b in zip(y1, y2) if a == b) / len(y1)
        kappa = cohen_kappa_binary(y1, y2)
        kappa_results[ind] = kappa
        sk = sklearn_kappa(y1, y2, weighted=False) if diagnostics else None
        if sk is None:
            sk_str = ""
        elif math.isnan(sk):
            sk_str = ", sklearn=undefined"
        else:
            sk_str = f", sklearn={sk:.3f}"
        kappa_str = f"{kappa:.3f}" if kappa is not None else "undefined"
        print(f"  {ind}: Kappa={kappa_str}, Exact={exact:.3f}{sk_str} (n={len(y1)})")

    print("\n--- AI-Based Dimensions (Weighted Kappa) ---")
    for dim in ai_dims:
        y1, y2 = all1[dim], all2[dim]
        if len(y1) < 2:
            continue
        exact = sum(1 for a, b in zip(y1, y2) if a == b) / len(y1)
        mae = sum(abs(a - b) for a, b in zip(y1, y2)) / len(y1)
        kappa = cohen_kappa_weighted(y1, y2)
        kappa_results[dim] = kappa
        sk = sklearn_kappa(y1, y2, weighted=True) if diagnostics else None
        if sk is None:
            sk_str = ""
        elif math.isnan(sk):
            sk_str = ", sklearn=undefined"
        else:
            sk_str = f", sklearn={sk:.3f}"
        kappa_str = f"{kappa:.3f}" if kappa is not None else "undefined"
        print(f"  {dim}: Kappa={kappa_str}, Exact={exact:.3f}, "
              f"MAE={mae:.3f}{sk_str} (n={len(y1)})")

    rule_kappas = [kappa_results[i] for i in rule_indicators
                   if kappa_results.get(i) is not None]
    ai_kappas = [kappa_results[d] for d in ai_dims
                 if kappa_results.get(d) is not None]
    print(f"\nMacro-avg Rule Kappa (defined only): {sum(rule_kappas)/len(rule_kappas):.3f}")
    print(f"Macro-avg AI Kappa: {sum(ai_kappas)/len(ai_kappas):.3f}")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if repo_rows:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=repo_rows[0].keys())
            writer.writeheader()
            writer.writerows(repo_rows)
        print(f"\nDetailed results saved to {output_path}")

    return kappa_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--diagnostics", action="store_true",
                        help="Print contingency tables and disagreement details")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[2]
    annotator1_dir = project_root / "data" / "ground_truth"
    annotator2_dir = project_root / "data" / "second_annotator" / "completed_annotations"
    output_path = project_root / "data" / "results" / "inter_annotator_agreement.csv"

    compute_agreement(annotator1_dir, annotator2_dir, output_path,
                      diagnostics=args.diagnostics)