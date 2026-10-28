# Structural Augmented Reasoning for Language Models

English HKUST CSE PhD thesis by Yubo Wang. The complete manuscript contains Introduction, Background (including the separate CIKM hyper-relational study), KGLink, GORAG, AGRAG, MGRAG, Discussion, and Conclusion. Main entry: `main.tex`. The reading copy `thesis.pdf` includes citation completion, the author-led wording revision, the ch01/ch02 literature expansion, and the Section 2.1 knowledge-structures rewrite and has 125 pages.

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
- `planning/background-structure-2026-10-28/REVIEW.md`: current Section 2.1 structure and style revision, seven directly related additions, 121-paper / 127-reference count, and source/PDF checks.
- `planning/reference-expansion-2026-10-28/REVIEW.md`: preceding literature expansion, original-bib provenance, primary verification, and partial Scholar crosschecks.
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

The preceding literature expansion added 56 published papers, including 36 from the author's original bib libraries and 20 externally found works. Section 2.1 has since been rewritten around explicit knowledge structures, model inputs and task adaptation. Nine no-longer-relevant introductory citations were replaced by seven directly related papers, three from original bib libraries and four from formal external publications. The current manuscript cites 127 unique reference entries, comprising 121 independent research papers under the existing conservative count. ch01 and ch02 cite 22 and 82 distinct works respectively. Primary-source and paragraph-level evidence is in the current review; Scholar verification remains limited to the preceding review's documented coverage.

Current sources have 22,276 narrative words, 24,218 words including headings/captions, and a 213-word abstract. Source-preservation checks and the clean XeLaTeX/Biber build passed. All 125 PDF pages were rendered and automatically checked; the rewritten section, chapter transitions, contents and relevant bibliography pages were visually reviewed. See `planning/background-structure-2026-10-28/REVIEW.md` and `planning/FINAL_QA.md`. The app's earlier independent preview issue remains documented in `planning/compile-repair-2026-10-27/REPORT.md`; the October 25 portable ZIP is an older snapshot.
