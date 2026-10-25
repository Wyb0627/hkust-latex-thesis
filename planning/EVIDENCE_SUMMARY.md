# Evidence and provenance summary

Updated 2026-10-25. Scope: claims, formulas, tables, figures, references and conditions adopted in the thesis. Source correspondence is distinguished from re-executing experiments or independently proving every theorem in the source papers. No new experiments were run.

## Selected versions

| Work | Controlling evidence | Authority and ledger |
|---|---|---|
| KGLink | Selected ICDE revision source and author-linked arXiv 2406.00318v1 PDF | AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; `verification-kglink.md` and `kglink-sources/manifest.json` |
| GORAG | Selected WWW camera-ready source and author-linked arXiv 2501.02844v4 PDF | AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; `verification-gorag.md` |
| AGRAG | Complete local `AGRAG_GORAG/ICDE2026.pdf` and active `ICDE2026.tex`/`sec-*_sigmod.tex` | AUTHOR_SELECTED_COMPLETE_LOCAL_VERSION, explicitly confirmed by author; retained at `published/agrag-local-complete.pdf`, SHA-256 `9922cc9633cfd3036e70cf0ffc51348cd790e233e8816ed22b11a1188596d820`; `verification-agrag.md` |
| MGRAG | Direct PVLDB 19(9), 2480–2493 publisher PDF plus selected source | PUBLISHER_PDF; `published/mgrag-pvldb-2026.pdf`, `verification-mgrag.md` |
| HyperKG/FormerGNN | Selected CIKM source and author-linked arXiv 2508.03280v1 PDF | AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; `verification-background.md` |

ACM/IEEE access restrictions were recorded. Author confirmation is not mislabeled as a direct publisher download. AGRAG's arXiv PDF lacks the data/main-result tables present in the chosen local complete version; those tables are verified against the chosen local PDF, not against nonexistent arXiv tables. Publication venue/author/date/DOI metadata are checked separately, including saved Crossref records and primary publication pages.

## Numerical and graphical checks

| Adopted evidence | Checked numeric or missing-value entries | Records |
|---|---:|---|
| KGLink selected tables | 68 | `kglink-table-cells.tsv`, chapter ledger |
| GORAG adopted tables | 250 | `gorag-main-cell-ledger.csv`, `gorag-other-cell-ledger.csv`; actual integrated PDF re-extraction also passes 250/250 |
| AGRAG 18 split tables | 652 | `agrag-cell-ledger.json`, independent `review-agrag.md`; local PDF → active source → thesis split tables match |
| MGRAG Tables 3–10 | 753 | `mgrag-cell-verification.json`, 92 checked rows, publisher → source → thesis correspondence |
| Background projection of HyperKG Table 6 | 42 | `background-table-cells.json`, all seven rows and six selected metric columns |
| **Total** | **1,765** | All adopted entries in these audits match their controlling evidence |

The counts above refer to the adopted result/statistics table audit units, not every number appearing in a paragraph, algorithm, axis label or citation. Key numerical statements and experimental conditions are additionally mapped in the individual chapter ledgers. The unparsed GORAG `03139` cell is not repaired into a decimal or adopted in a result table; the complete CAD block is excluded, while unambiguous CAD values are discussed.

All **27** copied research graphic files pass a new source-file/target-file/manifest SHA-256 comparison: `qa/final/asset-hash-verification.json`. They form 21 figure environments. Layout changes are LaTeX size/placement/captions only. No plotted values were estimated from pixels and no research image was redrawn. Current figure manifests identify original figure/page locations. The thesis contains 46 table labels, 47 displayed math environments, one algorithm environment and a separately described greedy path procedure; detailed source/formula locators are in the chapter ledgers.

## Method, formula and interpretation checks

