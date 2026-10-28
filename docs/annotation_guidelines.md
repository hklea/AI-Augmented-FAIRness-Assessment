# Annotation Guidelines
## FAIR4RS Ground Truth Construction
**Thesis:** AI-Augmented FAIRness Assessment of Research Software: A Hybrid Approach
**Author:** Klea Haxhiu
## Version History
v1.0 — initial guidelines

v1.1 — updated after sunpy/sunpy pilot annotation
- Added LICENSE.rst to license file variants under A1
- Collector updated to check for .rst extension

v1.2 — updated after numpy/numpy pilot annotation  
- Added R2 edge case: a DOI badge alone without an accompanying 
  citation instruction in the README text does not count for R2. 
  There must be an explicit instruction such as "please cite" or 
  "if you use X cite this paper". A badge label such as "Nature 
  Paper" describes what the link is, not an instruction to cite it.

 v1.3 — updated after scikit-learn pilot annotation
- Added COPYING and COPYING.txt to license file variants under A1
- Collector updated to check for COPYING variants 

- v1.4 (2026-07-12): R2 clarified — CITATION.bib/CITATION.txt/CITATION 
  count for R2; "appreciate citations/citing" phrasing counts; 
  CITATION.cff alone does not satisfy R2; scipy annotation corrected.
---

## Purpose

This document defines how I score GitHub repositories against FAIR4RS
indicators when building the manual ground truth. It exists for three
reasons: to keep my own annotations consistent across all 30 repositories,
to define the exact criteria the LLM is prompted against, and to make the
annotation process replicable if needed.

The rule of thumb throughout: score what is *documented*, not what exists
in the code. If a dependency is listed in `requirements.txt` but never
mentioned in the README, that counts for the rule-based check but not
for the qualitative score.

---

## Repository Inclusion

Before annotating, check that the repository meets all of the following.
If it does not, exclude it and log the reason.

- The README is primarily in English
- The repository contains research or scientific software — not a tutorial,
  course assignment, or configuration template
- There has been at least one commit in the last three years
- The README is at least 200 words
- The repository is publicly accessible at the time of annotation

Research software means software written to support or conduct scientific
research: data analysis tools, simulation software, computational pipelines,
domain-specific libraries. A general-purpose utility library is only included
if it is explicitly associated with a publication or research project.

---

## Scoring Scale

**Rule-based dimensions** are binary — 0 if the file or field is absent,
1 if it is present.

**AI-based dimensions** use a 0–2 scale:

- **0** — the dimension is entirely absent
- **1** — the dimension is addressed but incomplete, ambiguous, or unclear
- **2** — the dimension is addressed completely and clearly enough that a
  new user could act on it without needing to look elsewhere

When deciding between 1 and 2: ask whether a new user could act on the
information without consulting external sources. If yes, score 2.

When deciding between 0 and 1: ask whether there is any attempt to address
the dimension, however incomplete. If yes, score 1.

---

## Rule-Based Dimensions

These six dimensions are checked programmatically and verified manually.
Each maps to a specific FRSM indicator from the FAIR-IMPACT framework.

**F1 — Persistent identifier (FRSM-01, FRSM-02)**
Score 1 if a DOI or equivalent persistent identifier is present anywhere
in the repository — in the README, in `CITATION.cff`, or in `codemeta.json`.
A GitHub URL alone does not count.

**F2 — Structured metadata file (FRSM-04, FRSM-07, FRSM-08)**
Score 1 if a `CITATION.cff`, `codemeta.json`, or equivalent structured
metadata file is present at the root level.

**A1 — License (FRSM-15, FRSM-16)**
Score 1 if a `LICENSE` file is present, or if a license is clearly identified
in the README or in a metadata file.

License files may use extensions including .md, .txt, .rst, or no 
extension. When A1 scores 0 for a well-known project, verify manually 
on GitHub before finalising the score.

License files may also be named COPYING or COPYING.txt — 
common in projects following GNU licensing conventions.

