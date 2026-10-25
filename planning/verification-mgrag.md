# MGRAG chapter verification ledger

Audit date: **2026-10-24**. Chapter: `chapter/ch06-mgrag.tex`. Auditor: MGRAG chapter/template agent. This ledger distinguishes publication correspondence from experiment reproduction and independent mathematical proof verification. The main agent owns the integrated thesis build and final PDF/style checks.

## 1. Source identity and authority

The controlling research source is the publisher PDF, **Yubo Wang, Haoyang Li, and Lei Chen, “MGRAG: Semantic Subgraph Matching and Graph-Aware Caching for Multimodal Retrieval-Augmented Generation,” Proceedings of the VLDB Endowment 19(9), 2480–2493, 2026, DOI 10.14778/3819518.3819565**.

- Publisher URL: https://www.vldb.org/pvldb/vol19/p2480-wang.pdf
- Local publisher copy: `planning/published/mgrag-pvldb-2026.pdf`.
- Publisher PDF SHA-256: `523ea970332fc8826037fa8e2966bf896e12d69f03ab8367a3d61bc6501f4a16`.
- Selected source root: `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/VLDB_MGRAG/pvldbstyle-master/anyrag_vldb26.tex`.
- Root SHA-256: `db7503428adf2ecfa76830fe219436301c4fd46fcc2b1b8c01381eace5985f4a`.
- Active research inputs: `section/introduction.tex`, `section/related_work.tex`, `section/method.tex`, `section/experiment.tex`. The source root's acknowledgment and bibliography are not research-method inputs.
- Comment-stripped reading copy: `planning/extracted/mgrag-active.tex.txt`. The original files, not this approximate parser, determine which material is active. Several original files contain historical tables, proofs, and algorithms inside `comment` blocks; those alternatives were not imported.
- Publisher text extraction: `planning/extracted/mgrag-published.txt`.

Supporting sources were retrieved from the public artifact repository. `planning/mgrag-source-manifest.json` records full hashes for the publisher PDF, technical report, repository tree, and inspected code snapshots. The repository tree SHA is `7fc670cd0ccd0d61f845bbfd8b062f7d0a31db70`; it identifies the inspected snapshot rather than proving which revision generated the published experiments.

| Supporting material | Local file | Use and boundary |
|---|---|---|
| Technical report linked by the paper | `planning/mgrag-tech_report.pdf`, text `planning/mgrag-tech-report.txt` | Inspect proof wording, graph-size discussion, and whether the recomputation budget is reported. Its stronger approximation language does not override the publisher theorem statement. |
| Main released implementation | `planning/mgrag-MMRAG.py` | Inspect configurable matching/cache behavior; no execution or equivalence claim. |
| Command-line interface | `planning/mgrag-run.py` | Locate the cache recomputation default. |
| Cache configuration | `planning/mgrag-cache-lmcache_config.py` | Inspect the 0.15 default and argument/environment mapping. |
| Model-specific automatic configuration | `planning/mgrag-cache-lmcache_model_config.py` | Establish that several recomputation ratios can be selected, so a single code default is insufficient to identify the published run. |

The chapter's opening attribution names the published paper. `bibliography/mgrag.bib` supplies the chapter-specific citation keys; shared bibliography deduplication and the authoritative merged file belong to the main agent. Personal contribution wording is not inferred from the publication's author order.

## 2. Research-question and chapter coverage

