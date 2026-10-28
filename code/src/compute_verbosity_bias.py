import csv
from pathlib import Path

from scipy.stats import spearmanr

from compute_kappa import parse_annotation


MAX_CHARS = 12000

DIMENSIONS = [
    "D1_installation",
    "D2_usage",
    "D3_purpose",
    "D4_dependencies",
    "D5_examples",
    "D6_contribution",
]

README_VARIANTS = (
    "README.md",
    "README.rst",
    "README.txt",
    "README",
)


def find_readme(repo_dir):
    for name in README_VARIANTS:
        path = repo_dir / name
        if path.exists():
            return path
    return None


def load_ground_truth(ground_truth_dir):
    data = {}

    for repo_dir in sorted(Path(ground_truth_dir).iterdir()):
        if not repo_dir.is_dir():
            continue

        annotation_path = repo_dir / "annotation.md"
        if not annotation_path.exists():
            continue

        scores = parse_annotation(annotation_path)

        readme_path = find_readme(repo_dir)

        if readme_path is None:
            readme_text = ""
        else:
            readme_text = readme_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        original_chars = len(readme_text)
        effective_text = readme_text[:MAX_CHARS]

        data[repo_dir.name] = {
            "scores": scores,
            "original_chars": original_chars,
            "effective_chars": len(effective_text),
            "original_words": len(readme_text.split()),
            "effective_words": len(effective_text.split()),
            "truncated": original_chars > MAX_CHARS,
        }

    return data


def load_llm_scores(csv_path):
    scores = {}

    with open(
        csv_path,
        newline="",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            scores[row["repo"]] = row

    return scores


def compute_spearman(x_values, y_values):
    rho, p_value = spearmanr(
        x_values,
        y_values,
    )

    return float(rho), float(p_value)


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parents[2]

    ground_truth_dir = (
        project_root
        / "data"
        / "ground_truth"
    )

    llm_csv = (
        project_root
        / "data"
        / "results"
        / "llm_scores_ground_truth.csv"
    )

    detail_output = (
        project_root
        / "data"
        / "results"
        / "verbosity_bias_details.csv"
    )

    summary_output = (
        project_root
        / "data"
        / "results"
        / "verbosity_bias_summary.csv"
    )

    ground_truth = load_ground_truth(
        ground_truth_dir
    )

    llm_scores = load_llm_scores(
        llm_csv
    )

    print(
        f"Loaded ground truth for "
        f"{len(ground_truth)} repos"
    )

    print(
        f"Loaded LLM scores for "
        f"{len(llm_scores)} repos\n"
    )

    detail_rows = []

    # -------------------------------------------------
    # Repository-level analysis
    # -------------------------------------------------

    for repo, repo_data in ground_truth.items():

        llm_row = llm_scores.get(repo)

        if llm_row is None:
            print(
                f"WARNING: no LLM result for {repo}"
            )
            continue

        human_scores = repo_data["scores"]

        human_total = sum(
            human_scores[dim]
            for dim in DIMENSIONS
            if human_scores.get(dim) is not None
        )

        llm_total = int(
            llm_row["llm_total"]
        )

        score_difference = (
            llm_total - human_total
        )

        detail_rows.append({
            "repo": repo,
            "human_total": human_total,
            "llm_total": llm_total,
            "score_difference": score_difference,
            "original_chars": repo_data["original_chars"],
            "effective_chars": repo_data["effective_chars"],
            "original_words": repo_data["original_words"],
            "effective_words": repo_data["effective_words"],
            "truncated": repo_data["truncated"],
        })

    print(
        f"Matched repositories: "
        f"{len(detail_rows)}"
    )

    truncated_count = sum(
        1
        for row in detail_rows
        if row["truncated"]
    )

    print(
        f"READMEs truncated at "
        f"{MAX_CHARS} characters: "
        f"{truncated_count}/{len(detail_rows)}\n"
    )

    score_differences = [
        row["score_difference"]
        for row in detail_rows
    ]

    repository_analyses = {}

    for measure in [
        "original_chars",
        "effective_chars",
        "original_words",
        "effective_words",
    ]:

        values = [
            row[measure]
            for row in detail_rows
        ]

        rho, p_value = compute_spearman(
            values,
            score_differences,
        )

        repository_analyses[measure] = {
            "rho": rho,
            "p_value": p_value,
        }

    print(
        "=== Repository-level verbosity analysis ===\n"
    )

    for measure, result in repository_analyses.items():

        print(
            f"{measure}: "
            f"rho={result['rho']:.3f}, "
            f"p={result['p_value']:.3f}"
        )

    # -------------------------------------------------
    # Per-dimension secondary analysis
    # -------------------------------------------------

    print(
        "\n=== Per-dimension verbosity analysis "
        "(effective README words) ===\n"
    )

    dimension_rows = []

    for dimension in DIMENSIONS:

        short = dimension.split("_")[0]
        score_col = f"{short}_score"

        lengths = []
        differences = []

        for repo, repo_data in ground_truth.items():

            llm_row = llm_scores.get(repo)

            if llm_row is None:
                continue

            human_score = (
                repo_data["scores"].get(
                    dimension
                )
            )

            if human_score is None:
                continue

            llm_score_raw = llm_row.get(
                score_col
            )

            if llm_score_raw is None:
                continue

            llm_score = int(
                llm_score_raw
            )

            difference = (
                llm_score - human_score
            )

            lengths.append(
                repo_data["effective_words"]
            )

            differences.append(
                difference
            )

        if len(lengths) < 3:
            print(
                f"{dimension}: too few observations"
            )
            continue

        rho, p_value = compute_spearman(
            lengths,
            differences,
        )

        print(
            f"{dimension}: "
            f"n={len(lengths)} "
            f"rho={rho:.3f}, "
            f"p={p_value:.3f}"
        )

        dimension_rows.append({
            "scope": "dimension",
            "dimension": dimension,
            "length_measure": "effective_words",
            "n": len(lengths),
            "rho": rho,
            "p_value": p_value,
        })

    # -------------------------------------------------
    # Save repository-level detail data
    # -------------------------------------------------

    detail_output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        detail_output,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        fieldnames = [
            "repo",
            "human_total",
            "llm_total",
            "score_difference",
            "original_chars",
            "effective_chars",
            "original_words",
            "effective_words",
            "truncated",
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(
            detail_rows
        )

    # -------------------------------------------------
    # Save summary results
    # -------------------------------------------------

    summary_rows = []

    for measure, result in repository_analyses.items():

        summary_rows.append({
            "scope": "repository",
            "dimension": "ALL",
            "length_measure": measure,
            "n": len(detail_rows),
            "rho": result["rho"],
            "p_value": result["p_value"],
        })

    summary_rows.extend(
        dimension_rows
    )

    with open(
        summary_output,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        fieldnames = [
            "scope",
            "dimension",
            "length_measure",
            "n",
            "rho",
            "p_value",
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(
            summary_rows
        )

    print(
        f"\nSaved repository details to: "
        f"{detail_output}"
    )

    print(
        f"Saved summary results to: "
        f"{summary_output}"
    )