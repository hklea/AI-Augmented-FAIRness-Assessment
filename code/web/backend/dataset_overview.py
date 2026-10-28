"""Reads already-computed result CSVs from data/results/ and shapes them into
JSON for the UI. Aggregate summaries are calculated from saved score rows;
individual assessments and validation metrics are never rerun here.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any
from presentation import clean_reasoning
from models import LLAMA, MODELS, model_config, result_filename
from llm_human_agreement import DIMS, PILOT_REPOS, cohen_kappa_weighted

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RESULTS_DIR = PROJECT_ROOT / "data" / "results"

RULE_BASED_INDICATORS = [
    "F1_persistent_id",
    "F2_metadata_file",
    "A1_license",
    "I1_dependency_file",
    "R1_readme_present",
    "R2_citation",
]


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as file:
        return list(csv.DictReader(file))


def full_dataset_summary() -> dict[str, Any]:
    rows = _read_csv(RESULTS_DIR / "rule_based_scores_full.csv")
    if not rows:
        return {"available": False}

    totals = [int(row["rule_based_total"]) for row in rows]
    prevalence = {
        indicator: round(
            100 * sum(int(row[indicator]) for row in rows) / len(rows), 1
        )
        for indicator in RULE_BASED_INDICATORS
    }
    distribution = {str(score): 0 for score in range(7)}
    for total in totals:
        distribution[str(total)] += 1

    return {
        "available": True,
        "repo_count": len(rows),
        "mean_total": round(sum(totals) / len(totals), 2),
        "prevalence_pct": prevalence,
        "total_distribution": distribution,
    }


def ground_truth_hybrid(model=LLAMA) -> dict[str, Any]:
    rows = _read_csv(RESULTS_DIR / result_filename("hybrid_fairness_profiles_ground_truth", model))
    if not rows:
        return {"available": False}

    profiles = []
    for row in rows:
        rule_total = int(row["rule_based_total"])
        llm_total = int(row["llm_total"])
        profiles.append(
            {
                "repo": row["repo"],
                "rule_based_total": rule_total,
                "llm_total": llm_total,
            }
        )

    return {
        "available": True,
        "repo_count": len(profiles),
        "profiles": profiles,
        "mean_total": round(sum(p["llm_total"] for p in profiles) / len(profiles), 2),
        "dimension_means": {
            f"D{i}": round(sum(int(row[f"D{i}_score"]) for row in rows) / len(rows), 2)
            for i in range(1, 7)
        },
    }


def _prf_table(filename: str) -> list[dict[str, Any]]:
    rows = _read_csv(RESULTS_DIR / filename)
    return [
        {
            "indicator": row["indicator"],
            "precision": round(float(row["precision"]), 3),
            "recall": round(float(row["recall"]), 3),
            "f1": round(float(row["f1"]), 3),
        }
        for row in rows
    ]


def evaluation_metrics(model=LLAMA) -> dict[str, Any]:
    def optional_number(value):
        if value is None or not str(value).strip():
            return None
        number = float(value)
        return round(number, 3) if math.isfinite(number) else None

    calibration_rows = _read_csv(RESULTS_DIR / result_filename("confidence_calibration", model))
    calibration_overall = [
        {
            "confidence": row["confidence"],
            "n": int(row["n"]),
            "exact_agreement": optional_number(row["exact"]),
            "mae": optional_number(row["mae"]),
            "kappa": optional_number(row["kappa"]),
        }
        for row in calibration_rows
        if row["scope"] == "overall"
    ]

    return {
    "rule_based_prf": _prf_table("rule_based_prf.csv"),
    "rule_based_prf_holdout": _prf_table("rule_based_prf_holdout.csv"),
    "rule_based_prf_holdout_note": (
        "Reported as an internal consistency check, not independent "
        "validation. Some annotations in this 20-repository subset were "
        "corrected during scorer validation using the finalized rubric."
    ),
    "confidence_calibration": calibration_overall,
}


def get_overview(model=LLAMA) -> dict[str, Any]:
    model_config(model)
    return {
        "model": model,
        "models": list(MODELS.values()),
        "full_dataset": full_dataset_summary(),
        "ground_truth_hybrid": ground_truth_hybrid(model),
        "evaluation": evaluation_metrics(model),
        "repositories": {
            "full": repository_list("full"),
            "hybrid": repository_list("hybrid", model),
        },
    }


def _cohort_rows(cohort: str, model=LLAMA) -> list[dict[str, str]]:
    model_config(model)
    filenames = {
        "full": "rule_based_scores_full.csv",
        "hybrid": result_filename("hybrid_fairness_profiles_ground_truth", model),
    }
    if cohort not in filenames:
        raise ValueError("Unknown dataset.")
    return _read_csv(RESULTS_DIR / filenames[cohort])


def repository_list(cohort: str, model=LLAMA) -> list[dict[str, Any]]:
    return sorted([
        {"id": row["repo"], "repo": row["repo"].replace("_", "/", 1),
         "rule_based_total": int(row["rule_based_total"]),
         "llm_total": int(row["llm_total"]) if "llm_total" in row else None}
        for row in _cohort_rows(cohort, model)
    ], key=lambda row: row["repo"].lower())


def language_groups(cohort: str = "full") -> dict[str, Any]:
    root = PROJECT_ROOT / "data" / ("ground_truth" if cohort == "hybrid" else "raw")
    groups: dict[str, list[dict[str, str]]] = {}
    for row in _cohort_rows(cohort):
        snapshot = (root / row["repo"]).resolve()
        metadata = {}
        if snapshot.is_relative_to(root.resolve()):
            try:
                metadata = json.loads((snapshot / "metadata.json").read_text(encoding="utf-8"))
            except (OSError, ValueError):
                pass
        language = metadata.get("language") if isinstance(metadata, dict) else None
        language = language.strip() if isinstance(language, str) and language.strip() else "Unknown"
        groups.setdefault(language, []).append({"id": row["repo"], "repo": row["repo"].replace("_", "/", 1)})
    total = sum(len(repos) for repos in groups.values())
    return {
        "cohort": cohort, "total": total,
        "unknown": len(groups.get("Unknown", [])),
        "language_count": len(groups.keys() - {"Unknown"}),
        "groups": [
            {"language": language, "count": len(repos),
             "percent": round(100 * len(repos) / total, 1),
             "repositories": sorted(repos, key=lambda repo: repo["repo"].lower())}
            for language, repos in sorted(groups.items(), key=lambda item: (-len(item[1]), item[0].lower()))
        ],
    }


def saved_report(repo_id: str, cohort: str, model=LLAMA) -> dict[str, Any] | None:
    # Look up the exact saved identifier before resolving any filesystem path.
    row = next((r for r in _cohort_rows(cohort, model) if r["repo"] == repo_id), None)
    if row is None:
        return None
    root = PROJECT_ROOT / "data" / ("ground_truth" if cohort == "hybrid" else "raw")
    snapshot = (root / repo_id).resolve()
    if not snapshot.is_relative_to(root.resolve()):
        return None
    metadata_path = snapshot / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.exists() else {}
    readme = None
    for name in ("README.md", "README.rst", "README.txt", "README"):
        if (snapshot / name).exists():
            readme = (snapshot / name).read_text(encoding="utf-8", errors="replace")
            break
    repo = row["repo"].replace("_", "/", 1)
    llm = None
    if cohort == "hybrid":
        llm = {"total": int(row["llm_total"]), "model": row["model"], "dimensions": {
            f"D{i}": {"score": int(row[f"D{i}_score"]),
                       "confidence": row[f"D{i}_confidence"],
                       "reasoning": clean_reasoning(row[f"D{i}_reasoning"])}
            for i in range(1, 7)
        }}
    return {
        "repo": repo, "source": "saved", "cohort": cohort,
        "assessed_at": row.get("llm_timestamp"),
        "metadata": {"description": metadata.get("description"),
                     "html_url": metadata.get("html_url", f"https://github.com/{repo}")},
        "rule_based": {key: int(row[key]) for key in RULE_BASED_INDICATORS + ["rule_based_total"]},
        "llm": llm, "readme": readme,
        "readme_available": bool(readme) if readme is not None else None,
        "readme_truncated": len(readme) > 12000 if readme is not None else None,
        "readme_limit": 12000,
    }


def compare_report(repo_id: str) -> dict[str, Any] | None:
    reports = {model: saved_report(repo_id, "hybrid", model) for model in MODELS}
    if not any(reports.values()):
        return None
    humans = {}
    for annotator in (1, 2):
        rows = _read_csv(RESULTS_DIR / result_filename(f"llm_human_agreement_annotator{annotator}"))
        row = next((r for r in rows if r["repo"] == repo_id), None)
        humans[str(annotator)] = {dim.split("_")[0]: int(row[f"human_{dim}"]) for dim in DIMS} if row else None
    return {"reports": reports, "humans": humans, "models": list(MODELS.values())}


def model_comparison_metrics(annotator=1, subset="all"):
    if annotator not in (1, 2) or subset not in ("all", "holdout"):
        raise ValueError("Unknown annotator or evaluation subset.")
    by_model = {}
    for model in MODELS:
        rows = _read_csv(RESULTS_DIR / result_filename(f"llm_human_agreement_annotator{annotator}", model))
        by_model[model] = {r["repo"]: r for r in rows if subset == "all" or r["repo"] not in PILOT_REPOS}
    common = set.intersection(*(set(rows) for rows in by_model.values()))
    results = []
    for model, rows in by_model.items():
        dimensions = []
        for dim in DIMS:
            pairs = [(int(rows[r][f"human_{dim}"]), int(rows[r][f"llm_{dim}"])) for r in sorted(common)]
            n = len(pairs)
            dimensions.append({"dimension": dim.split("_")[0], "n": n,
                "exact": sum(h == m for h, m in pairs) / n if n else None,
                "mae": sum(abs(h-m) for h, m in pairs) / n if n else None,
                "kappa": cohen_kappa_weighted([h for h,m in pairs], [m for h,m in pairs])})
        summary = {}
        for metric in ("exact", "mae", "kappa"):
            values = [d[metric] for d in dimensions if d[metric] is not None]
            summary[metric] = sum(values) / len(values) if values else None
        results.append({"model": model, "dimensions": dimensions, "summary": summary})
    return {"n": len(common), "annotator": annotator, "subset": subset, "results": results}
