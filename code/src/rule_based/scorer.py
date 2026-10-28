import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


README_VARIANTS = (
    "README.md",
    "README.rst",
    "README.txt",
    "README",
)

# Each group lists alternative filenames that satisfy one FAIR scoring rule.
LICENSE_FILES = (
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "LICENSE.rst",
    "COPYING",
    "COPYING.txt",
)

DEPENDENCY_FILES = (
    "requirements.txt",
    "requirements-dev.txt",
    "environment.yml",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "Pipfile",
    "package.json",
    "Cargo.toml",
    "Project.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
)

STRUCTURED_METADATA_FILES = (
    "CITATION.cff",
    "codemeta.json",
)

EXPLICIT_CITATION_FILES = (
    "CITATION.md",
    "CITATION",
    "CITATION.txt",
    "CITATION.bib",
    "CITATION.cff",  
)


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON object, returning an empty mapping for missing/invalid files."""
    if not path.exists():
        return {}
    try:
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError) as error:
        print(f"  Warning: could not read {path.name}: {error}")
        return {}


def load_fair_checks(repo_dir: Path) -> dict[str, Any]:
    return load_json(repo_dir / "fair_file_checks.json")


def load_metadata(repo_dir: Path) -> dict[str, Any]:
    return load_json(repo_dir / "metadata.json")


def find_readme(repo_dir: Path) -> Path | None:
    """Return the first recognized README variant in priority order."""
    for filename in README_VARIANTS:
        path = repo_dir / filename
        if path.exists():
            return path
    return None


def load_readme(repo_dir: Path) -> str:
    path = find_readme(repo_dir)
    if path is None:
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def file_exists(
    repo_dir: Path,
    checks: dict[str, Any],
    filename: str,
) -> bool:
    """Check both the precomputed file inventory and the repository snapshot."""
    return bool(checks.get(filename)) or (repo_dir / filename).exists()


def contains_doi(text: str) -> bool:
    """Detect common persistent identifiers, including DOI, Zenodo, and SWH IDs."""
    patterns = (
        r"\bdoi:\s*10\.\d{4,9}/\S+",
        r"https?://doi\.org/10\.\d{4,9}/\S+",
        r"https?://zenodo\.org/(?:badge/latestdoi/|record/|doi/)",
        r"10\.5281/zenodo\.\d+",
        r"\bswh:1:[a-z]+:[a-f0-9]+\b",
        r"\bDOI-10\.\d{4,9}[/%]",
        r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b",
    )
    return any(re.search(pattern, text, flags=re.IGNORECASE)
               for pattern in patterns)


def read_optional_text(repo_dir: Path, filename: str) -> str:
    path = repo_dir / filename
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def has_persistent_identifier(
    repo_dir: Path,
    readme_text: str,
) -> bool:
    """Search user-facing and structured metadata files for a persistent ID."""
    # These are the places where projects most commonly publish citation IDs.
    searchable_text = "\n".join(
        (
            readme_text,
            read_optional_text(repo_dir, "CITATION.cff"),
            read_optional_text(repo_dir, "codemeta.json"),
        )
    )
    return contains_doi(searchable_text)


def has_explicit_citation_instruction(readme_text: str) -> bool:
    """Return whether the README explicitly asks users to cite the project."""
    # Normalize whitespace so patterns also match instructions split across lines.
    text = " ".join(readme_text.lower().split())
    patterns = (
        r"\bplease cite\b",
        r"\bhow to cite\b",
        r"\bciting (?:this|the|our)\b",
        r"\bcite this (?:repository|software|project|library|package|tool)\b",
        r"\bif you use\b.{0,180}\bcite\b",
        r"\bcitation instructions\b",
        r"\bwe (?:would )?appreciate (?:it if you would )?(?:your )?`?cit(?:e|ing|ations?)\b",
        r"\bcite (?:it|them|the (?:software|paper|article|publication))\b",
        r"\bciting in your work\b",
        r"\*\*cite\b",
        r"\bplease (?:consider )?cit(?:e|ing)\b",
    )
    return any(re.search(pattern, text) for pattern in patterns)


def has_declared_license(
    checks: dict[str, Any],
    metadata: dict[str, Any],
    readme_text: str,
    repo_dir: Path,
) -> bool:
    """Detect a license file, metadata declaration, or README statement."""
    # Prefer unambiguous evidence before falling back to README wording.
    if any(file_exists(repo_dir, checks, name) for name in LICENSE_FILES):
        return True
    metadata_license = metadata.get("license")
    if isinstance(metadata_license, dict):
        if metadata_license.get("spdx_id") or metadata_license.get("name"):
            return True
    elif metadata_license:
        return True
    text = " ".join(readme_text.lower().split())
    license_patterns = (
        r"\blicensed under\b",
        r"\breleased under\b.{0,100}\blicen[sc]e\b",
        r"\blicen[sc]e:\s*(?:apache|mit|bsd|gpl|lgpl|mpl|cecill)",
        r"\bdistributed under\b.{0,100}\blicen[sc]e\b",
    )
    return any(re.search(pattern, text) for pattern in license_patterns)


def score_rule_based(repo_dir: Path) -> dict[str, int]:
    """Calculate the six binary FAIR indicators for one repository snapshot."""
    checks = load_fair_checks(repo_dir)
    metadata = load_metadata(repo_dir)
    readme_text = load_readme(repo_dir)

    # bool values are converted to 0/1 so every satisfied rule contributes one
    # point to the final score.
    scores: dict[str, int] = {}

    scores["F1_persistent_id"] = int(
        has_persistent_identifier(repo_dir, readme_text)
    )

    scores["F2_metadata_file"] = int(
        any(
            file_exists(repo_dir, checks, filename)
            for filename in STRUCTURED_METADATA_FILES
        )
    )

    scores["A1_license"] = int(
        has_declared_license(checks, metadata, readme_text, repo_dir)
    )

    scores["I1_dependency_file"] = int(
        any(
            file_exists(repo_dir, checks, filename)
            for filename in DEPENDENCY_FILES
        )
    )

    scores["R1_readme_present"] = int(find_readme(repo_dir) is not None)

    scores["R2_citation"] = int(
        any(
            file_exists(repo_dir, checks, filename)
            for filename in EXPLICIT_CITATION_FILES
        )
        or has_explicit_citation_instruction(readme_text)
    )

    scores["rule_based_total"] = sum(scores.values())
    return scores


def save_scores_csv(
    rows: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """Write score rows to CSV, using the first row to define its columns."""
    if not rows:
        raise ValueError("No scores were generated.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def score_dataset(input_dir: Path, output_path: Path) -> None:
    """Score valid repository folders and save the combined CSV report."""
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    rows: list[dict[str, Any]] = []
    skipped: list[str] = []

    for repo_dir in sorted(input_dir.iterdir()):
        # Ignore ordinary files and hidden directories such as .git.
        if not repo_dir.is_dir() or repo_dir.name.startswith("."):
            continue

        required_files = (
            repo_dir / "metadata.json",
            repo_dir / "fair_file_checks.json",
        )

        # A complete snapshot needs both API metadata and the file inventory.
        if not all(path.exists() for path in required_files):
            skipped.append(repo_dir.name)
            print(f"Skipping {repo_dir.name}: required files missing")
            continue

        scores = score_rule_based(repo_dir)
        rows.append({"repo": repo_dir.name, **scores})
        print(f"{repo_dir.name}: {scores['rule_based_total']}/6")

    save_scores_csv(rows, output_path)

    print(f"\nScored repositories: {len(rows)}")
    print(f"Skipped repositories: {len(skipped)}")
    print(f"Results saved to: {output_path}")

    if skipped:
        print("\nSkipped repository folders:")
        for name in skipped:
            print(f"  - {name}")


def parse_args() -> argparse.Namespace:
    """Parse command-line input and output paths."""
    parser = argparse.ArgumentParser(
        description="Run the rule-based FAIR scorer on repository snapshots."
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Directory containing one folder per repository.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output CSV path.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    score_dataset(arguments.input, arguments.output)
