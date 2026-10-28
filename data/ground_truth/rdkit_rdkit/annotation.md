repo_id: rdkit/rdkit
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 0

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear conda install command inline. Link to detailed install docs for advanced cases.

D2_usage: 1     confidence: MEDIUM
D2_notes: Links to Getting Started in Python guide externally. No inline usage code in README.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — cheminformatics and machine-learning software in C++ and Python. Feature list provided.

D4_dependencies: 1     confidence: MEDIUM
D4_notes: Conda install implies Python but no explicit version requirements or environment info in README.

D5_examples: 1     confidence: MEDIUM
D5_notes: Links to Getting Started guide and blog for tips. No inline code examples.

D6_contribution: 1     confidence: HIGH
D6_notes: GitHub discussions, mailing list, issue tracker, LinkedIn group all present. No contribution process or CONTRIBUTING.md described.

exclusion_reason:
general_notes: F2=0 — no CITATION.cff or codemeta.json. R2=0 — Zenodo badge present but no explicit citation instruction per v1.2 edge case. A1=1 — license clearly identified in README with link to license.txt even though no LICENSE file in root.