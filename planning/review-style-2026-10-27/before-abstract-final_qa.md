# Current thesis QA

Updated 2026-10-27 (Asia/Shanghai), following the targeted prose review.

Current reading artifact: `thesis.pdf`; source entry: `main.tex`. PDF SHA-256: `ddcaf569a655c37b691c2d0a1e94ea435db4b3bd1d4f4fa1cc21ee71bbfe49db`. There are 128 pages, comprising 14 front-matter pages, 109 body pages and 5 reference pages. Narrative words: 25,604; including headings/captions: 27,546; abstract: 261 words. Exact chapter counts and physical/printed page ranges are in `CHAPTER_COUNTS.md`.

## Compilation and content preservation

`UV_CACHE_DIR=/private/tmp/thesis-style-uv-cache uv run python -B /Users/ybwang/.agents/skills/latex-paper-en/scripts/compile.py main.tex --compiler xelatex` passed. The project build script's final-log conditions were also applied. No undefined references/citations, duplicate labels, missing characters, overfull boxes or Biber warnings/errors were found. Shell escape remained disabled. Logs: `review-style-2026-10-27/build.txt`, mirrored in `qa/build-current.txt`.

47 displayed formula blocks, one algorithm, 10 inline tabular environments, 166 labels and 127 citation calls match the before snapshot byte for byte. All 22 external table files, 27 graphics and merged bibliography preserve their hashes. `review-style-2026-10-27/verification.json` records the comparisons. Source inconsistencies, algorithm caveats, original precision and missing recomputation budget b remain as recorded in the existing evidence ledgers.

## PDF inspection

`inspect_thesis_pdf.py` and `summarize_pdf_typography.py` were rerun with bundled Python dependencies. Current machine records and seven all-page contact sheets are in `qa/final/`. All 128 pages were inspected at overview scale. Background and Discussion chapter endings, the GORAG formula flagged by the approximate margin check, and the Discussion condition table were also inspected at larger size. No introduced clipping, overlapping content, broken table continuation or near-empty short continuation page was found. The initially flagged GORAG subscript was resolved by condensing the preceding repeated explanation; the final margin check is clear.

The 27 research graphics remain original assets. The earlier source-resolution limits of the small MGRAG portraits remain unchanged. This pass did not repeat publisher verification, experiments, institutional formatting research or portable-package rebuilds. The October 25 QA checkpoint is preserved at `review-style-2026-10-27/previous-final_qa.md`, including its historical source/geometry/package checks.

## Delivery state

Current deliverables are workspace sources, `thesis.pdf`, and `review-style-2026-10-27/REVIEW.md`. The October 25 ZIP is a historical snapshot and predates these edits. Real signature dates, department-head identity, title-page numeral clarification and missing MGRAG run metadata remain author/institutional items in `AUTHOR_ACTIONS.md`.
