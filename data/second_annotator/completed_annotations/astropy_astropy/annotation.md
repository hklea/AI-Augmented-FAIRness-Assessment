repo_id: astropy/astropy
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
D1_notes: Includes pip install command and links to a complete, live install guide with environment setup and prerequisites.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete usage example in the README; usage is deferred to documentation/website without an actionable snippet here.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear statement of a community core astronomy package in Python fostering interoperability.

D4_dependencies:        0  confidence: HIGH
D4_notes: No human-readable dependency or environment description in the README text (only install command / external install guide).

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation linked but no explicit tutorial/examples section or inline example in the README.

D6_contribution:        2  confidence: HIGH
D6_notes: Contributing section with CONTRIBUTING.md summary link, developer guide, Slack/discourse/mailing lists.

exclusion_reason:
general_notes: Zenodo DOI present. R2=1 from plain CITATION file (fair_file_checks) and Acknowledging and Citing section. CITATION.cff also present (F2).
