repo_id: healpy/healpy
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: pip install/upgrade commands plus Python requirements and link to INSTALL.rst for further options.

D2_usage:               2  confidence: HIGH
D2_notes: Points to healpy tutorial docs and mybinder; capabilities section also describes what users can do.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear explanation of HEALPix spherical pixelization for CMB/astrophysics and healpy as the Python wrapper.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explicit Python versions, NumPy, Matplotlib, Astropy, and notes on python-dev / optional HEALPix+cfitsio builds; Windows unsupported called out.

D5_examples:            2  confidence: HIGH
D5_notes: Links to tutorial documentation and a mybinder badge for executable examples.

D6_contribution:        2  confidence: HIGH
D6_notes: Contribute section describes fork/PR workflow; GitHub issues and StackOverflow support channels also listed.

exclusion_reason:
general_notes: F1 from Zenodo/JOSS DOIs. R2=1 from plain CITATION file plus Acknowledgements instructing to cite papers via CITATION. No CITATION.cff/codemeta (F2=0). A1 from COPYING.
