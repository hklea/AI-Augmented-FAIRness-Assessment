repo_id: rdkit/rdkit
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: conda install command plus link to Install.md with more detailed installation instructions.

D2_usage:               2  confidence: HIGH
D2_notes: Points to Getting Started in Python guide for actionable usage after install.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of cheminformatics and ML software in C++/Python with listed capabilities.

D4_dependencies:        0  confidence: HIGH
D4_notes: No human-readable dependency or environment requirements listed in the README beyond conda install.

D5_examples:            2  confidence: HIGH
D5_notes: Getting Started guide and docs/blog linked; qualifies as accessible tutorial/getting-started material.

D6_contribution:        1  confidence: HIGH
D6_notes: Support via GitHub discussions, mailing list, and issues, but no contribution guidelines described.

exclusion_reason:
general_notes: Zenodo DOI badge gives F1=1. R2=0 — badge alone without please-cite wording or CITATION.md/bib/txt. A1=1 from clear BSD license identification and license.txt link (checked LICENSE* flags were false). I1=1 from setup.cfg as packaging/dependency config equivalent.