| Chapter section / label | Technical content | Publisher location | Check |
|---|---|---|---|
| `sec:mgrag:problem`, `sec:mgrag:overview` | Multimodal evidence, query-aware graph construction, semantic path correspondence, graph-guided context computation | pp.2480–2484, Figures 1–2 | Read and matched. Chapter connects the research questions without asserting implementation inheritance from AGRAG. |
| `sec:mgrag:ranking` | Caption-based coarse ranking, bge-base-en-v1.5, 256-token text chunks, 32-token overlap, averaged mixed query embedding, Euclidean distance | pp.2483–2484, §3.2, equations (3)–(5) | Operations and reported sizes matched; no direct joint visual embedding is substituted for the caption encoder. |
| `sec:mgrag:construction` | Query graph, typed placeholders, query-conditioned extraction, passage nodes and `consists_in`, incremental chunk consumption | pp.2484–2485, §3.3, equations (6)–(9), Figure 3 | Matched; explicit iteration-prefix notation is a presentation clarification of the published incremental procedure. |
| `sec:mgrag:matching` | Entity mapping, path-level objective, entity/path thresholds, anchor selection, similarity-modified VF2, greedy extension, final edge-wise validation | pp.2485–2486, Definition 2, Algorithms 1–2, equations (10)–(13) | Matched at method/condition level. Condensed algorithm is a restatement of the published procedure, not a replacement algorithm or implementation claim. |
| `sec:mgrag:cache` | Layer-wise top-b% selective KV recomputation, reuse from construction, fixed-size LRU storage, four graph features, attention terms | pp.2483 and 2486–2487, Definition 1, §3.4, equation (14), Figure 4 | Matched; recomputation and replacement/eviction are distinguished. No cross-query graph-memory contribution is invented. |
| `sec:mgrag:complexity` | Published offline and online bounds and measured-small-graph condition | p.2487, §3.5 | Expressions copied semantically; no polynomial worst-case claim. |
| `sec:mgrag:protocol` | Seven datasets, backbone, hardware, metrics and baseline implementation choices | pp.2488–2489, §4.1 | Matched; caption's “7 MRAMG sub dataset” wording is resolved through the actual dataset paragraph and columns. |
| `sec:mgrag:results` | Full-system quality, construction/matching substitutions, query-hop results | pp.2489–2490, Tables 4, 7–8 | Numerical rows checked as described below. |
| `sec:mgrag:cost-results` | TTFT, hours, module time/token pairs, construction bottleneck | p.2489, Tables 5–6 | Every imported numeric row matched. Lowest TTFT remains CacheBlend(V.), not MGRAG. |
| `sec:mgrag:ablations` | Forward ablations, inverse ablations, matching threshold/path-length sensitivity | pp.2490–2491, Tables 9–10, Figure 5 | Preserved the cache evidence as well as construction/matching evidence. |
| `sec:mgrag:discussion` | Interpretation and material conditions | Synthesis of the above | New explanatory prose, with no new experiment, derived aggregate result, or claim of universal reasoning improvement. |

The query/film example in the chapter is taken from original Figure 3. It describes the illustrated actor, film, poster action, and release-year relations; it is not represented as an additional evaluated case or independently sourced film-history claim.

## 3. Formula and algorithm ledger

“Matched” below means correspondence to the publisher method and notation after explicit local renaming. It does not mean numerical rerunning of a model or independent validation of the paper's complete proofs.

