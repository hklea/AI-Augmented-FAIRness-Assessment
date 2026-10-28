repo_id: PlasmaPy/PlasmaPy
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
D1_notes: pip install commands for macOS/Linux and Windows plus link to detailed install documentation.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete usage snippet in the README; points to documentation and example gallery for how to use the package.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of a community Python package for plasma research and education analogous to Astropy for astronomy.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Mentions Python version selection for install (e.g. py -3.14) but does not list required packages in README prose.

D5_examples:            2  confidence: HIGH
D5_notes: Links an example gallery of Jupyter notebooks demonstrating PlasmaPy capabilities.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md and contributor guide linked; issues, discussions, Matrix chat, mailing list, and meetings also provided.

exclusion_reason:
general_notes: Zenodo DOI gives F1=1. CITATION.cff gives F2=1. R2=1 from explicit "please cite PlasmaPy" section (not from CITATION.cff alone).
