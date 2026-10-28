# Prana et al. (2019) — Categorizing the Content of GitHub README Files

---

## Full Citation
Prana, G. A. A., Treude, C., Thung, F., Atapattu, T., & Lo, D. (2019).
Categorizing the content of GitHub README files.
*Empirical Software Engineering*, 24, 1296–1327.
https://doi.org/10.1007/s10664-018-9660-3

---

## Main Contribution
First large-scale empirical study to systematically categorize the content of GitHub
README files. The authors produce an annotated dataset, a coding schema of eight
content categories, and an automated multi-label SVM classifier that can predict
which categories a README section belongs to. They also evaluate whether
automatically labeling sections with badges improves information discovery for
software professionals.

---

## Key Ideas
- README files are the primary first-impression document for any GitHub repository
  and are central to documentation quality and discoverability.
- Content can be systematically categorized into eight types: **What, Why, How,
  When, Who, References, Contribution, Other**.
- "What" (what the project does) and "How" (installation, usage, configuration)
  dominate README files; "Why" (purpose/motivation) and "When" (project status)
  are rare.
- Automated classification of README sections is feasible and practically useful,
  achieving F1 = 0.746 with an SVM classifier.
- Visual labeling of README sections was perceived positively by the majority of
  software professionals surveyed (60% preferred labeled files).

---

## Methodology

### Dataset
- 393 randomly sampled GitHub repositories (statistically representative, 95%
  confidence level, CI = 4.94).
- 4,226 README sections extracted using GitHub Flavored Markdown parsing.
- Repositories filtered: English-only, ≥ 2 KB, software development repos only.
- Categories of repos: end-user applications (42%), libraries (27.9%), learning
  resources (17.4%), frameworks (7.3%), UI (5.4%).

