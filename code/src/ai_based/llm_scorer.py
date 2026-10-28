import json
import subprocess
from pathlib import Path


def load_readme(repo_dir):
    path = Path(repo_dir) / "README.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


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

D2 — Usage clarity
- A concrete command, code snippet, workflow, or executable example in the README counts as evidence for score 2.
- External documentation, tutorials, or usage guides may count as score 1 if they are clearly linked and described.
- Score 0 if no usage information is present.

D3 — Purpose description
- A concise one- or two-sentence description may score 2 if it clearly explains what the software does and its intended domain or audience.
- Length is not required; clarity is.

D4 — Dependency description
- Score 2 when required and/or optional dependencies are explicitly listed in human-readable form.
- Score 1 when dependency information is only partially provided (e.g. pip install package[extras]).
- Score 0 when no meaningful dependency or environment information is provided.

D5 — Examples and tutorials
- Installation commands and test commands are not usage examples.
- Score 2 when the README contains a concrete example demonstrating the intended use of the software.
- Score 1 when clearly named tutorials, cookbooks, galleries, examples pages, or documentation resources are linked but no concrete example appears in the README.
- Score 0 when no examples or tutorials are provided.

D6 — Contribution information
- Score 2 when contribution guidance is provided together with at least one support or community channel (issue tracker, contributor guide, mailing list, forum, chat, Discord, discussions, etc.).
- Score 1 when contribution or support information is only partially present.
- Score 0 when neither contribution nor support information is available.

Dimensions to score:

D1 - Installation clarity: Can a new user install this software from the README alone?
D2 - Usage clarity: Can a new user understand how to run or use this software from the README alone?
D3 - Purpose description: Does the README clearly explain what the software does and why it exists?
D4 - Dependency description: Does the README describe in human-readable form what environment or dependencies are needed?
D5 - Examples or tutorials: Does the repository provide concrete examples that support reuse?
D6 - Contribution information: Does the README explain how to contribute or get support?

Repository: {repo_name}

README:
{readme_text}

Respond in JSON only, no other text:
{{
  "D1_installation": {{"score": 0, "confidence": "HIGH", "reasoning": "one sentence"}},
  "D2_usage": {{"score": 0, "confidence": "HIGH", "reasoning": "one sentence"}},
  "D3_purpose": {{"score": 0, "confidence": "HIGH", "reasoning": "one sentence"}},
  "D4_dependencies": {{"score": 0, "confidence": "HIGH", "reasoning": "one sentence"}},
  "D5_examples": {{"score": 0, "confidence": "HIGH", "reasoning": "one sentence"}},
  "D6_contribution": {{"score": 0, "confidence": "HIGH", "reasoning": "one sentence"}}
}}"""

def run_llm(prompt, model="llama3.1:8b"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip()


def parse_response(response):
    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        json_str = response[start:end]
        json_str = " ".join(json_str.split())
        return json.loads(json_str, strict=False)
    except Exception as e:
        print(f"Parse error: {e}")
        print(f"Raw response: {response}")
        return None


def score_llm(repo_dir, model="llama3.1:8b"):
    repo_name = Path(repo_dir).name
    readme_text = load_readme(repo_dir)

    if not readme_text:
        print(f"No README found for {repo_name}")
        return None

    prompt = build_prompt(repo_name, readme_text)
    print(f"Running LLM on {repo_name}...")
    response = run_llm(prompt, model)
    scores = parse_response(response)
    return scores


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]
    repo_dir = project_root / "data" / "pilot" / "healpy_healpy"
    scores = score_llm(repo_dir)

    if scores:
        print("\nLLM Scores for healpy_healpy:")
        for dim, result in scores.items():
            print(f"  {dim}: {result['score']} ({result['confidence']}) — {result['reasoning']}")