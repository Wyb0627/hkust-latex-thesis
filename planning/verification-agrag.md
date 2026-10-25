# AGRAG source verification

Audit date: 2026-10-24. Updated by the independent gorag reviewer after the author's version decision. **Status: AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION_CROSSCHECKED.** Chapter: `chapter/ch05-agrag.tex`. This status denotes fidelity to the complete local PDF explicitly selected by the author; it does not claim that the PDF was obtained directly from IEEE or that all source-internal mathematical claims have been independently proved.

## Author decision and source identity

The author explicitly chose `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/ICDE2026.pdf` and its corresponding source over the incomplete arXiv PDF. This resolves which version supplies the thesis's AGRAG methods and results. The local PDF has 15 physical pages, 670,757 bytes, SHA-256 `9922cc9633cfd3036e70cf0ffc51348cd790e233e8816ed22b11a1188596d820`; metadata records a 24 April 2026 build. It contains dataset TableII, main results TableIII, efficiency TableIV, ablation TableVI and low-resource TablesVII/VIII. The arXiv file's differing table inventory is no longer used to decide which complete results to adopt.

The selected entry is `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/ICDE2026.tex`, with active `section/sec-*_sigmod.tex` inputs as identified in `planning/source_roots.json` and `SOURCE_MAP.md`. The suffix records source history; unsuffixed older files, rebuttals and inactive tables are excluded. Working source extraction is `planning/extracted/agrag-active.tex.txt`.

Acquisition history is retained: IEEE record11629443 could not be fetched, and its stamp endpoint returned HTTP418. HKUST Research Portal confirms the publication identity. The direct publisher PDF was not downloaded. The author's explicit local-version selection supplies the authority for comparison in this project.

The supplementary local `AGRAG_GORAG/proof.pdf`, extracted in `planning/extracted/agrag-proof.txt`, is a separate proof document. It is not silently treated as a publisher PDF or a replacement method specification. The author directed main-text precedence for conflicting descriptions.

## Numeric table verification

The independent reviewer re-parsed active original table bodies after excluding `%` comments and `comment` environments; the owner's table generator was not run during review. Selected source columns were compared with the 18 split-table records in `planning/agrag-table-cells.json`, then compared independently with the corresponding complete local PDF rows. **652/652 numerical entries match in both comparisons.** Original decimal strings, comma grouping, paired time/token order and emphasis are retained in the adopted split tables. Paired cells count as two numerical entries.

| Local PDF table / physical page | Active source label and raw line | Thesis table files | Compared numerical entries | Status |
|---|---|---|---:|---|
| III / p9 | `tab:main_exp`, `sec-experiment_results_sigmod.tex:94` | `chapter/tables/agrag-main-{creative,summary,complex,fact,class}.tex` | 242 | MATCH_AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION |
| IV / p10 | `tab:efficiency`, same file:183 | `chapter/tables/agrag-efficiency.tex` (time and token blocks) | 176 | MATCH_AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION |
| VI / p11 | `tab:abl_exp`, same file:416 | `chapter/tables/agrag-ablation.tex` (four quality blocks and cost block) | 156 | MATCH_AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION |
| VII / p11 | `tab:exp_low`, same file:473 | `chapter/tables/agrag-low-resource.tex` | 54 | MATCH_AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION |
| VIII / p11 | `tab:exp_low_eff`, same file:499 | `chapter/tables/agrag-low-resource-efficiency.tex` | 24 | MATCH_AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION |

PDF TableVIII is alongside TableIX. Its first row was separately re-extracted from the left page column using `pdftotext -f 11 -l 11 -x 0 -y 0 -W 306 -H 792 -layout ...` to exclude adjacent TableIX numbers. This resolved a reading-layout artifact without altering a research asset or source value.

Dataset TableII on physical p9 was read separately. The chapter's adopted prose statistics match: Novel5,140 chunks/63,887 entities/163,169 relations; Medical1,030/12,426/52,054; WOS24 chunks,9,396 tests,133 labels; IFS-Rel11 chunks,2,560 tests,64 labels. Query counts match Novel CG67/CS362/CR610/FR971 and Medical166/289/509/1,098. The questionable average MCST node/edge statistics are not adopted in the chapter.

All quoted main/ablation/low-resource narrative values were checked against these table columns. Main versus ablation time and token series remain separate; their differing measurements were not averaged. The chapter reports cases in which a variant exceeds the full method, such as no-HR Novel creative faithfulness0.519 versus0.513 and no-MCMI Medical fact ROG0.359 versus0.357. No universal-best claim or inferred significance statement was added.

