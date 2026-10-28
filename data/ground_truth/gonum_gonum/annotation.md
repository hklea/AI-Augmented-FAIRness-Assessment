repo_id: gonum/gonum
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 0
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 0

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear go get command provided inline. Pure Go installation, no additional setup needed.

D2_usage: 0     confidence: HIGH
D2_notes: No usage instructions or examples of any kind in README.

D3_purpose: 1     confidence: MEDIUM
D3_notes: Name implies numeric libraries for Go but no explicit description of purpose or research context in README. Only installation and build info provided.

D4_dependencies: 1     confidence: HIGH
D4_notes: Go version support stated — two most recent Go releases. No other dependency information.

D5_examples: 0     confidence: HIGH
D5_notes: No examples or tutorials referenced in README.

D6_contribution: 1     confidence: HIGH
D6_notes: Issue tracker mentioned, Google Group linked. No contribution process described and no CONTRIBUTING.md despite file being present — not referenced in README.

exclusion_reason:
general_notes: F1=0 no DOI. F2=0 no structured metadata. R2=0 no citation instruction. I1=0 Go module — dependency managed via go.mod not detected by script. D6=1 not 2 because CONTRIBUTING.md exists but is not referenced or linked in README.