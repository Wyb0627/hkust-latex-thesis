# Current source QA and PDF checkpoint

Updated 2026-10-27 (Asia/Shanghai), after the research-thread revision.

## Source verification

Nine narrative files were revised, beginning with Introduction and then the abstract, Background, research-chapter openings and summaries, Discussion, and Conclusion. The manuscript follows the author-approved transition from existing-KG enrichment and supervised learning to task-driven graph retrieval without model fine-tuning, followed by textual and multimodal evidence reasoning.

`research-thread-2026-10-27/source-checks.json` verifies unchanged numeric tokens, citation-key multiplicities, labels, inline math, equation/align environments, algorithms, figures, longtables, and tabular contents. The Introduction's first table caption was shortened. No data, experiment setting, research graphic, or algorithm was changed.

Current counts are 20,594 narrative words, 22,525 including headings/captions, and 207 abstract words. Actual chapter page ranges are in `CHAPTER_COUNTS.md`.

## Compilation

The `latex-paper-en` compile entry point completed with the installed XeLaTeX, latexmk, and Biber toolchain, with shell escape disabled. The command and final log are recorded in `research-thread-2026-10-27/REVIEW.md` and `compile.log` in that directory.

The final LaTeX log has no undefined references/citations, missing characters, duplicate labels/destinations, overfull boxes, or LaTeX errors. Biber has no warnings/errors. Existing non-fatal document-class and package notices remain unchanged.

## Reading copy and visual inspection

`main.pdf` and `thesis.pdf` have identical SHA-256 `c33dcf2714d92fd4c62d730feead96561de4a6f401244ca53f649b5374777f26`. There are 115 A4, unrotated pages, including 14 preliminary, 96 body, and 5 reference pages. All 95 fonts are embedded. No page has empty extracted text.

All 115 pages were rendered and reviewed in six contact sheets. Detailed renders of the abstract, Introduction opening, KGLink ending, Discussion ending, and Conclusion were also reviewed. Added transitions initially created short spill pages; redundant prose was compressed to remove them. No clipping, overlapping objects, unresolved references, or detached chapter-ending lines were observed in the final renders.

PDF geometry and word-bounding-box checks are in `research-thread-2026-10-27/pdf-qa/pdf-preflight.json`. Four approximate 25 mm margin flags concern embedded source-figure text on printed pages 30, 44, 45, and 88. The flagged items are axis labels/ticks, extending roughly 0.3–2.5 points beyond the approximate body threshold. The source graphics are unchanged and render without clipping. These flags are recorded, not treated as missing text or suppressed.

Original figure limitations from earlier typography reviews remain in `qa/final/typography-summary.json`. Current page numbers and PDF hashes come from the new `research-thread-2026-10-27/` checkpoint; older artifacts under `qa/final/` describe the preceding revision.

## Earlier preview diagnosis and author items

This revision validates the local compiled PDF. The app's independent preview was not retried or modified; its earlier failure is documented in `compile-repair-2026-10-27/REPORT.md`. Institutional fields and source-specific author items remain in `AUTHOR_ACTIONS.md` and the evidence ledgers. The previous QA document is archived in `research-thread-2026-10-27/before/FINAL_QA.md`.

The author edited the acknowledgements concurrently near completion. That source was preserved and included in the final rebuild. Decompressed page-content hashes verify that only PDF page 5 changed; the other 114 page streams are identical to the visually inspected reading copy. The revised acknowledgement page was rendered and inspected separately. See `research-thread-2026-10-27/pdf-qa/acknowledgements-update.json`.
