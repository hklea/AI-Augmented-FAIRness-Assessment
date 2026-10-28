repo_id: openmc-dev/openmc
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 1     confidence: HIGH
D1_notes: Installation instructions exist but only as a link to external User's Guide. No inline commands in README.

D2_usage: 1     confidence: HIGH
D2_notes: No inline usage examples. Complete documentation linked externally on Read the Docs.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — Monte Carlo particle transport code using constructive solid geometry and HDF5 cross sections. Origin at MIT stated.

D4_dependencies: 0     confidence: HIGH
D4_notes: No dependency or environment information in README. Installation guide is entirely external.

D5_examples: 1     confidence: MEDIUM
D5_notes: No inline examples. Links to User's Guide and documentation externally.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.md present. Discussion forum linked, GitHub Issues linked, troubleshooting section referenced.

exclusion_reason:
general_notes: README contains explicit citation instructions with a publication DOI (F1=1, R2=1). CITATION.cff is present (F2=1). Installation, troubleshooting, and user guidance are primarily provided through the external User's Guide.