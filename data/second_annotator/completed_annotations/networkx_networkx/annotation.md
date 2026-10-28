repo_id: networkx/networkx
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       0
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: pip install commands including optional extras, plus link to a complete live installation guide.

D2_usage:               2  confidence: HIGH
D2_notes: Concrete shortest-path example with import, graph construction, and expected output in the README.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear statement that NetworkX is for creation, manipulation, and study of complex networks.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Mentions optional dependencies via pip extras but does not state Python version or required packages in README prose.

D5_examples:            2  confidence: HIGH
D5_notes: Inline working example plus explicit Tutorial link on networkx.org.

D6_contribution:        2  confidence: HIGH
D6_notes: Bugs section covers reporting issues and PRs; links contributor guide, discussions, Discord, and mailing list.

exclusion_reason:
general_notes: No DOI/PID in README or metadata files checked (F1=0). No CITATION.cff/codemeta (F2=0). No citation file or please-cite wording (R2=0).
