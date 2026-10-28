# Second Annotator Instructions
**Thesis:** AI-Augmented FAIRness Assessment of Research Software: A Hybrid Approach  
**Author:** Klea Haxhiu  
**Task:** Independent annotation of 30 GitHub repositories

---

## Purpose

You will independently annotate 30 GitHub repositories against a set of
FAIR4RS indicators. The annotations will be used to measure
inter-annotator agreement as part of the evaluation.

---

## Independence

Please complete all annotations independently. Do not discuss individual
repository scores until the annotation process has been completed.
Record only your own judgments. Do not compare repositories against each
other — score each repository independently according to the guidelines.

---

## Guidelines

These annotations must follow the final Annotation Guidelines (v1.3),
provided in provided in `annotation_guidelines_v1.4.md`. Do not modify or
reinterpret the scoring criteria.

---

## Repository Versions

The repositories should be annotated as they exist at the time of this
annotation. Use the GitHub links provided in `repos_to_annotate.md`.

---

## How to Annotate

1. Read `annotation_guidelines_v1.3.md` carefully before starting
2. Open `repos_to_annotate.md` to see the list of repositories
3. For each repository open the corresponding folder in `blank_annotations/`
4. Read the `README.md` file provided in the folder
5. Check `fair_file_checks.json` to see which files exist in the repository
6. Fill in all fields in `annotation.md`
7. Save the file and move to the next repository

---

## What to Score

**Rule-based dimensions (F1, F2, A1, I1, R1, R2):**
- Binary: 0 or 1
- Check repository files and README as described in the guidelines

**AI-based dimensions (D1-D6):**
- Scale: 0, 1, or 2
- Score based on README content only
- Always add a brief note explaining your score
- Always add a confidence flag: HIGH, MEDIUM, or LOW

---

## Files Provided

- `annotation_guidelines_v1.3.md` — scoring rules and definitions
- `repos_to_annotate.md` — list of 30 repositories with links
- `blank_annotations/` — 30 folders, one per repository, each containing:
  - `README.md` — the repository README to read for D1-D6 scoring
  - `fair_file_checks.json` — which files exist in the repo root, for F1-R2 scoring
  - `metadata.json` — general repository metadata
  - `annotation.md` — blank form to fill in

---

## Questions

If anything is unclear, please ask before starting — not after.
Consistency with the guidelines is more important than speed.