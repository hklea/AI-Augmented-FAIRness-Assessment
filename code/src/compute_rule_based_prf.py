import csv
from pathlib import Path

from compute_kappa import parse_annotation

RULE_INDICATORS = [
    "F1_persistent_id",
    "F2_metadata_file",
    "A1_license",
    "I1_dependency_file",
    "R1_readme_present",
    "R2_citation",
]

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


def load_ground_truth(ground_truth_dir, exclude_repos=None):
    gt = {}
    for repo_dir in sorted(Path(ground_truth_dir).iterdir()):
        if not repo_dir.is_dir():
            continue
        if exclude_repos and repo_dir.name in exclude_repos:
            continue
        ann_path = repo_dir / "annotation.md"
        if not ann_path.exists():
            continue
        gt[repo_dir.name] = parse_annotation(ann_path)
    return gt


def load_rule_based_scores(csv_path):
    scores = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            repo = row["repo"]
            scores[repo] = {ind: int(row[ind]) for ind in RULE_INDICATORS}
    return scores


def compute_prf(ground_truth, predicted, indicator):
    tp = fp = fn = tn = 0
    missing = []
    mismatches = []
    for repo, gt_scores in ground_truth.items():
        y_true = gt_scores.get(indicator)
        pred_scores = predicted.get(repo)
        if pred_scores is None:
            missing.append(repo)
            continue
        y_pred = pred_scores.get(indicator)
        if y_true is None or y_pred is None:
            continue
        if y_true != y_pred:
            mismatches.append({"repo": repo, "manual": y_true, "predicted": y_pred})
        if y_true == 1 and y_pred == 1:
            tp += 1
        elif y_true == 0 and y_pred == 1:
            fp += 1
        elif y_true == 1 and y_pred == 0:
            fn += 1
        elif y_true == 0 and y_pred == 0:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else None
    recall = tp / (tp + fn) if (tp + fn) > 0 else None
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision is not None and recall is not None and (precision + recall) > 0
        else None
    )
    return {
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "precision": precision, "recall": recall, "f1": f1,
        "missing": missing, "mismatches": mismatches,
    }


def run_prf(ground_truth_dir, rule_based_csv, output_path, exclude_repos=None, label="30 repos"):
    ground_truth = load_ground_truth(ground_truth_dir, exclude_repos=exclude_repos)
    predicted = load_rule_based_scores(rule_based_csv)

    print(f"\n=== Rule-based P/R/F1 ({label}) ===")
    print(f"Loaded ground truth for {len(ground_truth)} repos")
    print(f"Loaded rule-based scores for {len(predicted)} repos\n")

    rows = []
    for ind in RULE_INDICATORS:
        result = compute_prf(ground_truth, predicted, ind)
        if result["missing"]:
            print(f"WARNING: {ind} missing predictions for: {result['missing']}")
        p = f"{result['precision']:.3f}" if result["precision"] is not None else "undefined"
        r = f"{result['recall']:.3f}" if result["recall"] is not None else "undefined"
        f1 = f"{result['f1']:.3f}" if result["f1"] is not None else "undefined"
        print(f"{ind}: TP={result['tp']} FP={result['fp']} FN={result['fn']} TN={result['tn']} "
              f"| Precision={p} Recall={r} F1={f1}")
        for m in result["mismatches"]:
            print(f"  MISMATCH: {m['repo']} manual={m['manual']} predicted={m['predicted']}")
        rows.append({
            "indicator": ind, "tp": result["tp"], "fp": result["fp"],
            "fn": result["fn"], "tn": result["tn"],
            "precision": result["precision"], "recall": result["recall"], "f1": result["f1"],
        })
        print()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    ground_truth_dir = project_root / "data" / "ground_truth"
    rule_based_csv = project_root / "data" / "results" / "rule_based_scores_ground_truth.csv"

    # Full 30-repo run (unchanged, existing Chapter 5 result)
    run_prf(
        ground_truth_dir=ground_truth_dir,
        rule_based_csv=rule_based_csv,
        output_path=project_root / "data" / "results" / "rule_based_prf.csv",
        label="30 repos",
    )

    # 20-repo holdout run (excludes the 10 pilot repos)
    run_prf(
        ground_truth_dir=ground_truth_dir,
        rule_based_csv=rule_based_csv,
        output_path=project_root / "data" / "results" / "rule_based_prf_holdout.csv",
        exclude_repos=PILOT_REPOS,
        label="20-repo holdout",
    )