repo_id: OpenMS/OpenMS
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    1
A1_license:          1
I1_dependency_file:  0
R1_readme_present:   1
R2_citation:         1

# AI-based
D1_installation:     1   confidence: MEDIUM
D1_notes: Build instructions linked for Linux, Windows and macOS separately but no inline commands. Users must follow external links.

D2_usage:            0   confidence: HIGH
D2_notes: No usage examples or commands in README. Features described extensively but no demonstration of how to actually use the software.

D3_purpose:          2   confidence: HIGH
D3_notes: Detailed description of capabilities — LC-MS data management, proteomics, metabolomics, Python bindings, workflow engine support. Clear and comprehensive.

D4_dependencies:     1   confidence: MEDIUM
D4_notes: Dependencies mentioned by name but no versions specified. Platform support listed (Windows, macOS, Linux).

D5_examples:         1   confidence: MEDIUM
D5_notes: Documentation link present and accessible but no inline examples. Tutorial linked externally.

D6_contribution:     1   confidence: MEDIUM
D6_notes: Discord and Gitter community channels present but no contribution process described in README. No CONTRIBUTING.md linked, no PR instructions or how-to-contribute section.

exclusion_reason:
general_notes: Strong rule-based score — CITATION.cff, LICENSE, DOI all present. D2 = 0 despite being a large research software project. No inline usage examples anywhere in README. No dependency specification file detected.