| Thesis label / operation | Publisher source | Check and interpretation |
|---|---|---|
| `eq:mgrag:query-embedding` | Equation (3), pp.2483–2484 | Arithmetic mean of text-query and image-caption representations retained. Single-modality behavior described in prose. |
| `eq:mgrag:distance` and ascending ranking | Equations (4)–(5), pp.2483–2484 | Euclidean distance and ascending ordering retained. The ordered collection is described as a ranked list rather than changing the metric. |
| `eq:mgrag:extraction` | Equation (6), p.2484 | LLM receives chunk, query, extraction prompt; produces entity/relation sets. |
| `eq:mgrag:graph-union` | Equation (7) and iterative prose, p.2484 | Chapter explicitly indexes the consumed prefix of chunks by iteration. Original source-to-entity pseudo-relation name/direction retained. No full-corpus union is implied at every iteration. |
| Entity/relation text embeddings | Equation (8), p.2484 | Described in prose; embeddings are not presented as new visual encodings. |
| `eq:mgrag:path-embedding` | Equation (9), p.2484 | Relation embeddings aggregated along a path; mean pooling is an allowed example in the paper. |
| `eq:mgrag:matching-objective` | Equation (10), p.2485 | Sum of best path similarities over query edges retained. Query entity mapping is explicit. |
| `eq:mgrag:matching-constraints` | Constraints below equation (10), p.2485 | Strict `> theta` tests for entity alignment and each supporting relation/path retained. Failure returns empty. |
| `alg:mgrag:matching` | Algorithm 1, p.2485; explanatory prose pp.2485–2486 | Validates each query edge, rejects a failed candidate, unions accepted path nodes/edges, normalizes by query-edge count, selects the highest-scoring valid result. Anchor retries and path cap are explained in adjoining prose. |
| `eq:mgrag:greedy-score` and path concatenation | Equation (11), equation (12), Algorithm 2, p.2486 | Candidate extension jointly aggregates current path, candidate edge, and endpoint embedding. Target reachability and threshold conditions retained. No claim that greedy failure proves infeasibility. |
| Serialization with `[SEP]` | Equation (13), p.2486 | Selected triples plus original consumed chunks and query enter generation. |
| `eq:mgrag:node-feature` | Inline f(u) definition, p.2487 | Arithmetic mean of degree, betweenness, eigenvector, closeness scores retained. Individual centrality equations are not redefined in the chapter. |
| `eq:mgrag:token-feature` | Inline GF definition, p.2487 | Mean of two endpoint feature scores for the associated fact retained. |
| `eq:mgrag:cache-score` | Equation (14), p.2487 | Attention-to-query sum + attention-to-graph sum + graph feature, with no extra learned coefficient or normalization invented. |
| Per-layer recompute rule | Equation (2), p.2483; §3.4 | Recompute top b% by score; reuse remaining cached states. b is symbolic because a fixed experimental budget was not established. |
| Offline bound and `eq:mgrag:complexity` | §3.5, p.2487 | Offline O(|C| d_emb l_c²); online terms retain embedding, exponential mapping, graph, and model-context costs. Bound is reported as published, not derived anew. |
| NP-hardness | Theorem 1 and proof sketch, p.2485; report appendix A.1 | Chapter attributes the published result and its restricted-instance sketch. Full proof correctness has not been independently established by this audit; no new proof is supplied. |
| Threshold quality | Theorem 2, p.2486 | Only the publisher's conditional local similarity guarantee is used. Under strict acceptance every supported query edge exceeds theta, hence so does their average when defined. No unconditional feasibility guarantee or global polynomial approximation result is claimed. |

### Mathematical/source conflicts that remain explicit

1. **Approximation wording is inconsistent across versions and within the publisher text.** Original `section/method.tex:840–849` calls Theorem 2 an approximation-ratio bound; the linked technical report appendix A.2 also argues for a theta approximation. The publisher's actual Theorem 2 on p.2486 states a **theta-bounded quality guarantee**, specifying edge cosine similarity at least theta conditional on a valid matched subgraph. Its surrounding introductory/proof-sketch sentences still use approximation language. The chapter follows the explicit publisher theorem statement. This is a source discrepancy, not a new stronger theorem established by the thesis.
2. **Greedy feasibility is conditional.** A locally selected path can reach a dead end while a different path would succeed. The chapter states that failure of greedy search does not establish absence of a valid path; the threshold guarantee applies to returned valid matches. It does not claim completeness.
3. **Path representations have two expressions in the method.** Equation (9) aggregates relation embeddings, while equation (11)/Algorithm 2 evaluates an extension containing path, candidate edge, and endpoint. The chapter describes both at their respective stages rather than silently replacing one with the other. A unified implementation-level specification would require an author-confirmed experiment revision.
4. **Betweenness notation is not silently standardized.** The publisher describes P(x,y) as all paths in its betweenness discussion. Standard betweenness often uses shortest paths. The chapter names and describes the feature but does not substitute a new centrality equation. This audit did not execute or establish the exact centrality implementation used for the reported runs.
5. **Induced-subgraph language is imprecise in the source.** Original prose calls matches induced over mapped endpoints, while Algorithms 1–2 also add intermediate path nodes/edges. The chapter describes the union of accepted paths, matching the actual algorithmic assembly, without asserting endpoint-only induced-subgraph equivalence.

