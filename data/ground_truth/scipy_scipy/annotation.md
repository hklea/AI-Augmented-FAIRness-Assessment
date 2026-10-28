repo_id: scipy/scipy
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 1     confidence: HIGH
D1_notes: Installation guide linked externally. No inline install command in README.

D2_usage: 1     confidence: HIGH
D2_notes: No inline usage examples. Documentation linked externally. Modules listed but no actionable code.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — open-source software for mathematics, science and engineering. Modules listed explicitly.

D4_dependencies: 1     confidence: HIGH
D4_notes: NumPy mentioned as core dependency. No version requirements or full dependency list in README.

D5_examples: 1     confidence: HIGH
D5_notes: No inline examples. Documentation and tutorials linked externally.

D6_contribution: 2     confidence: HIGH
D6_notes: Contributing guide linked, bug reports, forum, code of conduct, security reporting all provided. Detailed list of contribution types beyond code.

exclusion_reason:
general_notes: DOI badge present linking to Nature paper (F1=1). CITATION.bib present (F2=1). Explicit "Citing in your work" link (R2=1). Well-known library with strong metadata but documentation quality relies heavily on external links.