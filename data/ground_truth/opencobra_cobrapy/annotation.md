repo_id: opencobra/cobrapy
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
D1_notes: Clear pip install command inline. Optional array dependency install also shown. Link to detailed INSTALL.rst for further info.

D2_usage: 1     confidence: HIGH
D2_notes: No inline usage examples or code. Documentation linked externally on readthedocs.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — constraint-based modeling package for genome-scale metabolic network analysis. Use cases and methods listed explicitly.

D4_dependencies: 1     confidence: HIGH
D4_notes: pip install implies Python but no version stated. Optional array dependency mentioned. No explicit environment requirements in README.

D5_examples: 1     confidence: HIGH
D5_notes: No inline examples. Documentation on readthedocs linked for tutorials.

D6_contribution: 2     confidence: HIGH
D6_notes: Contributing guidelines linked explicitly. Google Group, Gitter chat linked. Code of conduct badge present.

exclusion_reason:
general_notes: Zenodo DOI badge present (F1=1). Explicit citation instruction "please cite doi:10.1186/..." with DOI (R2=1). F2=0 no structured metadata file. Clean and well-structured README.