**I1 — Dependency specification file (FRSM-13)**
Score 1 if any standard dependency file is present: `requirements.txt`,
`environment.yml`, `setup.py`, `pyproject.toml`, `package.json`, `Cargo.toml`,
or equivalent.

**R1 — README file present (FRSM-13)**
Score 1 if a README file exists at the root level in any format. This is
a presence check only — quality is assessed in the AI-based dimensions.

**R2 — Citation information (FRSM-17)**
Does the repository provide explicit citation information for users?

Score 1 if any of the following are present:
- A dedicated citation file: `CITATION.md`, `CITATION.bib`, 
  `CITATION.txt`, or plain `CITATION`
- An explicit citation instruction in the README such as:
  "please cite", "how to cite", "if you use X cite this paper",
  "we would appreciate citations", or "we would appreciate your citing"

Score 0 if:
- Only a DOI badge is present without an accompanying citation 
  instruction (badge alone does not count)
- Only `CITATION.cff` is present — this is captured by F2, not R2
- Only a link to a paper without explicit citation instruction

Edge case: A DOI badge alone without an accompanying citation instruction in the README text does not count. There must be 
an explicit instruction such as "please cite" or "if you use X cite this paper". A badge label such as "Nature Paper" 
describes what the link is, not an instruction to cite it.

---

## AI-Based Dimensions

These six dimensions assess qualitative aspects of README content. The
theoretical basis for choosing them comes from Treude et al. (2020) for
quality dimensions, Prana et al. (2019) for README content categories,
and Imani et al. (2024) for practitioner adoption criteria — all mapped
onto FAIR4RS reusability and findability indicators.

For each dimension, score based on the README text only. If the README
links to external documentation, check whether the link is live and
accessible before crediting it.

---

**D1 — Clarity of installation instructions**
*FAIR4RS: R1, R1.2 — Treude: Understandability, Clarity — Prana: How*

Can a new user install this software from the README alone?

Score 2 if step-by-step instructions are present, complete, and list all
prerequisites. A new user could follow them without external help.

Score 1 if instructions exist but are incomplete, ambiguous, or missing
some prerequisites. Something like "install via pip" with no version or
environment context is a 1.

Score 0 if no installation instructions are present at all.

If instructions reference a separate `INSTALL.md` that is complete and
accessible, score 2. If instructions are present but clearly outdated,
score 1.

---

**D2 — Clarity of usage instructions**
*FAIR4RS: R1, R1.2 — Treude: Understandability, Effectiveness — Prana: How*

Can a new user understand how to run or use this software from the README?

Score 2 if at least one concrete example is provided — a command, code
snippet, or workflow — with enough context that a new user could run it.

Score 1 if usage is described but only at a high level, without actionable
examples. A single `python main.py` with no explanation of arguments is a 1.

Score 0 if no usage instructions are present.

---

**D3 — Description of software purpose**
*FAIR4RS: F2, R1 — Treude: Clarity — Prana: What, Why*

Does the README explain what the software does and why it exists?

Score 2 if the README contains a clear description of what the software
does and what research purpose it serves. A reader unfamiliar with the
domain should be able to understand the scope.

Score 1 if a description is present but vague, or so technically dense
that the purpose is not accessible to a non-specialist.

Score 0 if no description of purpose is present — for example, a README
that contains only installation steps.

---

**D4 — Dependency and environment description**
*FAIR4RS: R1, I1 — Treude: Effectiveness — Prana: How*

Does the README describe in human-readable form what environment is needed?

Score 2 if dependencies and environment requirements are explicitly described
in the README text — not just listed in a file, but explained. This includes
Python version, OS requirements, or any non-obvious prerequisites.

Score 1 if some dependency information is mentioned but incomplete — for
example, only mentioning Python without a version, or only pointing to a
requirements file without explaining it.

Score 0 if no dependency or environment information appears in the README.

Note: the presence of a `requirements.txt` is captured in I1. This dimension
is specifically about whether the README explains dependencies to a human
reader, not whether a machine-readable file exists.

