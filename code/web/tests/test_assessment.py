"""Regression checks for cohort provenance and failed evidence collection.

Run: python -m unittest discover -s code/web/tests -v
"""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
import main
import dataset_overview as dataset
import live_assessment as live
import requests
from presentation import clean_reasoning
from models import LLAMA, QWEN
from ai_based import run_llm_ground_truth_qwen as qwen
from pydantic import ValidationError


class ModelSupport(unittest.TestCase):
    def test_qwen_overview_and_reports_preserve_model_provenance(self):
        overview = dataset.get_overview(QWEN)
        self.assertEqual(overview["model"], QWEN)
        self.assertEqual(overview["ground_truth_hybrid"]["repo_count"], 30)
        for row in overview["repositories"]["hybrid"]:
            report = dataset.saved_report(row["id"], "hybrid", QWEN)
            self.assertEqual(report["llm"]["model"], QWEN)
            self.assertEqual(report["llm"]["total"], row["llm_total"])
        self.assertIsNone(dataset.saved_report("astropy_astropy", "full", QWEN)["llm"])
        comparison = dataset.compare_report("astropy_astropy")
        self.assertEqual(comparison["reports"][LLAMA]["llm"]["total"], 4)
        self.assertEqual(comparison["reports"][QWEN]["llm"]["total"], 5)
        self.assertEqual(comparison["humans"]["1"]["D1"], 1)
        json.dumps(comparison, allow_nan=False)

    def test_agreement_filters_and_known_baseline(self):
        metrics = dataset.model_comparison_metrics()
        self.assertEqual(metrics["n"], 30)
        self.assertAlmostEqual(metrics["results"][0]["summary"]["kappa"], 0.329, places=3)
        for annotator in (1, 2):
            holdout = dataset.model_comparison_metrics(annotator, "holdout")
            self.assertEqual(holdout["n"], 20)
            json.dumps(holdout, allow_nan=False)
        with patch.object(dataset, "_read_csv", return_value=[]):
            empty = dataset.model_comparison_metrics()
            self.assertEqual(empty["n"], 0)
            self.assertIsNone(empty["results"][0]["summary"]["kappa"])

    def test_unknown_model_and_filters_are_rejected(self):
        with self.assertRaises(ValidationError):
            main.AssessRequest(repo="owner/repo", model="unknown")
        with self.assertRaises(ValueError):
            dataset.get_overview("../../.env")
        with self.assertRaises(ValueError):
            dataset.model_comparison_metrics(3)

    @patch.dict(live.os.environ, {"KISTE_API_TOKEN": "test-only"})
    @patch.object(live, "run_llm")
    @patch.object(qwen, "run_llm")
    def test_qwen_uses_kiste_and_validates_fenced_output(self, runner, ollama):
        valid = {dim: {"score": 1, "confidence": "MEDIUM", "reasoning": "Evidence"} for dim in qwen.DIMS}
        runner.return_value = "```json\n" + json.dumps(valid) + "\n```"
        result = live.run_llm_assessment("owner_repo", "x" * 14000, QWEN)
        self.assertEqual(result["total"], 6)
        self.assertEqual(result["model"], QWEN)
        self.assertIn("x" * 12000, runner.call_args.args[0])
        self.assertNotIn("x" * 12001, runner.call_args.args[0])
        ollama.assert_not_called()
        valid[qwen.DIMS[0]]["score"] = True
        runner.return_value = json.dumps(valid)
        self.assertIn("error", live.run_llm_assessment("owner_repo", "README", QWEN))
        runner.return_value = ""
        result = live.run_llm_assessment("owner_repo", "README", QWEN)
        self.assertIn("KISTE", result["error"])
        self.assertNotIn("total", result)

    @patch.dict(live.os.environ, {}, clear=True)
    @patch.object(qwen, "run_llm")
    def test_missing_kiste_token_never_calls_service(self, runner):
        self.assertIn("KISTE_API_TOKEN", live.run_llm_assessment("owner_repo", "README", QWEN)["error"])
        runner.assert_not_called()