## 4. Numerical evidence and tables

All imported numbers originate in publisher Tables 3–10. The active TeX table bodies were extracted, and the scalar/missing-mark sequences in **92 source data rows** were compared with isolated publisher-PDF table crops. The automated row match checks **753 numeric or missing-mark tokens**; range endpoints and repeated measurements count as tokens, so 753 is not a claim of 753 independent observations. Every row is `PASS` in `planning/mgrag-cell-verification.json`.

The comparison program is `planning/mgrag-verify-tables.py`; source-to-thesis table generation is `planning/mgrag-build-tables.py`. The latter preserves source formatting semantics, replacing `uline` by `underline` where appropriate. For wide matching and hop tables, explicit transposition/splitting retains all source values, not an estimated subset. `planning/mgrag-table-cells.json` retains the full-system and matching matrices for inspection.

| Publisher table / page | Source TeX location | Thesis file / label | Verified numeric/missing tokens | Fidelity and conditions |
|---|---|---|---:|---|
| 3 / 2488 | `section/experiment.tex:104–127`, `tab:dataset_statistic` | `chapter/tables/mgrag-datasets.tex`, `tab:mgrag:datasets` | 49 | All seven dataset columns, counts, corpus-size abbreviations, query-hop ranges and averages preserved. T/I modality row also inspected. |
| 4 / 2489 | `section/experiment.tex:205–268`, active `tab:main_exp` | `chapter/tables/mgrag-main.tex`, `tab:mgrag:main` | 168 | All seven datasets × four metrics × six methods retained. MMQA GraphRAG/LightRAG dashes retain the >3-day meaning. Four decimal places retained. |
| 5 / 2489 | `section/experiment.tex:377–399`, `tab:efficiency_MGRAG` | `chapter/tables/mgrag-breakdown.tex`, `tab:mgrag:breakdown` | 56 | Query counts, time/token pairs, match times and E2E values retained. No totals recalculated. Publisher caption explicitly states minutes for KGC; chapter reads the time entries using that table-level convention. |
| 6 / 2489 | `section/experiment.tex:401–425`, `tab:system_comp` | `chapter/tables/mgrag-cache.tex`, `tab:mgrag:cache` | 30 | All five system rows, four quality metrics, seconds TTFT, hours total time retained. V/H identify different retrieval frameworks. |
| 7 / 2490 | `section/experiment.tex:433–490`, `tab:gm_experiment` | `chapter/tables/mgrag-matching.tex`, `tab:mgrag:matching` | 336 | Seven datasets × four metrics × twelve variants retained. Transposed into dataset/method rows with four metric columns for readability. Three-decimal precision and original highlights retained. |
| 8 / 2490 | `section/experiment.tex:595–617`, `tab:hop_performance` | `chapter/tables/mgrag-hops.tex`, `tab:mgrag:hops` | 54 | Six original hop rows and both methods' eight outputs retained; query count repeated when each original row becomes two method rows. Time remains minutes. |
| 9 / 2490 | `section/experiment.tex:620–641`, `tab:abl_exp` | `chapter/tables/mgrag-ablation.tex`, `tab:mgrag:ablation` | 20 | Four variants, all metrics, hours retained. Variant labels expanded for readability without changing the tested components. |
| 10 / 2491 | `section/experiment.tex:651–677`, `tab:inv_abl` | `chapter/tables/mgrag-inverse.tex`, `tab:mgrag:inverse` | 40 | All eight rows retained, including repeated full-MGRAG configuration. PSGM/GKV combinations and hours preserved. |

### Checked principal statements

