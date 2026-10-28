repo_id: datajoint/datajoint-python
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
D1_notes: pip and conda install commands provided.

D2_usage:               1  confidence: MEDIUM
D2_notes: Pipeline diagram and high-level workflow concepts present, but no actionable code snippet in the README; points to docs/tutorials.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear explanation of a relational workflow framework for scientific data pipelines with provenance.

D4_dependencies:        0  confidence: HIGH
D4_notes: No human-readable dependency or environment requirements listed in the README.

D5_examples:            2  confidence: HIGH
D5_notes: Explicit Tutorials link and DataJoint Elements example pipelines documented in Resources.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md linked; GitHub Discussions for community support.

exclusion_reason:
general_notes: F1 from arXiv DOI badge. F2=0 — no CITATION.cff/codemeta. R2=1 from explicit "Cite DataJoint" with paper citation (not DOI badge alone).
