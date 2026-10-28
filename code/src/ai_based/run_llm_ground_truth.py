import csv
import json
import requests
from datetime import datetime
from pathlib import Path


MODEL = "llama3.1:8b"
MAX_CHARS = 12000

DIMS = [
    "D1_installation",
    "D2_usage",
    "D3_purpose",
    "D4_dependencies",
    "D5_examples",
    "D6_contribution",
]

SCORE_ITEM_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "integer", "enum": [0, 1, 2]},
        "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
        "reasoning": {"type": "string"},
    },
    "required": ["score", "confidence", "reasoning"],
    "additionalProperties": False,
}

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {dim: SCORE_ITEM_SCHEMA for dim in DIMS},
    "required": DIMS,
    "additionalProperties": False,
}


def load_readme(repo_dir):
    for filename in ["README.md", "README.rst", "README.txt", "README"]:
        path = Path(repo_dir) / filename
        if path.exists():
            return path.read_text(encoding="utf-8", errors="ignore")
    return ""


def build_prompt(repo_name, readme_text):
    return f"""You are a research software FAIRness assessor. Your task is to evaluate the documentation quality of a GitHub repository README against a structured rubric derived from FAIR4RS principles.

Use only the README text provided below. Do not use prior knowledge about the repository or assume information that is not explicitly documented in the README.

Score each dimension on a 0-2 scale:
- 0 = not present
- 1 = partially present or incomplete
- 2 = clearly and completely present

Important scoring guidance:
- Use only information explicitly visible in the README.
- Do not assume content exists behind external links.
- External links alone generally support a score of 1, not 2.
- Score based on the evidence present in the README itself.

D1 — Installation clarity
- Score 2 when complete, actionable installation steps and required prerequisites are provided.
- Score 1 when installation information exists but is incomplete or mainly links externally.
- Score 0 when no installation instructions are present.

D2 — Usage clarity
- Score 2 when a concrete command, code snippet, workflow, or executable example is present in the README.
- Score 1 when external documentation or tutorials are clearly linked but no inline example appears.
- Score 0 when no usage information is present.

D3 — Purpose description
- Score 2 when the README clearly explains what the software does and its intended domain or audience.
- Score 1 when a description is present but vague or incomplete.
- Score 0 when no description of purpose is present.

D4 — Dependency description
- Score 2 when required and/or optional dependencies are explicitly listed in human-readable form.
- Score 1 when dependency information is only partially provided.
- Score 0 when no meaningful dependency or environment information is provided.

D5 — Examples and tutorials
- Installation, testing, contribution, development setup, and generic documentation links do not count as examples.
- Score 2 only when the README contains a meaningful usage example, or explicitly links to an example gallery or tutorial demonstrating software use and that linked content is included in the supplied evidence.
- Score 1 when the README explicitly references an example gallery, tutorial, cookbook, or example notebooks, but their content is not supplied.
- Score 0 when no examples or tutorials are mentioned.

D6 — Contribution information
- Score 2 when contribution guidance is provided together with at least one support or community channel.
- Score 1 when contribution or support information is only partially present.
- Score 0 when neither contribution nor support information is available.

For every score, cite the specific README evidence in the reasoning.
Do not describe a generic documentation, installation, or contribution link as a usage example or tutorial.

Repository: {repo_name}

README:
{readme_text}

Evaluate the README carefully and assign evidence-based scores.

Do not copy default or placeholder scores.
Return one result for every required dimension using the supplied JSON schema.
Every score must reflect the README evidence and must be exactly 0, 1, or 2.
"""


def run_llm(prompt, model=MODEL):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": OUTPUT_SCHEMA,
        "options": {
            "temperature": 0,
        },
    }
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=300,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"  Ollama API error: {error}")
        return ""
    data = response.json()
    return data.get("response", "").strip()


def parse_response(response):
    try:
        parsed = json.loads(response)
        for dim in DIMS:
            if dim not in parsed:
                print(f"  Missing dimension: {dim}")
                return None
            if parsed[dim]["score"] not in [0, 1, 2]:
                print(f"  Invalid score for {dim}: {parsed[dim]['score']}")
                return None
            if parsed[dim]["confidence"] not in ["HIGH", "MEDIUM", "LOW"]:
                print(f"  Invalid confidence for {dim}")
                return None
        return parsed
    except Exception as e:
        print(f"  Parse error: {e}")
        return None