### Approach
- **Qualitative coding (open coding):** Two annotators independently coded all
  sections using a coding schema developed iteratively. Inter-rater agreement
  (Cohen's Kappa) = 0.858. Disagreements resolved by a third annotator + majority
  vote.
- **Coding schema:** Eight categories (What, Why, How, When, Who, References,
  Contribution, Other). Sections can receive multiple labels (multi-label).
- **Classifier:** Binary Relevance multi-label classification. One binary SVM
  classifier per category. Oversampling used to handle class imbalance.
- **Feature extraction:**
  - *Statistical features:* TF-IDF on preprocessed section text (content +
    heading). Content abstraction applied (links, code blocks, images, numbers
    replaced with tokens).
  - *Heuristic features:* 55 linguistic patterns (heading/content), single-word
    non-English heading check, repository name match, non-ASCII content flag.
- Dataset split: 25% development set (feature design), 75% evaluation set
  (10-fold cross-validation).

### Evaluation
- Primary metric: weighted F1 score.
- Additional metrics: Kappa (0.831), ROC AUC (0.957), MCC (0.844).
- Compared five classifiers: SVM (best, F1=0.746), LR (0.739), RF (0.696),
  kNN (0.588), NB (0.518).
- User survey: 20 software professionals shown README files with/without
  auto-generated badges; perceived usefulness assessed.

### Tools / Models
- scikit-learn (Python) for all classifiers.
- NLTK for stop word removal and non-English word detection.
- arules (R) for association rule mining.
- GitHub Flavored Markdown parser for section extraction.

---

## Important Findings
1. **"How" dominates:** 58.4% of all sections; present in 88.5% of files.
2. **"What" is near-universal:** Present in 97% of files.
3. **"Why" and "When" are rare:** Only 25.7% and 21.4% of files include them
   respectively — despite being important for reusability and status clarity.
4. **"Contribution" is surprisingly low:** Only 27.8% of files, even though all
   repos are public open-source.
5. **Association rules:** Files containing "Who" content almost certainly (98%
   confidence) also contain "What". "How" and "What" are strongly co-occurring.
6. **Feature importance:** Statistical (TF-IDF) features outperform heuristics
   overall (F1 drops from 0.746 to 0.706 without them). Heading-based heuristics
   are the most useful heuristic subtype.
7. **Per-category F1:** "How" is best (0.861), "Contribution" second (0.814),
   "Other" worst (0.303).
8. **User perception:** 60% preferred auto-labeled README files; only 2/20
   preferred the unlabeled version.

---

## Relevance to My Thesis
This paper is directly relevant to the AI-based component of the FAIRness
assessment system in several ways:

- **README as the primary documentation artifact:** Your thesis focuses on
  assessing README quality for FAIR4RS reusability and findability indicators.
  Prana et al. establish that READMEs are structured into predictable content
  types — this supports the idea that LLM-based scoring can be guided by
  section-level content signals.
- **Content gaps map to FAIR gaps:** The finding that "Why" (purpose/motivation)
  and "When" (project status) sections are rare in practice directly maps to
  FAIR4RS reusability deficits. Your LLM rubric dimensions (installation
  instructions, usage description, contribution guidelines, dependency
  description) overlap strongly with the "How", "Who", and "Contribution"
  categories here.
- **Methodological foundation:** The coding schema (especially What/How/When/Who/
  Contribution) can serve as a structural reference for defining your LLM scoring
  rubric. The annotation methodology and inter-rater agreement process are also
  relevant for your ground truth construction (30 manually annotated repos).
- **Baseline comparison:** The SVM classifier in this paper represents a
  rule/heuristic-based NLP baseline that pre-dates LLMs. Your work extends this
  line by replacing or augmenting such classifiers with instruction-tuned LLMs for
  qualitative scoring.

---

## Important Insight
> The scarcity of "Why" and "When" content in README files is not just a
> documentation style issue — it reflects a systematic gap in communicating
> *purpose* and *maturity* of software. These are exactly the dimensions that
> FAIR4RS reusability requires but rule-based tools like F-UJI cannot detect.
> This validates your thesis's core argument: rule-based tools miss qualitative
> content, and AI is needed to fill that gap.

A secondary insight: heading-level features are strong signals for content
classification. This suggests that prompting an LLM to look at section headings
alongside content (rather than treating the README as a flat blob of text) could
improve your AI component's consistency and interpretability.

---

## Limitations / Gaps
- **English-only:** Non-English READMEs were excluded, limiting generalizability
  to international research software communities.
- **GitHub-only:** Findings may not generalize to other platforms (e.g., GitLab,
  Zenodo, Codeberg) — relevant since your thesis notes these as future work.
- **No quality assessment:** The paper categorizes *what* content is present, not
  *how well* it is written. It cannot distinguish a good installation guide from a
  poor one — this is precisely the gap your LLM component addresses.
- **Single survey, small N:** 20 participants for the perceived usefulness study
  is limited; recruited via Mechanical Turk which may introduce selection bias.
- **Static snapshot:** READMEs were collected at one point in time; no longitudinal
  analysis of how documentation evolves.
- **"Other" category weak:** F1 = 0.303 for "Other" suggests the classifier
  struggles with edge cases, implying that LLMs (with richer context understanding)
  may handle ambiguous content better.

---

## Keywords
`README files` · `GitHub` · `documentation quality` · `content classification` ·
`multi-label classification` · `SVM` · `TF-IDF` · `open coding` · `MSR` ·
`software documentation` · `FAIR` · `reusability`

---

## Use Later In

### Literature Review
- Cite as foundational work establishing that README content is categorizable and
  that qualitative dimensions (Why, When) are systematically underrepresented.
- Use to motivate why rule-based tools cannot assess documentation quality — they
  detect *presence* of a README, not its *content* or *completeness*.
- Position your LLM approach as a natural extension: where Prana et al. classify
  *what type* of content exists, your system scores *how well* FAIR-relevant
  content is expressed.

### Methodology
- Use the eight-category coding schema as a structural reference when defining your
  LLM rubric dimensions (especially the mapping: How ↔ installation/usage;
  Contribution ↔ contribution guidelines; Who ↔ license/credits; When ↔ project
  status).
- Reference their annotation methodology (open coding, inter-rater Kappa, majority
  vote) as a model for your own ground truth construction process.
- Cite the section-level feature importance findings to justify prompting the LLM
  at the section/heading level rather than on the full README text.

### Evaluation
- Use the finding that 'How' and 'What' sections dominate to contextualize why
  your system might score higher on those FAIR dimensions across repositories.
- Reference the per-category F1 scores as a prior NLP baseline to compare against
  if you implement any classification step in your pipeline.

### Discussion
- Use the "Why" and "When" scarcity findings as empirical evidence supporting your
  argument that current documentation practices do not meet FAIR4RS reusability
  requirements.
- Discuss how the low F1 for ambiguous categories ("Other") in rule/heuristic
  systems motivates LLM-based approaches that handle nuance better.
- Reference the positive user perception of labeled READMEs as indirect support
  for the value of making documentation quality assessments interpretable and
  transparent — aligned with your thesis's transparency design goal (separate
  rule-based and AI scores).


