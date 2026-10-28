import csv
from datetime import datetime
from pathlib import Path


def merge_profiles(rule_path, llm_path, output_path):
    """Merge rule-based and LLM evaluation CSVs by repository name.

    Only repositories present in both input files are included in the output.
    The returned list contains the same dictionaries that are written to CSV.
    """
    # Index each input by repository so matching records can be joined directly.
    with open(rule_path, encoding="utf-8") as f:
        rule_rows = {r["repo"]: r for r in csv.DictReader(f)}

    with open(llm_path, encoding="utf-8") as f:
        llm_rows = {r["repo"]: r for r in csv.DictReader(f)}

    # An inner join prevents incomplete profiles when one evaluation is missing.
    common = set(rule_rows.keys()) & set(llm_rows.keys())
    print(f"Rule-based repos: {len(rule_rows)}")
    print(f"LLM repos: {len(llm_rows)}")
    print(f"Common repos: {len(common)}")

    # Keep the output column order explicit and stable for downstream analysis.
    fieldnames = [
        "repo", "generated_at",
        # Rule-based indicators
        "F1_persistent_id", "F2_metadata_file", "A1_license",
        "I1_dependency_file", "R1_readme_present", "R2_citation",
        "rule_based_total",
        # LLM scores
        "D1_score", "D1_confidence", "D1_reasoning",
        "D2_score", "D2_confidence", "D2_reasoning",
        "D3_score", "D3_confidence", "D3_reasoning",
        "D4_score", "D4_confidence", "D4_reasoning",
        "D5_score", "D5_confidence", "D5_reasoning",
        "D6_score", "D6_confidence", "D6_reasoning",
        "llm_total",
        # Model info
        "model", "llm_timestamp",
    ]

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    # Use one timestamp for the whole batch so its rows can be identified together.
    generated_at = datetime.now().isoformat()

    # Sorting makes output deterministic regardless of input CSV row order.
    for repo in sorted(common):
        r = rule_rows[repo]
        l = llm_rows[repo]
        row = {
            "repo": repo,
            "generated_at": generated_at,
            "F1_persistent_id": r["F1_persistent_id"],
            "F2_metadata_file": r["F2_metadata_file"],
            "A1_license": r["A1_license"],
            "I1_dependency_file": r["I1_dependency_file"],
            "R1_readme_present": r["R1_readme_present"],
            "R2_citation": r["R2_citation"],
            "rule_based_total": r["rule_based_total"],
            "D1_score": l["D1_score"],
            "D1_confidence": l["D1_confidence"],
            "D1_reasoning": l["D1_reasoning"],
            "D2_score": l["D2_score"],
            "D2_confidence": l["D2_confidence"],
            "D2_reasoning": l["D2_reasoning"],
            "D3_score": l["D3_score"],
            "D3_confidence": l["D3_confidence"],
            "D3_reasoning": l["D3_reasoning"],
            "D4_score": l["D4_score"],
            "D4_confidence": l["D4_confidence"],
            "D4_reasoning": l["D4_reasoning"],
            "D5_score": l["D5_score"],
            "D5_confidence": l["D5_confidence"],
            "D5_reasoning": l["D5_reasoning"],
            "D6_score": l["D6_score"],
            "D6_confidence": l["D6_confidence"],
            "D6_reasoning": l["D6_reasoning"],
            "llm_total": l["llm_total"],
            "model": l["model"],
            "llm_timestamp": l["timestamp"],
        }
        rows.append(row)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} hybrid profiles to {output_path}")
    return rows


if __name__ == "__main__":
    # Resolve data paths from the repository root, independent of the current
    # working directory used to launch this script.
    project_root = Path(__file__).resolve().parents[2]
    rule_path = project_root / "data" / "results" / "rule_based_scores_ground_truth.csv"
    llm_path = project_root / "data" / "results" / "llm_scores_ground_truth.csv"
    output_path = project_root / "data" / "results" / "hybrid_fairness_profiles_ground_truth.csv"

    merge_profiles(rule_path, llm_path, output_path)
