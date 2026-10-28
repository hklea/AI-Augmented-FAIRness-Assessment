# Comparison with the howfairis Tool
**Date:** 2026-07-09
**Tool:** howfairis (https://github.com/fair-software/howfairis)
**Repos:** 30 ground truth repositories (10 pilot + 20 additional)

## What is howfairis?

howfairis is a command-line tool developed by the Netherlands eScience Center
that checks GitHub repositories against 5 fair-software.eu recommendations:

1. Repository — is the code in a public repository?
2. License — does the repository have a license?
3. Registry — is the software in a software registry (PyPI, conda, etc.)?
4. Citation — is there a citation file or Zenodo badge?
5. Checklist — does the repo have a fair-software.eu badge?

Each dimension is binary (pass/fail). The tool produces a compliance score
from 0/5 to 5/5.

In this work, howfairis is used as an external baseline for comparison
because it is an established FAIR software assessment tool that evaluates
repository-level FAIR indicators.

*Note: The comparison was conducted on the 30 ground truth repositories
used during framework development and evaluation, as the objective was
to compare assessment coverage and indicator scope rather than to
benchmark performance across the full dataset.*

---

## Results

| Repository | Domain | Language | howfairis | Repo | License | Registry | Citation | Checklist |
|------------|--------|----------|-----------|------|---------|----------|----------|-----------|
| biopython/biopython | bioinformatics | Python | 3/5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| sunpy/sunpy | astronomy | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| numpy/numpy | scientific-computing | Python | 3/5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| astropy/astropy | astronomy | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| healpy/healpy | astronomy | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| networkx/networkx | scientific-computing | Python | 3/5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| jupyter/nbconvert | scientific-computing | Python | 2/5 | ✅ | ✅ | ❌ | ❌ | ❌ |
| nilearn/nilearn | neuroscience | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenMS/OpenMS | bioinformatics | C++ | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| scikit-learn/scikit-learn | scientific-computing | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| mne-tools/mne-python | neuroscience | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| fieldtrip/fieldtrip | neuroscience | MATLAB | 3/5 | ✅ | ✅ | ❌ | ✅ | ❌ |
| brian-team/brian2 | neuroscience | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| rdkit/rdkit | cheminformatics | C++ | 3/5 | ✅ | ✅ | ❌ | ✅ | ❌ |
| openbabel/openbabel | cheminformatics | C++ | 2/5 | ✅ | ✅ | ❌ | ❌ | ❌ |
| cdk/cdk | cheminformatics | Java | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| PlasmaPy/PlasmaPy | astronomy | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| yt-project/yt | astronomy | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| openmc-dev/openmc | computational-physics | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| Geant4/geant4 | computational-physics | C++ | 3/5 | ✅ | ✅ | ❌ | ✅ | ❌ |
| MITgcm/MITgcm | climate-science | Fortran | 3/5 | ✅ | ✅ | ❌ | ✅ | ❌ |
| Ouranosinc/xclim | climate-science | Python | 5/5 | ✅ | ✅ | ✅ | ✅ | ✅ |
| JuliaClimate/ClimateTools.jl | climate-science | Julia | 3/5 | ✅ | ✅ | ❌ | ✅ | ❌ |
| scipy/scipy | scientific-computing | Python | 3/5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| gonum/gonum | scientific-computing | Go | 2/5 | ✅ | ✅ | ❌ | ❌ | ❌ |
| rust-ml/linfa | scientific-computing | Rust | 3/5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| opencobra/cobrapy | computational-biology | Python | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |
| datajoint/datajoint-python | research-software | Python | 3/5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| nextflow-io/nextflow | bioinformatics | Groovy | 3/5 | ✅ | ✅ | ❌ | ✅ | ❌ |
| InsightSoftwareConsortium/ITK | reproducible-research | C++ | 4/5 | ✅ | ✅ | ✅ | ✅ | ❌ |

---

## Key Findings

### Finding 1 — FAIR software badge absent in 29 of 30 repositories
The fair-software.eu badge was absent in 29 of the 30 evaluated
repositories. Only xclim (Ouranosinc/xclim) achieved a full 5/5
score, including the checklist badge. Consequently, the checklist
indicator contributed little to differentiation across the dataset
and is not informative as a comparative metric in this sample.

### Finding 2 — howfairis does not assess documentation quality
howfairis has no equivalent of our D1-D6 dimensions. It cannot
evaluate installation clarity, usage instructions, purpose description,
dependency documentation, examples, or contribution guidelines. This
is the primary gap the proposed hybrid framework addresses.

### Finding 3 — Lowest-scoring repositories
Three repositories scored 2/5 — nbconvert, openbabel, and gonum.
All three lack registry badges and citation metadata. Our rule-based
scorer similarly found F1=0 and F2=0 for these repositories,
indicating broad consistency between the two approaches on
metadata-level assessment.

### Finding 4 — Registry check relies on README badges
howfairis detects registry presence by checking for badges in the
README (PyPI badge, conda badge, crates.io badge, Maven badge, etc.)
rather than checking the registry directly. This suggests the registry
indicator relies on README metadata rather than independently verifying
software registration. Notably, howfairis correctly detected the
crates.io badge for linfa (Rust) and the Maven badge for cdk (Java),
demonstrating multi-ecosystem awareness.

### Finding 5 — License detection is consistent
All 30 repositories passed the license check in howfairis, consistent
with our rule-based scorer which also found A1=1 for all repos in the
ground truth set. During development, support for additional license
filename variants (e.g., LICENSE.rst) was added to the rule-based
implementation to improve compatibility with scientific software
repositories.

### Finding 6 — Repository dimension passes universally
All 30 repositories passed the repository check, which verifies that
the code is in a public GitHub repository. This dimension is not
discriminating across the dataset and adds limited comparative value
when evaluating repositories already selected from GitHub.

---

## Comparison of Scope

The comparison highlights that the two approaches are largely
complementary rather than directly comparable, since they evaluate
different aspects of FAIR research software.

Although both approaches assess selected aspects of FAIR research
software, there is only partial overlap between their indicators.
Both evaluate licensing and citation-related metadata, while the
proposed framework additionally assesses persistent identifiers
and dependency metadata.

| Dimension | howfairis | Hybrid Framework (Rule-Based) | Hybrid Framework (AI-Based) |
|-----------|-----------|-------------------------------|------------------------------|
| Open repository | ✅ | ❌ | ❌ |
| License | ✅ | ✅ (A1) | ❌ |
| Software registry | ✅ | ❌ | ❌ |
| Citation metadata | ✅ | ✅ (F2, R2) | ❌ |
| Checklist badge | ✅ | ❌ | ❌ |
| Persistent identifier | ❌ | ✅ (F1) | ❌ |
| Dependency file | ❌ | ✅ (I1) | ❌ |
| Installation clarity | ❌ | ❌ | ✅ (D1) |
| Usage instructions | ❌ | ❌ | ✅ (D2) |
| Purpose description | ❌ | ❌ | ✅ (D3) |
| Dependency description | ❌ | ❌ | ✅ (D4) |
| Examples/tutorials | ❌ | ❌ | ✅ (D5) |
| Contribution info | ❌ | ❌ | ✅ (D6) |

---

## Score Distribution

| howfairis Score | Count | Repositories |
|----------------|-------|--------------|
| 5/5 | 1 | xclim |
| 4/5 | 14 | sunpy, astropy, healpy, nilearn, OpenMS, scikit-learn, mne-python, brian2, cdk, PlasmaPy, yt, openmc, cobrapy, ITK |
| 3/5 | 12 | biopython, numpy, networkx, fieldtrip, rdkit, geant4, MITgcm, ClimateTools.jl, scipy, linfa, datajoint, nextflow |
| 2/5 | 3 | nbconvert, openbabel, gonum |
| 1/5 | 0 | — |
| 0/5 | 0 | — |

---

## Conclusion

howfairis provides a lightweight, fast check of 5 high-level FAIR
software recommendations. It is useful as a first-pass screening tool
but has notable limitations in the context of research software
reusability assessment:

- It cannot assess documentation quality in any form
- The checklist dimension was not informative in this sample as only
  one repository (xclim) carried the required badge
- The registry indicator relies on README badge presence rather than
  independent verification of software registration
- The repository dimension passed universally and did not differentiate
  between repositories in this sample

The proposed hybrid framework extends metadata-based assessment by
incorporating six qualitative documentation dimensions (D1-D6),
thereby addressing documentation aspects of software reusability
emphasized in the FAIR4RS principles. The comparison illustrates that
the two approaches are largely complementary: howfairis evaluates
repository-level FAIR software indicators efficiently, while the hybrid
framework targets the documentation quality dimensions that
howfairis does not address.