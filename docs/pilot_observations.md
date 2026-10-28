# Pilot Annotation Observations
**Date:** 2026-05-29
**Repos annotated:** 10
**Guidelines version:** 1.3

## Key Findings

### Finding 1 — Rule-based and AI-based scores are not strongly correlated
Rule-based FAIR indicators and README documentation quality are 
not strongly correlated. Several repositories with strong FAIR 
metadata (e.g. astropy, OpenMS) scored only moderately on 
qualitative README dimensions, while repositories with weaker 
FAIR metadata (e.g. networkx, nbconvert) often provided stronger 
onboarding documentation and executable examples.

### Finding 2 — Repositories with weak FAIR metadata can provide strong onboarding
This preliminary observation suggests that rule-based tools may 
not capture important aspects of documentation quality and 
software onboarding. The differing patterns between rule-based and AI-based scores 
observed in several repositories warrant further investigation in the full evaluation.

### Finding 3 — External documentation links create scoring ambiguity for D1, D2, D5
Most repos score 1 on installation, usage and examples — they 
link to external tutorials but provide nothing actionable inline. 
Only nbconvert and networkx provided real inline executable 
examples scoring 2. The boundary between score 1 and 2 for 
external links required explicit clarification in the guidelines.

### Finding 4 — Rule-based file detection required iterative refinement
The collector initially missed:
- LICENSE.rst (sunpy) — fixed in v1.1
- COPYING (healpy, scikit-learn) — fixed in v1.3

This demonstrates a concrete limitation of rule-based approaches: 
they are only as complete as the set of patterns they check for. 
A rule-based tool cannot detect what it was not explicitly 
programmed to find. This is a real empirical finding from the 
pilot data, not a theoretical argument, and directly supports 
the thesis argument that rule-based assessment has systematic 
blind spots.

Specific case: during pilot annotation of sunpy/sunpy, the 
collector returned A1 = 0 despite the repository having a valid 
open source license stored as LICENSE.rst. This false negative 
would have gone undetected without manual verification.

### Finding 5 — D4 was one of the weakest dimensions in the pilot set
Dependency documentation in READMEs was systematically weak 
across the pilot repositories. Most repos scored 0 or 1 on D4. 
Only healpy and biopython scored 2. This suggests that even 
projects with generally good documentation habits rarely explain 
their environment requirements in human-readable form in the README.

### Finding 6 — Large well-known projects do not always have stronger READMEs
numpy and astropy have strong rule-based scores but D1 and D2 
scores of 0-1. numpy has no installation instructions at all in 
its README. This is a preliminary observation that would need 
to be confirmed across the full dataset.

### Finding 7 — Pilot annotation improved the rubric
The pilot phase exposed several ambiguous cases that were not 
anticipated in the initial guidelines. Three guideline revisions 
(v1.1–v1.3) were required to handle real-world repository 
practices such as LICENSE.rst, COPYING, and DOI badges without 
explicit citation instructions. This demonstrates the value of 
pilot annotation before constructing the final ground truth 
dataset and confirms that iterative rubric refinement is a 
necessary part of the annotation methodology.

## Collector Issues Found and Fixed
- v1.1: LICENSE.rst added to A1 variants after sunpy annotation
- v1.3: COPYING and COPYING.txt added after scikit-learn annotation

## Guidelines Revisions
- v1.1: LICENSE.rst added to license file variants under A1
- v1.2: R2 edge case — DOI badge without explicit citation
        instruction does not count
- v1.3: COPYING and COPYING.txt added to license file variants

## Where These Findings Appear in the Thesis
- Methodology chapter — rule-based component limitations,
  iterative guideline refinement process
- Results chapter — rule-based vs AI-based score divergence
  as primary empirical finding
- Discussion chapter — evidence that rule-based tools miss valid
  FAIR indicators, motivation for hybrid approach
- Evaluation chapter — LICENSE.rst false negative as concrete
  example of rule-based blind spot