# Treude, Middleton & Atapattu (2020) — Beyond Accuracy: Assessing Software Documentation Quality

---

## Full Citation
Treude, C., Middleton, J., & Atapattu, T. (2020).
Beyond Accuracy: Assessing Software Documentation Quality.
In *Proceedings of the 28th ACM Joint European Software Engineering Conference
and Symposium on the Foundations of Software Engineering (ESEC/FSE '20)*,
pp. 1509–1512.
https://doi.org/10.1145/3368089.3417045

---

## Main Contribution
Proposes a ten-dimensional framework for assessing software documentation
quality, adapted from the data and information quality community (Wang &
Strong 1996; Eppler 2001). The framework goes deliberately "beyond accuracy"
— the dominant focus of prior work — to cover dimensions such as readability,
clarity, structure, and conciseness. A pilot study with four technical editors
evaluating 41 documents across five documentation genres (reference docs,
README files, tutorials, blog articles, Stack Overflow threads) provides initial
empirical evidence for the framework's applicability and reveals genre-level
quality trends.

---

## Key Ideas
- Documentation quality cannot be reduced to accuracy and completeness alone;
  these are necessary but not sufficient conditions for useful documentation.
- Quality is multi-dimensional: the paper defines ten dimensions spanning
  **structure** (structure, cohesion), **content** (quality, effectiveness,
  consistency, clarity, understandability), and **style** (appeal, readability,
  conciseness).
- Each dimension is operationalized as a single answerable question (e.g.,
  "Does the document contain ambiguity?" for Clarity), making the framework
  practically applicable as a rubric or scoring instrument.
- README files and reference documentation rank highest across most quality
  dimensions; blog articles rank lowest across all ten.
- The framework is designed to be genre-independent and assessable without
  reference to external artefacts (i.e., no code or task context needed).

---

## The Ten Quality Dimensions

| Dimension | Question |
|---|---|
| Quality | How well-written is this document (spelling, grammar)? |
| Appeal | How interesting is it? |
| Readability | How easy was it to read? |
| Understandability | How easy was it to understand? |
| Structure | How well-structured is the document? |
| Cohesion | How well does the text fit together? |
| Conciseness | How succinct is the information provided? |
| Effectiveness | Does the document make effective use of technical vocabulary? |
| Consistency | How consistent is the use of terminology? |
| Clarity | Does the document contain ambiguity? |

---

## Methodology

### Dataset
- 41 documents sampled across five genres, all related to the R programming
  language (controlled for domain variation).
- Reference documentation (8), README files (8), tutorials (8), blog articles
  (9), Stack Overflow threads (8).
- Sources: R language manual, GitHub-curated R projects, tutorialspoint.com,
  R-bloggers.com, Stack Overflow.

### Approach
- **Framework design:** Authors reviewed dimensions from Wang & Strong (1996),
  Eppler (2001), and Knight & Burn (2005), selecting those applicable to
  software documentation, independent of access logistics, and checkable
  without external artefacts. Accuracy and completeness were explicitly
  excluded as they require external reference points.
- **Pilot study:** Four technical editors recruited via Upwork (required:
  technical writing + programming experience). Editors rated each document
  on all ten dimensions using a 1–10 scale and also suggested edits in
  Microsoft Word.
- Most documents were rated by two editors (75 total evaluation records).

### Evaluation
- Results reported as average dimension rating per genre (Table 3).
- No inter-rater agreement metric reported for this pilot — acknowledged
  as a limitation.
- Edit data (4,000+ events) was collected but ultimately not analysed due
  to technical challenges with Word formatting artefacts.

### Tools / Models
- Microsoft Word (Review interface) for edit collection.
- No automated NLP or ML models — purely human expert assessment.
- Framework derived from: Wang & Strong (1996), Eppler (2001),
  Knight & Burn (2005), Pitler & Nenkova (2008).

---

## Important Findings
1. **README files score high:** Among the top-rated genres for structure (7.6),
   understandability (7.0), appeal (6.5), and clarity (8.7). Only reference
   documentation scores higher on some dimensions.
2. **Blog articles score lowest across all ten dimensions**, particularly in
   readability (4.6) and structure (3.8) — a surprising result the authors
   did not expect given the framework was designed to reduce genre bias.
3. **Consistency is the most uniformly high dimension** across all genres
   (range: 8.5–9.3), suggesting terminology consistency is generally well
   handled in software documentation.
4. **Structure shows the widest variance** (3.8 for blogs vs. 7.6 for READMEs),
   meaning it is the dimension most sensitive to documentation genre.
5. **Appeal is universally low** (5.3–6.5), suggesting software documentation
   is rarely perceived as engaging regardless of genre.
6. Accuracy and completeness were deliberately excluded from the framework
   because they require external context — a key theoretical choice that
   separates this work from prior documentation research.

---

## Relevance to My Thesis
This paper is the most direct theoretical foundation for your LLM-based
documentation quality scoring component. Specifically:

- **The ten-dimension framework directly informs your LLM rubric.** Your
  rubric dimensions (clarity and completeness of installation instructions,
  presence of usage examples, contribution guidelines, dependency descriptions)
  map onto Treude et al.'s dimensions: Understandability, Clarity, Structure,
  Completeness (implicitly), and Effectiveness. You can cite this framework
  as the theoretical basis for *why* you chose qualitative dimensions and
  *how* they are operationalized.
- **The "beyond accuracy" argument is your core justification.** Rule-based
  tools like F-UJI check for the *presence* of documentation — effectively
  an accuracy/completeness check. This paper provides theoretical grounding
  for why that is insufficient and why dimensions like clarity, structure,
  and understandability require a different assessment method (i.e., your
  LLM component).
- **README files score well structurally but vary in deeper dimensions.**
  This supports your thesis's assumption that README presence is not the
  same as README quality — a repository can have a README that passes
  rule-based checks but still fails on understandability or clarity.
- **The framework is designed to be assessable without external artefacts**
  (no code context needed), which validates using it as a prompt rubric for
  an LLM that only sees the README text.
- **The pilot used human expert raters** — directly analogous to your
  manual ground truth annotation of 30 repositories. You can cite their
  methodology when justifying your own annotation process and its limitations
  (single annotator, small N).

---

## Important Insight
> The deliberate exclusion of *accuracy* and *completeness* from this
> framework is theoretically significant for your thesis. It means that
> even a "complete" README (one that passes F-UJI's rule-based checks)
> can still score poorly on readability, clarity, or structure. This is
> your strongest theoretical argument for why rule-based FAIRness
> assessment is insufficient on its own, and why an LLM — capable of
> evaluating these softer dimensions — adds genuine value beyond what
> any rule-based tool can provide.

A secondary insight: the framework's questions are short, direct, and
answerable on a numeric scale — this is essentially the format of a
structured LLM prompt. You could adapt these questions almost directly
as sub-prompts in your LLM scoring rubric and cite Treude et al. as
the source, giving your rubric design a peer-reviewed theoretical anchor.

---

## Limitations / Gaps
- **Very small pilot:** Only 4 technical editors and 41 documents. Results
  are preliminary and the authors are explicit that this is a vision paper,
  not a full empirical study.
- **No inter-rater reliability reported:** The absence of a Kappa or ICC
  score means we cannot assess how consistently the framework is applied
  across raters — a significant gap for a quality assessment instrument.
- **Single programming language (R):** All documents are R-related, limiting
  generalizability across languages and domains — directly relevant to your
  multi-domain dataset of research software repositories.
- **No automated component:** The framework is entirely manual. The paper
  proposes future automated classification but does not implement it —
  this is precisely the gap your LLM component fills.
- **Edit data unusable:** The 4,000+ editor edits could not be analysed due
  to Word formatting artefacts, leaving the qualitative "how documentation
  fails" question unanswered.
- **Genre preconception bias acknowledged:** Editors may apply different
  implicit standards to different genres (an "8" for a README may not equal
  an "8" for a Stack Overflow post), undermining cross-genre comparability.
- **Dimensions overlap:** The paper itself acknowledges ambiguity between
  similar dimensions (e.g., structure vs. cohesion, clarity vs.
  understandability) — a challenge that also applies when prompting an LLM
  with these dimensions.

---

## Keywords
`documentation quality` · `software documentation` · `quality framework` ·
`readability` · `clarity` · `structure` · `README files` · `beyond accuracy` ·
`information quality` · `technical editing` · `multi-dimensional assessment`

---

## Use Later In

### Literature Review
- Cite as the primary theoretical framework justifying multi-dimensional
  documentation quality assessment beyond presence/absence checks.
- Use the "beyond accuracy" argument to position F-UJI and rule-based tools
  as incomplete — they assess accuracy/completeness at best, while dimensions
  like clarity, understandability, and structure remain unevaluated.
- Note that this paper proposes future automated classification models for
  documentation quality — your thesis is a direct implementation of that
  vision, applied to the FAIRness context.
- Cite alongside Prana et al. (2019) to show the progression: Prana
  categorizes *what* is in READMEs; Treude et al. defines *how to judge
  quality*; your thesis applies LLMs to *automate that judgment* for
  FAIR4RS indicators.

### Methodology
- Use the ten-dimension framework as the theoretical basis for your LLM
  rubric design. Map your rubric dimensions explicitly to the relevant
  Treude et al. dimensions in your methodology chapter.
- Cite the framework's design principle (assessable without external
  artefacts) to justify why your LLM prompt uses only README text as input.
- Reference their pilot study methodology (expert raters, structured rubric,
  numeric scale) as a methodological precedent for your manual ground truth
  annotation.
- The 0–2 scoring scale in your rubric is a simplified version of their
  1–10 scale — cite this design choice and justify the simplification
  (consistency, LLM reliability at coarser scales).

### Evaluation
- Use their finding that README files score high on structure but vary on
  deeper dimensions to contextualize why some repositories in your dataset
  may pass rule-based checks but fail LLM-based quality scoring.
- Reference the lack of inter-rater reliability reporting in their pilot
  as motivation for why your thesis explicitly measures annotator consistency
  in ground truth construction.

### Discussion
- Discuss the overlap between Treude et al.'s dimensions and your FAIR4RS
  reusability indicators — clarity of installation instructions (Clarity +
  Understandability), dependency descriptions (Effectiveness), contribution
  guidelines (Structure).
- Use the "blog articles score lowest" finding to make a broader point:
  documentation quality is not uniform across genres or repositories, which
  is why automated scalable assessment (your system) is needed.
- Acknowledge the dimension overlap limitation (structure vs. cohesion) as
  a parallel challenge in LLM prompting — and explain how your rubric
  addresses this through more concrete, FAIR-specific operationalizations.


  # Imani et al. (2024) — Does Documentation Matter? An Empirical Study of Practitioners' Perspective on OSS Adoption

---

## Full Citation
Imani, A., Radmanesh, S., Ahmed, I., & Moshirpour, M. (2024).
Does Documentation Matter? An Empirical Study of Practitioners' Perspective
on Open-Source Software Adoption.
*arXiv preprint arXiv:2403.03819*
https://doi.org/10.6084/m9.figshare.24210366.v1

---

## Main Contribution
First empirical study to systematically examine the role of OSS documentation
in industry practitioners' adoption decision-making (PAP — Practitioners'
Adoption Procedure). Through interviews (n=10) and surveys (n=42+29), the
authors identify nine adoption criteria that practitioners look for in OSS
documentation, the challenges they face, and the confidence levels they have
in finding relevant information. They then build two automated tools: a
BERTopic-based topic model to extract PAP-relevant documentation sections,
and DocMentor — a hybrid TF-IDF + ChatGPT system that augments documentation
with explanations, examples, and references to improve comprehension across
varying domain knowledge levels.

