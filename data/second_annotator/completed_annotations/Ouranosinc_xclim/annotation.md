repo_id: Ouranosinc/xclim
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
D1_notes: pip and conda install commands provided in Quick Install.

D2_usage:               2  confidence: HIGH
D2_notes: Concrete Python example computing monthly mean temperature with xclim/xarray, plus rename-time example.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of a climate services library for indicators, downscaling, bias adjustment, and ensemble analysis.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Mentions xarray/dask and CF/CMIP6 conventions; Python version badge present, but full required package list not in README prose.

D5_examples:            2  confidence: HIGH
D5_notes: Inline usage example plus links to Basic Usage and In-Depth notebook examples.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.rst linked; issues, discussions, and contributing guidelines described.

exclusion_reason:
general_notes: F1 from Zenodo/JOSS DOIs. F2 from CITATION.cff. R2=1 from explicit "How to cite this library" section asking readers to refer to the JOSS article.
