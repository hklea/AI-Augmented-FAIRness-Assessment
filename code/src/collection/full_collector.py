import os
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

from config import TOPICS, REPOS_PER_TOPIC, MIN_STARS
from filters import is_valid
from save_results import save_dataset

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN not found. Check your .env file.")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def search_repositories(topic, per_page=30, page=1):
    query = f"topic:{topic} stars:>{MIN_STARS} archived:false"
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        print("  Rate limit hit — waiting 60 seconds...")
        time.sleep(60)
        return search_repositories(topic, per_page, page)
    else:
        print(f"  Error {response.status_code}: {response.text}")
        return None


def extract_repo_entry(repo, source_topic):
    return {
        "id": repo["id"],
        "owner": repo["owner"]["login"],
        "repo": repo["name"],
        "full_name": repo["full_name"],
        "description": repo.get("description", ""),
        "language": repo.get("language", ""),
        "stars": repo["stargazers_count"],
        "topics": repo.get("topics", []),
        "pushed_at": repo.get("pushed_at", ""),
        "created_at": repo.get("created_at", ""),
        "license": repo["license"]["name"] if repo.get("license") else "",
        "source_topic": source_topic,
        "url": repo["html_url"]
    }


def collect_full_dataset():
    project_root = Path(__file__).resolve().parents[3]
    output_dir = project_root / "data" / "raw"

    all_repos = []
    seen_ids = set()

    for topic in TOPICS:
        print(f"\nSearching topic: {topic}")
        collected = 0
        page = 1

        while collected < REPOS_PER_TOPIC:
            results = search_repositories(topic, per_page=30, page=page)
            if not results or not results.get("items"):
                break

            for repo in results["items"]:
                if collected >= REPOS_PER_TOPIC:
                    break
                if repo["id"] in seen_ids:
                    continue
                if not is_valid(repo):
                    continue

                seen_ids.add(repo["id"])
                all_repos.append(extract_repo_entry(repo, topic))
                collected += 1
                print(f"  [{collected}/{REPOS_PER_TOPIC}] {repo['full_name']}")

            page += 1
            time.sleep(1)

        print(f"  Done: {collected} repos for topic: {topic}")

    print(f"\nTotal unique repositories collected: {len(all_repos)}")
    save_dataset(all_repos, output_dir)


if __name__ == "__main__":
    collect_full_dataset()