---

## Key Ideas
- OSS documentation is a primary, heavily used resource in industry adoption
  decisions — 91.18% of survey participants confirmed relying on it.
- Practitioners rated documentation importance at a median of 4–5 out of 5,
  yet they report significant challenges in finding relevant information within
  it (findability, missing information, reading challenges, version/doc
  inconsistency).
- Nine adoption criteria emerge from practitioner interviews: Project
  Maintenance, Compatibility, Functionality, License Compatibility, Community
  Adoption, Existence of Use Case Examples, Ease of Use, Project Versioning,
  Performance.
- Not all documentation content is equally relevant to adoption; automated
  topic-level extraction can filter PAP-relevant sections from large corpora.
- LLMs (ChatGPT) can augment documentation to improve comprehension, though
  effectiveness varies by criterion and practitioner domain knowledge level.
- Findability of relevant information is the top reported challenge —
  practitioners know what they need but struggle to locate it in documentation.

---

## Methodology

### Dataset
- **Interview corpus:** 10 senior practitioners (avg. 20 years industry
  experience, avg. 20 years OSS experience), diverse sectors.
- **Survey corpus:** 42 participants (interview triangulation survey) +
  29 additional respondents (online survey via Qualtrics + LinkedIn + snowball
  sampling). Average experience: 11–15 years software industry, 6–10 years
  OSS integration.