## Formula and method verification

The current checked chapter snapshot has SHA-256 `c44a0089f144e249eed67b681fc7290dcefa0d58293d57fcce93b21e1322fc33`. The following comparisons use the author-selected complete local PDF and active source, with physical page numbers.

| Thesis label / topic | Local original equation / page | Check |
|---|---|---|
| `eq:agrag:chunking` | (1), p4 | Chunk length/overlap interface retained. |
| `eq:agrag:extraction-score`, `eq:agrag:entities` | (2), p4; (3), p5 | Count/text-length/log normalization and IDF term retained; original strict threshold and reported b3/tau0.5 retained. No rescaling step invented. |
| `eq:agrag:relations` | (4), p5 | LLM relation extraction takes extracted entities, chunk and prompt. |
| `eq:agrag:mapping`, `eq:agrag:filter` | (7)–(9), p5 | Cosine fact mapping, top-ka raw set and model-based filtering preserved. |
| `eq:agrag:propagation` | (10), p5 | Recurrence and ordering of the d terms match. d0.5/change threshold10^-7 retained. |
| Personalization prose / `eq:agrag:graph-operator` | (11),(12), p6 | Source 0/1 personalization and neighbor/nonedge entries reproduced; no silent normalization. “Node participating in a mapped fact” makes the source's u-in-triple-set wording readable without a new probability normalization. |
| Passage scaling / `eq:agrag:edge-cost` | source paragraph and (14), p6 | Passage score factor0.05; cosine-derived edge cost `(1-MS)/2`; pseudo-edge penalty10 preserved. |
| `eq:agrag:mcmi-objective` | (15), p6 | Sum over per-edge c/(su+sv), not a ratio of global sums. |
| `eq:agrag:marginal`, `eq:agrag:acceptance` | (17), p7 | Candidate cost divided by its node score; strict `< r(G)` acceptance and `>=` stopping condition preserved. No monotonic-decrease theorem added. |
| Graph serialization | (18), p7 | Selected node/edge strings supply the graph context. |
| `eq:agrag:hybrid`, `eq:agrag:generation` | (20)–(22), p7 | Top-kr hybrid chunks, arithmetic mean of dense similarity and BM25, graph/query/chunks generation interface retained. |
| `eq:agrag:rouge` | Metric c, p8 | LCS(G,Y)/generated length |G| retained. Not silently replaced by ROUGE-L F1. |
| `eq:agrag:coverage`, `eq:agrag:faithfulness` | Metrics d/e, p8 | Required-reference-evidence denominator versus generated-claim denominator retained. |

The original Figure2 example (p5) and its running-example prose (p7) support the chapter's mapped-fact strings and blood-vessels answer. The chapter identifies this as the original qualitative illustration. It does not present the figure as an additional controlled experiment.

## Protocol checks

- Entity extraction replaces only the entity-selection stage. Relations, raw-triplet filtering and answer generation remain model-based.
- Entity nodes, passage nodes, Contains links, synonym links and pseudo-node connections match the original representation.
- Main backbone is Qwen2.5-14B-Instruct/vLLM. Dense passage representations use Contriever for AGRAG/HippoRAG2 and bge-large-en-v1.5 for the other baselines. Raw-triplet filtering uses Qwen3-Reranker-0.6B. Main hardware is Intel Xeon Gold5220R plus one NVIDIA A10080GB.
- Chunk length256/overlap32; ka=kr=5; max n-gram3; extraction threshold0.5; global RAG retrieval top-k5. The synonym threshold is a source symbol; no unreported numeric value was invented.
- Classification indexes one training passage per label; AGRAG and HippoRAG2 retrieve associated labels to form a candidate set. This is distinct from GORAG's round-based online-update protocol.
- Classification ACC is exact label matching, REC is macro recall; QA ACC uses model-assigned0/0.5/1. ROG/COV/FS retain the source's exact formulas and task assignments. No common pooled score was derived.
- The low-resource experiment changes both backbone (Qwen3-4B-Instruct-2507) and hardware (two2080Ti GPUs). It is not described as an isolated model-size ablation.
- Parameter settings tested are b in{1,3,5,7} and tau in{0.1,0.3,0.5,0.7}. Original heatmap cells were not converted into new estimated numeric observations.

## Figure verification

Four copied PDF files are independently hash-checked against their original assets and visually matched to the selected complete local PDF. The separate JSON manifest still contained its initial pending-visual status at review time; the reviewer owns only this record and `review-agrag.md`, so did not edit it.

