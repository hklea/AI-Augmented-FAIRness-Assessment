# LLM Scoring Experiments
**Model:** llama3.1:8b (Ollama, local)

---

## Experiment 1 — Biopython
**Date:** 2026-05-31

### Scores

| Dimension | Human | LLM v1.0 | LLM v1.1 | Observation |
|---|---:|---:|---:|---|
| D1 installation | 2 | 2 | 2 | stable match |
| D2 usage | 1 | 1 | 0 | regressed in v1.1 |
| D3 purpose | 2 | 2 | 1 | regressed in v1.1 |
| D4 dependencies | 2 | 1 | 2 | improved after clarification |
| D5 examples | 1 | 0 | 0 | consistently too strict |
| D6 contribution | 2 | 2 | 2 | stable match |

**Agreement**
- Prompt v1.0: 4/6 (66.7%)
- Prompt v1.1: 4/6 (66.7%)

### Observations
- D4 improved after explicit clarification.
- D5 remained too strict despite prompt update.
- D2 and D3 became less accurate in v1.1.
- Prompt changes can improve one dimension while degrading another.

---

## Experiment 2 — Healpy
**Date:** 2026-05-31

### Scores

| Dimension | Human | LLM run 1 | LLM run 2 | Observation |
|---|---:|---:|---:|---|
| D1 installation | 2 | 2 | 2 | stable match |
| D2 usage | 1 | 0 | 0 | consistently too strict |
| D3 purpose | 2 | 2 | 1 | unstable |
| D4 dependencies | 2 | 1 | 0 | too strict and unstable |
| D5 examples | 2 | 1 | 1 | too strict on external tutorials |
| D6 contribution | 2 | 1 | 2 | unstable |

**Agreement**
- Run 1: 3/6 (50%)
- Run 2: 3/6 (50%)

### Observations
- Repeated runs on the same repository produced different scores.
- D2 was consistently underestimated.
- D5 was consistently underestimated.
- D3, D4 and D6 showed instability across runs.
- Output instability provides empirical motivation for the planned confidence/uncertainty layer.

---

## Experiment 3 — NetworkX (Prompt v1.1)
**Date:** 2026-05-31

### Scores

| Dimension | Human | LLM run 1 | LLM run 2 | Observation |
|---|---:|---:|---:|---|
| D1 installation | 2 | 2 | 2 | stable match |
| D2 usage | 2 | 2 | 1 | unstable |
| D3 purpose | 2 | 2 | 2 | stable match |
| D4 dependencies | 1 | 0 | 1 | unstable, second run matched |
| D5 examples | 2 | 2 | 2 | stable match |
| D6 contribution | 2 | 1 | 1 | consistently underestimated |

**Agreement**
- Run 1: 4/6 (66.7%)
- Run 2: 4/6 (66.7%)

### Observations
- The model correctly identified inline executable examples for D5 in both runs.
- D2 changed from 2 to 1 between runs despite identical input.
- D4 changed from 0 to 1 between runs despite identical input.
- D6 was consistently scored lower than the human annotation.
- Repeated runs continue to show output instability, supporting the need for a confidence/uncertainty mechanism.

---

## Experiment 4 — nbconvert (Prompt v1.1)
**Date:** 2026-05-31

### Scores

| Dimension | Human | LLM run 1 | LLM run 2 | Observation |
|---|---:|---:|---:|---|
| D1 installation | 2 | 1 | 1 | consistently underestimated |
| D2 usage | 2 | 0 | 0 | consistently missed command example |
| D3 purpose | 2 | 2 | 0 | unstable |
| D4 dependencies | 1 | 1 | 0 | unstable |
| D5 examples | 2 | 1 | 1 | consistently underestimated |
| D6 contribution | 2 | 2 | 2 | stable match |

**Agreement**
- Run 1: 3/6 (50%)
- Run 2: 1/6 (16.7%)

### Observations
- The model failed to recognize the `jupyter nbconvert --to html mynotebook.ipynb` command as a valid usage example for D2.
- The model consistently underestimated D5 despite the README containing an inline command example and a linked examples repository.
- D3 changed from 2 to 0 across repeated runs, showing strong output instability.
- D6 was the only consistently correct dimension.
- This experiment provides strong evidence that Prompt v1.1 is insufficient for command-line tool READMEs.


---

## Prompt v1.2 Evaluation
**Date:** 2026-05-31
**Repositories:** Biopython, Healpy, NetworkX, nbconvert

### Scores

**Biopython**
| Dimension | Human | LLM v1.2 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 1 | 1 | ✓ |
| D3 purpose | 2 | 2 | ✓ |
| D4 dependencies | 2 | 1 | ✗ |
| D5 examples | 1 | 2 | ✗ overcorrected |
| D6 contribution | 2 | 2 | ✓ |

**Agreement: 4/6 (66.7%)**

**Healpy**
| Dimension | Human | LLM v1.2 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 1 | 0 | ✗ |
| D3 purpose | 2 | 2 | ✓ |
| D4 dependencies | 2 | 0 | ✗ |
| D5 examples | 2 | 1 | ✗ |
| D6 contribution | 2 | 2 | ✓ |

**Agreement: 3/6 (50%)**

