repo_id: biopython/biopython
annotated_date: 2026-07-17

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: README has clear pip install/upgrade/uninstall, wheel note, Python version requirements, and full source-build steps with compiler/header prerequisites.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete end-user Bio API or workflow example in the README; usage is deferred to external docs. Testing commands are present but are not library usage instructions.

D3_purpose:             2  confidence: HIGH
D3_notes: States Biopython provides freely available Python tools for computational molecular biology; scope is clear to a non-specialist.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explicit Python version matrix, required NumPy, and optional deps (ReportLab, matplotlib, BioSQL drivers, etc.) with why each is needed.

D5_examples:            2  confidence: HIGH
D5_notes: Points to the live Biopython Tutorial and Cookbook / API docs (https://biopython.org/docs/latest/) as the main reuse examples; qualifies as an accessible tutorial link.

D6_contribution:        2  confidence: HIGH
D6_notes: Links to CONTRIBUTING.rst plus issue tracker and mailing lists; contribution path and community channels are both present.

exclusion_reason:
general_notes: Annotated from provided README and fair_file_checks.json. DOI and explicit citation ask appear in README text. No CITATION.cff/codemeta at root (F2=0).
