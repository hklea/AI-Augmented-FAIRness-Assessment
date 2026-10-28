repo_id: gonum/gonum
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       0
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: go get install command and notes on supported Go versions/platforms.

D2_usage:               0  confidence: HIGH
D2_notes: No usage instructions or code examples showing how to use Gonum libraries.

D3_purpose:             0  confidence: HIGH
D3_notes: README has no description of what Gonum is or why it exists; jumps straight to installation and build details.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explicitly describes supported Go compiler versions and OS/architectures for building/testing.

D5_examples:            0  confidence: HIGH
D5_notes: No examples or tutorials linked or included in the README.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md present; GitHub issues and gonum-dev Google Group for discussion.

exclusion_reason:
general_notes: No software DOI/PID in README or CITATION.cff/codemeta (F1=0, F2=0). R2=0. I1=1 from go.mod (Go equivalent dependency file). A1 from LICENSE.
