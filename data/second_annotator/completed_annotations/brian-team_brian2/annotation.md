repo_id: brian-team/brian2
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        0  confidence: HIGH
D1_notes: No installation commands or install guide link in the README; only dependency lists and package badges.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete code example in the README; mybinder quickstart and docs link provide partial paths to use without an inline workflow.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of a Python spiking neural network simulator designed to be easy to learn and extensible.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explicit required and optional packages with version floors listed in the README (Python, NumPy, SymPy, Cython, etc.).

D5_examples:            2  confidence: HIGH
D5_notes: mybinder badge links an executable notebook; documentation site also linked.

D6_contribution:        1  confidence: HIGH
D6_notes: Issue tracker and Discourse forum/chat present, but no contribution guidelines or CONTRIBUTING process described.

exclusion_reason:
general_notes: F1 from article DOI and Zenodo badge. F2 from CITATION.cff/codemeta. R2=1 from CITATION.md and explicit "we kindly ask you to cite our article" wording.
