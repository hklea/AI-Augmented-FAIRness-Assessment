repo_id: yt-project/yt
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
D1_notes: conda and pip install commands plus link to fuller installing documentation on the project site.

D2_usage:               2  confidence: HIGH
D2_notes: Getting Started section lists Quickstart notebooks covering introduction through volume rendering; also points to yt Hub.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of analyzing and visualizing volumetric data across astrophysics and other domains.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Python version badge present but README does not explain required packages or environment in prose.

D5_examples:            2  confidence: HIGH
D5_notes: Multiple Quickstart notebooks linked in-repo plus yt Hub for running notebooks with example data; docs include tutorials.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.rst guidelines plus users/devel mailing lists and Slack invite.

exclusion_reason:
general_notes: F1 from DOI in root CITATION file (and method-paper reference). F2=0 — no CITATION.cff/codemeta. R2=1 from plain CITATION file and "please consider citing" wording. A1 from COPYING.
