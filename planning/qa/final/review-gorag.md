# Final integrated PDF review — GORAG / Chapter 4

Reviewed 2026-10-24. Reviewer: gorag agent. Latest checked input: final integrated `thesis.pdf`, 137 physical pages, A4, SHA-256 `ba011690c5fb5fab2cfdff754c3284f1f898407f2a0c8f3d7b30065c5fc8c83f` (metadata build time18:54:18). The initial full chapter inspection used the preceding138-page build, SHA-256 `406fd804f8eb9cfcff57396e0556087bede62b347fa64ee79f2117828b170b87`; the latest build received the targeted verification described below. Scope: **physical pages55–73**, printed pages41–59. No chapter, table, main, bibliography or shared file was edited during this review.

## Result

The reviewed chapter has no detected clipping, overlapping text, broken equation glyphs, missing research asset, missing table cell, split table row, distorted original plot, or unresolved citation marker. All **250 adopted numeric table cells** were independently re-extracted from the actual integrated PDF and matched the previously checked original-source cell ledgers (zero differences). The two minor caption grammar issues found in the preceding build have been corrected and verified in the latest build; no open chapter-layout issue remains in this review.

## Resolved issues from the preceding build

| Priority | Actual PDF location | Issue | Suggested correction |
|---|---|---|---|
| FIXED / rechecked | Physical65 / printed51, Table4.2 caption | “with 1 support examples per label” has a singular/plural mismatch. | “with one support example per label”. |
| FIXED / rechecked | Physical66 / printed52, Table4.5 caption | Same singular/plural mismatch. | “with one support example per label”. |

Both captions originate in the active `chapter/tables/gorag-main-tables.tex` copies. The main agent corrected them. The reviewer then re-extracted physical55–73 from the latest137-page PDF: the chapter text differs only in those two captions and their centering spaces. Fresh120dpi renders of physical65/66 (`gorag-review/caption-fix-065.png`, `caption-fix-066.png`) show both corrections cleanly, with unchanged table placement and legibility. All250 numeric cells were rechecked against the ledger in the latest PDF and still match. The succeeding18:54:18 build was checked by extracting the same physical55–73 again: it is text-identical to the caption-corrected18:51:18 build (zero diff). The caption-corrected build SHA was `93c6bda671c831129e92b3f8422f8e9c330f0dbbd22980bfcc8f12962fc33891`. No chapter/shared authoring file was edited by this reviewer.

## Visual inspection performed

- Contact sheets `planning/qa/final/contact-3.png` and `contact-4.png` were inspected for the entire chapter's page flow and neighboring chapter transitions.
- Fresh120dpi renders of physical55–73 were generated with `pdftoppm -f 55 -l 73 -r 120 -png thesis.pdf planning/qa/final/gorag-review/page`.
- Every page containing a figure, table or displayed equation was inspected at120dpi: **56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72**. Remaining prose pages55,57,73 were reviewed in the contact-sheet overview. Render files are `planning/qa/final/gorag-review/page-055.png` through `page-073.png`.
- Original diagrams and plots were compared with the already inspected source assets and author-confirmed publication-equivalent PDF recorded in `planning/verification-gorag.md`. No experimental picture was redrawn.

## Figures and equations

| Object | Physical page(s) | Findings |
|---|---|---|
| Fig4.1 task illustration | 56 | Original two-round illustration complete; labels and source citation legible. |
| Fig4.2 pipeline | 58 | Complete original wide vector figure; small annotation text is readable on the120dpi render, with no clipping. Caption immediately follows. |
| Fig4.3 runtime panels | 69 | WOS/CAD panels, bar colors, minute axes, model labels and R1–R4 legend intact. Caption explicitly states that the panel(b) legend applies to both. |
| Fig4.4 round-split curves | 71 | All original curves, axis ticks, one-/five-shot panel labels and right-hand legend preserved. Caption states the four/six/eight-round source splits. No points were inferred or replaced. |
| Fig4.5 original contextual-abuse case | 72 | Original text/graph/output illustration complete and legible; source citation resolves. |
| Eqs4.1–4.9 | 56,58–63 | Script symbols, hats, superscripts/subscripts, sums, fractions, union/intersection and update arrows render clearly. Equations stay within margins and numbering is sequential. Label-bridge factors and original score denominators remain visible. |

The final PDF's GORAG source citation is numbered[2]; method/data references appear as resolved numeric citations. No `??`, raw BibTeX keys, empty citation brackets or tool-reference tokens were found in the chapter extract.

## Tables and numeric extraction

| Tables | Physical page(s) | Numeric entries checked against source ledger | Findings |
|---|---|---:|---|
| Table4.1 dataset statistics | 64 | 30 | Transposition retains all adopted counts and comma grouping. New-label counts are identified, and the table is unbroken. |
| Tables4.2–4.7 WOS/IFS main results | 65–67 | 168 | Six shot-specific tables retain all seven method rows and four round columns. Natural-size small text is legible. Bold and underline follow original emphasis, including the non-best GORAG value0.4988 beside HippoRAG2's0.5008. The prose onp67 explicitly reports that comparison. |
| Table4.8 ablations | 68 | 20 | Five variants, four rounds, and the full-method control series preserved. No row split or missing decimal. |
| Table4.9 tokens/historic USD cost | 69 | 12 | Decimal precision, dollar signs and original units retained. No columns missing. |
| Table4.10 zero-shot | 70 | 20 | Five methods and four rounds complete; model citations fit in the first column. |
| **Total** | | **250** | **Zero final-PDF-to-ledger numeric differences.** |

The invalid original CAD literal `03139` and the inconsistent intermediate graph-growth increment remain excluded from the adopted final tables, as previously agreed and documented. They were not silently corrected. The retained CAD prose values and graph-growth endpoints have not changed from the source-checked chapter.

## Page flow and scope limits

Printed page numbers are centered at the bottom and run41–59 across this chapter. No isolated table header or table continuation appears. The four main-result tables share physical66 but fit within the page with complete captions and rows. Figures remain within approximately one page of their discussion; Fig4.5 is on the page after its first explicit reference. Chapter4 ends on physical73 and Chapter5 starts on74.

This report verifies the actual integrated PDF pages listed above. It does not re-prove source-internal algorithmic claims, replace the separate source audit, or certify bibliography metadata for the whole thesis. Those are covered by the corresponding evidence records and the main agent's final audit.

## Main-agent final delta acceptance

Final artifact `95cac4f970108cfdd2d3c49ddfa71e9f5685042e1995cd789ce6835c9b509c7f`,137pages. Subsequent edits change only five AGRAG caption citation spaces and two paragraph-pagination controls in Chapters5/6; no results/formulas/assets change. The main agent re-rendered/inspected physical95–96 and111–112 and regenerated the complete preflight/contact sheets. The previously recorded MGRAG single-line paragraph start is now fixed. See `planning/FINAL_QA.md`.
