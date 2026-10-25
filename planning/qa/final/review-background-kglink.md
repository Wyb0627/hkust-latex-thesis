# Final integrated PDF review: Background and KGLink

Reviewed 2026-10-24 against the frozen `thesis.pdf` (138 physical pages), SHA-256:

`406fd804f8eb9cfcff57396e0556087bede62b347fa64ee79f2117828b170b87`

Scope: physical pp. **24–54**, printed pp. **10–40**. Chapter 2 occupies physical pp. 24–35; Chapter 3 occupies pp. 36–54. This matches `planning/qa/final/pdf-preflight.json`.

## Result

**No blocking or actionable rendering defects found in the reviewed chapters.** Original figures, all six tables, and all ten numbered equations in this scope are present and readable. No clipping, overlapping labels, missing glyph boxes, obscured legends, broken table rules, or unresolved cross-reference marks were found.

## Inspection method and coverage

- Inspected `contact-2.png` and `contact-3.png` for every page in the assigned range, including chapter openings, text flow, page furniture, float distribution, and heading placement.
- Independently rendered physical pp. **29, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 50, 52, 53** from the frozen final PDF using `pdftoppm -r 120 -png -singlefile`, then opened every render with `view_image`.
- The independent renders are temporary files in `/private/tmp/codex-bg-kglink-final-review/`; the reviewed artifact remains the frozen final PDF.
- Reviewed text extraction for physical pp. 24–54 for missing-reference/glyph/placeholder signals. The `???` occurring on p. 37 belongs to the original task-illustration graphic (unknown column heading), not an unresolved LaTeX reference.

## Figure checks

| Object | Physical / printed page | Finding |
|---|---|---|
| Figure 2.1, HKG decomposition | 33 / 19 | All four methods, arrows, relation/entity markers, combined relation labels, and color legend remain visible. Vector content is sharp. Caption is separate and fully inside the text block. Matches the previously verified original Fig. 1. |
| Figure 3.1, two annotation examples | 37 / 23 | Both subfigures and labels are aligned; player names, type labels, dates, and column markers remain legible. Neither subfigure is cropped. |
| Figure 3.2, KGLink overview | 38 / 24 | Entire two-part architecture is visible. Module names, colored pathways, loss blocks, and connections remain readable. The fine cell/token subscripts are necessarily smaller than the main module labels but remain sharp; the detailed pipeline and representation figures provide larger views. |
| Figure 3.3, KG processing | 40 / 26 | All three processing steps and score annotations remain legible. Figure, caption, and Eq. (3.1) have adequate separation. |
| Figure 3.4, cross-column example | 41 / 27 | Album/musician table, candidate entities, colored regions, red links, and labels are visible. It uses a centered float page with generous surrounding whitespace; this is clean and does not require repair. |
| Figure 3.5, representation task | 45 / 31 | Green masked and yellow ground-truth pathways, token/vector labels, and explanatory boxes remain legible. No box/arrow/caption collisions. |
| Figure 3.6, row budget | 52 / 38 | Both original curves remain intact, with readable axes, legends, `all` category, and subfigure labels. Table 3.4 and caption are separated from the plot. |
| Figure 3.7, runtime | 53 / 39 | Training/inference legend, numeric bar labels, method names, hour axis, and MTab `N/A` remain visible. Baseline labels at the smallest bars are retained and readable. |

No research image was redrawn or modified during this review. Prior source-copy and SHA-256 records remain in the chapter evidence ledgers.

## Table checks

| Object | Physical / printed page | Finding |
|---|---|---|
| Table 2.1, retrieval organizations | 29 / 15 | Three columns fit the text width; wrapped descriptions stay within cells and rows align. Citations are resolved. |
| Table 2.2, projected FormerGNN results | 34 / 20 | Dataset groupings and all seven rows are aligned; metric headers, three-decimal values, bold, and underline markings are visible. No row splits or lost rules. |
| Table 3.1, main annotation results | 49 / 35 | Both dataset groups and accuracy/F1 columns align. MTab's missing-value hyphens remain missing entries; best-value bolding is visible. |
| Table 3.2, ablation score projection | 50 / 36 | Variant names and all four score columns are readable; no clipped DeBERTa row or overlapping caption. |
| Table 3.3, no-KG subset | 50 / 36 | Numeric/non-numeric headers and all rows fit. It is clearly separated from Table 3.2. |
| Table 3.4, row filter | 52 / 38 | Long row names fit; grouped headers and all values align. Caption is not split from the table. |

## Equations, labels, and typography

