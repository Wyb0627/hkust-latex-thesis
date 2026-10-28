# Structural Augmented Reasoning for Language Models

English HKUST CSE PhD thesis by Yubo Wang. The complete manuscript contains Introduction, Background (including the separate CIKM hyper-relational study), KGLink, GORAG, AGRAG, MGRAG, Discussion, and Conclusion. Main entry: `main.tex`. The reading copy `thesis.pdf` includes citation completion, the author-led wording revision, and the ch01/ch02 literature expansion and has 125 pages.

## Build

Install a TeX distribution providing XeLaTeX, Biber, latexmk and the packages used by the vendored class; Python 3 is used for bibliography integration and build checks. From this directory run:

```sh
make
```

The build checks the paths of latexmk, XeLaTeX and Biber, adding the active `/Library/TeX/texbin` directory to the build process PATH when needed. It prints the resolved paths and stops if a required program is missing. The build merges `bibliography/*.bib` into `thesis-references.bib`, compiles with shell escape disabled, checks unresolved references, missing characters, duplicate labels and overfull boxes, and copies `main.pdf` to `thesis.pdf`. If BibLaTeX retains a stale auxiliary rerun flag, the build explicitly logs an auxiliary cleanup and repeats the build once. Bibliographic metadata are deduplicated by DOI or normalized title; original citation keys survive as BibLaTeX aliases. Edit the bibliography fragments, not the generated merged file.

```sh
make counts    # TeXcount output under planning/qa/
make clean     # generated LaTeX auxiliary files only
```

All compiled chapter, table, figure, bibliography and template inputs are inside this project. The original research directories are needed only for provenance rechecking or optional table regeneration, not ordinary compilation. Do not rerun paper-specific generators after editing thesis tables without reviewing their output.

## Template and review records

The adopted class is HKFoggyU v0.11.6, pinned to release commit `1a9230d`, under `template/hkust-thesis-v0.11.6/`. Its LPPL license and source are retained. Font selection explicitly uses TeX Gyre Termes/XITS Math. The original MPhil example remains in `legacy/mars-2010/` and is not part of the build.

- `planning/WRITING_PROGRESS.md`: current state and directly executable next tasks.
- `planning/CHAPTER_COUNTS.md`: narrative/caption/heading words and actual PDF page ranges.
- `planning/EVIDENCE_SUMMARY.md`: version authority, source checks and known source discrepancies.
- `planning/verification-{kglink,gorag,agrag,mgrag,background}.md`: detailed evidence records.
- `planning/STYLE_AUDIT.md`: current whole-manuscript writing audit.
- `planning/reference-expansion-2026-10-28/REVIEW.md`: current 123-paper / 129-reference count, 56 additions, original-bib provenance, primary verification, partial Scholar crosschecks, and source/PDF checks.
- `planning/citations-wording-2026-10-28/REVIEW.md`: preceding seven-position citation completion and full-manuscript author-led wording pass.
- `planning/research-thread-2026-10-27/REVIEW.md`: preceding research narrative, style references, exact edits, and source/PDF checks.
- `planning/review-sun-style-2026-10-27/REVIEW.md`: preceding reference-led style revision and compiler diagnostics.
- `planning/FINAL_QA.md`: final compilation, typography and actual-PDF checks.
- `planning/review-round2/REVIEW_SUMMARY.md`: earlier independent full-manuscript review and source corrections.
- `planning/review-style-2026-10-27/REVIEW.md`: defensive-writing and punctuation review with exact edits.
- `planning/review-style-2026-10-27/ABSTRACT_REVISION.md`: latest abstract revision and HKUST CSE abstract comparisons.
- `planning/AUTHOR_ACTIONS.md`: the remaining author/institutional information.

Twenty-seven research graphics are original source files with recorded hashes. Table values preserve the selected papers' precision, units, missing markers and experimental settings. No new experiment or replacement experimental graphic is included.

The manuscript is complete for author and supervisor review. The unfilled signature date and department-head field must be completed from real information; signatures and institutional approval are outside the manuscript build. The title-page numeral follows the visible official sample pending departmental clarification. Source-internal theory discrepancies and an unreported MGRAG experimental recomputation budget are documented rather than silently repaired.

The manuscript follows the author-approved progression from KGLink's use of an existing KG and supervised fine-tuning to GORAG's graph construction from task data and prediction without model fine-tuning. AGRAG and MGRAG extend this direction to connected textual evidence and query-aware multimodal matching. The preceding wording pass completed seven empty citation positions and extended the author's problem-to-method transitions across the manuscript.

The current literature expansion adds 56 published papers, including 36 from the author's original bib libraries and 20 externally found works. The manuscript now cites 129 unique reference entries, comprising 123 independent research papers under a conservative count that excludes six software/data/duplicate-report entries. All newly added conference papers are CCF A full papers; six additions are journal articles. Google Scholar crosschecking was partial because it requested CAPTCHA verification; all 56 additions were independently checked against official proceedings, journal or publisher-deposited metadata. ch01 and ch02 now cite 22 and 84 distinct works respectively.

Current sources have 22,182 narrative words, 24,124 words including headings/captions, and a 213-word abstract. Source-preservation checks and the clean XeLaTeX/Biber build passed. The 125-page PDF was rendered and visually reviewed. See `planning/reference-expansion-2026-10-28/REVIEW.md` and `planning/FINAL_QA.md`. The app's earlier independent preview issue remains documented in `planning/compile-repair-2026-10-27/REPORT.md`; the October 25 portable ZIP is an older snapshot.
