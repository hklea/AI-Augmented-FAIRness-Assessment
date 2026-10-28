repo_id: sunpy/sunpy
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: README points to the stable installation guide (docs.sunpy.org), verified live with complete step-by-step conda/miniforge install and prerequisites.

D2_usage:               2  confidence: HIGH
D2_notes: Points to the live tutorial and example gallery for newcomers; tutorial pages provide runnable chapter examples.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of solar physics data access, loading, coordinates, and analysis tools in Python.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: README says the install guide covers dependencies but does not itself list Python version or required packages in prose.

D5_examples:            2  confidence: HIGH
D5_notes: Links to accessible tutorial and example gallery demonstrating meaningful use.

D6_contribution:        2  confidence: HIGH
D6_notes: Contributing section links Developers Guide and Newcomers guide plus chat, mailing list, discourse, and issues.

exclusion_reason:
general_notes: Zenodo DOI badge and CITATION.cff present. R2 supported by explicit "we would appreciate your citing it" wording (not by CITATION.cff alone).
