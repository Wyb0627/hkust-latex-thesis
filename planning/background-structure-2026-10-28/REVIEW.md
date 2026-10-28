# Background Section 2.1 revision

Date: 2026-10-28 (Asia/Shanghai).

## Scope and organization

Section 2.1 is now *Knowledge Structures for Language Models*. Eight paragraphs introduce graph facts, existing and task-built sources, mention-to-node mapping, neighborhoods/paths/subgraphs, learned knowledge representations, textual knowledge inputs, parameter and retrieval adaptation, and the transition to table annotation. The chapter opening was updated to reflect this order.

The rewrite removes the standalone KGE scoring-function catalogue and the XLNet/T5/InstructGPT pre-training history. KEPLER remains as an example of knowledge incorporation during language representation learning. FormerGNN and Sections 2.2–2.8 are unchanged.

## Style references

Read the author's current Chapter 1, the active AGRAG introduction selected by `AGRAG_GORAG/ICDE2026.tex`, and the active GORAG introduction selected by `AGRAG_GORAG/WWW/GORAG_WWW.tex`. Compared the concrete task examples and problem-to-method transitions with printed pp. 2–5 of `sample_thesis/yushi_sun.pdf`, including a rendered page. The revision uses direct explanations of operations, short examples and explicit transitions. It contains no sentence dash or prose colon. Reference prose was used for organization and tone, without copying its wording.

## Citation selection and support

Seven newly cited papers replace nine works whose introductory passages were removed. Three were selected from original author libraries: the Ji et al. knowledge-graph survey and Graph Neural Prompting from `GFM4Graph/GFM.bib`, and Think-on-Graph from `CoT Survey/sample-base.bib`. Four were selected from formal external publications: BLINK and KnowBERT (EMNLP main proceedings), K-BERT (AAAI), and KEPLER (TACL). Candidate search also consulted the previous eleven-library original-bib inventory.

Official ACL/AAAI publication pages support the specific mechanisms described. IEEE-deposited Crossref metadata and the author manuscript verify the survey; its final issue year is 2022, correcting the original bib's online-first year 2021. AAAI metadata supplies Graph Neural Prompting's volume, issue and pages. Think-on-Graph's official ICLR 2024 poster page and author manuscript verify its identity and iterative graph exploration. The OpenReview page requested browser verification, so the ICLR conference record was used instead. No Google Scholar coverage is claimed for this revision.

`citation-ledger.json` maps each addition to the exact revised paragraph and its original library or official source. The `primary/` directory preserves the accessed records. Existing citations support KGLink, GORAG, AGRAG, MGRAG, Wikidata, BERT, Transformer, GPT-3, RAG, HippoRAG and KnowGPT. Their claims remain within the methods described by the current source chapters and existing evidence records.

Citation counting resolves the generated bibliography's aliases and excludes the same six software/data/duplicate-report entries as the preceding review. The current manuscript cites **127 unique entries**, comprising **121 independent research papers**. Removed references remain in the bibliography fragments for provenance but are not counted as cited works.

## Source checks

`source-checks.json` confirms that Sections 2.2 onward, all chapter labels, and inline mathematics are unchanged. Baseline hashes confirm that only `chapter/ch02-background.tex` changed among the abstract/chapter/figure inputs. Existing formulas, algorithms, tables and figures are preserved. Before snapshots and the focused manuscript diff are retained in this directory.

## Build and PDF review

The initial compile retained a stale BibLaTeX rerun flag. A clean rebuild through the same `latex-paper-en/scripts/compile.py` resolved it; no warning was suppressed. The final log checks cover unresolved references/citations, missing glyphs, duplicate labels/destinations, overfull boxes, LaTeX errors, and Biber warnings/errors. See `compile-clean.log` and `compile-layout.log`.

`python3 scripts/inspect_thesis_pdf.py` initially exited 1 because that interpreter lacked `pypdf`. The same script was then run with explicit `pypdf`, `pdfplumber` and `pillow` dependencies in an isolated uv environment, without changing the inspection logic. The initial rendering revealed a hyphenated section heading and a closing transition split across pages. The section title and transition were shortened before the final layout build.


The final PDF has **125 pages** (14 preliminary, 102 body, 9 reference). Section 2.1 occupies printed pp. 9–10; Section 2.2 begins on p. 11. The shortened heading fits on one line and the closing transition stays on p. 10. Enlarged visual checks covered physical pp. 6, 23–25, 117–119 and 125; the chapter contact sheet was also reviewed. All pages were rendered and automatically inspected. No clipping, overlap, broken citation or new spacing defect was observed in the reviewed pages. All PDF fonts are embedded. Actual chapter start pages remain unchanged.

Current counts are **22,276 narrative words**, **24,218 including headings/captions**, and **213 abstract words**. The Biber bibliography contains 127 entries. `final-validation.json` contains the final PDF hash and checks; current renders and page maps are in `planning/qa/final/`.
