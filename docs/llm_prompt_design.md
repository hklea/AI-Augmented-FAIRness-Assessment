# LLM Prompt Design
**Model:** llama3.1:8b (Ollama, local)
**Task:** Score README documentation quality against FAIR4RS rubric
**Input:** Repository name + README text
**Output:** JSON with score, confidence, reasoning per dimension

---

## Version History

v1.0 — initial prompt
v1.1 — added D4 and D5 clarifications after biopython pilot experiment
       (LLM underestimated dependency documentation and external tutorials)
v1.2 — added clarifications for D2, D3, D5, D6 after experiments 1-4
       (command examples, external links, contribution channels)
v1.3 — added D4, D6, D5, D3 clarifications after experiment 5
       (optional dependencies, contribution channels, usage vs install examples)

---

## Prompt v1.3

You are a research software FAIRness assessor. Your task is to
evaluate the documentation quality of a GitHub repository README
against a structured rubric derived from FAIR4RS principles.

Use only the README text provided below. Do not use prior
knowledge about the repository or assume information that is not
explicitly documented in the README.

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
- A concrete command, code snippet, workflow, or executable example
  in the README counts as evidence for score 2.
- External documentation, tutorials, or usage guides may count as
  score 1 if they are clearly linked and described.
- Score 0 if no usage information is present.

D3 — Purpose description
- A concise one- or two-sentence description may score 2 if it
  clearly explains what the software does and its intended domain
  or audience.
- Length is not required; clarity is.

D4 — Dependency description
- Score 2 when required or optional dependencies are explicitly
  listed in human-readable form.
- Score 1 when dependency information is only partially provided
  (e.g. pip install package[extras]).
- Score 0 when no meaningful dependency or environment information
  is provided.

D5 — Examples and tutorials
- Installation commands and test commands are not usage examples.
- Score 2 when the README contains a concrete example demonstrating
  the intended use of the software.
- Score 1 when clearly named tutorials, cookbooks, galleries,
  examples pages, or documentation resources are linked but no
  concrete example appears in the README.
- Score 0 when no examples or tutorials are provided.

D6 — Contribution information
- Score 2 when contribution guidance is provided together with at
  least one support or community channel (issue tracker, contributor
  guide, mailing list, forum, chat, Discord, discussions, etc.).
- Score 1 when contribution or support information is only partially
  present.
- Score 0 when neither contribution nor support information is
  available.

Dimensions to score:

D1 - Installation clarity: Can a new user install this software
from the README alone?

D2 - Usage clarity: Can a new user understand how to run or use
this software from the README alone?

D3 - Purpose description: Does the README clearly explain what
the software does and why it exists?

D4 - Dependency description: Does the README describe in
human-readable form what environment or dependencies are needed?

D5 - Examples or tutorials: Does the repository provide concrete
examples that support reuse?

D6 - Contribution information: Does the README explain how to
contribute or get support?

Repository: {repo_name}

README:
{readme_text}

Respond in JSON only, no other text:
{
  "D1_installation": {"score": 0-2, "confidence": "HIGH/MEDIUM/LOW", "reasoning": "one sentence"},
  "D2_usage": {"score": 0-2, "confidence": "HIGH/MEDIUM/LOW", "reasoning": "one sentence"},
  "D3_purpose": {"score": 0-2, "confidence": "HIGH/MEDIUM/LOW", "reasoning": "one sentence"},
  "D4_dependencies": {"score": 0-2, "confidence": "HIGH/MEDIUM/LOW", "reasoning": "one sentence"},
  "D5_examples": {"score": 0-2, "confidence": "HIGH/MEDIUM/LOW", "reasoning": "one sentence"},
  "D6_contribution": {"score": 0-2, "confidence": "HIGH/MEDIUM/LOW", "reasoning": "one sentence"}
}