- **Dataset scope:** MMQA plus six MRAMG subsets = seven datasets, from §4.1.1 and actual Table 3 columns. The caption's “7 sub dataset of MRAMG” is inconsistent and was not copied into thesis prose. Author instruction is to follow the paper's main text.
- **Backbone/hardware:** Qwen2.5-VL-7B-Instruct; Intel Xeon Gold 5220R at 2.20 GHz; one A100-SXM4-40GB; text chunk 256, overlap 32; retrieval amount five. Publisher §4.1 pp.2488–2489. The source sometimes swaps the placement of “VL” in the model name; the canonical identifier is used in the chapter.
- **MMQA quality:** MGRAG ACC 0.7442 vs VanillaRAG 0.7053 and HippoRAG2 0.6335, from Table 4. No percentage-point/relative-percent conversion was needed.
- **Cross-dataset quality:** MGRAG has the largest published value in every Table 4 row; no missing GraphRAG/LightRAG MMQA entry is treated as zero. Smaller Wiki differences are reported directly.
- **Matching comparison:** Exact/approximate/semantic substitutions come from Table 7; the table actually contains nine matching baselines plus two construction baselines even though its caption says five matching baselines. Chapter lists the actual columns.
- **Hop comparison:** ACC 0.613→0.624 for one-hop and 0.661→0.738 for six-hop; VanillaRAG remains faster in every listed hop group. Query-group sizes are retained.
- **TTFT:** CacheBlend(V.) 3.1 s is the smallest entry; MGRAG 3.2 s ties vLLM(V.). The chapter does not repeat the publication's broad prose claim of superiority on every efficiency metric.
- **Cache-system totals:** MGRAG 4.3 h vs Table 6's vLLM(H.) 8.8 h and CacheBlend(H.) 8.3 h. This is a comparison of complete retrieval/cache compositions, not an isolated causal estimate of the graph feature.
- **Module bottleneck:** KGC is the largest listed time component in each Table 5 row. MMQA KGC 193.0, Match 0.14, QA 8.9, E2E 248.1 retained. Recipe 525.7/1.74/191.3/808.7 retained.
- **Inverse ablation:** Hippo.+PSGM 0.7372 / 4.1 h and Hippo.+PSGM+GKV 0.7442 / 4.3 h retained. Adding recomputation improves the reported quality while increasing this configuration's time. Vanilla additions also increase time. No universal cache speedup is inferred.
- **Sensitivity:** theta 0.6 and maximum path length 3 are the published sensitivity discussion's preferred settings. Curves are reproduced, not digitized into new numeric tables.

### Numerical/reporting qualifications

- Table 5 E2E times need not equal the sum of listed module times; chapter preserves separately measured totals. Some reported token totals differ by one from the displayed component sums (e.g. Web 4,623 + 3,101 vs 7,723; Recipe 4,351 + 3,173 vs 7,525). These values are retained literally. No source number is “corrected” through arithmetic.
- Table 6 reports vLLM(H.) at 8.8 h, whereas Table 10's Hippo. baseline is 7.5 h. The publication does not fully reconcile these table-specific timings. The chapter keeps each in its own comparison and does not derive a cross-table speedup.
- Time units in Table 8 are minutes. Its timing aggregation is not further specified in the caption; chapter retains the values without converting them into a new per-query statistic.
- Table 5 caption explicitly places “in minutes” after KGC time. The chapter uses minutes for that table's time entries. If the author intended different units for Match/QA/E2E, that requires author clarification; no conversion was performed.
- No new uncertainty estimates, significance markers, experimental results, human-evaluation results, or inferred curve values were added. Commented `tab:human_eval` and historical/commented results are excluded.

## 5. Original-figure ledger

Every asset below was copied byte-for-byte from the selected source directory. Full absolute origin paths and full SHA-256 values are in `planning/mgrag-assets.json`. Publisher pages were rendered and visually compared with the chapter figures. Adjustments are limited to LaTeX width, placement, and thesis captions.