---

**D5 — Presence of examples or tutorials**
*FAIR4RS: R1.2 — Treude: Effectiveness — Prana: How — Imani: Use case examples*

Does the repository provide concrete examples that support reuse?

Score 2 if at least one complete, working example is provided — an inline
code block, a Jupyter notebook, an example script, or a link to an accessible
tutorial that demonstrates meaningful use of the software.

Score 1 if examples are referenced or partially present but too minimal
to be useful, or if a link to examples is broken or inaccessible.

Score 0 if no examples or tutorials are present or referenced anywhere.

---

**D6 — Contribution and community information**
*FAIR4RS: R1.2 — Treude: Structure — Prana: Contribution, Who*

Does the repository explain how to contribute or get support?

Score 2 if contribution guidelines are present (inline or via a
`CONTRIBUTING.md`) and at least one of the following is also present:
maintainer contact, issue tracker reference, community channel, or
support instructions.

Score 1 if some community information is present — for example, only
an email address or only a link to issues — but no contribution process
is described.

Score 0 if no contribution or community information is present.

---

## Confidence Flags

After scoring each AI-based dimension, record a confidence flag.

**HIGH** — the evidence clearly supports the score. Another annotator
would very likely agree.

**MEDIUM** — the score required judgment. The README is ambiguous or
only partially addresses the dimension. Another annotator might score ±1.

**LOW** — the score is uncertain. Use this when the README is very short
(under 100 words), primarily non-English, consists mostly of images or
badges, or when the dimension is extremely difficult to judge from the
text alone. LOW flags indicate that human review is recommended before
using the score in evaluation.

---

## Annotation Record

For each repository, fill in the following. Keep a brief justification
note for every AI-based score, even when confidence is HIGH.

```
repo_id:
annotated_date:

# Rule-based
F1_persistent_id:       [0/1]
F2_metadata_file:       [0/1]
A1_license:             [0/1]
I1_dependency_file:     [0/1]
R1_readme_present:      [0/1]
R2_citation:            [0/1]

# AI-based
D1_installation:        [0/1/2]  confidence: [HIGH/MEDIUM/LOW]
D1_notes:

D2_usage:               [0/1/2]  confidence: [HIGH/MEDIUM/LOW]
D2_notes:

D3_purpose:             [0/1/2]  confidence: [HIGH/MEDIUM/LOW]
D3_notes:

D4_dependencies:        [0/1/2]  confidence: [HIGH/MEDIUM/LOW]
D4_notes:

D5_examples:            [0/1/2]  confidence: [HIGH/MEDIUM/LOW]
D5_notes:

D6_contribution:        [0/1/2]  confidence: [HIGH/MEDIUM/LOW]
D6_notes:

exclusion_reason:       [if excluded; otherwise blank]
general_notes:
```

---

## Annotation Process

Annotate each repository independently — do not compare to others in the
set while scoring. Record justification notes as you go, not after the fact.

For the pilot batch (first 15 repos): after completing all 15, review every
MEDIUM and LOW confidence flag and identify any dimensions where you were
consistently uncertain. Revise these guidelines where needed — adding edge
cases or clarifying definitions — before starting the final batch. Do not
change scores retroactively; instead document what changed and why.

For the final batch (remaining 15 repos): follow the revised guidelines.
Flag any new edge cases that were not covered.

---

## References

- Chue Hong et al. (2022). FAIR Principles for Research Software. *Scientific Data*.
- Chue Hong et al. (2025). Metrics for Automated FAIR Software Assessment. FAIR-IMPACT D5.2.
- Treude, Middleton & Atapattu (2020). Beyond Accuracy. *ESEC/FSE 2020*.
- Prana et al. (2019). Categorizing the Content of GitHub README Files. *Empirical Software Engineering*.
- Imani et al. (2024). Does Documentation Matter? *arXiv:2403.03819*.
- Wilkinson et al. (2016). The FAIR Guiding Principles. *Scientific Data*.