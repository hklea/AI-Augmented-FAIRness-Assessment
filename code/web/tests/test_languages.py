"""Language groups preserve cohort membership and missing metadata."""
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
import main
import dataset_overview as dataset


class LanguageGroups(unittest.TestCase):
    def test_saved_membership_and_unknown_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            results = root / "data" / "results"
            results.mkdir(parents=True)
            ids = ["a_python", "b_missing", "c_null", "d_broken"]
            for filename, members in [("rule_based_scores_full.csv", ids),
                                      ("hybrid_fairness_profiles_ground_truth.csv", ids[:1])]:
                with (results / filename).open("w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(["repo"])
                    writer.writerows([[repo] for repo in members])
            for folder, repo, text in [("raw", ids[0], '{"language":"Python"}'),
                                       ("raw", ids[2], '{"language":null}'),
                                       ("raw", ids[3], 'invalid json'),
                                       ("raw", "extra_repo", '{"language":"Rust"}'),
                                       ("ground_truth", ids[0], '{"language":"C"}')]:
                path = root / "data" / folder / repo
                path.mkdir(parents=True)
                (path / "metadata.json").write_text(text, encoding="utf-8")
            with patch.object(dataset, "PROJECT_ROOT", root), patch.object(dataset, "RESULTS_DIR", results):
                full = dataset.language_groups("full")
                self.assertEqual((full["total"], full["unknown"], full["language_count"]), (4, 3, 1))
                groups = {g["language"]: g for g in full["groups"]}
                self.assertEqual(groups["Unknown"]["percent"], 75)
                self.assertEqual(groups["Python"]["repositories"], [{"id": ids[0], "repo": "a/python"}])
                self.assertEqual(dataset.language_groups("hybrid")["groups"][0]["language"], "C")
                json.dumps(full, allow_nan=False)

    def test_empty_and_invalid_cohort(self):
        with patch.object(dataset, "_read_csv", return_value=[]):
            self.assertEqual(dataset.language_groups()["groups"], [])
            self.assertEqual(dataset.language_groups()["total"], 0)
        with self.assertRaises(ValueError):
            dataset.language_groups("invalid")
