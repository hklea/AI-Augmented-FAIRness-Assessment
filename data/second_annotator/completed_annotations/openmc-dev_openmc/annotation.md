repo_id: openmc-dev/openmc
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Points to detailed installation instructions in the User's Guide (stable docs).

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete run/example in the README; usage deferred to Read the Docs user documentation.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of a Monte Carlo particle transport code with CSG and continuous-energy methods.

D4_dependencies:        0  confidence: HIGH
D4_notes: No human-readable dependency or environment requirements listed in the README.

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation linked for usage, but README does not point to a specific tutorial or include an inline example.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md present; discussion forum, troubleshooting docs, and GitHub issues for bugs/features.

exclusion_reason:
general_notes: F1 from DOI in Citing section. F2 from CITATION.cff. R2=1 from explicit citing instruction with bibliographic reference. I1 from pyproject.toml (CMakeLists.txt also present).
