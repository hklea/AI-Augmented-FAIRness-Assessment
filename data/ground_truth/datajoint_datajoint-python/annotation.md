repo_id: datajoint/datajoint-python
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Both pip and conda install commands provided inline. Clear and complete.

D2_usage: 1     confidence: MEDIUM
D2_notes: No inline code examples. Pipeline image shown but not actionable. Tutorials linked externally.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — framework for scientific data pipelines based on Relational Workflow Model. Four key principles explained inline.

D4_dependencies: 1     confidence: HIGH
D4_notes: pip/conda install implies Python but no version requirements stated in README.

D5_examples: 2     confidence: HIGH
D5_notes: Tutorials linked explicitly at docs.datajoint.com/tutorials. DataJoint Elements with example pipelines for neuroscience linked.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.md present and linked. GitHub Discussions linked for community support.

exclusion_reason:
general_notes: DOI badge present with explicit citation instruction "Cite DataJoint" (F1=1, R2=1). F2=0 no CITATION.cff or codemeta.json. Clean well-structured README.