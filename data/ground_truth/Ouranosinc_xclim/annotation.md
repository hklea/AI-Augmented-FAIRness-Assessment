repo_id: Ouranosinc/xclim
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
D1_notes: Both pip and conda install commands provided inline. Clear and complete.

D2_usage: 2     confidence: HIGH
D2_notes: Inline Python code example showing how to compute monthly mean temperature. Concrete and actionable.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — Python library for climate services with climate indicators, statistical downscaling, bias adjustment, and ensemble analysis tools.

D4_dependencies: 2     confidence: HIGH
D4_notes: xarray and dask explicitly mentioned as core dependencies inline with explanation of why they are used.

D5_examples: 2     confidence: HIGH
D5_notes: Inline code example present. Basic Usage Examples and In-Depth Examples notebooks linked and accessible on readthedocs.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.rst present. Issue tracker, GitHub Discussions, contributing guidelines all linked. Translation contributions mentioned.

exclusion_reason:
general_notes: Zenodo DOI badge + JOSS DOI + explicit "How to cite" section with DOI (F1=1, R2=1). One of the most complete READMEs in the dataset — scores 2 on all AI dimensions.