- **OSS documentation corpus:** 1,383 Sphinx-based documentation websites
  (from Read the Docs), covering 52 OSS domains derived from GitRanking
  taxonomy (top 50% of GitHub topics). Final dataset: 744,608 unique sentences.

### Approach
- **RQ1 & RQ2 (Practitioner perspective):** Semi-structured remote interviews
  (avg. 30 min, recorded, transcribed). Two authors independently coded
  transcripts using negotiated agreement; 81% inter-annotator agreement.
  Survey used Likert scale, multiple-choice, and open-ended questions.
- **RQ3 (Topic extraction):** Guided BERTopic (semisupervised) trained on
  744,608 sentences. Embedding: all-MiniLM-L6-v2 (SBERT). Dimensionality
  reduction: UMAP. Clustering: HDBSCAN. Topic representations fine-tuned via
  KeyBertInspired + MaximalMarginalRelevance (MMR). Five Topics of Interest
  (TOIs): License, Functional Suitability, Compatibility, Project Maintenance,
  Outlier. Evaluated on 447 manually labelled sentences (95% CI, 5% margin
  of error). Weighted F1 = 69%.
- **RQ4 (Documentation augmentation):** DocMentor = TF-IDF (for known
  technical term detection across domain-specific corpus) + ChatGPT (for
  novel term detection + explanation/example/reference generation). Evaluated
  by 10 practitioners on 5-point Likert scale across 5 dimensions.