class SavedReports(unittest.TestCase):
    def test_terminal_corrections_are_applied_without_duplicate_fragments(self):
        self.assertEqual(clean_reasoning("installation in\x1b[2D\x1b[K information"), "installation information")
        self.assertEqual(clean_reasoning("prerequisi\x1b[10D\x1b[K prerequisites."), "prerequisites.")

    def test_every_listed_report_preserves_its_saved_scores(self):
        overview = dataset.get_overview()
        for cohort, rows in overview["repositories"].items():
            for row in rows:
                with self.subTest(cohort=cohort, repo=row["id"]):
                    report = dataset.saved_report(row["id"], cohort)
                    self.assertEqual(report["rule_based"]["rule_based_total"], row["rule_based_total"])
                    self.assertEqual(sum(report["rule_based"][k] for k in dataset.RULE_BASED_INDICATORS), row["rule_based_total"])
                    self.assertEqual(report["cohort"], cohort)
                    if cohort == "full":
                        self.assertIsNone(report["llm"])
                    else:
                        self.assertEqual(sum(d["score"] for d in report["llm"]["dimensions"].values()), row["llm_total"])
                    json.dumps(report, allow_nan=False)

    def test_astropy_example_and_terminal_code_cleanup(self):
        report = dataset.saved_report("astropy_astropy", "hybrid")
        self.assertEqual(report["rule_based"]["rule_based_total"], 6)
        self.assertEqual(report["llm"]["total"], 4)
        self.assertIn("astropy", report["readme"].lower())
        self.assertNotIn("\x1b", json.dumps(report["llm"], ensure_ascii=False).replace("\\u001b", "\x1b"))

    def test_unknown_identifiers_cannot_resolve_files(self):
        self.assertIsNone(dataset.saved_report("../../.env", "hybrid"))
        with self.assertRaises(ValueError):
            dataset.saved_report("astropy_astropy", "unknown")


class LiveCollection(unittest.TestCase):
    @patch.object(live.requests, "get")
    def test_readme_404_is_absence_but_other_failures_are_errors(self, get):
        get.return_value = Mock(status_code=404)
        self.assertEqual(live.fetch_readme("owner", "repo"), "")
        for status in (403, 429, 500):
            get.return_value = Mock(status_code=status)
            with self.assertRaises(RuntimeError):
                live.fetch_readme("owner", "repo")

    @patch.object(live.requests, "get")
    def test_inventory_failures_never_become_negative_scores(self, get):
        for status in (403, 404, 429, 500):
            get.return_value = Mock(status_code=status)
            with self.assertRaises(RuntimeError):
                live.check_fair_files("owner", "repo")
        get.return_value = Mock(status_code=200)
        get.return_value.json.return_value = {"message": "unexpected"}
        with self.assertRaises(RuntimeError):
            live.check_fair_files("owner", "repo")

    @patch.object(live.requests, "get", side_effect=requests.Timeout())
    def test_network_timeout_has_actionable_message(self, get):
        with self.assertRaisesRegex(RuntimeError, "retry"):
            live.fetch_metadata("owner", "repo")

    @patch.object(live, "score_rule_based")
    @patch.object(live, "fetch_readme", side_effect=RuntimeError("Collection failed"))
    @patch.object(live, "fetch_metadata", return_value={})
    def test_failed_collection_stops_scoring(self, metadata, readme, scorer):
        with self.assertRaises(RuntimeError):
            live.assess_repo_live("owner/repo")
        scorer.assert_not_called()

    @patch.object(live, "run_llm", return_value="")
    @patch.object(live, "check_fair_files", return_value={})
    @patch.object(live, "fetch_readme", return_value="A research tool")
    @patch.object(live, "fetch_metadata", return_value={"html_url": "https://github.com/owner/repo"})
    def test_unavailable_llm_preserves_structural_results(self, metadata, readme, checks, llm):
        report = live.assess_repo_live("owner/repo")
        self.assertIn("rule_based_total", report["rule_based"])
        self.assertIn("error", report["llm"])
        self.assertNotIn("total", report["llm"])
        self.assertEqual(report["source"], "live")


if __name__ == "__main__":
    unittest.main()
