repo_id: opencobra/cobrapy
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
D1_notes: pip install with virtualenv recommendation, optional MATLAB extras, and link to INSTALL.rst for further detail.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete FBA/API example in the README; usage deferred to Read the Docs documentation.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of constraint-based metabolic modeling with FBA/FVA and related COBRA methods.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Python version badge and optional MATLAB-related extras mentioned; full required dependency list not detailed in README prose.

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation linked; README does not include an inline example or explicitly labeled tutorials gallery.

D6_contribution:        2  confidence: HIGH
D6_notes: Contributing guidelines linked; Google Group and Gitter for help/support.

exclusion_reason:
general_notes: F1 from Zenodo badge and article DOI in cite sentence. F2=0 — no CITATION.cff/codemeta. R2=1 from explicit "If you use COBRApy... please cite".