- Eq. **(2.1)** on physical p. 32: qualifier-set subscripts and upper bound render correctly.
- Eq. **(3.1)** on p. 40: set union, intersection, neighborhood notation, and cell indices fit without collision with the equation number.
- Eqs. **(3.2)–(3.3)** on p. 42: maximum/summation limits, cell/row indices, and labels are clear.
- Eq. **(3.4)** on p. 44: the two-line serialization expression stays inside the text block with its number aligned to the right. Special-token brackets and column indices render correctly.
- Eq. **(3.5)** on p. 45: Softmax, projection, fraction, and temperature symbol are intact.
- Eqs. **(3.6)–(3.8)** on p. 46: DMLM distribution order matches the preserved source expression; CE denominator and uncertainty-weighted fractions are visible, with no clipped symbols or numbering overlap.
- Eq. **(3.9)** on p. 47: preprocessing expression and nested parentheses are legible.
- Captions, chapter and section headings, italic model/type names, mathematical fonts, and centered footer page numbers are consistent across the inspected range.
- The Chapter 3 discussion heading on p. 53 is followed by body text and continues on p. 54. It is not stranded at the page bottom.

This review certifies visual rendering for the stated scope and frozen hash. It does not extend to other chapters, submission metadata, or an altered/recompiled PDF.

## Final freeze revalidation

The subsequently frozen deliverable has **137 physical pages**, SHA-256:

`ba011690c5fb5fab2cfdff754c3284f1f898407f2a0c8f3d7b30065c5fc8c83f`

Revalidated 2026-10-24. Chapter 2/3 physical pagination remains **24–54**. Using the same `pdfplumber` `page.extract_text()` method as `scripts/inspect_thesis_pdf.py`, compared the final PDF's 31 pages with the page-text snapshots used for the visual review above: **zero text deltas on all 31 pages**. The main agent confirms the chapter sources have not changed; the later changes normalize external bibliography months and add HyperFormer's DOI. No further raster review is needed for these unchanged chapter pages. The visual findings above therefore carry forward to this final hash for the same chapter scope.

### Independent check of new headline quantitative claims

Separately read the actual final-PDF abstract (physical p. 2) and Introduction §1.4 quantitative paragraph (physical p. 22). The following checks use original per-chapter source ledgers and published-table transcriptions, independently of the new headline wording.

| Claim in final abstract/introduction | Independent evidence | Result |
|---|---|---|
| KGLink VizNet weighted F1 **96.07%**; Introduction compares Doduo **95.06** on the percentage scale | `planning/kglink-table-cells.tsv`, original KGLink Table I, VizNet weighted F1 column; full model uses BERT | Correct scores, dataset, and scale. No source-prose arithmetic error was inherited. |
| GORAG fourth-round WOS ten-shot accuracy **0.4929**, Qwen2.5-7B; Introduction also states same-round one-shot **0.4420** | `planning/gorag-main-cell-ledger.csv`: WOS/GORAG/R4/shot10=`0.4929`; WOS/GORAG/R4/shot1=`0.4420`. Main CAD/WOS backbone is Qwen2.5-7B per `verification-gorag.md`. | Correct **main-table** entries and conditions. The headline does not substitute `0.6646` from a different series or the separate ablation's one-shot result. |
| AGRAG Medical contextual-summarization coverage **0.690** and accuracy **0.604**, Qwen2.5-14B-Instruct | `planning/agrag-main-cells.json`, `summary` segment: last two columns are Medical COV/ACC; full AGRAG row is `0.690`/`0.604`. Main-model condition checked in `verification-agrag.md`. | Correct task, dataset, metrics, and backbone. These are not the creative-generation columns. |
| Removing AGRAG hybrid retrieval gives Medical summarization coverage **0.420** | `planning/agrag-table-cells.json`, `ablation-summary`, AGRAG w.o. HR row: Medical COV=`0.420`; the same ablation's full row retains `0.690`. | Correct ablation, column, and comparison. |
| MGRAG MMQA accuracy **0.7442**, Qwen2.5-VL-7B-Instruct | `planning/mgrag-table-cells.json`, `main`, MMQA/ACC row, MGRAG column; backbone in Chapter 6/published setting | Correct result and model. |
| MGRAG serving comparison **4.3 h** versus vLLM with HippoRAG2 **8.8 h** | `planning/mgrag-pdf-table-system_comp.txt`, original Table 6 on MMQA: MGRAG time cost=`4.3 h`; vLLM (H.)=`8.8 h`, with H explicitly denoting HippoRAG2 | Correct system pair, unit, and dataset context. The Introduction identifies this as the associated serving comparison rather than reusing a module breakdown or the inverse-ablation's different time series. |

**No numeric or experimental-condition error found in the new headline statements.** This check does not add an aggregate improvement or a cross-task comparison; each measurement remains associated with its own study and setting.

## Main-agent final delta acceptance

Final artifact `95cac4f970108cfdd2d3c49ddfa71e9f5685042e1995cd789ce6835c9b509c7f`,137pages. Subsequent edits change only five AGRAG caption citation spaces and two paragraph-pagination controls in Chapters5/6; no results/formulas/assets change. The main agent re-rendered/inspected physical95–96 and111–112 and regenerated the complete preflight/contact sheets. The previously recorded MGRAG single-line paragraph start is now fixed. See `planning/FINAL_QA.md`.
