import requests
import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

FAIR_FILES = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.rst",
    "COPYING", "COPYING.txt",
    "README.md", "README.rst", "README.txt", "README",
    "CITATION.cff", "CITATION.md", "CITATION.bib", "CITATION.txt", "CITATION",
    "codemeta.json",
    "requirements.txt", "requirements-dev.txt",
    "setup.py", "setup.cfg", "pyproject.toml",
    "environment.yml", "Pipfile",
    "package.json", "Cargo.toml",
    "Project.toml", "Manifest.toml",
    "go.mod", "go.sum",
    "pom.xml", "build.gradle", "build.gradle.kts",
    "CONTRIBUTING.md", "CONTRIBUTING.rst",
]


def fetch_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {**HEADERS, "Accept": "application/vnd.github.raw"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    print(f"  README error {response.status_code}")
    return None


def fetch_metadata(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    print(f"  Metadata error {response.status_code}")
    return None


def check_fair_files(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {}
    data = response.json()
    if not isinstance(data, list):
        return {}
    contents = [f["name"] for f in data]
    return {fair_file: fair_file in contents for fair_file in FAIR_FILES}


def fetch_all():
    project_root = Path(__file__).resolve().parents[3]
    dataset_path = project_root / "data" / "raw" / "cleaned_dataset.json"
    output_base = project_root / "data" / "raw"

    with open(dataset_path, encoding="utf-8") as f:
        repos = json.load(f)

    print(f"Total repos to fetch: {len(repos)}")

    for i, repo in enumerate(repos):
        owner = repo["owner"]
        name = repo["repo"]
        folder_name = f"{owner}_{name}"
        output_dir = output_base / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Skip if already fully fetched
        if (output_dir / "metadata.json").exists():
            print(f"[{i+1}/{len(repos)}] Skipping {owner}/{name} — already fetched")
            continue

        print(f"[{i+1}/{len(repos)}] Fetching {owner}/{name}...")

        # Fetch README only if not already saved
        if not (output_dir / "README.md").exists():
            readme = fetch_readme(owner, name)
            if readme:
                with open(output_dir / "README.md", "w", encoding="utf-8") as f:
                    f.write(readme)
                print(f"  README.md saved")

        # Fetch fair file checks only if not already saved
        if not (output_dir / "fair_file_checks.json").exists():
            fair_checks = check_fair_files(owner, name)
            with open(output_dir / "fair_file_checks.json", "w", encoding="utf-8") as f:
                json.dump(fair_checks, f, indent=4)
            print(f"  fair_file_checks.json saved")

        # Always fetch metadata
        metadata = fetch_metadata(owner, name)
        if metadata:
            with open(output_dir / "metadata.json", "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
            print(f"  metadata.json saved")

        time.sleep(0.5)

    print(f"\nDone. All repos fetched.")


if __name__ == "__main__":
    fetch_all()