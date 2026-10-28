import json
import csv
from pathlib import Path
from datetime import datetime, timezone


def save_dataset(repos, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    json_path = output_dir / f"full_dataset_{timestamp}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=4)

    csv_path = output_dir / f"full_dataset_{timestamp}.csv"
    if repos:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=repos[0].keys())
            writer.writeheader()
            writer.writerows(repos)

    print(f"Saved {len(repos)} repos to {json_path}")
    print(f"CSV summary: {csv_path}")
    return json_path, csv_path