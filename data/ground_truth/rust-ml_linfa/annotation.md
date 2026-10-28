repo_id: rust-ml/linfa
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 0
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 0

# AI-based
D1_installation: 0     confidence: HIGH
D1_notes: No installation instructions or Cargo installation commands are provided in the README.

D2_usage: 0     confidence: HIGH
D2_notes: No usage examples, quickstart, or workflow demonstrating how to use the library are provided.

D3_purpose: 2     confidence: HIGH
D3_notes: Purpose is clearly explained as a comprehensive machine learning toolkit for Rust, comparable in spirit to scikit-learn. Major algorithms and intended use are described in detail.

D4_dependencies: 2     confidence: HIGH
D4_notes: README explains optional BLAS/LAPACK backends, feature flags, Cargo configuration, supported platforms, and dependency selection in detail.

D5_examples: 0     confidence: HIGH
D5_notes: No executable code examples or tutorial workflows are included in the README.

D6_contribution: 1     confidence: HIGH
D6_notes: Community chat and roadmap for contributors are linked, encouraging community involvement, but no contribution guide or CONTRIBUTING file is referenced.

exclusion_reason:
general_notes: No software DOI, CITATION file, or codemeta metadata detected (F1=0, F2=0, R2=0). Documentation strongly describes project scope and configuration but lacks installation guidance and usage examples. A1 corrected from 0 to 1 during final rule-based validation — metadata.json confirms Apache-2.0 license (spdx_id present) and the README explicitly states "Licensed under the Apache License, Version 2.0"; the original annotation was an error.