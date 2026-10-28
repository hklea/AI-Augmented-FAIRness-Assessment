repo_id: numpy/numpy
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        0  confidence: HIGH
D1_notes: No installation instructions in the README; only website/docs links and a post-install test command.

D2_usage:               0  confidence: HIGH
D2_notes: Feature list only; no how-to-use instructions or runnable usage example. The provided command runs the test suite, not library usage.

D3_purpose:             2  confidence: HIGH
D3_notes: States NumPy is the fundamental package for scientific computing and lists core capabilities clearly.

D4_dependencies:        0  confidence: HIGH
D4_notes: Mentions pytest/hypothesis only for testing; no human-readable runtime dependency or environment requirements for using NumPy.

D5_examples:            1  confidence: MEDIUM
D5_notes: General documentation link present but README does not clearly point to a tutorial/examples resource; no inline example.

D6_contribution:        2  confidence: HIGH
D6_notes: Detailed Call for Contributions plus contributing docs link, mailing list, issues, and community contact channels.

exclusion_reason:
general_notes: F1 from Nature DOI badge (10.1038/s41586-020-2649-2). R2=0 per guidelines — Nature Paper DOI badge alone is not an instruction to cite; no CITATION.md/bib/txt and no please-cite wording.
