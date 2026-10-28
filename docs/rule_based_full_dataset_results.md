# Full Dataset Summary and Rule-Based Scoring Statistics
**Date:** 2026-07-12
**Dataset:** 188 research software repositories
**Scorer version:** 2.0

## Dataset Overview
- Total repositories: 188
- Research domains: 10 (bioinformatics, computational-biology, astronomy,
  neuroscience, climate-science, scientific-computing, research-software,
  cheminformatics, computational-physics, reproducible-research)
- Collection method: GitHub Search API, topic-based queries
- Cleaning: 198 collected → 188 after keyword filtering

## Language Distribution
| Language | Count | Percentage |
|----------|-------|------------|
| Python | 86 | 46% |
| C++ | 29 | 15% |
| Jupyter Notebook | 18 | 10% |
| Unknown | 10 | 5% |
| HTML | 6 | 3% |
| Go | 5 | 3% |
| JavaScript | 4 | 2% |
| Rust | 4 | 2% |
| Julia | 4 | 2% |
| R | 4 | 2% |
| C | 4 | 2% |
| Other | 14 | 7% |

## Rule-Based Scoring Results (Full Dataset)
The rule-based scorer evaluates six binary indicators (F1, F2, A1, I1,
R1, and R2), giving a maximum possible score of 6.

**Results file:** rule_based_scores_full.csv
**Repos scored:** 188
**Repos skipped:** 0
**Average score:** 3.86/6

### Score Distribution
| Score | Count | Percentage |
|-------|-------|------------|
| 6/6 | 15 | 8% |
| 5/6 | 43 | 23% |
| 4/6 | 61 | 32% |
| 3/6 | 42 | 22% |
| 2/6 | 23 | 12% |
| 1/6 | 4 | 2% |

### Indicator Frequencies
| Indicator | Description | Positive | Percentage |
|-----------|-------------|----------|------------|
| F1 | Persistent identifier (DOI/Zenodo) | 95/188 | 51% |
| F2 | Structured metadata (CITATION.cff/codemeta) | 58/188 | 31% |
| A1 | License file present | 182/188 | 97% |
| I1 | Dependency file present | 123/188 | 65% |
| R1 | README present | 188/188 | 100% |
| R2 | Citation information present | 79/188 | 42% |

### Observations
The observed score distribution spans the full range from 1/6 to 6/6,
indicating substantial variability in metadata-based FAIR compliance
across the dataset.

All 188 repositories contain a README file (R1=100%), while software
licensing is also widely adopted (A1=97%). In contrast, structured 
metadata files (F2=31%), persistent identifiers (F1=51%), and citation 
guidance (R2=42%) are substantially less common.

---

## Ground Truth Scoring Results (30 repos)
**Results file:** rule_based_scores_ground_truth.csv
**Repos scored:** 30
**Repos skipped:** 0

The 30 ground-truth repositories were used to validate the rule-based
implementation against manually assigned annotations following the
finalized annotation guidelines (v1.4). Two manual annotations were
updated during the validation process:
- scipy/scipy: F2 corrected from 1 to 0
- mne-tools/mne-python: R2 corrected from 1 to 0

These results establish the metadata-based baseline that will be compared
with the AI-based documentation assessment in the subsequent evaluation.