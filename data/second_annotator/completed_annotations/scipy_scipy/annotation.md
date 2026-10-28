repo_id: scipy/scipy
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Points to the SciPy install guide for installation instructions.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete usage example in the README; documentation links provided for how to use SciPy.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of open-source software for mathematics, science, and engineering with listed modules.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Notes that SciPy works with NumPy arrays and runs on popular OSes, but does not list package versions in README prose.

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation linked; README does not include an inline example or explicitly labeled tutorials section.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.rst and detailed Call for Contributions with contributing guide, forum, and issues.

exclusion_reason:
general_notes: F1 from Nature DOI badge. F2=0 — no CITATION.cff/codemeta. R2=1 from CITATION.bib and explicit "Citing in your work" link (not from DOI badge alone). A1 from LICENSE.txt. I1 from pyproject.toml/environment.yml.
