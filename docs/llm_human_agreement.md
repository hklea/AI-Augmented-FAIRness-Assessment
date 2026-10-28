# LLM vs Human Agreement Analysis
**Date:** 2026-07-22
**Model:** llama3.1:8b (temperature=0)
**Repositories:** 30 ground truth repositories
**Script:** code/src/llm_human_agreement.py

## Method

LLM-generated documentation quality scores (D1--D6) were compared
against manual annotations from two independent annotators. Agreement
was quantified using Cohen's linearly weighted Kappa, exact match
accuracy, and Mean Absolute Error (MAE). All Kappa values were
cross-validated against scikit-learn's cohen_kappa_score.

Two comparisons were performed:
- LLM vs primary annotator (thesis author)
- LLM vs second annotator (independent)

## Results

### LLM vs Primary Annotator (macro-avg κ=0.329)

| Dimension | Kappa | Exact | MAE | LLM lower | LLM higher |
|-----------|-------|-------|-----|-----------|------------|
| D1 Installation | 0.605 | 70.0% | 0.333 | 8 | 1 |
| D2 Usage | 0.274 | 46.7% | 0.567 | 14 | 2 |
| D3 Purpose | -0.071 | 86.7% | 0.133 | 2 | 2 |
| D4 Dependencies | 0.480 | 60.0% | 0.433 | 8 | 4 |
| D5 Examples | 0.192 | 36.7% | 0.700 | 17 | 2 |
| D6 Contribution | 0.494 | 63.3% | 0.400 | 9 | 2 |

### LLM vs Second Annotator (macro-avg κ=0.275)

| Dimension | Kappa | Exact | MAE | LLM lower | LLM higher |
|-----------|-------|-------|-----|-----------|------------|
| D1 Installation | 0.480 | 70.0% | 0.433 | 9 | 0 |
| D2 Usage | 0.276 | 50.0% | 0.600 | 13 | 2 |
| D3 Purpose | -0.056 | 86.7% | 0.167 | 2 | 2 |
| D4 Dependencies | 0.338 | 53.3% | 0.567 | 7 | 7 |
| D5 Examples | 0.156 | 30.0% | 0.867 | 21 | 0 |
| D6 Contribution | 0.454 | 60.0% | 0.433 | 9 | 3 |

## Key Findings

### Finding 1 — LLM systematically scores lower than humans
Across both annotators and almost all dimensions, the LLM assigned
lower scores than human annotators more frequently than higher scores.
This is most pronounced in D5 (17/30 lower vs A1, 21/30 lower vs A2)
and D2 (14/30 lower vs A1, 13/30 lower vs A2).

This systematic underscoring is consistent with the external link
policy — the LLM evaluates only README text and cannot access linked
documentation. Repos that link to tutorials or usage guides rather
than providing them inline receive lower LLM scores than human
annotators assign after considering the existence of those resources.

### Finding 2 — D5 and D2 show weakest agreement
D5 (Examples) and D2 (Usage) show the lowest Kappa values against
both annotators. These are the dimensions most affected by the
external link policy — usage examples and tutorials are frequently
provided via external links rather than inline.

### Finding 3 — D1 shows strongest agreement
D1 (Installation) achieved the highest Kappa against both annotators
(0.605 vs A1, 0.480 vs A2). Installation instructions are typically
provided inline as pip install or conda install commands, making them
directly accessible to the LLM.

### Finding 4 — D3 negative Kappa is a prevalence effect
D3 (Purpose) shows κ≈-0.07 despite 86.7% exact agreement. This is
the same prevalence paradox observed in A1 during inter-annotator
analysis. Almost all repositories (28/30) received a human score of
2 for purpose description, leaving insufficient variation for
meaningful Kappa computation.

### Finding 5 — Agreement is consistent across both annotators
The pattern of strong and weak dimensions is consistent between the
two comparisons (LLM vs A1 and LLM vs A2), suggesting the findings
reflect genuine LLM behaviour rather than idiosyncrasies of one
annotator's scoring style.

## Comparison with Inter-Annotator Agreement

| Comparison | Macro-avg Kappa |
|------------|----------------|
| Human A1 vs Human A2 | 0.709 |
| LLM vs Human A1 | 0.329 |
| LLM vs Human A2 | 0.275 |

Human-human agreement substantially exceeds LLM-human agreement,
confirming that the LLM assessment is less reliable than human
annotation for this task. This motivates the hybrid approach —
combining deterministic rule-based checks with LLM-based scoring
while flagging uncertain assessments for human review.

## Conclusion

LLM-human agreement was moderate overall (macro-avg κ=0.329 vs
primary annotator), substantially lower than inter-annotator
agreement (κ=0.709). The weakest dimensions were D5 and D2, where
the LLM systematically assigned lower scores than human annotators,
likely due to its inability to access external documentation.
The strongest dimension was D1, where installation instructions
are typically provided inline. These findings inform the discussion
of LLM limitations in Chapter 6 and support the design decision
to present LLM scores alongside confidence flags rather than as
standalone assessments.