### Evaluation
- Topic model: weighted average precision 73%, recall 68%, F1 69%.
- DocMentor: median informativeness 3.75/5, technical term clarification
  3.75/5, comprehension improvement 3.75/5, PAP helpfulness 3/5.
- Weakest DocMentor performance: project maintenance (familiar terminology).
  Strongest: license comprehension improvement (median 4/5).

### Tools / Models
- BERTopic (semisupervised, guided topic modeling)
- SBERT (all-MiniLM-L6-v2 embeddings)
- UMAP + HDBSCAN (dimensionality reduction + clustering)
- OpenAI ChatGPT (term explanation + augmentation)
- TF-IDF (technical term detection)
- Qualtrics (survey distribution)
- HTTrack (documentation mirroring)

---

## Important Findings
1. **Documentation is critical to adoption:** 100% of interviewees and 91.18%
   of survey participants confirmed relying on OSS documentation for adoption
   decisions. Median importance rating: 5/5 (interviews), 4/5 (survey).
2. **Findability is the top challenge:** The most frequently reported
   documentation challenge was difficulty *finding* relevant information —
   practitioners know what they need but cannot locate it efficiently.
3. **Missing information is the second most cited challenge**, followed by
   reading difficulties, version/documentation inconsistency, and inaccurate
   dependency documentation.
