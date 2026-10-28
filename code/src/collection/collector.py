import csv
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

FAIR_FILES = [
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "LICENSE.rst",   #just added this 
    "COPYING",        # added v1.3
    "COPYING.txt",    # added v1.3
    "CITATION.cff",
    "CITATION.md",
    "CITATION",
    "codemeta.json",
    "requirements.txt",
    "environment.yml",
    "setup.py",
    "pyproject.toml",
    "package.json",
    "Cargo.toml",
]


def get_project_root():
    return Path(__file__).resolve().parents[3]


def fetch_json(url):
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {url}")
        return None

    return response.json()


def fetch_repo_metadata(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    return fetch_json(url)


def fetch_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.raw",
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"README error {response.status_code}: {owner}/{repo}")
        return None

    return response.text


def file_exists(owner, repo, file_path):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    response = requests.get(url, headers=HEADERS)

    return response.status_code == 200


def check_fair_files(owner, repo):
    results = {}

    for file_name in FAIR_FILES:
        results[file_name] = file_exists(owner, repo, file_name)

    return results


def save_repo_data(owner, repo):
    project_root = get_project_root()
    repo_dir = project_root / "data" / "pilot" / f"{owner}_{repo}"
    repo_dir.mkdir(parents=True, exist_ok=True)

    print(f"Collecting {owner}/{repo}...")

    metadata = fetch_repo_metadata(owner, repo)
    readme = fetch_readme(owner, repo)
    fair_file_checks = check_fair_files(owner, repo)

    if metadata:
        with (repo_dir / "metadata.json").open("w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)

    if readme:
        with (repo_dir / "README.md").open("w", encoding="utf-8") as file:
            file.write(readme)

    with (repo_dir / "fair_file_checks.json").open("w", encoding="utf-8") as file:
        json.dump(fair_file_checks, file, indent=4)

    print(f"Saved {owner}/{repo}")


def read_pilot_repositories():
    project_root = get_project_root()
    csv_path = project_root / "data" / "pilot_repositories.csv"

    repos = []

    with csv_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            owner = row["owner"].strip()
            repo = row["repo"].strip()
            repos.append((owner, repo))

    return repos


if __name__ == "__main__":
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN not found. Check your .env file.")

    repositories = read_pilot_repositories()

    for owner, repo in repositories:
        save_repo_data(owner, repo)

    print("Pilot data collection completed.")