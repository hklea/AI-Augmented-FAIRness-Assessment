repo_id: mne-tools/mne-python
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear pip install command provided inline. Links to full installation guide for advanced options.

D2_usage: 1     confidence: MEDIUM
D2_notes: No inline usage examples or quickstart code. Links to external documentation for tutorials.

D3_purpose: 2     confidence: HIGH
D3_notes: First paragraph clearly describes what MNE-Python does and lists all analysis modules.

D4_dependencies: 2     confidence: HIGH
D4_notes: Full list of minimum required dependencies with version numbers explicitly listed in README.

D5_examples: 1     confidence: MEDIUM
D5_notes: No inline code examples. Links to external documentation for tutorials and examples.

D6_contribution: 2     confidence: HIGH
D6_notes: Contributing guidelines linked explicitly. Forum linked for questions. Issue tracker mentioned.

exclusion_reason:
general_notes: Zenodo DOI badge present (F1=1). CITATION.cff + codemeta.json present (F2=1). R2 corrected from 0 to 1 during final rule-based validation — the repository contains CITATION.cff, which satisfies R2 under the finalized annotation guideline definition of citation information.