import requests
from pathlib import Path


# Function to fetch repository README
def fetch_readme(owner, repo):

    # GitHub README API endpoint
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    # Ask GitHub to return raw markdown content
    headers = {
        "Accept": "application/vnd.github.raw"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return None

    return response.text


if __name__ == "__main__":

    owner = "scikit-learn"
    repo = "scikit-learn"

    # Fetch README content
    readme = fetch_readme(owner, repo)

    if readme:

        # Print first 500 characters only
        print(readme[:500])

        # Get project root directory
        project_root = Path(__file__).resolve().parents[3]

        # Create output path
        output_path = project_root / "data" / "raw" / "sklearn_README.md"

        # Save README markdown file
        with output_path.open("w", encoding="utf-8") as file:
            file.write(readme)

        print("README saved successfully.")