4. **Practitioner confidence is low for critical criteria:** Confidence in
   finding license information, functionality, and use case examples is only
   moderate (median 3–4/5). Project versioning has the lowest confidence
   (median 2.75 in interviews).
5. **Top adoption criteria:** Maintenance and compatibility ranked highest in
   importance, followed by functionality, license, and community adoption.
6. **BERTopic achieves reasonable but imperfect extraction:** F1 = 69% on
   PAP-relevant topic classification. False positives arise from terminology
   overlap between topics (e.g., "permission/license" appearing in functional
   suitability context).
7. **LLM augmentation is promising but not yet reliable enough:** DocMentor
   median scores cluster around 3.75/5 — useful but with clear room for
   improvement. PAP helpfulness specifically scored only 3/5, suggesting
   augmentation needs further tailoring to adoption workflows.

---

## Relevance to My Thesis
This paper connects to your thesis from the practitioner-side perspective —
it empirically validates why documentation quality matters for software
adoption and reuse, and it directly supports the LLM component of your
FAIRness assessment system.

- **Empirical validation of your thesis premise:** The finding that 91% of
  practitioners rely on OSS documentation for adoption decisions, and that
  findability and missing information are the top challenges, directly
  supports your argument that improving documentation assessment (via your
  hybrid FAIRness system) has real-world impact on software reuse and
  reproducibility.
- **Adoption criteria ↔ FAIR4RS reusability indicators:** The nine practitioner
  criteria map closely onto your LLM scoring rubric dimensions. Specifically:
  Ease of Use ↔ clarity of usage instructions; Functionality/Examples of Use
  Cases ↔ presence of examples and tutorials; License Compatibility ↔ license
  indicator (rule-based); Project Maintenance/Versioning ↔ project status
  (FAIR4RS findability); Compatibility ↔ dependency specification. This mapping
  lets you argue that your rubric is grounded in what practitioners actually
  need, not just what the FAIR framework prescribes.
- **DocMentor as a parallel to your AI component:** DocMentor combines a
  corpus-based method (TF-IDF) with an LLM (ChatGPT) to assess and augment
  documentation — structurally similar to your hybrid approach (rule-based +
  LLM). You can position your work as a FAIRness-specific instantiation of
  this general hybrid paradigm, applied to assessment rather than augmentation.
- **LLM reliability concerns validated:** DocMentor's moderate PAP helpfulness
  score (median 3/5) and the BERTopic false positive problem (terminology
  overlap) provide empirical precedent for your thesis's second research
  question about LLM failure modes and reliability. Cite this paper when
  discussing why uncertainty quantification in your AI component is necessary.
- **Findability challenge motivates dimension-level assessment:** The finding
  that practitioners struggle to find relevant information within documentation
  supports your design choice to score documentation at a content dimension
  level (installation, usage, contribution) rather than just flagging README
  presence.

---

## Important Insight
> The top challenge practitioners report is not that documentation is *absent*,
> but that relevant information is *hard to find* within it. This is the
> practitioner-level analogue of your thesis's core argument: rule-based tools
> detect documentation presence (e.g., F-UJI flags "README exists") but cannot
> assess whether the right information is actually in there, clearly expressed,
> and easy to locate. This paper provides interview and survey data from real
> practitioners that directly validates why your LLM-based qualitative
> assessment is needed.

A secondary insight: the adoption criteria identified here (especially
Maintenance, Compatibility, Ease of Use, and Examples) are almost exactly
the FAIR4RS reusability sub-dimensions your LLM rubric targets. This means
you can cite Imani et al. as practitioner-side evidence that your rubric
dimensions are not arbitrary — they reflect what the industry actually looks
for when evaluating software for reuse.

---

