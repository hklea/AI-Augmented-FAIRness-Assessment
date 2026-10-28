# Inter-Annotator Agreement
**Date:** 2026-07-22
**Annotators:** 2 (primary: thesis author, secondary: independent annotator)
**Repositories:** 30 ground truth repositories
**Guidelines version:** v1.4
**Script:** code/src/compute_kappa.py

## Method

The second annotator independently annotated all 30 ground truth
repositories using the finalised annotation guidelines (v1.4) and
the pre-fetched README files and FAIR file presence data provided
in the annotation package. No primary annotations were shared
before the second annotator completed their work.

Inter-annotator agreement was quantified using:
- Cohen's unweighted Kappa for binary rule-based indicators (F1-R2)
- Cohen's linearly weighted Kappa for ordinal AI-based dimensions (D1-D6)

All Kappa values were cross-validated against scikit-learn's
cohen_kappa_score implementation and confirmed to match.

## Results

### Rule-Based Indicators

| Indicator | Kappa | Exact | Note |
|-----------|-------|-------|------|
| F1 — Persistent identifier | 0.710 | 90.0% | Substantial |
| F2 — Structured metadata | 1.000 | 100.0% | Almost perfect |
| A1 — License | 0.000 | 96.7% | Prevalence effect |
| I1 — Dependency file | 0.286 | 76.7% | Fair — see notes |
| R1 — README present | undefined | 100.0% | Single observed class |
| R2 — Citation information | 0.796 | 90.0% | Substantial |
| **Macro-avg (defined only)** | **0.558** | | Excludes undefined R1 |

### AI-Based Dimensions

| Dimension | Kappa | Exact | MAE | Note |
|-----------|-------|-------|-----|------|
| D1 — Installation | 0.539 | 70.0% | 0.300 | Moderate |
| D2 — Usage | 0.747 | 83.3% | 0.167 | Substantial |
| D3 — Purpose | 0.789 | 96.7% | 0.033 | Substantial |
| D4 — Dependencies | 0.743 | 80.0% | 0.200 | Substantial |
| D5 — Examples | 0.585 | 70.0% | 0.300 | Moderate |
| D6 — Contribution | 0.849 | 90.0% | 0.100 | Almost perfect |
| **Macro-avg** | **0.709** | | | Substantial overall |

## Key Findings

### A1 — Prevalence effect
A1 yielded κ=0.000 despite 96.7% exact agreement. This is a known
limitation of Cohen's Kappa when one class strongly dominates — in
this case 29/30 repositories have a license file, leaving almost no
variation for Kappa to measure. The high exact agreement (96.7%)
indicates that annotators reached the same decision for almost all
repositories despite the low κ value.

### R1 — Single observed class
R1 is undefined because all 30 repositories have a README file,
meaning neither annotator ever assigned a score of 0. Kappa requires
variation in both classes to be computable. Exact agreement is 100%.

### I1 — Low agreement
Seven repositories showed disagreement on I1:
- Geant4/geant4 (C++)
- JuliaClimate/ClimateTools.jl (Julia)
- OpenMS/OpenMS (C++)
- cdk/cdk (Java)
- gonum/gonum (Go)
- nextflow-io/nextflow (Groovy)
- rust-ml/linfa (Rust)

All disagreements followed the pattern that the primary annotator
assigned a score of 0 while the second annotator assigned a score
of 1. Manual inspection suggested that the disagreements were
associated with language-specific dependency or build configurations
whose interpretation differed between annotators.

### AI dimensions — Overall assessment
The macro-average weighted Kappa of 0.709 for the six AI-based
dimensions indicates substantial overall agreement. D3 (purpose)
and D6 (contribution) showed the strongest agreement. D1
(installation) and D5 (examples) showed moderate agreement,
reflecting genuine ambiguity in how to score partially present
or externally linked content.

## Conclusion

Inter-annotator agreement is satisfactory for the purposes of this
thesis evaluation. The AI-based dimensions (macro-avg κ=0.709)
show consistent moderate-to-substantial agreement, supporting the
reliability of the manual ground truth annotations. The lower
agreement on I1 is likely attributable to differences in the
interpretation or detection of dependency and build files and will
be discussed as a limitation in the evaluation chapter.