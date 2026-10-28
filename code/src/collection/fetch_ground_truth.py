import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# GitHub API token is read from .env so authenticated requests have a higher
# rate limit. Expected .env entry: GITHUB_TOKEN=...
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Shared headers for GitHub API calls. The Accept header requests the v3 API.
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Scientific/open-source projects used as the manually selected sample.
REPOS = [
    ("mne-tools", "mne-python"),
    ("fieldtrip", "fieldtrip"),
    ("brian-team", "brian2"),
    ("rdkit", "rdkit"),
    ("openbabel", "openbabel"),
    ("cdk", "cdk"),
    ("PlasmaPy", "PlasmaPy"),
    ("yt-project", "yt"),
    ("openmc-dev", "openmc"),
    ("Geant4", "geant4"),
    ("MITgcm", "MITgcm"),
    ("Ouranosinc", "xclim"),
    ("JuliaClimate", "ClimateTools.jl"),
    ("scipy", "scipy"),
    ("gonum", "gonum"),
    ("rust-ml", "linfa"),
    ("opencobra", "cobrapy"),
    ("datajoint", "datajoint-python"),
    ("nextflow-io", "nextflow"),
    ("InsightSoftwareConsortium", "ITK"),
]

# Files that are useful signals for FAIRness, citation, licensing,
# reproducibility, packaging, and contribution practices.
FAIR_FILES = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.rst",
    "COPYING", "COPYING.txt",
    "README.md", "README.rst", "README.txt", "README",
    "CITATION.cff", "CITATION.md", "CITATION.bib",
    "codemeta.json",
    "requirements.txt", "requirements-dev.txt",
    "setup.py", "setup.cfg", "pyproject.toml",
    "environment.yml", "Pipfile",
    "CONTRIBUTING.md", "CONTRIBUTING.rst",
]


def fetch_metadata(owner, repo):
    """Fetch general GitHub repo metadata such as stars, license, topics, etc."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    print(f"  Metadata error {response.status_code} for {owner}/{repo}")
    return None


def fetch_readme(owner, repo):
    """Fetch the repository README as raw text."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {**HEADERS, "Accept": "application/vnd.github.raw"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    print(f"  README error {response.status_code} for {owner}/{repo}")
    return None


def check_fair_files(owner, repo):
    """Check which expected FAIR-related files exist in the repository root."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"  FAIR files error {response.status_code} for {owner}/{repo}")
        return {}

    data = response.json()
    if not isinstance(data, list):
        return {}

    contents = [f["name"] for f in data]

    # Keep one boolean result per target file so later analysis can compare
    # repositories using the same fixed schema.
    checks = {}
    for fair_file in FAIR_FILES:
        checks[fair_file] = fair_file in contents

    return checks


def fetch_all():
    """Fetch all configured repositories and save one output folder per repo."""
    # parents[3] points from code/src/collection/fetch_ground_truth.py back to
    # the project root, so output lands in the shared data directory.
    project_root = Path(__file__).resolve().parents[3]
    output_base = project_root / "data" / "ground_truth"

    for owner, repo in REPOS:
        folder_name = f"{owner}_{repo}"
        output_dir = output_base / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nFetching {owner}/{repo}...")

        # Metadata
        metadata = fetch_metadata(owner, repo)
        if metadata:
            with open(output_dir / "metadata.json", "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
            print(f"  metadata.json saved")

        # README
        readme = fetch_readme(owner, repo)
        if readme:
            with open(output_dir / "README.md", "w", encoding="utf-8") as f:
                f.write(readme)
            print(f"  README.md saved")

        # FAIR file checks
        fair_checks = check_fair_files(owner, repo)
        with open(output_dir / "fair_file_checks.json", "w", encoding="utf-8") as f:
            json.dump(fair_checks, f, indent=4)
        print(f"  fair_file_checks.json saved")

    print("\nDone. All ground truth repos fetched.")


if __name__ == "__main__":
    fetch_all()
