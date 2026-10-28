repo_id: Geant4/geant4
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Points to the Installation Guide covering platforms and configuration options.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete application example in the README; points to website and user documentation for how to use the toolkit.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of particle-through-matter simulation for HEP, nuclear, medical, and space applications.

D4_dependencies:        0  confidence: HIGH
D4_notes: No dependency or environment requirements described in the README text.

D5_examples:            1  confidence: MEDIUM
D5_notes: User documentation linked; README does not include an inline example or clearly labeled examples gallery.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.rst present; User Forum and Bugzilla tracker for questions and bugs.

exclusion_reason:
general_notes: F1 from DOI in CITATION.cff. F2 from CITATION.cff. R2=0 — CITATION.cff alone does not satisfy R2; README lists reference papers without an explicit please-cite instruction. I1=1 from CMakeLists.txt (C++ equivalent).
