# Current source QA and PDF checkpoint

Updated 2026-10-28 (Asia/Shanghai), after citation completion and the author-led wording revision.

## Source and citation verification

The current pass makes 44 exact replacements across the abstract and eight chapters. It follows the author's latest Introduction changes and extends the problem-to-method transitions, concrete wording, and textual/multimodal research progression throughout the manuscript.

All seven empty citation positions were completed with seven distinct works: six already in the thesis bibliography and one additional, primary-source-verified CVPR paper. One combined position now has separate citations for multi-hop QA and summarization. The claim-specific citation map, original-library provenance, primary links, and metadata corrections are in [the review record](citations-wording-2026-10-28/REVIEW.md).

`citations-wording-2026-10-28/source-checks.json` confirms unchanged numerical tokens, labels, cross-references, inline math, equations, algorithms, figures, and tables in all nine narrative files. Every pre-existing nonempty citation occurrence remains. All 100 cited keys resolve, including aliases; the merged bibliography has 75 unique works and 31 retained aliases. The generic checker limitations and the correction of the Faiss preprint entry type are recorded explicitly in the review.

## Compilation

The final clean rebuild passed through the `latex-paper-en` skill entry point with XeLaTeX, latexmk, and Biber, with shell escape disabled. An intermediate incremental run failed because `main.bcf` was absent; regenerating auxiliary state with the same toolchain resolved it. Commands and output are in `citations-wording-2026-10-28/compile-case-rebuild.log`.

The final LaTeX log contains no unresolved references/citations, missing characters, duplicate labels/destinations, overfull boxes, or LaTeX errors. Biber has no warnings or errors. Existing non-fatal class/package notices remain.

## Reading copy and visual inspection

`main.pdf` and `thesis.pdf` have identical SHA-256 `5adbc3791bd69d19ebf85ba6ed3d20d53f7446dcfd4a4ae4320b49456cd19d32`. The PDF contains 115 unrotated A4 pages: 14 preliminary, 96 body, and 5 reference pages. All 95 fonts are embedded, and every page contains extracted text.

All 115 pages were rendered and reviewed in six contact sheets. Detailed renders of the abstract, Introduction's first two pages, and first/final reference pages were also checked. Citations appear as numeric references, the new paper appears in the bibliography, and no new clipping, overlap, detached chapter-ending lines, or pagination defect was observed.

The same four approximate 25 mm margin flags remain on printed pages 30, 44, 45, and 88. They concern embedded source-figure axis labels/ticks and are unchanged from the preceding checkpoint; the graphics remain unclipped. The preflight report and renders are under `citations-wording-2026-10-28/pdf-qa/`.

Current counts are 20,612 narrative words, 22,543 including headings/captions, and a 213-word abstract. Chapter ranges are unchanged and recorded in `CHAPTER_COUNTS.md`.

## Historical checkpoints and author items

The preceding QA document is saved in `citations-wording-2026-10-28/before/planning/FINAL_QA.md`. Earlier reference-led and research-thread reviews remain historical records. The app's independent preview issue remains documented in `compile-repair-2026-10-27/REPORT.md`; this checkpoint verifies the local compiled PDF. Institutional fields and source-specific author items remain in `AUTHOR_ACTIONS.md` and the evidence ledgers.