**NetworkX**
| Dimension | Human | LLM v1.2 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 2 | 2 | ✓ |
| D3 purpose | 2 | 2 | ✓ |
| D4 dependencies | 1 | 0 | ✗ |
| D5 examples | 2 | 2 | ✓ |
| D6 contribution | 2 | 0 | ✗ |

**Agreement: 4/6 (66.7%)**

**nbconvert**
| Dimension | Human | LLM v1.2 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 2 | 2 | ✓ |
| D3 purpose | 2 | 1 | ✗ |
| D4 dependencies | 1 | 2 | ✗ overcorrected |
| D5 examples | 2 | 1 | ✗ |
| D6 contribution | 2 | 2 | ✓ |

**Agreement: 3/6 (50%)**

### Overall v1.2 observations
- D2 improved significantly — inline command examples now correctly 
  scored as 2 in networkx and nbconvert.
- D3 improved in most cases — short descriptions now accepted as score 2.
- D4 became less reliable — both overcorrection and undercorrection observed.
- D5 remains inconsistent — external tutorial links still not reliably scored as 1.
- D6 regressed in networkx — scored 0 despite contribution channels present.
- Output instability persists across all repos and dimensions.

### Comparison v1.1 vs v1.2
- v1.2 improved D2 and D3 overall.
- v1.2 degraded D4 and D6 in some repos.
- Prompt changes have cascading effects — improving one dimension 
  can degrade another.
- This is a known challenge in LLM prompt engineering.

### Average Agreement

| Prompt Version | Average Agreement |
|---|---:|
| v1.0 | 66.7% (Biopython only) |
| v1.1 | ~58% across tested repos |
| v1.2 | 58.3% across tested repos |

Observation:
Prompt v1.2 improved D2 and D3 scoring but did not increase overall agreement. Improvements in some dimensions were offset by regressions in others.


---

## Experiment 6 — All four repos (Prompt v1.3)
**Date:** 2026-05-31

### Scores

**Biopython**
| Dimension | Human | LLM v1.3 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 1 | 0 | ✗ |
| D3 purpose | 2 | 1 | ✗ |
| D4 dependencies | 2 | 2 | ✓ |
| D5 examples | 1 | 1 | ✓ |
| D6 contribution | 2 | 2 | ✓ |

**Agreement: 4/6 (66.7%)**

**Healpy**
| Dimension | Human | LLM v1.3 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 1 | 0 | ✗ |
| D3 purpose | 2 | 2 | ✓ |
| D4 dependencies | 2 | 1 | ✗ |
| D5 examples | 2 | 0 | ✗ |
| D6 contribution | 2 | 2 | ✓ |

**Agreement: 3/6 (50%)**

**NetworkX**
| Dimension | Human | LLM v1.3 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 2 | 2 | ✓ |
| D3 purpose | 2 | 1 | ✗ |
| D4 dependencies | 1 | 2 | ✗ |
| D5 examples | 2 | 1 | ✗ |
| D6 contribution | 2 | 2 | ✓ |

**Agreement: 3/6 (50%)**

**nbconvert**
| Dimension | Human | LLM v1.3 | Match |
|---|---:|---:|---|
| D1 installation | 2 | 2 | ✓ |
| D2 usage | 2 | 0 | ✗ |
| D3 purpose | 2 | 1 | ✗ |
| D4 dependencies | 1 | 0 | ✗ |
| D5 examples | 2 | 1 | ✗ |
| D6 contribution | 2 | 0 | ✗ |

**Agreement: 1/6 (16.7%)**

### Overall v1.3 Agreement
**11/24 = 45.8%** — lower than v1.2

### Observations
- D2 regressed in biopython and nbconvert despite clarifications.
- D5 regressed in healpy — scored 0 despite tutorial links present.
- D6 regressed in nbconvert — scored 0 despite community channels present.
- v1.3 did not improve over v1.2 overall.
- Further prompt iteration shows diminishing returns.
- This is a key finding: prompt engineering alone cannot fully resolve
  LLM scoring instability on this task with llama3.1:8b.

### Summary across all prompt versions

| Prompt | Biopython | Healpy | NetworkX | nbconvert | Average |
|---|---:|---:|---:|---:|---:|
| v1.0 | 4/6 (66.7%) | — | — | — | 66.7% |
| v1.1 | 4/6 (66.7%) | 3/6 (50%) | 4/6 (66.7%) | 3/6 (50%) | 58.3% |
| v1.2 | 4/6 (66.7%) | 3/6 (50%) | 4/6 (66.7%) | 3/6 (50%) | 58.3% |
| v1.3 | 4/6 (66.7%) | 3/6 (50%) | 3/6 (50%) | 1/6 (16.7%) | 45.8% |

### Conclusion
Prompt v1.2 produced the best overall agreement at 58.3%.
Further iteration did not improve results. The remaining disagreements
appear to reflect model-level limitations rather than prompt ambiguity.
Prompt v1.2 is selected as the final prompt for the AI-based component.


### Addendum — Healpy additional run (Prompt v1.3)
A third run on Healpy produced 4/6 agreement (vs 3/6 in run 1).
D4 changed from 1 to 2, D5 changed from 0 to 1.
This further confirms output instability across repeated runs.
Dimensions with inconsistent scores across runs should be flagged
as uncertain and recommended for human review.