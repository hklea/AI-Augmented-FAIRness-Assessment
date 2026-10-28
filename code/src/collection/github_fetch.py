import requests
import json
from pathlib import Path

# Function to fetch repository metadata from GitHub API
def fetch_repo_metadata(owner, repo):

    # GitHub API endpoint for a repository
    url = f"https://api.github.com/repos/{owner}/{repo}"

    # Send GET request to GitHub
    response = requests.get(url)

    # Check if request failed
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return None

    # Convert JSON response into Python dictionary
    return response.json()


# Entry point of the script
if __name__ == "__main__":

    # Example repository:
    # https://github.com/scikit-learn/scikit-learn
    owner = "scikit-learn"
    repo = "scikit-learn"

    # Fetch repository data
    data = fetch_repo_metadata(owner, repo)

    # Print selected metadata fields
    if data:
        print("Repository name:", data["name"])
        print("Description:", data["description"])
        print("Stars:", data["stargazers_count"])
        print("Main language:", data["language"])

    # FAIR-related metadata
        print("License:", data["license"]["name"] if data["license"] else "No license")
        print("Topics:", data["topics"])
        print("Created at:", data["created_at"])
        print("Updated at:", data["updated_at"])    
        
    # Save metadata into JSON file
    project_root = Path(__file__).resolve().parents[3]
    output_path = project_root / "data" / "raw" / "sklearn_metadata.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Metadata saved successfully.")
