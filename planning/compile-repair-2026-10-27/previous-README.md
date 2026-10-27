# Structural Augmented Reasoning for Language Models

English HKUST CSE PhD thesis by Yubo Wang. The complete manuscript contains Introduction, Background (including the separate CIKM hyper-relational study), KGLink, GORAG, AGRAG, MGRAG, Discussion, and Conclusion. Main entry: `main.tex`. The existing reading copy `thesis.pdf` predates the latest full-thesis prose revision; see the current compilation state below.

## Build

Install a TeX distribution providing XeLaTeX, Biber, latexmk and the packages used by the vendored class; Python 3 is used for bibliography integration and build checks. From this directory run:

```sh
make
```

The build merges `bibliography/*.bib` into `thesis-references.bib`, compiles with shell escape disabled, checks unresolved references, missing characters, duplicate labels and overfull boxes, and copies `main.pdf` to `thesis.pdf`. If BibLaTeX retains a stale auxiliary rerun flag, the build explicitly logs an auxiliary cleanup and repeats the build once. Bibliographic metadata are deduplicated by DOI or normalized title; original citation keys survive as BibLaTeX aliases. Edit the bibliography fragments, not the generated merged file.

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
- `planning/review-sun-style-2026-10-27/REVIEW.md`: latest reference-led style revision, exact edits and compiler diagnostics.
- `planning/FINAL_QA.md`: final compilation, typography and actual-PDF checks.
- `planning/review-round2/REVIEW_SUMMARY.md`: earlier independent full-manuscript review and source corrections.
- `planning/review-style-2026-10-27/REVIEW.md`: defensive-writing and punctuation review with exact edits.
- `planning/review-style-2026-10-27/ABSTRACT_REVISION.md`: latest abstract revision and HKUST CSE abstract comparisons.
- `planning/AUTHOR_ACTIONS.md`: the remaining author/institutional information.

Twenty-seven research graphics are original source files with recorded hashes. Table values preserve the selected papers' precision, units, missing markers and experimental settings. No new experiment or replacement experimental graphic is included.

The manuscript is complete for author and supervisor review. The unfilled signature date and department-head field must be completed from real information; signatures and institutional approval are outside the manuscript build. The title-page numeral follows the visible official sample pending departmental clarification. Source-internal theory discrepancies and an unreported MGRAG experimental recomputation budget are documented rather than silently repaired.

The latest Sun-reference style pass applies 198 prose edits across all eight chapters. Current sources have 19,975 narrative words, 21,917 words including headings/captions, and a 206-word abstract. The built-in compiler fails when invoking Biber, so no updated PDF export or current pagination is certified. `thesis.pdf` remains the previous 128-page abstract-revision export. Exact changes and checks are in `planning/review-sun-style-2026-10-27/REVIEW.md`; the October 25 portable ZIP is an older snapshot.
