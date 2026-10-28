repo_id: InsightSoftwareConsortium/ITK
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: pip and conda install for Python packages; notes C++ core can be built with CMake; Download link provided.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete code snippet in the README; usage deferred to documentation, Software Guide, and examples site.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of N-dimensional image processing, segmentation, and registration with medical imaging context.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Mentions CMake for building the C++ core; does not list full dependency/environment requirements in README prose.

D5_examples:            2  confidence: HIGH
D5_notes: Explicit Examples site (examples.itk.org) and Software Guide PDF linked.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md for patches; Discourse for questions and GitHub issues for development tracking.

exclusion_reason:
general_notes: Zenodo DOI gives F1=1. CITATION.cff gives F2=1. R2=1 from Citation section instructing how to cite (papers/books/CITATION.cff), not from DOI badge alone.