def already_scored(repo_name, parsed_output_dir):
    return (parsed_output_dir / f"{repo_name}.json").exists()


def save_raw_output(repo_name, raw_response, raw_output_dir, attempt=1):
    raw_output_dir.mkdir(parents=True, exist_ok=True)
    with open(raw_output_dir / f"{repo_name}_attempt{attempt}.txt", "w", encoding="utf-8") as f:
        f.write(raw_response)


def save_parsed_output(repo_name, scores, parsed_output_dir):
    parsed_output_dir.mkdir(parents=True, exist_ok=True)
    with open(parsed_output_dir / f"{repo_name}.json", "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)


def append_result(row, output_path):
    file_exists = output_path.exists()
    fieldnames = [
        "repo", "model", "timestamp",
        "D1_score", "D1_confidence", "D1_reasoning",
        "D2_score", "D2_confidence", "D2_reasoning",
        "D3_score", "D3_confidence", "D3_reasoning",
        "D4_score", "D4_confidence", "D4_reasoning",
        "D5_score", "D5_confidence", "D5_reasoning",
        "D6_score", "D6_confidence", "D6_reasoning",
        "llm_total"
    ]
    with open(output_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]
    ground_truth_dir = project_root / "data" / "ground_truth"
    output_path = project_root / "data" / "results" / "llm_scores_ground_truth.csv"
    raw_output_dir = project_root / "data" / "results" / "raw_llm" / MODEL.replace(":", "_")
    parsed_output_dir = project_root / "data" / "results" / "parsed_llm" / MODEL.replace(":", "_")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    repos = sorted([d for d in ground_truth_dir.iterdir()
                    if d.is_dir() and not d.name.startswith(".")])

    print(f"Found {len(repos)} repos")
    print(f"Model: {MODEL}")
    print(f"Output: {output_path}\n")

    newly_scored = 0
    skipped = 0
    failed = 0

    for i, repo_dir in enumerate(repos):
        repo_name = repo_dir.name
        print(f"[{i+1}/{len(repos)}] {repo_name}")

        if already_scored(repo_name, parsed_output_dir):
            print(f"  Already scored — skipping")
            skipped += 1
            continue

        readme_text = load_readme(repo_dir)
        if not readme_text:
            print(f"  No README found — skipping")
            failed += 1
            continue

        if len(readme_text) > MAX_CHARS:
            print(f"  README truncated ({len(readme_text)} → {MAX_CHARS} chars)")
            readme_text = readme_text[:MAX_CHARS]

        prompt = build_prompt(repo_name, readme_text)

        # Attempt 1
        raw_response = run_llm(prompt)
        if raw_response:
            save_raw_output(repo_name, raw_response, raw_output_dir, attempt=1)
        scores = parse_response(raw_response) if raw_response else None

        # Attempt 2 if needed
        if scores is None:
            print(f"  Retrying...")
            raw_response = run_llm(prompt)
            if raw_response:
                save_raw_output(repo_name, raw_response, raw_output_dir, attempt=2)
            scores = parse_response(raw_response) if raw_response else None

        if scores is None:
            print(f"  Failed after retry — skipping")
            failed += 1
            continue

        row = {
            "repo": repo_name,
            "model": MODEL,
            "timestamp": datetime.now().isoformat(),
        }
        total = 0
        for dim in DIMS:
            short = dim.split("_")[0]
            row[f"{short}_score"] = scores[dim]["score"]
            row[f"{short}_confidence"] = scores[dim]["confidence"]
            row[f"{short}_reasoning"] = scores[dim]["reasoning"]
            total += scores[dim]["score"]
        row["llm_total"] = total

        append_result(row, output_path)
        save_parsed_output(repo_name, scores, parsed_output_dir)
        newly_scored += 1
        print(f"  D1={row['D1_score']} D2={row['D2_score']} D3={row['D3_score']} "
              f"D4={row['D4_score']} D5={row['D5_score']} D6={row['D6_score']} "
              f"Total={total}/12")

    print(f"\nDone. Newly scored: {newly_scored}, Skipped: {skipped}, Failed: {failed}")