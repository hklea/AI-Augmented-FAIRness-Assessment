import json
import sys
from pathlib import Path
from filters import has_excluded_keywords


def clean_dataset(input_path):
    with open(input_path, encoding="utf-8") as f:
        repos = json.load(f)

    print(f"Original dataset: {len(repos)} repos")

    cleaned = []
    removed = []

    for repo in repos:
        if has_excluded_keywords(repo):
            removed.append(repo)
        else:
            cleaned.append(repo)

    print(f"Removed {len(removed)} repos:")
    for repo in removed:
        print(f"  - {repo['full_name']}")

    print(f"Cleaned dataset: {len(cleaned)} repos")

    output_path = Path(input_path).parent / "cleaned_dataset.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=4)

    removed_path = Path(input_path).parent / "removed_repos.json"
    with open(removed_path, "w", encoding="utf-8") as f:
        json.dump(removed, f, indent=4)

    print(f"Saved cleaned dataset to {output_path}")
    print(f"Saved removed repos to {removed_path}")
    return cleaned


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_dataset.py <path_to_dataset.json>")
    else:
        clean_dataset(sys.argv[1])