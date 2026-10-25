# KGLink source verification and chapter handoff

Updated 2026-10-24. Chapter owner: KGLink writing agent. Status: **AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT**. Full source reading, downloaded-PDF comparison, adopted table-cell checks, and original-asset copying complete; integrated thesis PDF QA remains pending. The author explicitly confirmed that the arXiv versions linked on their website are the formally published PDF versions. The downloaded file is accurately described as author-confirmed publication-equivalent; direct IEEE acquisition remains unavailable.

## Source identity

- Selected source: `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/KGLink/KGLink_ICDE_revision/KGLink.tex`, as specified by `source_roots.json`.
- Local compiled PDF: same directory, `KGLink.pdf`. Its 13-page text and active TeX were inspected; it is explicitly recorded as a local research copy, not an IEEE download.
- Another root-level `KGLink_ICDE.pdf` is dated 2023-11-20 and has an older abstract and method wording. It is excluded from the chapter.
- Publication metadata: Yubo Wang, Hao Xin, Lei Chen, “KGLink: A Column Type Annotation Method that Combines Knowledge Graph and Pre-Trained Language Model,” ICDE 2024, pp. 1023–1035, DOI `10.1109/ICDE60146.2024.00083`, IEEE document 10597678. Metadata confirmed against IEEE-deposited Crossref DOI metadata, saved as `planning/kglink-sources/crossref.json`, and the author's publication list.
- Download attempts: IEEE document page and `stampPDF/getPDF.jsp?tp=&arnumber=10597678` returned a JavaScript robot-verification HTML page, not a PDF. The HTML response is retained as `planning/kglink-sources/ieee-download.bin`. An `iel7` request also returned HTML. These are failed acquisitions, not publication evidence.
- Local source/PDF/BibTeX hashes: `planning/kglink-sources/manifest.json`.

## Publication-equivalent comparison and adopted material

Downloaded `https://arxiv.org/pdf/2406.00318` to `planning/kglink-sources/kglink-author-confirmed-publication.pdf` (v1). After removing its exact arXiv side stamp and tokenizing whitespace, the entire extracted PDF text is identical to the selected local PDF: equality true. `planning/kglink-sources/comparison.json` preserves the comparison method and counts. This establishes that the local selected research PDF and the author-confirmed reference agree in their textual content; it does not assert a byte-identical IEEE file.

Visually reviewed the relevant downloaded PDF pages 3–10 and 12, including the source architecture, entity-filtering, DMLM, result, ablation, and row-filter objects. Original assets were copied after this comparison. SHA256 source/target equality is recorded for all nine images in `planning/kglink-assets.json`, including original figure number, physical PDF page, and destination. None was redrawn or edited.

| Adopted evidence | Source TeX | Publication-equivalent physical page | Target | Check |
|---|---|---:|---|---|
| Motivation subfigures | 112–130 | 3, Fig. 2(a,b) | fig:kglink:motivation | Original PDF assets; visual match |
| Framework | 168–177 | 4, Fig. 3 | fig:kglink:framework | Original PNG; visual match |
| KG process | 218–222 | 5, Fig. 4 | fig:kglink:kg-pipeline | Original PDF; visual match |
| Neighborhood example | 256–260 | 6, Fig. 5 | fig:kglink:overlap | Original PNG; visual match |
| Masked-type training | 343–349 | 7, Fig. 6 | fig:kglink:representation | Original PNG; visual match |
| Runtime | 495–502 | 9, Fig. 7 | fig:kglink:runtime | Original PDF; printed values used |
| Main results | 542–579 | 9, Table I | tab:kglink:main | 28 cells incl. 2 missing marks checked |
| Ablation scores | 621–648 | 10, Table II | tab:kglink:ablation | 20 numeric cells checked; score-column projection |
| No-KG subset | 810–824 | 12, Table IV | tab:kglink:no-kg | 12 numeric cells checked |
| Row-filter comparison | 828–849 | 12, Table V | tab:kglink:row-filter | 8 numeric cells checked |
| Row-budget curves | 899–910 | 12, Fig. 10(a,b) | fig:kglink:row-budget | Both original PDF subfigures; no plot digitization |

Per-cell records, row source lines, datasets, conditions, target labels, and statuses are in `planning/kglink-table-cells.tsv` (68 records). Main-model values are the original three-run averages. Input constraints, training settings, exact-label metrics, and the no-linkage subset definition were checked against Section IV and Section V of the reference PDF.

## Research question and formula map

RQ1 concerns supplementing table context with graph evidence while learning the target dataset's type vocabulary. The chapter explains BM25 cell linking; cross-column one-hop filtering; row ranking by linking score; candidate-type aggregation across rows; the KG feature sequence; whole-table serialization; contextual masked-type representation training; classification; and uncertainty weighting. Its source publication is acknowledged at chapter opening.