- KGLink: selected linking/filtering, candidate-type and feature construction, serialization, projection, source-order DMLM loss and adaptive task loss are retained. VizNet uses the main-text 73,034-column count as instructed; the contradictory 74,141 table total is not substituted. Ablation checkbox semantics and source numeric-statistic wording are not invented.
- GORAG: keyword/cost/update formulas and prediction-before-update timing are preserved. The operational terminal/auxiliary-tree/path account follows the author-selected main text. The appendix's first-MST construction does not silently become a standard Mehlhorn proof. Round-generalization points retain their different partitions; main and ablation series remain distinct.
- AGRAG: extraction and threshold, anchors, exact propagation operator (including nonedge entries), damping/scaling, edge cost, sum objective, candidate acceptance, hybrid score and source-specific ROG/COV/FS definitions are retained. No hidden matrix normalization, ratio-of-sums replacement or supplementary monotonicity theorem is introduced. The initial-tree statement is not a guarantee for the full expanded objective.
- MGRAG: query-dependent construction, entity mapping, path semantics, greedy extension, serialization, graph-feature/cache score and published cost expressions are traced. The graph's retrieval and recomputation contributions are both retained. The threshold condition applies to valid accepted matches; search completeness is not asserted. Table-specific times/totals are preserved despite source inconsistencies, and b remains unreported as a fixed experimental value.
- HyperKG: decomposition and qualifier/graph-reception claims are located in the independent background section. Selected dataset columns and actual metric rankings are explicit; no downstream LM result is attributed to FormerGNN.

The individual ledgers provide exact source labels/pages, retained conditions, source conflicts and what was not independently established. These are source-faithfulness checks, not a claim of complete implementation equivalence, experiment reproduction, statistical significance testing or a new proof of the source theorems.

## References and synthesis

105 source bibliography entries are merged into 74 distinct works using DOI/title identity, with 31 original keys retained as aliases. No duplicated bibliography entries or unresolved citation keys remain in the final build. Primary-source corrections for Transformer, BM25, Contriever, RAGAs, LongLLMLingua, LightRAG and HyperFormer are recorded in `bibliography-primary-corrections.md`. Background literature descriptions are checked at the primary-record/manuscript level indicated by `verification-background.md`; external papers are not all claimed to have a line-by-line full-text audit.

Introduction, Discussion, Conclusion and Abstract synthesize the four separately implemented studies. They introduce no unified implementation, algorithmic dependency, cross-task numerical average or additional experimental result. The newly quoted headline results in the actual abstract/introduction were independently checked against their original table columns and backbones. Personal leadership/collaborator wording and dates are author-confirmed; unconfirmed signature details remain blank.

## Independent round-two verification — 2026-10-25

The full review and dispositions are in `review-round2/REVIEW_SUMMARY.md`. All47 original displayed equation/align blocks remain byte-identical and the22 external result-table files preserve their ordered numeric token streams (`review-round2/invariance-check.json`). The27 original graphic hashes were checked again. These invariance checks supplement, rather than replace, the1,765-entry source audits above.

New checks corrected the KGLink candidate-type cap (up to three per row from each column's KG entities); omitted the source's unitless9.70 selected-class average; corrected GORAG's model role to label-description generation and classification; removed unsupported AGRAG pseudo-node lifecycle wording; and restored MGRAG Algorithm1's query-anchor/evidence-counterpart loop from publisher p2485. MGRAG search failure is explicitly algorithmic, not a certificate that no valid match exists. Its listed module times do not sum to the reported total; no residual component was invented.

The new Discussion Table7.2's model, local hardware, supervision, evidence state and outcomes were checked separately against all four controlling studies; GPT-4o service use is distinguished from the local GPU setup. Assessment-rule differences are explicit. This table is not a new experiment and is outside the adopted-result entry count above.

**Formatting override:** earlier chapter ledgers describe source numeric emphasis at their initial checkpoints. Round2 removes149 numerical bold/underline marks from `agrag-efficiency.tex`, `agrag-ablation.tex`, and `mgrag-matching.tex` because inherited markings disagree with the literal ranks. Method-name emphasis and every measurement/unit/missing marker remain; no new rank was imposed. Other original tables are unchanged. Generator formatting was synchronized without regenerating result tables. See `review-round2/rank-emphasis-changes.json`.
