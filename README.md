# Structural Augmented Reasoning for Language Models

English HKUST CSE PhD thesis by Yubo Wang. The complete manuscript contains Introduction, Background (including the separate CIKM hyper-relational study), KGLink, GORAG, AGRAG, MGRAG, Discussion, and Conclusion. Main entry: `main.tex`. Reading copy: `thesis.pdf`.

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
- `planning/STYLE_AUDIT.md`: whole-manuscript defensive-writing audit.
- `planning/FINAL_QA.md`: final compilation, typography and actual-PDF checks.
- `planning/review-round2/REVIEW_SUMMARY.md`: independent full-manuscript review, source corrections, and before/after verification.
- `planning/AUTHOR_ACTIONS.md`: the remaining author/institutional information.

Twenty-seven research graphics are original source files with recorded hashes. Table values preserve the selected papers' precision, units, missing markers and experimental settings. No new experiment or replacement experimental graphic is included.

The manuscript is complete for author and supervisor review. The unfilled signature date and department-head field must be completed from real information; signatures and institutional approval are outside the manuscript build. The title-page numeral follows the visible official sample pending departmental clarification. Source-internal theory discrepancies and an unreported MGRAG experimental recomputation budget are documented rather than silently repaired.

The current portable bundle is `deliverables/thesis-project-2026-10-25.zip`. Round two removes repeated explanations; the accepted manuscript has 133 pages, 27,843 narrative words and 29,785 words including headings/captions. This is below the initial working word range; the plan permits a shorter complete manuscript without filler. Exact chapter counts and remaining author information are in the records above.
