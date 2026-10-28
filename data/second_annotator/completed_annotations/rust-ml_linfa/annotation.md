repo_id: rust-ml/linfa
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       0
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        1  confidence: MEDIUM
D1_notes: Discusses Cargo feature flags for WASM and BLAS backends but lacks a basic end-user install command (e.g. cargo add) or full install guide.

D2_usage:               0  confidence: HIGH
D2_notes: No concrete code example showing how to run or use linfa algorithms in the README.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of a Rust ML toolkit akin to scikit-learn, with algorithm table describing purpose and status.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explains BLAS/LAPACK backend options, platform support matrix, and WASM feature requirements in README prose.

D5_examples:            1  confidence: MEDIUM
D5_notes: docs.rs and website linked; README does not include an inline working example or clearly labeled tutorial.

D6_contribution:        1  confidence: HIGH
D6_notes: Community chat and roadmap issue invite involvement, but no contribution guidelines/CONTRIBUTING process described.

exclusion_reason:
general_notes: No DOI/CITATION.cff (F1=0, F2=0, R2=0). A1=1 from clear Apache/MIT dual-license text (LICENSE-APACHE2/LICENSE-MIT present; standard LICENSE* flags were false). I1=1 from Cargo.toml.