| Target asset | Original figure / physical page | SHA-256 | Check |
|---|---|---|---|
| `figures/agrag/AGRAG_pipeline.pdf` | Fig1 / p4 | `84de949296d180d41981827640d998124070d804c7189ffc26daf77f7aa203ee` | Byte-identical; visual match. |
| `figures/agrag/GERAG_example.pdf` | Fig2 / p5 | `05240a54e06bfb2de9c2ef2bb9baea2cd5ce52977bb740aa925adc71a32402f0` | Byte-identical; graph labels, costs, scores, colors and example answer match. |
| `figures/agrag/heatmap_novel.pdf` | Fig3a / p12 | `b57050eba05cf56e7a49cca85ef6a95eb6221c13d339e744ef20492a2c455981` | Byte-identical; four tasks, axes, tested parameters and color scales match. |
| `figures/agrag/heatmap_medical.pdf` | Fig3b / p12 | `3a473d3af15987a0cc70c3f55d072da3881c25dd6a4eb4f4a7060c38a9519634` | Byte-identical; four task panels retained. |

## Source-internal consistency issues and adopted treatment

These issues were previously raised with the author. The author selected the complete local version and instructed main-text precedence. They remain documented; the thesis does not silently repair the experiment or method.

1. **MCMI objective and monotonic argument.** With fixed scores and nonnegative costs, adding an edge increases the stated sum objective; the supplementary monotonic-decrease argument does not follow for that expression. The chapter preserves both the reported objective and the operational acceptance condition but does not assert monotonic decrease or a new global guarantee.
2. **PPR entries.** The specified neighbor/nonedge entries generally are not a row-stochastic matrix, and the source's triple-set membership notation for a node is imprecise. The chapter calls it a reported graph operator and reproduces the entries. Code-level equivalence or convergence under all graph conditions has not been independently established.
3. **Approximation scope and paths.** The framework overview is broader than detailed Theorem2; Algorithm3's initial path domain also needs care. The chapter attributes the 2-approximation statement to initial MCST connectivity only. It does not extend it to MCMI expansion or supply a repaired proof.
4. **Cycles and insertion.** Figure2 and narrative describe cyclic evidence; the listed update adds a neighboring node and edge. The chapter uses the original illustration and reported expansion condition without inventing a separate cycle-closing operation.
5. **Complexity/storage.** The source's dense-adjacency/O(E) storage wording is inconsistent under ordinary dense storage accounting. The chapter describes stored objects and graph-operation counts, and retains empirical time/token evidence; it does not assert a validated whole-pipeline or dense-memory bound.
6. **Average MCST statistics.** Dataset TableII has average edge counts exceeding average node counts. These entries are not used in the thesis as simple-tree measurements. Other adopted dataset counts were checked directly.

## Review and remaining checks

`planning/review-agrag.md` contains the independent first/second-pass review, resolved findings, numeric checks and defensive-writing audit. Latest source pages4–12 were rendered and inspected for equations, figure correspondence, and table conditions. An earlier standalone chapter build succeeded with four small overfull paragraphs; the main agent has since edited the text. The final integrated thesis must be rebuilt and visually inspected after those edits. Bibliographic key availability was checked for all23 current citations; metadata verification beyond the own-paper record and reused primary records remains the main agent's bibliography audit.

This source audit does not claim a new implementation reproduction, an independent proof of every published theorem, or final integrated-PDF clearance. No experiment was added and no original research image was redrawn.


## Independent round-two integration — 2026-10-25

The pseudo-node is described as a connectivity device rather than an indexing device, avoiding an unconfirmed claim about lifecycle; the cost10 and source method remain. All17 displayed formula blocks are byte-identical. Repeated metric/example assurances were removed while retaining the source propagation entries, sum objective, expansion test, metric denominators and changed low-resource model/hardware. Numerical rank emphasis was removed from `chapter/tables/agrag-efficiency.tex` (35 marks) and `agrag-ablation.tex` (55); this overrides historical claims that source highlighting is preserved. Every literal value/unit/missing marker is unchanged. The optional table generator's formatting was synchronized without table regeneration. Source supplementary monotonicity/normalization conflicts remain unresolved and are not thesis guarantees.

Current PDF/counts and visual findings are in `FINAL_QA.md`; prior chapter audit counts remain historical. Full dispositions: `review-round2/REVIEW_SUMMARY.md`. No new experiment was run.
