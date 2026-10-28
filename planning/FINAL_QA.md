# Current source QA and PDF checkpoint

Updated 2026-10-28 (Asia/Shanghai), after the Section 2.1 knowledge-structures rewrite.

## Source and citation verification

Section 2.1 and the chapter opening were rewritten; Sections 2.2 onward and all other narrative files remain byte-identical to this revision's baseline. All labels, inline math, displayed formulas, algorithms, figures and tables are preserved. See `background-structure-2026-10-28/source-checks.json`.

The current manuscript cites **127 unique entries**, comprising **121 independent research papers** after the same six software/data/encyclopedia/duplicate-report exclusions. The Biber bibliography contains 127 entries, matching the final PDF reference [127]. ch01/ch02 cite 22/82 distinct works. The merged database contains 138 works and 31 retained aliases; uncited entries do not inflate the count.

Seven directly related publications replace nine removed introductory citations. Three additions come from original author bib libraries; four come from official EMNLP, AAAI and TACL records. The survey and graph prompting sources were also checked against primary records. See [the current review](background-structure-2026-10-28/REVIEW.md) and its citation ledger. Scholar coverage remains limited to the preceding literature expansion's documented partial check.

## Compilation

The initial incremental build retained a stale BibLaTeX rerun flag. A clean rebuild through the `latex-paper-en` skill's `compile.py` resolved it. The final layout build passed with shell escape disabled. The final log has no undefined references/citations, missing characters, duplicate labels/destinations, overfull boxes or LaTeX errors. Biber has no warnings or errors. Existing non-fatal class/package notices remain. Logs: `background-structure-2026-10-28/compile-clean.log` and `compile-layout.log`.

## Reading copy and visual inspection

`main.pdf` and `thesis.pdf` are identical. SHA-256: `11951828b2f94db09b2b8ceefb5c0b61c3bb30ab4a388a20b86ecec2ac556d82`.

The PDF has **125 A4 pages**, comprising 14 preliminary, 102 body and 9 reference pages. All 95 font records are embedded. All pages were rendered and automatically inspected; the approximate margin check reported no flags with the current explicitly provisioned PDF dependencies.

Enlarged visual review covered physical pp. 6, 23–25, 117–119 and 125, with chapter-level review of the second contact sheet. The Section 2.1 heading fits on one line. Its closing transition stays on printed p. 10; Section 2.2 starts on p. 11. No clipping, overlap or broken citations was observed in these reviewed pages. Actual chapter start pages remain unchanged.

Current counts are **22,276 narrative words**, **24,218 including headings/captions**, and **213 abstract words**. Renders and page maps are in `planning/qa/final/`; the current revision's `final-validation.json` and `chapter-counts.json` preserve the checkpoint.

## Historical checkpoints and author items

The preceding QA is preserved in `background-structure-2026-10-28/before/planning/FINAL_QA.md`. Earlier literature and wording records remain historical checkpoints. Institutional fields and source-specific items remain in `AUTHOR_ACTIONS.md` and evidence ledgers. The app's earlier independent preview issue remains documented in `compile-repair-2026-10-27/REPORT.md`; this checkpoint verifies the local compiled PDF.
