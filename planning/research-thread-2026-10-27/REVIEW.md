# Research narrative revision

Updated 2026-10-27 (Asia/Shanghai).

## Author-approved research thread

The author confirmed that the transition from KGLink to GORAG was motivated by the restrictions of an existing external KG and the need for task-specific fine-tuning. The intended direction was to construct knowledge from task data and use an LLM's semantic capabilities without requiring either a predefined KG or model fine-tuning. Generalizability is a research motivation; no new cross-domain transfer result is asserted.

The manuscript now develops the following progression.

1. KGLink supplies missing table context through an existing KG and learns the annotation vocabulary through supervised training.
2. GORAG constructs and maintains a graph from classification data and adapts its retrieval index while keeping the language model fixed.
3. AGRAG extends evidence retrieval to connected facts and source context for textual answers.
4. MGRAG extends it to query-aware multimodal construction, semantic path matching, and context recomputation.

AGRAG and MGRAG are presented as two extensions of task-driven retrieval. Their chapter transitions explain the additional evidence requirements without asserting that one implementation was derived from another.

## Reference-led writing choices

- The author's manually revised opening in `chapter/ch01-introduction.tex`, lines 6–8, retains its wording and examples. The last sentence receives only the grammatical correction from *evidences* to *evidence* and removal of the duplicated *therefore*.
- AGRAG reference introduction at `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/section/sec-introduction_sigmod.tex` supplies the task, mechanism, unresolved requirement, and proposed method pattern.
- GORAG reference introduction and conclusion at `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/WWW/section/` supply concrete label-update examples and direct descriptions of retrieval and online indexing.
- `sample_thesis/yushi_sun.pdf`, Chapter 1, printed pages 1–5, supplies the organization around a common research objective and the connection of each research chapter to that objective. Promotional wording and sentence punctuation are governed by the author's current instructions.

The new prose introduces the task requirement before the method, uses direct subjects and verbs, and avoids sentence-level dashes and rhetorical colons. Colons remain in publication titles, RQ headings, and mathematical notation. En dashes in entity associations and page ranges remain technical notation.

## Scope of the revision

Introduction was revised first, including Motivation, Scope, RQ2–RQ4, the GORAG contribution, and the chapter roadmap. The same narrative was then applied to the abstract, Background opening and closing, research-chapter openings and summaries, Discussion, and Conclusion. Redundant restatements were shortened after reading the compiled pages. Formula definitions, algorithm steps, experimental descriptions and results were retained.

Original manuscript files are in `before/`. `manuscript.diff` compares against the author's actual working files at the start of this revision, including the author's uncommitted opening edits and comments. `edits.json` records 29 changed paragraph blocks.

## Claim–evidence map

| Narrative claim | Supporting source | Status |
|---|---|---|
| KGLink uses an existing graph and supervised representation learning | Chapter 3 graph processing, language-model integration, and experiments | Supported |
| GORAG constructs task-specific relationships and changes the index without parameter fine-tuning | Chapter 4 indexing and online-update definitions; author's explanation in this conversation | Supported |
| AGRAG adds connected facts and source context for answer coverage | Chapter 5 subgraph expansion, hybrid retrieval, and ablations | Supported |
| MGRAG makes extraction query-dependent and matches query relations to semantic paths | Chapter 6 construction, matching, and substitution experiments | Supported |
| Graph features guide selective KV recomputation | Chapter 6 recomputation score and cache experiments | Supported |
| The transition was intended to broaden applicability | Author's stated motivation | Motivation; no new generalization measurement claimed |

