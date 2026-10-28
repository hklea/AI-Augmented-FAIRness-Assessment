repo_id: sunpy/sunpy
annotated_date: 2026-05-28

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    1
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         1

# AI-based
D1_installation:     1   confidence: MEDIUM
D1_notes: Installation section exists but only links to external docs. No inline steps or prerequisites.

D2_usage:            1   confidence: MEDIUM
D2_notes: Usage section exists but only links to tutorial and example gallery. No inline commands or code.

D3_purpose:          2   confidence: HIGH
D3_notes: Clear description of what sunpy does and what domain it serves. Accessible to non-specialists.

D4_dependencies:     1   confidence: MEDIUM
D4_notes: Python version hinted via badges but never stated explicitly in README text. No environment requirements described.

D5_examples:         2   confidence: HIGH
D5_notes: Links to live example gallery with real working examples demonstrating meaningful use.

D6_contribution:     2   confidence: HIGH
D6_notes: Contribution guidelines, issues page, chat room, mailing list and community forum all present.

exclusion_reason:
general_notes: Well-maintained research project. README is thin on inline content but compensates with rich external documentation. A1 license scored 0 — LICENSE file not found by collector, worth verifying manually.

---
general_notes: LICENSE.rst found manually on GitHub — collector 
missed it. Fixed FAIR_FILES list to include .rst extension.