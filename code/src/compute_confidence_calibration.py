import csv
from pathlib import Path

from compute_kappa import parse_annotation, cohen_kappa_weighted


DIMENSIONS = [
    "D1_installation",
    "D2_usage",
    "D3_purpose",
    "D4_dependencies",
    "D5_examples",
    "D6_contribution",
]

CONFIDENCE_LEVELS = ["HIGH", "MEDIUM", "LOW"]


def load_ground_truth(ground_truth_dir):
    gt = {}

    for repo_dir in sorted(Path(ground_truth_dir).iterdir()):
        if not repo_dir.is_dir():
            continue

        ann_path = repo_dir / "annotation.md"

        if not ann_path.exists():
            continue

        gt[repo_dir.name] = parse_annotation(ann_path)

    return gt


def load_llm_scores(csv_path):
    scores = {}

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            repo = row["repo"]
            scores[repo] = row

    return scores


def calculate_metrics(y_true, y_pred):
    n = len(y_true)

    if n == 0:
        return {
            "n": 0,
            "exact": None,
            "mae": None,
            "kappa": None,
        }

    exact = sum(
        1 for true, pred in zip(y_true, y_pred)
        if true == pred
    ) / n

    mae = sum(
        abs(true - pred)
        for true, pred in zip(y_true, y_pred)
    ) / n

    # Kappa is secondary here.
    # It may be unstable or undefined for very small
    # or highly imbalanced confidence groups.
    kappa = None

    if n >= 2:
        try:
            kappa = cohen_kappa_weighted(
                y_true,
                y_pred,
            )
        except Exception:
            kappa = None

    return {
        "n": n,
        "exact": exact,
        "mae": mae,
        "kappa": kappa,
    }


def compute_dimension_calibration(
    ground_truth,
    llm_scores,
    dimension,
):
    """
    Compute calibration separately for one dimension.

    Example:
    D1_installation uses:
      D1_score
      D1_confidence
    """

    short = dimension.split("_")[0]

    score_col = f"{short}_score"
    confidence_col = f"{short}_confidence"

    groups = {
        level: {
            "y_true": [],
            "y_pred": [],
        }
        for level in CONFIDENCE_LEVELS
    }

    for repo, gt_scores in ground_truth.items():

        y_true = gt_scores.get(dimension)
        llm_row = llm_scores.get(repo)

        if llm_row is None:
            continue

        if y_true is None:
            continue

        y_pred_raw = llm_row.get(score_col)
        confidence = llm_row.get(confidence_col)

        if not y_pred_raw:
            continue

        if confidence not in CONFIDENCE_LEVELS:
            continue

        y_pred = int(y_pred_raw)

        groups[confidence]["y_true"].append(
            y_true
        )

        groups[confidence]["y_pred"].append(
            y_pred
        )

    results = {}

    for level in CONFIDENCE_LEVELS:

        y_true = groups[level]["y_true"]
        y_pred = groups[level]["y_pred"]

        results[level] = calculate_metrics(
            y_true,
            y_pred,
        )

    return results


def compute_overall_calibration(
    ground_truth,
    llm_scores,
):
    """
    Pool predictions from all six dimensions and
    group them only by confidence level.

    Maximum possible observations:
    30 repositories x 6 dimensions = 180.
    """

    groups = {
        level: {
            "y_true": [],
            "y_pred": [],
        }
        for level in CONFIDENCE_LEVELS
    }

    for dimension in DIMENSIONS:

        short = dimension.split("_")[0]

        score_col = f"{short}_score"
        confidence_col = f"{short}_confidence"

        for repo, gt_scores in ground_truth.items():

            y_true = gt_scores.get(dimension)
            llm_row = llm_scores.get(repo)

            if llm_row is None:
                continue

            if y_true is None:
                continue

            y_pred_raw = llm_row.get(score_col)
            confidence = llm_row.get(
                confidence_col
            )

            if not y_pred_raw:
                continue

            if confidence not in CONFIDENCE_LEVELS:
                continue

            y_pred = int(y_pred_raw)

            groups[confidence]["y_true"].append(
                y_true
            )

            groups[confidence]["y_pred"].append(
                y_pred
            )

    results = {}

    for level in CONFIDENCE_LEVELS:

        y_true = groups[level]["y_true"]
        y_pred = groups[level]["y_pred"]

        results[level] = calculate_metrics(
            y_true,
            y_pred,
        )

    return results


def format_value(value):
    if value is None:
        return "undefined"

    return f"{value:.3f}"


if __name__ == "__main__":

    project_root = (
        Path(__file__).resolve().parents[2]
    )

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

    output_path = (
        project_root
        / "data"
        / "results"
        / "confidence_calibration.csv"
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

    rows = []

    # -------------------------------------------------
    # Per-dimension confidence calibration
    # -------------------------------------------------

    print(
        "=== Per-dimension confidence calibration ===\n"
    )

    for dimension in DIMENSIONS:

        print(f"--- {dimension} ---")

        results = compute_dimension_calibration(
            ground_truth,
            llm_scores,
            dimension,
        )

        for level in CONFIDENCE_LEVELS:

            result = results[level]

            print(
                f"  {level}: "
                f"n={result['n']} "
                f"Exact={format_value(result['exact'])} "
                f"MAE={format_value(result['mae'])} "
                f"Kappa={format_value(result['kappa'])}"
            )

            rows.append({
                "scope": "dimension",
                "dimension": dimension,
                "confidence": level,
                "n": result["n"],
                "exact": result["exact"],
                "mae": result["mae"],
                "kappa": result["kappa"],
            })

        print()

    # -------------------------------------------------
    # Overall pooled confidence calibration
    # -------------------------------------------------

    print(
        "=== Overall confidence calibration ===\n"
    )

    overall_results = compute_overall_calibration(
        ground_truth,
        llm_scores,
    )

    for level in CONFIDENCE_LEVELS:

        result = overall_results[level]

        print(
            f"{level}: "
            f"n={result['n']} "
            f"Exact={format_value(result['exact'])} "
            f"MAE={format_value(result['mae'])} "
            f"Kappa={format_value(result['kappa'])}"
        )

        rows.append({
            "scope": "overall",
            "dimension": "ALL",
            "confidence": level,
            "n": result["n"],
            "exact": result["exact"],
            "mae": result["mae"],
            "kappa": result["kappa"],
        })

    # -------------------------------------------------
    # Save results
    # -------------------------------------------------

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as f:

        fieldnames = [
            "scope",
            "dimension",
            "confidence",
            "n",
            "exact",
            "mae",
            "kappa",
        ]

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)

    print(
        f"\nSaved to {output_path}"
    )