| Target formula | Original equation | Physical page | Treatment |
|---|---:|---:|---|
| eq:kglink:entity-filter | 3 | 5 | Same set operation; explicit column-set notation |
| eq:kglink:cell-score | 4 | 5 | Same maximum; nonempty-set condition stated |
| eq:kglink:row-score | 5 | 5 | Same sum |
| eq:kglink:serialization | 11 | 7 | Same multi-column sequence with explicit special tokens |
| eq:kglink:vocabulary-projection | 14 | 8 | Same temperature-scaled vocabulary projection |
| eq:kglink:dmlm | 13 | 8 | Source order preserved exactly: masked probabilities multiply log ground-truth probabilities |
| eq:kglink:classification | 16 | 8 | Logit notation renamed locally; same cross-entropy |
| eq:kglink:joint-loss | 17 | 8 | Same uncertainty-weighted objective |
| eq:kglink:preprocessing | Section III.C expression | 8 | Reproduced reported asymptotic expression; no new theorem |

The main agent added the vocabulary projection and DMLM expression to the current chapter. The expression has been checked against original Eqs. 14 and 13 on reference PDF p. 8: `-sum y_msk log y_gt`, with the original distribution order intact. The task description follows the publication prose. The implementation's composition function phi is not assigned a guessed operation. No random seed, teacher-freezing rule, or optimizer setting absent from the source is invented.

## Source conflicts and author-directed treatment

The author has directed that publication prose takes precedence over internal table conflicts. These differences remain recorded for traceability.

1. **VizNet denominator.** TeX 525 states multi-column VizNet has 32,265 tables, 73,034 columns, and 77 types. Table III (TeX 744) lists 74,141 total columns. Its counts (9,489 numeric; 9,278 non-numeric without feature-vector evidence; 55,374 without candidate types) use the latter denominator. Chapter uses 73,034 from the dataset prose as explicitly authorized. Table III is not adopted; its counts/percentages are not recomputed.
2. **Ablation component mask.** Table II row `KGLink w/o fv` (TeX 638) leaves the KG-candidate-type column empty and ticks KG feature vector. The prose at TeX 702 defines this variant as removing the feature vector. Scores are 87.02/85.68 (SemTab) and 95.98/95.70 (VizNet). The chapter follows the prose definition and adopts only the numeric score columns. The contradictory checkmark columns are not reproduced or silently edited. The `w/o ct` prose removes both KG sources and matches the empty columns.
3. **DMLM direction.** Eq. 13, TeX 377, writes `-sum y_msk log y_gt`. The narrative describes recovering masked representations from contextual ground-truth representations. Retain the published formula once obtained; do not reverse it based on conventional teacher/student expectations. The current chapter now reproduces this formula without reversing the distributions, and explains the task using publication prose. No implementation claim about gradient conventions is added.
4. **Numeric statistics.** TeX 291 describes “mean, variance, and average value”; mean and average duplicate each other. The chapter states numeric summary information without inventing a third statistic such as median.
5. **Complexity language.** TeX 473 calls RECA exponential in the number of tables, while the commented comparison describes a quadratic `T^2` term. The chapter reproduces the preprocessing expression and explains operation-dependent costs. It does not repeat the exponential comparison or add a theorem.
6. **Qualitative labels.** TeX 878 names Artist/Year/Rank; TeX 880 later names Year/Code. No per-class numerical table resolves the mismatch. The chapter uses the uncontested SemTab qualitative cases and omits the disputed VizNet class list.

## Chapter and QA status

- Chapter: `chapter/ch03-kglink.tex`. TeXcount command `texcount -brief chapter/ch03-kglink.tex`: **4579 prose + 88 headings + 234 captions**, with 9 displayed math environments, 4 tables, and 7 figure environments (9 copied assets).
- Citation increment: `bibliography/kglink.bib`, 15 entries. KGLink DOI metadata directly checked against Crossref; baseline entries imported from the selected source and marked for central bibliography verification.
- Defensive-language audit: `planning/kglink-style-audit.md`; unnecessary non-claim caveats and reporting-process prose removed.
- Dependencies: graphicx, amsmath, booktabs; no shared macros or algorithm environment required by this chapter.
- Compile/layout status: independently syntax-inspected; final integrated template compilation, page widths, figure legibility, and thesis PDF QA are the main agent's next checks. No full-thesis compile result is claimed here.


## Independent round-two integration — 2026-10-25

The implementation description now explicitly states up to three candidate types per row from the KG entities in each column, following controlling PDF p9 §IV.B and source around line663. It is placed with candidate types, so the preceding ten-entity limit still refers to retrieved entities. The selected Athlete/Protein/Film result keeps the >10-test-sample and top-three-increase criterion, but omits9.70: both source around line874 and PDF p12 report it without a unit. No percentage/percentage-point interpretation was invented. All9 KGLink displayed math blocks are unchanged; repeated serialization/no-linkage scope prose was consolidated without changing the dataset subset or measured scores.

Current PDF/counts and visual findings are in `FINAL_QA.md`; prior chapter audit counts remain historical. Full dispositions: `review-round2/REVIEW_SUMMARY.md`. No new experiment was run.