| Publisher figure / page | Thesis label | Copied file | SHA-256 |
|---|---|---|---|
| 1 / 2481 | `fig:mgrag:motivation` | `figures/mgrag/motivation.pdf` | `f8a3ff8c98c879a675535edd763f2543c221bfaad7bd44571268ae7d545edc28` |
| 2 / 2484 | `fig:mgrag:pipeline` | `figures/mgrag/pipeline_new.pdf` | `71ecdb7b516429517ecfee00ca890072f03bc02a43c0b18bd32ae63866a3c54b` |
| 3 / 2485 | `fig:mgrag:query-graph` | `figures/mgrag/query_graph.pdf` | `0f97a6724733ef2750a0362912c5c9dda6868206a97ef8b8a07b31dc746466c8` |
| 4 / 2487 | `fig:mgrag:cache` | `figures/mgrag/graph_based_cache.pdf` | `dc9b9478d8c1e3e85b6b09df00f6912b8772c481fc1d2d225fabbd559635fc21` |
| 5a / 2491 | `fig:mgrag:sensitivity` subfigure | `figures/mgrag/acc_vs_theta_fixed_lp.pdf` | `4175f44107be766e5c43ad64f85c3a0a737a340c738e8c244926e3cefee78bb7` |
| 5b / 2491 | `fig:mgrag:sensitivity` subfigure | `figures/mgrag/acc_vs_lp_fixed_theta.pdf` | `89944f51e523fadfc4f2a44e1736c531aca6f394a76f9aead62929dad6f1348e` |

The source and publisher Figure 4 caption uses “event-agnostic” despite describing the graph-aware mechanism. The thesis caption states the actual graph-feature operation directly and leaves the original image unchanged. The original parameter plots contain embedded Type 3 fonts without Unicode mapping. They were preserved rather than redrawn; final PDF/preflight checks should account for these original source fonts.

## 6. Reproduction parameters and unresolved items

### KV recomputation budget: NOT_REPORTED as a fixed published experiment setting

The paper describes top-b% recomputation in Definition 1 and §3.4. A fixed numerical b for the experiment tables was not found in the publisher PDF or inspected technical-report text. The released `planning/mgrag-run.py:60` has `blend_recompute_ratio` default **0.15**, and `planning/mgrag-cache-lmcache_config.py:50,126` also has 0.15. However, `planning/mgrag-MMRAG.py:118` can take a ratio from `auto_hyperparams`, and `planning/mgrag-cache-lmcache_model_config.py:96,104,112,120` contains **0.10, 0.15, 0.20, 0.25** choices. The snapshot therefore supplies configurable values, not the published run configuration. The chapter keeps b symbolic and identifies this missing reporting detail once in its interpretation. Author-confirmed logs/configuration would be required to resolve it.

### Other boundaries

- Formal source comparison is complete for the material adopted into this chapter. No new experiments were run, and paper results were not computationally reproduced.
- The linked technical report was read for the inspected claims, but its additional experiments were not imported. Its complete proof correctness was not independently established.
- Code was inspected only for parameters and source discrepancies; there is no claim of full code-to-paper behavioral equivalence.
- The source root has old VLDB metadata placeholders (`14`, `1`, `2020`, `XXX`); bibliography metadata is taken from the publisher PDF instead.
- `bibliography/mgrag.bib` initially inherited an undated Contriever/TMLR entry from the paper's BibTeX. The publisher references also show `[n.d.]`. A secondary index suggests 2022, but the official OpenReview page/PDF returned a browser verification page during this run. The chapter agent did not invent a year. Main bibliography deduplication may supply an independently verified canonical entry.
- nano-graphrag's primary repository was checked; its reference title was normalized to the actual project name/description, with access date 2026-10-24, without guessing an individual author.

## 7. Chapter build, word count, and visual checks

At the chapter agent's last successful local build, `planning/mgrag-chapter-smoke.tex` produced `planning/qa/mgrag-chapter-smoke.pdf`, **29 physical pages: 27 chapter pages and 2 bibliography pages**. This is an isolated test, not the final integrated thesis pagination.

