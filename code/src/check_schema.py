import json
from pathlib import Path

gt_dir = Path("data/ground_truth")
for repo_dir in sorted(gt_dir.iterdir()):
    if not repo_dir.is_dir():
        continue
    f = repo_dir / "fair_file_checks.json"
    if not f.exists():
        continue
    data = json.loads(f.read_text(encoding="utf-8"))
    if "go.mod" not in data:
        print(repo_dir.name, "- OLD SCHEMA (missing go.mod key)")