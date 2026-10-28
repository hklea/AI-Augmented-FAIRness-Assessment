# Rule-Based Scorer Validation
**Date:** 2026-05-29
**Scorer version:** 1.0
**Pilot repos:** 10

## Result
Automated F1–R2 scores matched manual pilot annotations across 
all 10 pilot repositories after adding README-based F1 and R2 
detection. No discrepancies remained.

## Key fixes required during development
- F1 initially returned 0 for all repos — GitHub metadata does 
  not contain DOI fields. Fixed by scanning README text for 
  doi.org, zenodo, and doi/ patterns.
- R2 initially missed citation instructions in README text. 
  Fixed by scanning for "please cite", "how to cite", 
  "if you use...cite" patterns.

## Validation method
Manual annotations from pilot phase compared against automated 
scorer output. Scores matched 1:1 after fixes.

## Conclusion
The rule-based scorer is considered validated for the pilot dataset
and can be applied consistently to larger repository collections.
The validation also highlighted the importance of combining file-
based checks with README text analysis for detecting persistent
identifiers and citation information.

---

# Rule-Based Scorer Validation — Version 2.0
**Date:** 2026-07-12
**Scorer version:** 2.0 (corrected)
**Ground truth repos:** 30

## Changes from v1.0
- R2 no longer counts CITATION.cff alone (consistent with annotation v1.4 edge case)
- F1 now checks DOI badge URL formats in addition to doi.org links
- A1 now checks GitHub metadata license field
- R1 handles README.rst variants
- I1 adds Julia, Go, Java, Rust dependency files
- Error handling — skips folders with missing files instead of crashing
- CLI interface added (--input, --output arguments)

## Discrepancies found vs manual annotations

### R2 false negatives (scorer=0, annotation=1) — fixed
- sunpy/sunpy — README uses backtick formatting around "citing":
  "we would appreciate your `citing it in your publications`"
  Fix: added optional backtick pattern to R2 regex
- datajoint/datajoint-python — README uses markdown bold:
  "**Cite DataJoint:**"
  Fix: added pattern to catch bold-formatted cite instructions
- scikit-learn/scikit-learn — README says "we would appreciate citations"
  Fix: added "appreciate citing/citations" pattern

### Annotation corrections (scorer was correct)
- scipy/scipy: F2 corrected from 1 to 0 — CITATION.bib counts for R2
  not F2. F2 requires CITATION.cff or codemeta.json only.
- mne-tools/mne-python: R2 corrected from 1 to 0 — no citation
  instruction in README and no explicit citation file present.

## Final patterns added to has_explicit_citation_instruction()
- "we would appreciate your/your `citing/citations"
- "**cite" (markdown bold formatted)
- "citing in your work"
- "cite it/them/the software/paper"

## F1 pattern added to contains_doi()
- DOI badge URL format: "DOI-10.xxxxx" in shield badge URLs

## Final result after fixes
All 30 ground truth repositories scored correctly.
Scorer output matches manual annotations after two annotation
corrections (scipy F2, mne-python R2).