repo_id: biopython/biopython
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    0
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         1

# AI-based
D1_installation:     2   confidence: HIGH
D1_notes: Step-by-step pip install present, Python versions explicitly listed (3.10-3.14), PyPy support noted, source compilation instructions included.

D2_usage:            1   confidence: MEDIUM
D2_notes: No inline usage examples or code snippets. Tutorial and Cookbook linked externally and accessible but nothing actionable in README itself.

D3_purpose:          2   confidence: HIGH
D3_notes: Clear description — international association developing Python tools for computational molecular biology. Purpose and audience immediately clear.

D4_dependencies:     2   confidence: HIGH
D4_notes: Python versions explicitly listed, NumPy required dependency named, optional dependencies listed with explanations of which modules need them.

D5_examples:         1   confidence: MEDIUM
D5_notes: Tutorial and Cookbook linked and accessible at biopython.org but no inline examples in README.

D6_contribution:     2   confidence: HIGH
D6_notes: CONTRIBUTING.rst linked, mailing list provided, issue tracker referenced, volunteer community described.

exclusion_reason:
general_notes: Strong rule-based and AI-based scores. Best inline dependency documentation seen so far — optional dependencies explained per module. D2 and D5 follow same external-link pattern as other repos.