Build command, from the thesis root:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -latexoption=-no-shell-escape -outdir=planning/qa planning/mgrag-chapter-smoke.tex
```

Biber was also run explicitly when citation/page trackers required another convergence pass:

```sh
biber --input-directory=planning/qa --output-directory=planning/qa mgrag-chapter-smoke
```

The final inspected standalone log had no undefined citation/reference, duplicate label, missing asset, or overfull-box diagnostic. Remaining messages were the vendor class-name/path warning, its inherited unused `UTF8` option, and its siunitx/physics notice. The bibliography uses a local sloppy paragraph setting in the standalone test to accommodate long source titles/URLs; the current shared main also has a bibliography wrapping setting.

Word count command:

```sh
texcount -utf8 -sum chapter/ch06-mgrag.tex
```

At handoff: **6,100 prose words**, **116 heading words**, **116 caption/outside-text words** in the chapter file, with table captions in separate inputs. The TeXcount “sum” includes additional equation weights and is not reported as the prose total. Saved output is `planning/mgrag-wordcount.txt`. The main agent should regenerate integrated counts after any edits.

All standalone pages were rendered for contact-sheet inspection; data-table pages and final pages were additionally rendered at 90 dpi. Original research figures were compared with publisher Figure pages 2481, 2484, 2485, 2487, and 2491. No clipping, missing glyph, table overflow, or altered experimental graphic was found. The long matching table repeats its column header across pages and explicitly repeats dataset names, preserving row interpretation during pagination. The full thesis's final float placement, front matter, TOC, references, figure readability at 100%, and actual final-page inspection remain the main agent's integrated checks.

## 8. Defensive-writing audit of this chapter

Scope: this chapter only, following the requested skill. The edits below were applied before handoff. Necessary scientific conditions remain in the method/protocol and one consolidated discussion paragraph.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| Framework | “Caption embeddings used during ranking do not replace the images in this final multimodal context.” | D12 | Minor | MIXED | Defines the representation through a negative alternative. | Wants the actual generator input. | State retained inputs. | “The final multimodal context retains the original images alongside their extracted relational representation.” |
| Original Figure 3 case | “...used here to explain the representation rather than to introduce another evaluation case.” | D8/D9 | Minor | DEFENSIVE | Discusses authoring procedure rather than the method. | Unnecessary assurance. | Delete procedural defense. | “These facts are the content of the published illustrative example.” |
| Construction stop | “...without introducing an additional unreported recovery mechanism.” | D2/D9 | Minor | DEFENSIVE | Explains what the writer did not add. | Interrupts algorithm reading. | Give the actual failure result. | “The matcher returns an empty result when no valid correspondence exists in its current graph.” |
| Cache comparisons | “...which is more informative than measuring token reuse alone.” | D10 | Minor | DEFENSIVE | Self-evaluates the evidence presentation. | Prefers the measurements. | Remove evaluative clause. | “These comparisons expose answer-quality and time changes under several compositions of retrieval and caching.” |
| Protocol | “...do not add confidence intervals or significance markers that were not reported.” | D2 | Minor | MIXED | Reports the writer's restraint. | Wants uncertainty reporting scope. | State the reported quantity. | “The publication reports point estimates for these experiments.” |
| Complete-system results | “...without treating their scales or question distributions as interchangeable.” | D12 | Minor | MIXED | Adds a negative interpretation disclaimer. | Repeats dataset-specific scope. | State variation. | “The reported gains vary with the dataset and metric.” |
| Construction substitutions | “They do not determine a universal ranking of extraction methods...” | D2/D12 | Minor | MIXED | Defends against an unproposed universal claim. | Would prefer concrete conditions. | State the evaluated setting. | “The evaluated extraction setting uses multimodal evidence and query-specific graphs.” |
| Cache timing | “...but it does not have the smallest TTFT entry.” | D12 | Minor | NECESSARY_CAVEAT | The result is material but can be positive. | Needs the actual fastest configuration. | Name it. | “MGRAG combines the highest answer-quality values with a total time of 4.3 hours; CacheBlend with VanillaRAG has the shortest TTFT.” |
| Hop results | “No synthetic cross-dataset average is needed to express that result.” | D9 | Minor | DEFENSIVE | Explains an unperformed analysis. | Adds no evidence. | State what the table retains. | “The hop-specific values retain the measured trade-off for each question group.” |

### Chapter-level defensive-writing score

**1/10** after these edits. This is not a score for the complete thesis and not a judgment of novelty or acceptance likelihood.

### Highest-priority removals

Applied: procedural non-claims about figures/recovery, universal-ranking disclaimers, self-evaluation of comparisons, repeated interpretation boundaries, and unmeasured causal explanations copied from the source discussion. The publication's claim of dominance on all efficiency metrics was replaced by the actual TTFT and total-time entries.

### Necessary caveats preserved

Caption-based ranking; original multimodal generator inputs; query-extraction dependence; valid-match condition for the threshold result; greedy search's possible failure; exponential mapping term; fixed backbone/hardware; table-specific time units and missing markers; symbolic/unreported fixed cache budget; host-pipeline dependence of inverse-ablation timing.

### Repeated phrase audit

`planning/mgrag-style-counts.json` excludes citation keys, labels, file paths, and math before counting prose. Counts are zero for “We emphasize that”, “It should be noted”, “For a fair comparison”, “We do not claim”, “Taken together”, “Together, these”, “promising”, “robust”, “comprehensive”, “preliminary”, and “within the evaluated scope”. Four prose colons remain, primarily inside formal publication names/definitions; no prose em dash was found. Source/BibTeX labels containing “robust” are not prose findings.

## 9. Direct next checks for the main agent

1. Rebuild the explicit full `main.tex` with the merged bibliography and final chapter contents; regenerate word/page counts from that build.
2. Inspect the actual integrated Figure 6.x/table pages at 100%, particularly the original pipeline's small labels and the long matching table's repeated headers.
3. Keep the local theorem statement and symbolic cache budget until author-confirmed experimental metadata resolves them; do not strengthen the theorem from report prose.
4. Preserve table-specific times and token totals literally; do not reconcile Table 6/Table 10 timings or displayed sums by overwriting published values.
5. Complete shared bibliography canonicalization/metadata checking and final PDF preflight. This chapter ledger does not certify the whole thesis or the unreported experiment configuration.

## Main integration resolution — 2026-10-24

The bibliography corrections flagged above have been applied. Primary evidence and exact corrections are in `planning/bibliography-primary-corrections.md`; Contriever’s author-linked arXiv v4 PDF explicitly confirms TMLR 08/2022 and all seven authors. Transformer and BM25 author records are corrected; HyperFormer DOI is supplied. Integrated pagination and final visual findings are recorded separately in `planning/FINAL_QA.md`; historical chapter counts remain checkpoint counts.


## Independent round-two integration — 2026-10-25

Publisher p2485 Algorithm1 was rechecked (`review-round2/mgrag-p2485.txt`). The thesis pseudocode now supplies query anchor gamma, iterates eligible evidence counterparts v_a, constrains mappings by I(gamma)=v_a, validates query edges and aggregates accepted results. The renaming avoids shadowing the edge endpoint v. Adjacent query-anchor retry prose remains. This restores the reported outer loop; it does not add a new search protocol. Empty output now means the search found no valid correspondence, preserving the disclosed greedy incompleteness. All12 displayed math blocks are unchanged. Numeric emphasis was removed from `chapter/tables/mgrag-matching.tex` (59 marks), overriding historical source-emphasis preservation while retaining every value. Listed MMQA module times are explicitly non-additive to the reported total; no reconciliation was invented. Cache quality/time results and symbolic b remain. Reviewer accepted the integrated source/protocol corrections.

Current PDF/counts and visual findings are in `FINAL_QA.md`; prior chapter audit counts remain historical. Full dispositions: `review-round2/REVIEW_SUMMARY.md`. No new experiment was run.
