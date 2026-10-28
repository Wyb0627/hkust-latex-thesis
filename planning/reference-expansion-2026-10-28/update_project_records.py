from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
counts=json.loads((out/'pdf-qa/chapter-counts.json').read_text());pre=json.loads((out/'pdf-qa/pdf-preflight.json').read_text())
files=[root/'chapter/front-abstract.tex',*sorted((root/'chapter').glob('ch0*.tex'))]
# Ignore source comments; retain printed names and headings for the punctuation audit.
body='\n'.join(re.sub(r'(?<!\\)%[^\n]*','',p.read_text()) for p in files)
patterns={'we do not claim':r'\bwe do not claim\b','to ensure fairness':r'\bto ensure fairness\b','it should be noted':r'\bit should be noted\b','taken together':r'\btaken together\b','preliminary':r'\bpreliminary\b','promising / encouraging / compelling':r'\b(?:promising|encouraging|compelling)\b','em dash / LaTeX triple hyphen':r'—|---','while':r'\bwhile\b','however':r'\bhowever\b'}
audit={k:len(re.findall(v,body,re.I)) for k,v in patterns.items()}
(out/'writing-patterns.json').write_text(json.dumps(audit,indent=2))
s='''# Writing check under the author's updated instructions

2026-10-28. Scope: manually review the newly expanded ch01/ch02 paragraphs, Abstract, Discussion and Conclusion, and scan all eight narrative chapters for defensive stock phrases and sentence punctuation. This complements the preceding full-manuscript wording pass in `../citations-wording-2026-10-28/`.

The audit uses `academic-defensive-writing-auditor`. Scientific protocol conditions are retained when they determine what the method or reported result means. No additional manuscript changes were needed after the final compilation.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| ch02, retrieval | The generated document guides retrieval; the retrieved source documents supply the evidence used downstream. | CLEAN | None | Technical distinction | Explains the different roles of generated queries and source evidence. | Clarifies HyDE without inventing provenance. | Retain. | Unchanged. |
| ch02, few-shot adaptation | These visual-learning settings establish related adaptation problems; incremental few-shot text classification introduces successive rounds of text labels and limited examples. | NECESSARY_CAVEAT | None | Yes | Identifies the domain and protocol difference in cited work. | Avoids presenting visual-learning studies as text experiments. | Retain. | Unchanged. |
| ch07, evaluation | Its source-defined ROUGE-L quantity divides longest-common-subsequence length by generated-answer length. | NECESSARY_CAVEAT | None | Yes | States the actual source metric. | Prevents confusion with alternative ROUGE-L conventions. | Retain. | Unchanged. |
| ch07, limitations | GORAG starts from sparse support data and can retain errors through prediction-derived updates. | NECESSARY_CAVEAT | None | Yes | Gives a concrete error-propagation mechanism. | Scientifically useful limitation. | Retain once in this limitations discussion. | Unchanged. |
| ch08, feedback | An online correction becomes available after the original prediction, and an answer assessment can guide only subsequent retrieval. | NECESSARY_CAVEAT | None | Yes | Specifies information availability. | Makes the future evaluation protocol interpretable. | Retain. | Unchanged. |

## Paper-level defensive-writing score

**1/10**, qualitative editorial assessment. No critical or major defensive passages were identified in the current review. The Abstract and Introduction motivate the methods through data and task requirements. Discussion states protocol differences directly; Conclusion describes the implemented progression. Necessary metric, timing and coverage conditions remain concise.

## Highest-priority removals

No additional deletion was justified in the current expanded paragraphs. The preceding author-led wording pass already removed repeated explanations and abstract editorial wording. The expansion adds named methods and the technical distinctions needed to connect them to the thesis, without calling the evidence comprehensive, fair or sufficient.

## Necessary caveats to preserve

- Existing-graph coverage and the annotation label vocabulary constrain KGLink's input and supervised predictor.
- GORAG's cumulative index uses the information available at each prediction, including prediction-derived associations.
- AGRAG's coverage and faithfulness measure different aspects of an answer; its source metric definition remains explicit.
- MGRAG's extraction, caption ranking and accepted matches affect what can enter retrieval and cache processing.
- Source-internal theory and unreported experimental recomputation settings remain recorded rather than being replaced by invented claims.

## Repeated phrase audit

Counts below use the abstract and eight chapter files, excluding LaTeX comments. “while” and “however” are context indicators, not automatic violations; inspected occurrences express model, evidence or protocol differences.

| Pattern | Occurrences |
|---|---:|
'''
for key,n in audit.items():s+=f'| {key} | {n} |\n'
s+='''
No sentence-level em dash or `---` appears in these narrative files. The retained colons belong to RQ headings and the original titles of KGLink, GORAG, AGRAG and MGRAG; the source comments do not print. Mathematical ranges and LaTeX double hyphens used for relations or names are not sentence-level em dashes.
'''
(out/'WRITING_CHECK.md').write_text(s)
# Keep the current project index accurate without rewriting historical records.
p=root/'README.md';s=p.read_text().replace('The reading copy `thesis.pdf` includes citation completion and the author-led wording revision and has 115 pages.','The reading copy `thesis.pdf` includes citation completion, the author-led wording revision, and the ch01/ch02 literature expansion and has 125 pages.')
s=s.replace('- `planning/citations-wording-2026-10-28/REVIEW.md`: current citation map, original-bib search, primary-source verification, wording edits, and source/PDF checks.','- `planning/reference-expansion-2026-10-28/REVIEW.md`: current 123-paper / 129-reference count, 56 additions, original-bib provenance, primary verification, partial Scholar crosschecks, and source/PDF checks.\n- `planning/citations-wording-2026-10-28/REVIEW.md`: preceding seven-position citation completion and full-manuscript author-led wording pass.')
old=s[s.index('The latest revision follows'):]
s=s[:s.index('The latest revision follows')]+'''The manuscript follows the author-approved progression from KGLink's use of an existing KG and supervised fine-tuning to GORAG's graph construction from task data and prediction without model fine-tuning. AGRAG and MGRAG extend this direction to connected textual evidence and query-aware multimodal matching. The preceding wording pass completed seven empty citation positions and extended the author's problem-to-method transitions across the manuscript.

The current literature expansion adds 56 published papers, including 36 from the author's original bib libraries and 20 externally found works. The manuscript now cites 129 unique reference entries, comprising 123 independent research papers under a conservative count that excludes six software/data/duplicate-report entries. All newly added conference papers are CCF A full papers; six additions are journal articles. Google Scholar crosschecking was partial because it requested CAPTCHA verification; all 56 additions were independently checked against official proceedings, journal or publisher-deposited metadata. ch01 and ch02 now cite 22 and 84 distinct works respectively.

Current sources have 22,182 narrative words, 24,124 words including headings/captions, and a 213-word abstract. Source-preservation checks and the clean XeLaTeX/Biber build passed. The 125-page PDF was rendered and visually reviewed. See `planning/reference-expansion-2026-10-28/REVIEW.md` and `planning/FINAL_QA.md`. The app's earlier independent preview issue remains documented in `planning/compile-repair-2026-10-27/REPORT.md`; the October 25 portable ZIP is an older snapshot.
'''
p.write_text(s)
(root/'planning/FINAL_QA.md').write_text(f'''# Current source QA and PDF checkpoint

Updated 2026-10-28 (Asia/Shanghai), after the ch01/ch02 literature expansion and the author's updated writing instructions.

## Source and citation verification

The current expansion adds 56 published papers: 36 from original paper libraries and 20 found externally. Actual cited unique entries increase from 73 to **129**. Excluding six software, data, encyclopedia or duplicate-report entries gives **123 independent research papers**. The merged database has 131 unique works and 31 old-key aliases; two uncited works do not inflate the count. The Biber bibliography contains 129 printed entries, matching PDF reference [129].

ch01 cites 22 distinct works (previously 12); ch02 cites 84 (previously 27). The final source ledger includes the official metadata source and every supporting paragraph. Newly added conference works are CCF A full papers; six additions are journal articles. All 56 have primary records. Scholar has saved crosschecks for 24 selected additions plus an earlier interactive REALM check; a CAPTCHA stopped further checks. Full coverage is not claimed for Scholar. See [the current review](reference-expansion-2026-10-28/REVIEW.md).

`reference-expansion-2026-10-28/source-checks.json` confirms that original nonempty citation occurrences and labels remain, with one new section label. Equations, inline math, algorithms, figures and tables are unchanged. The abstract and chapters 3–8 are byte-identical to the start of this expansion. The earlier whole-manuscript wording pass and empty citation completion remain in `citations-wording-2026-10-28/REVIEW.md`.

## Compilation

The final clean rebuild passed through the `latex-paper-en` skill's `compile.py` with XeLaTeX, latexmk and Biber, with shell escape disabled. The final log has no undefined references/citations, missing characters, duplicate labels/destinations, overfull boxes or LaTeX errors. Biber has no warnings or errors. Existing non-fatal class/package notices remain. Build output: `reference-expansion-2026-10-28/compile-final.log`.

## Reading copy and visual inspection

`main.pdf` and `thesis.pdf` are identical. SHA-256: `{pre['pdf_sha256']}`.

The PDF has **125 unrotated A4 pages**: 14 preliminary, 102 body and 9 reference pages. All 95 fonts are embedded; every page has extracted text. All 125 pages were rendered and reviewed in seven contact sheets. Enlarged review covered the Introduction opening, new few-shot section, multimodal discussion, and first/final reference pages (physical pages 15, 26, 31, 117, 125). No new clipping, overlap or malformed citations was observed.

The four approximate margin flags concern the same original embedded source-figure axis labels as before, now on printed pages 36, 50, 51 and 94. They remain unclipped. Renders, page maps and bounds are under `reference-expansion-2026-10-28/pdf-qa/`; the final summary is `final-validation.json`.

Current counts: **22,182 narrative words**, **24,124 including headings/captions**, **213 abstract words**. Actual chapter page ranges are in `CHAPTER_COUNTS.md`. The writing audit found no sentence-level em dashes or common reviewer-facing stock disclaimers in the narrative files; scientific protocol conditions were retained.

## Historical checkpoints and author items

The preceding QA is preserved in `reference-expansion-2026-10-28/before/planning/FINAL_QA.md`. Earlier records are historical checkpoints. Institutional fields and source-specific author items remain in `AUTHOR_ACTIONS.md` and evidence ledgers. The app's earlier independent preview issue remains documented in `compile-repair-2026-10-27/REPORT.md`; this checkpoint verifies the local compiled PDF.
''')
(root/'planning/STYLE_AUDIT.md').write_text('''# Current thesis writing audit

Updated 2026-10-28 (Asia/Shanghai).

The manuscript retains the author's problem-to-method progression: existing-KG enrichment and supervised adaptation in KGLink, task-data graph construction and fixed-parameter prediction in GORAG, then connected textual evidence in AGRAG and query-aware multimodal matching in MGRAG.

The preceding [author-led wording pass](citations-wording-2026-10-28/REVIEW.md) made 44 exact replacements across the abstract and eight chapters and completed seven empty citation positions. It corrected grammar, repeated expressions and abstract editorial wording while preserving scientific conditions.

The current [literature expansion](reference-expansion-2026-10-28/REVIEW.md) adds evidence-backed ch01/ch02 prose and 56 published papers, reaching 129 distinct references and a conservative 123 independent papers. It adds a few-shot adaptation section and explains how the cited methods connect to the thesis, rather than inserting unrelated citation clusters. Every addition has a claim-level location and an official metadata record. Scholar crosschecking is explicitly partial.

The author's updated instructions prohibit defensive prose and sentence-level em dashes and discourage sentence colons. The [writing check](reference-expansion-2026-10-28/WRITING_CHECK.md) reviews new paragraphs, Abstract, Discussion and Conclusion and scans all narrative files. No stock reviewer-facing disclaimer or sentence-level em dash was found. Colons remain in RQ headings and original paper titles. Necessary conditions on information availability, source coverage, metrics and extraction errors remain.

Original citations, labels, formulas, algorithms, figures and tables passed preservation checks. Abstract and chapters 3–8 are unchanged in this expansion. Current counts are 22,182 narrative words, 24,124 including headings/captions and a 213-word abstract. The 125-page PDF passed clean XeLaTeX/Biber and visual checks; see `FINAL_QA.md`.

Previous audits are preserved in the corresponding dated `before/` directories and historical reviews.
''')
(root/'planning/WRITING_PROGRESS.md').write_text('''# Thesis writing progress

Updated 2026-10-28 (Asia/Shanghai), after the ch01/ch02 literature expansion.

## Current manuscript

The research progression remains existing-KG enrichment and supervised adaptation in KGLink, task-data graph construction and prediction without fine-tuning in GORAG, then connected textual evidence in AGRAG and query-aware multimodal matching in MGRAG.

The preceding full-manuscript wording pass followed the author's Introduction changes and completed seven empty citation positions. The current expansion adds 56 published papers (36 original-library, 20 external) and related prose in ch01/ch02. Actual cited unique references increase from 73 to 129; excluding software, data and duplicate reports leaves 123 independent papers. ch01/ch02 cite 22/84 distinct works. All 56 additions have official records; new conference papers are CCF A full papers. Scholar crosschecking was partial because it requested CAPTCHA verification.

The latest review, exact changes, provenance, source checks and citation-to-paragraph map are in [the current review](reference-expansion-2026-10-28/REVIEW.md). The updated academic-writing check is `reference-expansion-2026-10-28/WRITING_CHECK.md`. The prior 44-replacement wording review remains in `citations-wording-2026-10-28/REVIEW.md`.

Narrative words: 22,182. Including headings/captions: 24,124. Abstract: 213 words. Original citations, labels, math, algorithms, tables and figures passed preservation checks. The abstract and chapters 3–8 are byte-identical to the start of this expansion. No research method or experiment was changed.

## Compilation and review

`main.pdf` and `thesis.pdf` are identical 125-page files. The final clean XeLaTeX/Biber rebuild passed. All pages were rendered and reviewed, with detailed inspection of new prose and first/final reference pages. Counts and hash are in `CHAPTER_COUNTS.md`; validation is in `FINAL_QA.md`.

The app's independent preview remains outside this revision. Its earlier failure and the working local project build are documented in `compile-repair-2026-10-27/REPORT.md`.

## Author review

The expanded manuscript is ready for author and supervisor review. Suggested focus is the new ch02 background section and the connection of the added literature to each research question. Real department-head identity, signatures/dates, title-page numeral clarification and source-specific items remain in `AUTHOR_ACTIONS.md`.
''')
print('Updated project records and writing check:',audit)
