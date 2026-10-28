repo_id: InsightSoftwareConsortium/ITK
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Both pip and conda install commands provided inline. C++ build from source via CMake also mentioned.

D2_usage: 1     confidence: HIGH
D2_notes: No inline usage examples. Examples linked externally at examples.itk.org. Software Guide linked.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — open-source toolkit for N-dimensional scientific image processing, segmentation and registration. Medical imaging context explained.

D4_dependencies: 1     confidence: HIGH
D4_notes: pip/conda install implies Python but no version requirements stated. CMake mentioned for C++ build but no details.

D5_examples: 2     confidence: HIGH
D5_notes: Dedicated examples website linked at examples.itk.org. Software Guide PDF linked. Multiple learning resources provided.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.md present and linked. Discussion forum, issue tracker, governance model all linked. Pull request process described.

exclusion_reason:
general_notes: Zenodo DOI badge present (F1=1). CITATION.cff present (F2=1). Explicit citation section with papers, BibTeX, and CITATION.cff instructions (R2=1). One of the most complete repos in the dataset.