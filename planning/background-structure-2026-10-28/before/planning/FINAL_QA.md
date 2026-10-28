# Current source QA and PDF checkpoint

Updated 2026-10-28 (Asia/Shanghai), after the ch01/ch02 literature expansion and the author's updated writing instructions.

## Source and citation verification

The current expansion adds 56 published papers: 36 from original paper libraries and 20 found externally. Actual cited unique entries increase from 73 to **129**. Excluding six software, data, encyclopedia or duplicate-report entries gives **123 independent research papers**. The merged database has 131 unique works and 31 old-key aliases; two uncited works do not inflate the count. The Biber bibliography contains 129 printed entries, matching PDF reference [129].

ch01 cites 22 distinct works (previously 12); ch02 cites 84 (previously 27). The final source ledger includes the official metadata source and every supporting paragraph. Newly added conference works are CCF A full papers; six additions are journal articles. All 56 have primary records. Scholar has saved crosschecks for 24 selected additions plus an earlier interactive REALM check; a CAPTCHA stopped further checks. Full coverage is not claimed for Scholar. See [the current review](reference-expansion-2026-10-28/REVIEW.md).

`reference-expansion-2026-10-28/source-checks.json` confirms that original nonempty citation occurrences and labels remain, with one new section label. Equations, inline math, algorithms, figures and tables are unchanged. The abstract and chapters 3–8 are byte-identical to the start of this expansion. The earlier whole-manuscript wording pass and empty citation completion remain in `citations-wording-2026-10-28/REVIEW.md`.

## Compilation

The final clean rebuild passed through the `latex-paper-en` skill's `compile.py` with XeLaTeX, latexmk and Biber, with shell escape disabled. The final log has no undefined references/citations, missing characters, duplicate labels/destinations, overfull boxes or LaTeX errors. Biber has no warnings or errors. Existing non-fatal class/package notices remain. Build output: `reference-expansion-2026-10-28/compile-final.log`.

## Reading copy and visual inspection

`main.pdf` and `thesis.pdf` are identical. SHA-256: `6e2a743fe4d42b94340c4958dc000e39840978c057727eb86f7c91bfc980dbb5`.

The PDF has **125 unrotated A4 pages**: 14 preliminary, 102 body and 9 reference pages. All 95 fonts are embedded; every page has extracted text. All 125 pages were rendered and reviewed in seven contact sheets. Enlarged review covered the Introduction opening, new few-shot section, multimodal discussion, and first/final reference pages (physical pages 15, 26, 31, 117, 125). No new clipping, overlap or malformed citations was observed.

The four approximate margin flags concern the same original embedded source-figure axis labels as before, now on printed pages 36, 50, 51 and 94. They remain unclipped. Renders, page maps and bounds are under `reference-expansion-2026-10-28/pdf-qa/`; the final summary is `final-validation.json`.

Current counts: **22,182 narrative words**, **24,124 including headings/captions**, **213 abstract words**. Actual chapter page ranges are in `CHAPTER_COUNTS.md`. The writing audit found no sentence-level em dashes or common reviewer-facing stock disclaimers in the narrative files; scientific protocol conditions were retained.

## Historical checkpoints and author items

The preceding QA is preserved in `reference-expansion-2026-10-28/before/planning/FINAL_QA.md`. Earlier records are historical checkpoints. Institutional fields and source-specific author items remain in `AUTHOR_ACTIONS.md` and evidence ledgers. The app's earlier independent preview issue remains documented in `compile-repair-2026-10-27/REPORT.md`; this checkpoint verifies the local compiled PDF.