## Defensive-writing audit

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reader reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| Introduction, Scope | The four studies have separate implementations and evaluations. | D12 | Minor | No | Implementation independence does not explain the research progression. | Interrupts the connection between studies. | Delete | Replaced by an explanation of adaptation through training, index maintenance, and query-specific evidence selection. |
| Introduction, results preview | The published measurements provide quantitative answers to these research questions. | D9 | Minor | No | Announces evidential status without explaining the measured outcome. | Adds an editorial assurance. | Rewrite | Experiments evaluate representation quality, adaptation to evolving labels, answer quality, and context-processing cost. |
| Background, language models | This thesis uses the term language model for both roles and specifies the relevant prediction interface in each research chapter. | D9 | Minor | No | BERT and generative model roles are already defined immediately before it. | Repeats a terminology assurance. | Delete | The preceding model-role definitions remain. |
| Background, hyper-relational study | The study provides a separate perspective on structural information within the thesis. Its experiments concern KG embedding models, while the four research chapters examine language-model augmentation. | D12 | Minor | Mixed | Repeated separation obscures the study's information-preservation role. | Makes the study sound detached from the argument. | Rewrite | Transforming source information into a graph determines which relationships a downstream model can access. The study analyzes this representation problem through fact decomposition, qualifier capture, and graph reception. |
| Discussion, metric comparison | A shared metric label can also conceal a different assessment rule. | D12 | Minor | Mixed | The warning precedes already explicit metric definitions. | Anticipates an unstated mistake. | Rewrite | The assessment rule follows the output being evaluated. |
| Discussion, final paragraph | Neither characterizes the answer quality of the full retrieval and generation pipeline. | D12 | Minor | Mixed | The positive scope statements already identify exactly what each structural condition concerns. | Repeats a non-claim. | Delete | The conditions remain stated as initial-tree cost and accepted path similarities. |

Qualitative paper-level defensive-writing score remains approximately 1/10. This revision primarily repairs the research narrative in a manuscript that had already received a defensive-writing cleanup. The score is an editorial judgment, not an experimental metric.

Highest-priority removals were the implementation-independence statement, the duplicated hyper-relational scope disclaimer, the announcement that published measurements answer the questions, and the repeated negative statement about full-pipeline guarantees.

Necessary scientific conditions remain in place. These include GORAG's prediction-before-insertion order and prediction-derived labels, KGLink's graph coverage and supervised type vocabulary, AGRAG's metric definitions and source-level theoretical conditions, and MGRAG's incomplete greedy search, conditional threshold result, missing numerical recomputation-budget metadata, and end-to-end versus component runtime distinctions.

Literal before/after phrase counts are in `phrase-counts.json`. All nine revised narrative files contain zero em dashes or LaTeX triple-hyphen sentence dashes. The non-key colons were checked manually and occur only in headings, publication titles, or mathematical notation.

## Validation

`source-checks.json` verifies unchanged numeric tokens, citation-key multiplicities, labels, inline math, displayed equations, algorithms, figures, longtables, and tabular contents in all nine revised files. Only the Introduction's first table caption changed; its cells and references remain intact.

Compilation uses the `latex-paper-en` skill entry point with the existing XeLaTeX/Biber toolchain and shell escape disabled.

```sh
python3 /Users/ybwang/.agents/skills/latex-paper-en/scripts/compile.py main.tex --compiler xelatex --recipe latexmk
```

The final compile log is `compile.log`. `inspect_pdf.py` checks LaTeX and Biber diagnostics, copies `main.pdf` to `thesis.pdf`, extracts bookmarks and geometry, and renders all pages through Poppler. It uses the existing Anaconda Python installation for pypdf and Pillow. PDF checks and contact sheets are in `pdf-qa/`.

The initial reference-extraction probe used an unavailable `fitz` module and exited before writing any files. Reference extraction subsequently used installed Poppler `pdftotext`. An intermediate rendering pass encountered obsolete thumbnails after the PDF page count changed; limiting the thumbnail list to the current page count corrected the contact-sheet input. These were tooling issues and did not change manuscript content or the TeX engine.

Current page counts and the final visual-inspection outcome are recorded in `../CHAPTER_COUNTS.md` and `../FINAL_QA.md`.

The author also revised `chapter/front-acknowledgements.tex` concurrently. These edits were left untouched and included in a final rebuild. Only PDF page 5 changed, as verified by decompressed page-stream hashes. This is separate from the nine-file narrative revision above.