## Limitations / Gaps
- **Snowball sampling bias:** Interview participants were recruited through
  personal networks, introducing potential selection bias toward certain
  industry sectors and experience levels.
- **Sphinx/Read the Docs only:** The OSS documentation corpus is restricted
  to Sphinx-based documentation, excluding GitHub READMEs, wikis, and other
  documentation formats — a significant gap since README files are the primary
  artifact in your thesis.
- **BERTopic F1 = 69%** is moderate; topic overlap (e.g., license vs.
  functional suitability terminology) causes systematic false positives —
  a challenge that LLM-based approaches with richer context understanding
  may handle better.
- **DocMentor evaluated by only 10 practitioners** on a small set of
  paragraphs — results are preliminary and not generalizable.
- **LLM used as black box:** ChatGPT prompts are fixed and iteratively tuned
  by one author; no systematic prompt engineering or ablation study is
  conducted. Reliability of LLM outputs is not formally characterized.
- **No FAIRness framing:** The paper addresses OSS adoption quality broadly
  but does not connect to FAIR principles, FAIR4RS, or reproducibility
  frameworks — the connection to your thesis requires explicit bridging.
- **Focus on augmentation, not assessment:** DocMentor improves documentation
  comprehension but does not score or assess documentation quality against a
  rubric — your thesis fills this gap by using LLMs for structured scoring.

---

## Keywords
`OSS documentation` · `software adoption` · `practitioner study` ·
`documentation quality` · `findability` · `BERTopic` · `topic modeling` ·
`LLM augmentation` · `ChatGPT` · `TF-IDF` · `information retrieval` ·
`open-source software` · `reuse` · `semi-structured interviews`

---

## Use Later In

### Literature Review
- Cite as empirical evidence that OSS documentation is the primary information
  source for adoption decisions — grounding your thesis in real practitioner
  behaviour rather than theoretical FAIR arguments alone.
- Use the findability challenge finding to argue that documentation *presence*
  (what rule-based tools detect) is insufficient — what matters is whether
  relevant information is *present, clear, and locatable*, which requires
  qualitative assessment.
- Map the nine adoption criteria to your FAIR4RS reusability indicators
  explicitly in a table or paragraph, citing this paper as the practitioner-
  side validation of your rubric's relevance.
- Position DocMentor as a parallel hybrid (rule-based + LLM) system, and
  differentiate your work: DocMentor augments documentation for comprehension;
  your system assesses documentation quality for FAIRness scoring.

### Methodology
- Cite the interview-derived adoption criteria as external validation for
  your LLM rubric dimensions — they were not invented for FAIR but emerge
  independently from what practitioners need.
- Reference the negotiated agreement annotation methodology (81% inter-rater
  agreement) as a methodological precedent comparable to your manual ground
  truth construction.
- Use the BERTopic topic overlap problem (license vs. functional suitability)
  to motivate why keyword/embedding-based classifiers are insufficient for
  nuanced documentation quality assessment, and why LLM-based approaches
  with full context understanding are preferable.

### Evaluation
- Reference DocMentor's PAP helpfulness score (median 3/5) when discussing
  the limitations of your own LLM component — it sets a realistic baseline
  for what current LLM-assisted documentation tools can achieve.
- Cite the practitioner confidence levels (median 3–4/5 for most criteria)
  as context for interpreting your own system's performance: even human
  practitioners are not always confident in finding what they need.

### Discussion
- Use the practitioner adoption criteria as a bridge between the FAIR4RS
  principles (abstract, principle-level) and real-world software reuse needs
  (concrete, practitioner-level). This strengthens the argument that assessing
  FAIRness documentation quality is not just an academic exercise but directly
  impacts whether software gets adopted and reused.
- Discuss LLM reliability concerns raised by DocMentor's evaluation in
  parallel with your own findings on LLM failure modes (your RQ2), citing
  this paper as prior evidence that LLM-based documentation tools face
  consistent challenges with domain-specific terminology and maintenance-
  related content.
- Note the Sphinx-only limitation as a gap your thesis partially addresses
  by focusing on README files — a more universally available and standardized
  documentation artifact across GitHub repositories.
