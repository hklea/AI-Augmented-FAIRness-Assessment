# LLM Scoring Results — Ground Truth Set
**Date:** 2026-07-13
**Model:** llama3.1:8b
**Repos scored:** 30/30
**Script:** code/src/ai_based/run_llm_ground_truth.py
**Results file:** data/results/llm_scores_ground_truth.csv

## Scoring Summary

- Average LLM total: 6.7/12
- Minimum: 2/12
- Maximum: 11/12
- Scale: 6 dimensions × 0–2 each (max 12)

## Method

The LLM scorer uses the Ollama API (llama3.1:8b, temperature=0) with
structured JSON output enforced via a schema. Each repository README
was provided as input and scored against six documentation quality
dimensions derived from FAIR4RS reusability indicators.

READMEs exceeding 12,000 characters were truncated. One repository
(Ouranosinc/xclim, 14,262 chars) was truncated to 12,000 characters.
This is documented as a limitation.

The LLM receives only README text and cannot access external links.
Consequently, linked resources not reproduced in the README are
treated as partial evidence (score 1) rather than complete evidence
(score 2). This design choice is considered when interpreting
differences between manual and LLM assessments.

The final implementation uses Ollama's HTTP API with structured JSON
output validation rather than parsing free-form text responses,
improving reproducibility and reducing parsing failures.
## Technical Notes

- Early development runs produced invalid JSON outputs for two repositories
  (OpenMS and xclim), including non-integer scores outside the permitted
  0–2 range.
- The final implementation uses Ollama's structured JSON output with a
  JSON schema to enforce valid scores and improve robustness.
- Raw model outputs are stored in
  `data/results/raw_llm/llama3.1_8b/`.
- Parsed JSON outputs are stored in
  `data/results/parsed_llm/llama3.1_8b/`.
- Resume logic is based on the presence of successfully parsed JSON files.

### Observations

The LLM scores span a wide range (2–11/12), indicating substantial
variation in README documentation quality across the ground-truth
repositories. Most repositories received scores between 5 and 8,
suggesting moderate documentation completeness according to the
defined rubric.

These scores will be compared against the manual annotations during
the evaluation to assess agreement between human and LLM-based
assessment.

## Score Distribution

| LLM Total | Count |
|-----------|-------|
| 2/12 | 2 |
| 3/12 | 1 |
| 4/12 | 2 |
| 5/12 | 5 |
| 6/12 | 3 |
| 7/12 | 5 |
| 8/12 | 5 |
| 9/12 | 3 |
| 10/12 | 3 |
| 11/12 | 1 |