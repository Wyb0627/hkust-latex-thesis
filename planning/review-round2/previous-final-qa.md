# Final integrated thesis QA — 2026-10-24

Artifact: `thesis.pdf`; entry: `main.tex`. Final PDF SHA-256: `95cac4f970108cfdd2d3c49ddfa71e9f5685042e1995cd789ce6835c9b509c7f`. **137 pages**: preliminary i–xiv, body 1–118, References 119–123. Current counts: **30,023 narrative words**, 31,951 including headings/captions, and a **261-word abstract**. Exact chapter ranges/counts: `CHAPTER_COUNTS.md`.

## Build and structural checks

- Successful fresh auxiliary-state build with XeLaTeX/Biber/latexmk, shell escape disabled. Reproducible command: `make`. Final log checked again after the last paragraph-layout changes.
- No unresolved reference/citation, duplicate label, missing graphic, missing character or overfull box. Biber has no warnings/errors. The build script rejects these conditions.
- Three inherited vendor notices remain: directory-qualified class name, unused UTF8 class option, and siunitx/physics command compatibility notice. Underfull paragraph diagnostics were inspected visually; they are not clipping or missing content.
- A stale BibLaTeX auxiliary MD5 rerun request was found after bibliography integration. A fresh auxiliary build removed it. This is recorded in `qa/final/clean-build.txt`; the build helper explicitly performs this cleanup once if the same request occurs again, rather than hiding the warning.
- All eight required chapters and the abstract use explicit inputs. Ordinary compilation uses only project-local inputs. Bibliography aliases produce 74 distinct reference entries. Front matter has no MPhil example names or invented officials.
- TOC, LOF, LOT, PDF bookmarks, chapter starts, labels and Arabic/Roman numbering were checked in the actual PDF. There are 45 tables, 21 figure environments, 47 displayed math environments, one pseudocode algorithm environment and the separately explained greedy path procedure.

## Geometry, fonts and image quality

| Check | Actual final PDF finding |
|---|---|
| Page geometry | Every page A4, 595.28 × 841.89 PDF points, no unintended rotation |
| Body font | TeX Gyre Termes, 11.955 PDF points = 12 TeX points; XITS Math |
| Margins | Class 25 mm on all sides; extracted text/figure glyphs stay inside the approximately 25 mm body boundary, excluding centered page numbers |
| Line spacing | Body baseline median 20.66 PDF points; upstream linespread 1.43 is its documented Word-style 1.5 spacing setting |
| Fonts | 95 font resources, all embedded. Some original figure Type 3 fonts are fully embedded rather than subset and 18 have no Unicode map; visible glyphs are preserved |
| Raster graphics | Main raster diagrams exceed 300 ppi. Seven instances of the original 220×293 portrait embedded in MGRAG Figures 6.3/6.4 render at 224–257 ppi; this source-resolution limit is retained, not concealed by upsampling |
| Research graphic identity | All 27 source/target/manifest hashes match. Vector diagrams/plots retained as original PDFs; no redraw |
| PDF properties | Unencrypted, no JavaScript, all 137 pages contain content. PDF/A or tagged-PDF compliance was not requested or certified |

The portrait is illustrative content inside the original graph/cache diagrams, rather than an experimental plot. At actual page scale the diagrams' labels and relationships remain readable; enlarging the source PDF preserves vector labels but cannot add portrait detail. A strict 300-ppi check for every embedded photo would require a genuinely higher-resolution original figure from the author. No replacement photo or resampled research figure was introduced.

## Actual visual inspection

All pages of the integrated PDF were rendered to seven contact sheets under `qa/final/`. Main-agent inspection covers preliminary pages, Introduction, AGRAG, Discussion, Conclusion and References, plus representative original graphics and the complete overview. Independent agents inspected all image/table/equation pages in Background/KGLink, GORAG and MGRAG at 100–140 dpi. Reports are `qa/final/review-background-kglink.md`, `review-gorag.md`, and `review-mgrag.md`.

The earlier review reports retain their inspected PDF hashes. The main agent then inspected the final deltas and accepts the current hash above: unchanged chapter text/layout inherits the earlier full review; changed pages were rendered and inspected again. The final changes are spacing before five AGRAG table citations and two local paragraph-pagination controls; source numbers, formulas and images are unchanged. The current preflight and contact sheets were regenerated after those changes.

Corrections applied and rechecked:

1. AGRAG Figure 5.3 moved alongside its parameter discussion at physical p95 / printed81, eliminating the detached chapter-end figure page and near-empty text page.
2. MGRAG Table 6.1 is intact at physical p111 / printed97. Table 6.8 is intact at p121 / printed107, and Figure 6.5 follows at p122 / printed108 rather than interrupting the table.
3. A one-word continuation below Figure 6.1 was removed by shortening the preceding paragraph's last sentence.
4. Single-line paragraph starts after the AGRAG parameter figure and MGRAG dataset table are kept with their following text. Final physical95–96 and111–112 were re-rendered and inspected.
5. Two GORAG captions now use “one support example”; the actual PDF's 250 adopted numeric cells were independently re-extracted with zero mismatches.
6. Abstract and Introduction headline values/backbones were independently checked against the source ledgers. The abstract is below the 300-word limit.

No clipping, overlapping text, illegible table values, broken continuation headers, missing figure material or unresolved reference was found in the accepted pages. Long MGRAG tables repeat headers and dataset labels across pages. The float-only KGLink illustration page is clean and intentional; it has more white space than ordinary text pages.

## Scope of acceptance and remaining author items

This is a complete unsigned manuscript for author/supervisor review. It is not institutional certification, a plagiarism report, an experimental reproduction or an independent validation of contradictory source proofs. Source correspondence and discrepancies are documented in `EVIDENCE_SUMMARY.md` and the chapter ledgers. No new experimental result, hidden protocol change or corrected source theorem was introduced.

The department-head identity, actual signature dates/signatures, title-page i display decision, and missing MGRAG fixed b setting remain explicit in `AUTHOR_ACTIONS.md`. The FYTGS guideline page again returned403; current official Library guidance was retrieved, and layout was checked against the local official PhD sample plus the prior current-requirements review. Recheck the institutional detail before formal submission.

## Portable source-package validation

`deliverables/thesis-project-2026-10-24.zip` was extracted into an independent temporary directory; its included reading PDF was removed and `make` compiled the complete thesis from source. Exit status0;137pages; extracted PDF text matches the delivered PDF byte-for-byte (text SHA-256 `d4845b4049f3450d5e767b384084fe6f54292b27479784817a2857d4c029f95d`). Compiled-input fingerprint: `bbeb08b62efa889ef236d51e5351d138f9e66ae486e62dcb59c7c5917b864c7b`. `qa/final/package-build-verification.json` and `package-build.txt` retain the result. Subsequent archive updates add only these review records; no compilation input changes. The final ZIP and PDF checksums are outside the ZIP in `deliverables/SHA256SUMS`.
