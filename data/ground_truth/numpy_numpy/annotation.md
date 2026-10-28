repo_id: numpy/numpy
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    0
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         0

# AI-based
D1_installation:     0   confidence: HIGH
D1_notes: No installation instructions in README. Only a test run command mentioned. Users directed nowhere for installation.

D2_usage:            0   confidence: HIGH
D2_notes: No usage examples or quickstart present. README covers purpose and contribution but not how to use the library.

D3_purpose:          2   confidence: HIGH
D3_notes: Clear description at top — fundamental package for scientific computing with Python, capabilities listed explicitly.

D4_dependencies:     1   confidence: MEDIUM
D4_notes: pytest and hypothesis mentioned for testing only. No runtime dependencies described in README text.

D5_examples:         1   confidence: MEDIUM
D5_notes: Documentation link present at numpy.org/doc but leads to reference manual not tutorials or worked examples.

D6_contribution:     2   confidence: HIGH
D6_notes: Detailed contribution section covering code, reviews, tutorials, website, design, translation. Mailing list, Slack, GitHub issues all present.

exclusion_reason:
general_notes: Surprising result for such a major project — D1 and D2 both 0. README focuses entirely on community and contribution, not on helping new users install or use the library. Strong contrast with biopython and healpy.