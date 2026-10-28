import shutil
from pathlib import Path

ALL_REPOS = [
    ("biopython", "biopython"),
    ("sunpy", "sunpy"),
    ("numpy", "numpy"),
    ("astropy", "astropy"),
    ("healpy", "healpy"),
    ("networkx", "networkx"),
    ("jupyter", "nbconvert"),
    ("nilearn", "nilearn"),
    ("OpenMS", "OpenMS"),
    ("scikit-learn", "scikit-learn"),
    ("mne-tools", "mne-python"),
    ("fieldtrip", "fieldtrip"),
    ("brian-team", "brian2"),
    ("rdkit", "rdkit"),
    ("openbabel", "openbabel"),
    ("cdk", "cdk"),
    ("PlasmaPy", "PlasmaPy"),
    ("yt-project", "yt"),
    ("openmc-dev", "openmc"),
    ("Geant4", "geant4"),
    ("MITgcm", "MITgcm"),
    ("Ouranosinc", "xclim"),
    ("JuliaClimate", "ClimateTools.jl"),
    ("scipy", "scipy"),
    ("gonum", "gonum"),
    ("rust-ml", "linfa"),
    ("opencobra", "cobrapy"),
    ("datajoint", "datajoint-python"),
    ("nextflow-io", "nextflow"),
    ("InsightSoftwareConsortium", "ITK"),
]

BLANK_TEMPLATE = """repo_id: {repo_id}
annotated_date:

# Rule-based
F1_persistent_id:
F2_metadata_file:
A1_license:
I1_dependency_file:
R1_readme_present:
R2_citation:

# AI-based
D1_installation:     confidence:
D1_notes:

D2_usage:            confidence:
D2_notes:

D3_purpose:          confidence:
D3_notes:

D4_dependencies:     confidence:
D4_notes:

D5_examples:         confidence:
D5_notes:

D6_contribution:     confidence:
D6_notes:

exclusion_reason:
general_notes:
"""


def setup():
    project_root = Path(__file__).resolve().parents[3]
    ground_truth_base = project_root / "data" / "ground_truth"
    output_base = project_root / "data" / "second_annotator" / "blank_annotations"
    output_base.mkdir(parents=True, exist_ok=True)

    for owner, repo in ALL_REPOS:
        folder_name = f"{owner}_{repo}"
        source_dir = ground_truth_base / folder_name
        output_dir = output_base / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nProcessing {owner}/{repo}...")

        for filename in ["README.md", "fair_file_checks.json", "metadata.json"]:
            source_file = source_dir / filename
            if source_file.exists():
                shutil.copy(source_file, output_dir / filename)
                print(f"  {filename} copied")
            else:
                print(f"  {filename} not found — skipping")

        repo_id = f"{owner}/{repo}"
        with open(output_dir / "annotation.md", "w", encoding="utf-8") as f:
            f.write(BLANK_TEMPLATE.format(repo_id=repo_id))
        print(f"  annotation.md created")

    print(f"\nDone. 30 repo folders created in {output_base}")


if __name__ == "__main__":
    setup()