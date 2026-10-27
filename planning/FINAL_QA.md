# Current source QA and PDF checkpoint

Updated 2026-10-27 (Asia/Shanghai), after repairing the project compilation entry point.

## Sources and compilation

The 198 prose edits across Chapters 1–8 are included in the updated PDF. Narrative words: 19,975; including headings/captions: 21,917; abstract: 206. Source-preservation checks remain at `review-sun-style-2026-10-27/verification.json`. This repair changed the build script, not the manuscript or experimental content.

The installed TeX Live 2023 provides XeLaTeX, latexmk 4.79 and Biber 2.19. Environment diagnosis and a TeX Live smoke test passed. An explicit Biber pass and full XeLaTeX rebuild succeeded. The repaired build script was verified with PATH restricted to `/usr/bin:/bin`; it explicitly locates the active MacTeX tools and logs their paths. Logs: `compile-repair-2026-10-27/terminal-build.txt`, `biber-rebuild.txt`, `repaired-build.txt`.

Final logs contain no undefined citations/references, missing characters, duplicate labels/destinations, Biber warning/error, LaTeX error or overfull box. Existing non-fatal warnings concern the vendored document-class path/name, an unused global option, and siunitx/physics integration.

## Updated exported PDF

`main.pdf` and `thesis.pdf` have identical SHA-256 `2e0fa332ed7ffd94111d25b45640d4fcf60e24baa97b90d277ae13c9f3941a87`. Total 115 pages: 14 preliminary, 96 body, 5 references. All pages are A4 and unrotated; all 95 fonts are embedded. No empty text page or body-margin violation was detected. All 115 pages were rendered and reviewed in six contact sheets; the abstract and algorithm were also inspected at higher resolution. Tables, figures, contents, bibliography and page numbers render without clipping or overlap. Question marks in the KGLink example figure are intentional missing-value placeholders, not unresolved references.

Original figure limitations remain recorded in `qa/final/typography-summary.json`: some raster instances are 224–257 ppi, and 18 embedded fonts from source graphics have no Unicode map. No graphics were replaced or upsampled. Chapter page ranges are regenerated in `CHAPTER_COUNTS.md`.

## App preview

The built-in compiler was retried after the successful project build. It still reports TeX Live exit -6 and Tectonic’s external Biber program-not-found error. This independent preview is not certified as repaired. The app helper also defaults to pdfLaTeX in a direct reproduction, which fails on this thesis’s unicode-math package. Details and bounded conclusions: `compile-repair-2026-10-27/REPORT.md`; retry: `built-in-retry.json` in that directory. No signed app bundle or system-wide environment was modified.

The previous 128-page PDF checkpoint is historical. The October 25 portable ZIP also predates the latest manuscript. Institutional and scientific author items remain in `AUTHOR_ACTIONS.md` and the existing evidence ledgers.
