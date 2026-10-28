repo_id: networkx/networkx
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    0
F2_metadata_file:    0
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         0

# AI-based
D1_installation:     2   confidence: HIGH
D1_notes: pip install command present, optional dependencies install shown, link to installation guide for additional details.

D2_usage:            2   confidence: HIGH
D2_notes: Real executable example present — shortest path graph example with full code and expected output shown inline.

D3_purpose:          2   confidence: HIGH
D3_notes: Short but clear — Python package for creation, manipulation and study of complex networks. Accessible to non-specialists.

D4_dependencies:     1   confidence: MEDIUM
D4_notes: pip install mentioned but no Python version requirements or explicit dependency list in README text.

D5_examples:         2   confidence: HIGH
D5_notes: Inline working code example present plus tutorial link accessible at networkx.org.

D6_contribution:     2   confidence: HIGH
D6_notes: GitHub issues, pull request guidance, contributor guide linked, mailing list, Discord, GitHub Discussions all present.

exclusion_reason:
general_notes: No DOI or citation information — F1 and R2 both 0. Strong inline documentation with real executable example. Similar pattern to nbconvert — weak metadata, good README quality.