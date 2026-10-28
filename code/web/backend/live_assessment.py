"""Live FAIRness assessment for a single, user-supplied GitHub repository.

Mirrors the snapshot method used by the offline collection pipeline
(code/src/collection/fetch_ground_truth.py): one metadata call, one README
call, and one root-contents call to check for FAIR-relevant filenames. The
snapshot is written to a temporary directory so the existing, validated
rule_based.scorer can run unmodified.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv
from presentation import clean_reasoning
from models import LLAMA, QWEN, MODELS, model_config
from importlib.util import find_spec

from rule_based.scorer import (
    DEPENDENCY_FILES,
    EXPLICIT_CITATION_FILES,
    LICENSE_FILES,
    STRUCTURED_METADATA_FILES,
    score_rule_based,
)
from ai_based.run_llm_ground_truth import (
    MAX_CHARS,
    build_prompt,
    parse_response,
    run_llm,
)

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_HEADERS = {"Accept": "application/vnd.github.v3+json"}
if GITHUB_TOKEN:
    GITHUB_HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"

# Same filename universe the rule-based scorer checks, plus README variants,
# so the live snapshot's fair_file_checks.json lines up with the scorer.
CHECK_FILES = sorted(
    set(LICENSE_FILES)
    | set(DEPENDENCY_FILES)
    | set(STRUCTURED_METADATA_FILES)
    | set(EXPLICIT_CITATION_FILES)
    | {"README.md", "README.rst", "README.txt", "README"}
)

REPO_URL_PATTERN = re.compile(
    r"^(?:https?://github\.com/)?(?P<owner>[\w.-]+)/(?P<repo>[\w.-]+?)(?:\.git|/)?$"
)


class RepoNotFoundError(Exception):
    pass


class InvalidRepoInputError(Exception):
    pass


def _github_get(url: str, headers: dict) -> requests.Response:
    try:
        return requests.get(url, headers=headers, timeout=15)
    except requests.RequestException as error:
        raise RuntimeError("Could not collect repository evidence from GitHub. Check the connection and retry.") from error


def parse_repo_input(text: str) -> tuple[str, str]:
    """Accept 'owner/repo' or a GitHub URL and return (owner, repo)."""
    text = text.strip()
    match = REPO_URL_PATTERN.match(text)
    if not match:
        raise InvalidRepoInputError(
            "Enter a GitHub repository as 'owner/repo' or a full GitHub URL."
        )
    return match.group("owner"), match.group("repo")


def fetch_metadata(owner: str, repo: str) -> dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = _github_get(url, GITHUB_HEADERS)
    if response.status_code == 404:
        raise RepoNotFoundError(f"Repository '{owner}/{repo}' was not found on GitHub.")
    if response.status_code != 200:
        raise RuntimeError(
            f"GitHub returned HTTP {response.status_code} while fetching {owner}/{repo}. Retry after checking API access or rate limits."
        )
    return response.json()


def fetch_readme(owner: str, repo: str) -> str:
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {**GITHUB_HEADERS, "Accept": "application/vnd.github.raw"}
    response = _github_get(url, headers)
    if response.status_code == 404:
        return ""
    if response.status_code != 200:
        raise RuntimeError(f"README collection failed (GitHub HTTP {response.status_code}). No assessment was produced. Please retry.")
    return response.text


def check_fair_files(owner: str, repo: str) -> dict[str, bool]:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
    response = _github_get(url, GITHUB_HEADERS)
    if response.status_code != 200:
        raise RuntimeError(f"File inventory collection failed (GitHub HTTP {response.status_code}). No assessment was produced. Please retry.")
    data = response.json()
    if not isinstance(data, list):
        raise RuntimeError("GitHub returned an invalid file inventory. Please retry collection.")
    contents = {entry["name"] for entry in data if "name" in entry}
    return {filename: filename in contents for filename in CHECK_FILES}


def _write_snapshot(tmp_dir: Path, metadata: dict, readme_text: str, checks: dict) -> None:
    (tmp_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    (tmp_dir / "fair_file_checks.json").write_text(
        json.dumps(checks, indent=2), encoding="utf-8"
    )
    if readme_text:
        (tmp_dir / "README.md").write_text(readme_text, encoding="utf-8")


def _summarize_metadata(metadata: dict) -> dict[str, Any]:
    license_info = metadata.get("license") or {}
    return {
        "full_name": metadata.get("full_name"),
        "description": metadata.get("description"),
        "html_url": metadata.get("html_url"),
        "stargazers_count": metadata.get("stargazers_count"),
        "language": metadata.get("language"),
        "license": license_info.get("name") if isinstance(license_info, dict) else None,
        "topics": metadata.get("topics", []),
        "updated_at": metadata.get("updated_at"),
    }


def run_llm_assessment(repo_name: str, readme_text: str, model: str) -> dict[str, Any]:
    """Score README against the D1-D6 rubric using the same prompt/schema the
    model-specific offline runner uses. Returns an error field on service
    failure so that the structural assessment remains available.
    """
    if not readme_text:
        return {"model": model, "error": "No README available to score."}

    model_config(model)
    error = {"model": model, "error": "Documentation assessment unavailable. Please retry."}
    prompt_builder, runner, parser = build_prompt, run_llm, parse_response
    catchable = (ValueError, RuntimeError, requests.RequestException)
    if model == QWEN:
        if not os.getenv("KISTE_API_TOKEN"):
            return {**error, "error": "KISTE is not configured. Set KISTE_API_TOKEN on the server."}
        try:
            from ai_based import run_llm_ground_truth_qwen as qwen
            import openai
        except ImportError:
            return {**error, "error": "KISTE support is unavailable. Install the project requirements on the server."}
        prompt_builder, runner, parser = qwen.build_prompt, qwen.run_llm, qwen.parse_response
        catchable = catchable + (openai.OpenAIError,)
    try:
        raw_response = runner(prompt_builder(repo_name, readme_text[:MAX_CHARS]), model=model)
        if not raw_response:
            message = "KISTE returned no assessment. Check server credentials and service access, then retry." if model == QWEN else "Ollama scoring unavailable. Start Ollama and pull the selected Llama model, then retry."
            return {**error, "error": message}
        parsed = parser(raw_response)
    except catchable:
        return error
    expected = ["D1_installation", "D2_usage", "D3_purpose", "D4_dependencies", "D5_examples", "D6_contribution"]
    if not isinstance(parsed, dict) or set(parsed) != set(expected):
        return {**error, "error": "The model returned an incomplete or invalid assessment. Please retry."}
    dims = {}
    total = 0
    for dim in expected:
        result = parsed[dim]
        if (not isinstance(result, dict) or type(result.get("score")) is not int
                or result["score"] not in (0, 1, 2)
                or result.get("confidence") not in ("HIGH", "MEDIUM", "LOW")
                or not isinstance(result.get("reasoning"), str) or not result["reasoning"].strip()):
            return {**error, "error": "The model returned invalid scores or explanations. Please retry."}
        dims[dim.split("_")[0]] = {**result, "reasoning": clean_reasoning(result["reasoning"])}
        total += result["score"]

    return {"dimensions": dims, "total": total, "model": model}


def assess_repo_live(
    repo_input: str,
    run_llm_scoring: bool = True,
    model: str = "llama3.1:8b",
) -> dict[str, Any]:
    model_config(model)
    owner, repo = parse_repo_input(repo_input)

    metadata = fetch_metadata(owner, repo)
    readme_text = fetch_readme(owner, repo)
    checks = check_fair_files(owner, repo)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        _write_snapshot(tmp_dir, metadata, readme_text, checks)
        rule_scores = score_rule_based(tmp_dir)

    result: dict[str, Any] = {
        "repo": f"{owner}/{repo}",
        "source": "live",
        "assessed_at": datetime.now(timezone.utc).isoformat(),
        "metadata": _summarize_metadata(metadata),
        "rule_based": rule_scores,
        "readme_available": bool(readme_text),
        "readme": readme_text,
        "readme_truncated": len(readme_text) > MAX_CHARS,
        "readme_limit": MAX_CHARS,
        "llm": None,
    }

    if run_llm_scoring:
        result["llm"] = run_llm_assessment(f"{owner}_{repo}", readme_text, model)

    return result


def model_availability():
    """Probe local Ollama only; KISTE configuration is not a connectivity test."""
    status = {LLAMA: {"available": False, "status": "Ollama unavailable"},
              QWEN: {"available": bool(os.getenv("KISTE_API_TOKEN")) and find_spec("openai") is not None,
                     "status": "Configured; connection checked when assessing" if os.getenv("KISTE_API_TOKEN") and find_spec("openai") is not None else "Server token or OpenAI dependency missing"}}
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        response.raise_for_status()
        names = {m.get("name") for m in response.json().get("models", [])}
        status[LLAMA] = {"available": LLAMA in names, "status": "Ready" if LLAMA in names else "Llama model is not installed in Ollama"}
    except (requests.RequestException, ValueError, TypeError, AttributeError):
        pass
    return [{**config, **status[model]} for model, config in MODELS.items()]
