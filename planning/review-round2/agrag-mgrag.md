# Round 2 independent review: AGRAG and MGRAG

Review date: 2026-10-25. Scope: read-only review of the complete current Chapters 5 and 6, every table they input, and the common framing in Chapters 1, 7, and 8. This reviewer edited only this report. The recommendations below leave all data, formulas, evaluation protocols, and algorithmic claims under their selected source authority.

## Result and priorities

No numerical transcription mismatch or backbone/hardware/metric-setting mismatch was found in the included AGRAG and MGRAG tables and quoted results. Two local wording changes would improve method fidelity. A third optional change would make the condensed MGRAG algorithm less ambiguous. Source-inherited highlighting errors and source-internal mathematical inconsistencies are separate from numerical transcription errors.

### R2-AM-1 — Avoid assigning the AGRAG pseudo node to an unconfirmed lifecycle stage (P2, small fidelity fix)

- Thesis: `chapter/ch05-agrag.tex:74`: “The pseudo connection is an indexing device”.
- Evidence: selected `planning/published/agrag-local-complete.pdf`, physical p.5, §III-C, places the paragraph beginning “Moreover, to guarantee the KG's connectivity” after PPR scores and semantic edge costs have been described. The corresponding active `section/sec-method_sigmod.tex` paragraph also follows `eq:edge_weigting` and precedes the MCMI definition. The source assigns pseudo-edge cost 10; it does not establish the thesis's characterization as an indexing-stage operation.
- Why it matters: the preceding thesis subsections separate corpus indexing from query-time propagation. “Indexing device” can imply that the pseudo node already participates in the graph on which all query scores are propagated, although the source's presentation does not resolve that ordering.
- Proposed fix: replace only “indexing device” with “connectivity device”. Preserve pseudo-edge cost 10, the sum objective, and the reported graph operator. Do not infer an implementation order or alter the propagation graph.

### R2-AM-2 — State greedy failure in terms of the search outcome (P2, small precision fix)

- Thesis: `chapter/ch06-mgrag.tex:120`: “The matcher returns an empty result when no valid correspondence exists in its current graph.”
- Evidence: publisher PDF `planning/published/mgrag-pvldb-2026.pdf`, p.2486, Algorithm 2 selects one locally highest-scoring qualifying extension and returns failure if the path cannot proceed. Algorithm 1 returns empty when its result set is empty. These are search outcomes; they are not an exhaustive infeasibility certificate. The current thesis correctly explains this at line 201.
- Why it matters: line 120 can be read as equating empty output with absence of a valid correspondence, while a greedy search can miss a valid path.
- Proposed fix: “The matcher returns an empty result when its search finds no valid correspondence in the current graph.” No algorithm, recovery rule, or new guarantee is needed.

### R2-AM-3 — Optionally restore the publisher algorithm's anchor-counterpart loop (P3, exposition fidelity)

- Thesis: `chapter/ch06-mgrag.tex:169–187`, especially line 171: “Select an anchor correspondence and enumerate candidate mappings”. Adjacent prose at line 159 describes highest-similarity anchor selection and trying another anchor when necessary.
- Evidence: publisher PDF p.2485 Algorithm 1 accepts a query anchor gamma and has an explicit outer loop over every evidence node v whose cosine similarity to gamma exceeds theta. For each v it enumerates mappings; the result set aggregates accepted candidates before returning the highest score. The adjoining source prose also discusses retrying query anchors. The active local TeX is less complete here, so the publisher PDF controls.
- Assessment: the thesis is explicitly condensed, so this is not evidence that it implements a different method. Its singular “anchor correspondence” nevertheless hides a source loop that can change which mappings are examined.
- Proposed fix if expanding the pseudocode: select query anchor gamma, iterate over evidence counterparts v satisfying the semantic threshold, enumerate mappings consistent with I(gamma)=v, and retain the existing validation/result steps. Keep query-anchor retry behavior in the prose. Do not invent backtracking, completeness, a final full-path threshold repair, or an additional failure fallback.

### R2-AM-4 — Source-inherited highlighting can misstate rankings (P3, presentation only)

The values match the controlling PDFs, but some copied bold/underline marks do not agree with numerical ordering. Examples:

- `chapter/tables/agrag-efficiency.tex:13–15`: IFS-Rel querying time 121 is bold, although SiReRAG is 117; WOS querying time 158 is underlined, although 140 is lower and full AGRAG is 132.
- `chapter/tables/agrag-ablation.tex:11–14`: Novel creative ACC 0.322 is underlined alongside 0.332; Novel COV underlines 0.365 although hybrid-only gives 0.378.
- `chapter/tables/agrag-ablation.tex:33–34`: Novel summarization ACC underlines 0.592 although the no-filter variant gives 0.597.
- `chapter/tables/mgrag-matching.tex:42–43`: Manual ROG underlines SM 0.378 although ISMAGS is 0.382; lines 57–58 underline Web RRWM ROG 0.157 although VJ is 0.160.

These errors are inherited, and the captions explicitly say source highlighting is retained. They are not transcription errors. A permissible editorial option is to remove rank highlighting from the affected tables and describe the values directly, or recompute highlighting consistently and identify it as thesis highlighting. Never change the values to make the marks correct. If exact source emphasis is intentionally retained, no further defensive explanation is needed.

## Independent source checks and coverage

Source selection was checked against `planning/source_roots.json` and `planning/SOURCE_MAP.md`. Active AGRAG entry is `ICDE2026.tex` with `sec-*_sigmod.tex` inputs. Active MGRAG entry is `anyrag_vldb26.tex` with `section/{introduction,related_work,method,experiment}.tex`. Commented historical variants were distinguished from active material. The selected PDFs, rather than stronger historical/local-source statements, control the findings.

| Area | Independent comparison | Outcome |
|---|---|---|
| AGRAG construction | Selected PDF pp.4–5; modified TF–IDF expression, strict extraction threshold, relation extraction, passage and synonym links | Source expression retained. b=3, tau=0.5; no rescaling or alternative extraction invented. Synonym threshold stays symbolic. |
| AGRAG influence | PDF p.5 equations (10)–(14), source active method | Recurrence, binary personalization interpretation, specified nonedge entries, damping 0.5, stopping tolerance 10^-7, passage scaling 0.05, similarity edge cost retained. |
| AGRAG connected selection | PDF pp.5–6 Definition 1, equations (15)–(18), Algorithm 3, detailed Theorem 2 | Sum of per-edge c/(s_u+s_v) retained. Candidate c/s and acceptance condition retained separately. Initial terminal-connecting stage receives the 2-approximation attribution; expansion receives no invented global approximation or monotonic-decrease claim. |
| AGRAG passage channel | PDF p.6 equations (20)–(22) | Dense/BM25 average, k_r=5, and graph-plus-hybrid inputs match. No score normalization added. |
| AGRAG task protocol | PDF pp.7–8 main settings, task descriptions and metrics | Novel/Medical GraphRAG-bench tasks and counts match. WOS/IFS-Rel one training passage per label and candidate-label generation match. Source dataset table's 24/11 chunk counts are retained, not silently repaired. |
| AGRAG metrics | PDF pp.7–8 | Classification ACC and macro REC separated from 0/0.5/1 model-assessed QA ACC. Generated-length denominator for ROG retained. COV and FS denominators and roles match. |
| AGRAG main settings | PDF p.8 | Qwen2.5-14B-Instruct, vLLM, Xeon Gold 5220R, one A100 80 GB; Contriever for AGRAG/HippoRAG2 dense retrieval, bge-large-en-v1.5 for other baselines, Qwen3-Reranker-0.6B filtering; chunks 256/overlap32 and k_a=k_r=5 match. |
| AGRAG main and efficiency tables | PDF Table III and IV | All eleven method rows and twenty-two main metric entries per row match the five thesis task tables. All indexing/query and input/output pairs match the thesis efficiency tables. Quoted values match their columns. |
| AGRAG ablations and low-resource setting | PDF Tables VI–VIII | Six ablation rows, all task/cost blocks, and all three low-resource method rows match. Qwen3-4B-Instruct-2507 and two 2080 Ti GPUs match. Main vs ablation cost differences remain separate. No one-variable model-size conclusion is asserted. |
| MGRAG ranking and construction | Publisher pp.2483–2485 equations (3)–(9) | Caption representations, averaged multimodal query encoding, Euclidean ranking, query-aware extraction, passage-to-entity consists_in orientation, incremental union and match/cap stopping match. Original multimodal chunks remain generator inputs. |
| MGRAG objective and matching | Publisher pp.2485–2486 equations (10)–(12), Algorithms 1–2 | Entity/path semantic conditions, relation-embedding aggregation, joint greedy extension, path union, average candidate score, greedy non-completeness match. Condensed anchor loop is the optional detail issue above. |
| MGRAG theoretical scope | Publisher p.2486 Theorem 2 | Thesis retains conditional threshold quality for an accepted match, not a global approximation guarantee. Technical-report bottleneck discussion is attributed separately. |
| MGRAG caching | Publisher pp.2483, 2486–2487 | Per-layer top-b% updates, fixed-size LRU cache, four centralities, average endpoint graph feature, two attention sums match. No new normalizer or learned coefficient. Fixed experimental b remains unknown. |
| MGRAG experimental conditions | Publisher pp.2488–2489 | Qwen2.5-VL-7B-Instruct; Xeon5220R 2.20 GHz; one A100-SXM4 40 GB; bge-base-en-v1.5 except Contriever for HippoRAG2 passage retrieval; chunk256/overlap32; reported top-k5 and selected baseline modes match. No experimental b inferred from code. |
| MGRAG metrics | Publisher p.2488 | SIM uses bge-base cosine answer similarity; ACC is reported proportion correct; ROG uses LCS comparison; BLEU names BLEU-1. Thesis does not invent the exact ACC adjudication protocol or a ROUGE denominator absent from this main paper. |
| MGRAG dataset and result tables | Publisher Tables3–10 pp.2488–2491 | Dataset statistics, all main results, all 12-method matching rows, cache, breakdown, hops, forward and inverse ablations match included tables. Original precision, dashes, seconds/minutes/hours and distinct totals retained. |
| MGRAG caching interpretation | Publisher Tables6,9,10 | MGRAG4.3h vs vLLM(H.)8.8h is a complete-composition comparison. Isolated inverse addition from Hippo.+PSGM4.1h to +GKV4.3h is correctly acknowledged as additional runtime with additional quality. CacheBlend(V.)3.1s has lower TTFT than MGRAG3.2s. |
| Common four-chapter thread | Entire ch01/ch07/ch08 | Separate evidence interfaces and model roles are maintained. No shared unified implementation, common hardware, pooled metric, common dataset or causal cross-chapter performance ranking is claimed. HyperKG remains the separate representation-level study. |

The figure references and textual examples were checked against source captions/method text. This report does not claim a fresh render-by-render graphical or thesis-layout audit.

## Source-internal issues to preserve without repair

1. The AGRAG sum objective and the operational expansion rule should remain verbatim mathematical source commitments. Adding positive-cost edges cannot be advertised as decreasing that fixed-score sum; the current chapter correctly avoids that claim. The detailed source's MCST guarantee must not become a guarantee for the whole expanded subgraph.
2. AGRAG's specified graph operator is not generally row stochastic. The chapter appropriately calls it the source's operator rather than silently normalizing it or claiming universal convergence. Do not replace its nonedge entries.
3. AGRAG Table II's one-passage-per-label protocol and 24/11 reported chunks may prompt a reproducibility question. Both are source facts; do not substitute 133/64 for the chunk counts or invent a sampling/chunk-consolidation rule.
4. MGRAG relation-only path aggregation and its joint extension representation have distinct published expressions. Do not invent one unified implementation to resolve their ambiguity.
5. MGRAG fixed experimental recomputation budget b is not established. Keep it symbolic; a released default does not identify the tables' run configuration. The numerical construction cap mu is likewise not supplied in the thesis; do not derive it from the baseline top-k statement.
6. MGRAG cache and inverse-ablation baselines have different reported total times; breakdown totals are not sums of the displayed module time entries. Current tables retain these facts. No unexplained residual should be assigned to a new invented component.

## Defensive-writing audit

The main remaining style issue is repeated evidence-boundary and source-preservation narration. It is mild, not rebuttal-like. Scientific qualifications concerning greedy failure, model-assessed metrics, host-pipeline cache comparisons, model/hardware changes and unknown b remain necessary; many adjacent sentences explaining that the thesis has preserved or separated them can be shortened.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| ch05:56 | “Equations … preserve the source formulation.” | D12 | Minor | DEFENSIVE | Editorial assurance follows an already cited formula. | Source fidelity is stated instead of explaining the method. | Delete final sentence. | End after the reported b and tau settings. |
| ch05:151 | “These expressions retain the distinct roles assigned to the candidate score and subgraph quantity in the method. This describes the paper's expansion rule separately from the initial tree construction.” | D12 | Minor | MIXED | Two assurances repeat the preceding exact comparison. | A straightforward rule sounds unusually defended. | Keep the formula distinction, delete these closing assurances. | “The candidate ratio uses s_v, whereas the subgraph objective sums c_e/(s_u+s_v).” |
| ch05:210 | “The chapter compares methods within each reported task and corpus rather than treating these query collections as interchangeable observations.” | D12 | Minor | MIXED | The chapter has already defined separate tasks and tables. | The methodology is clear; repeated non-pooling assurances add little. | Keep query counts and omit this sentence here. | “Their differing sizes and answer requirements are relevant to interpretation.” |
| ch05:240 | “The evaluation therefore reports the actual task metrics instead of deriving a common aggregate score across QA and classification.” | D12 | Minor | DEFENSIVE | Restates ch05:18 and217–219. | Slows the metric explanation. | Delete; retain technical metric definitions and the useful example at238. | No replacement. |
| ch05:263 | “AGRAG reduces indexing time in these comparisons while its query totals remain above HippoRAG2 on Novel and Medical.” | D11 | Minor | CLEAN but redundant | This repeats the same concrete result at261. | Unnecessary recap. | Delete duplicate last sentence. | Keep the discussion of different cost columns. |
| ch05:281 | “They are not averaged or substituted for one another when discussing a component intervention.” | D2/D12 | Minor | DEFENSIVE | Main/ablation measurements are already identified as separate. | Sounds like a response to an imagined objection. | Keep one positive reporting statement. | “The main and ablation tables report separate time and token measurements.” |
| ch06:61 | “Equations … retain the averaging and Euclidean-ranking operations of the published method.” | D12 | Minor | DEFENSIVE | Equations and immediately adjacent explanations already establish these operations. | Editorial verification interrupts the method. | Delete. | No replacement. |
| ch06:149 | “The objective and constraints follow the published formulation.” | D12 | Minor | DEFENSIVE | Again reassures rather than adding method content. | Repeated attribution sounds cautious. | Delete this first sentence; retain the unit of validation. | “Each query edge is validated against a supporting evidence path.” |
| ch06:226 and406 | Both identify that the tables do not give a fixed experimental b. | D7/D12 | Minor | NECESSARY_CAVEAT, repeated | Missing b materially limits reproducibility, but it need only be stated once clearly. | Repetition can obscure the actual limitation. | State once in cache subsection or end limitations; cross-reference only if necessary. | “The publication does not specify a fixed numerical b for its experimental tables.” |
| ch06:335 | “The hop-specific values retain the measured trade-off for each question group.” | D11 | Minor | DEFENSIVE | Merely repeats the preceding sentence's measured quality-cost interpretation. | Formulaic end-of-paragraph summary. | Delete. | No replacement. |
| ch06:346 | “Reporting both values preserves the contribution of the cache policy without assuming that every application of recomputation reduces total runtime.” | D2/D12 | Minor | MIXED | The direction of the numbers already shows the point. | Useful finding is buried under a non-claim. | Lead with measured trade-off. | “Adding graph-aware recomputation raises accuracy from 0.7372 to0.7442 and total time from 4.1 to 4.3 hours in this composition.” |
| ch06:350 | “The end-to-end measurement is retained separately … The original totals and their reported precision are preserved.” | D12 | Minor | MIXED | The module sum discrepancy is material; preservation/precision assurances are editorial. | Reader wants to know the totals differ, not repeated assurances about copying. | Keep one factual boundary. | “The end-to-end total is reported separately from the listed module times.” |
| ch07:86 | “The research chapters preserve the scope of the source claims … without extending a local statement to an untested global property.” | D12 | Minor | MIXED | Local guarantee scope matters, but this repeats the chapter-level theorem discussion. | Central discussion shifts toward manuscript self-defense. | Keep substantive comparison of tree guarantee vs threshold condition; remove editorial assurances. | “AGRAG's approximation statement concerns initial tree construction; MGRAG's threshold condition concerns accepted semantic matches. The experiments measure their complete pipelines.” |

### Paper-level defensive-writing score

For the reviewed AGRAG/MGRAG and relevant common framing subset: **3/10 (mild)**. This is not a score for unreviewed chapters or for the complete thesis's novelty or validity.

### Highest-priority removals

1. Remove repeated “preserve/retain the source formulation” sentences after the formulas, retaining citations and exact expressions.
2. Remove duplicate claims that distinct task metrics are not pooled; keep the metric definitions and one common-framing explanation.
3. Express the cache quality/time result positively using its numbers, retaining the host-pipeline conditions once.
4. State unknown experimental b once; do not delete it or infer a value.
5. Shorten ch07:86 to its two actual local theoretical scopes.

### Necessary caveats to preserve

- AGRAG classification vs model-assessed answer accuracy, source ROG denominator, and separate coverage/faithfulness meanings.
- AGRAG main/ablation measurements and changed low-resource backbone/hardware.
- Initial MCST-only approximation attribution; no global expanded-objective guarantee.
- MGRAG valid-match condition, greedy search's possible miss, captions before visual extraction, and original multimodal generator inputs.
- MGRAG complete-composition cache comparison vs inverse addition, 3.1s versus3.2s TTFT, and the observed added time for recomputation in inverse ablations.
- Unknown fixed experimental b and source-reported measurement units/totals.

### Repeated phrase audit

Counts below are case-insensitive word/word-family matches in the two full chapter TeX files after removing ordinary unescaped percent comments. They include captions/labels where the ordinary word appears; they are diagnostics, not automatic deletion targets.

| Construction | AGRAG | MGRAG |
|---|---:|---:|
| reported | 20 | 15 |
| published | 3 | 26 |
| source | 21 | 5 |
| preserve* | 7 | 8 |
| retain* | 18 | 12 |
| under the/these/this | 8 | 5 |
| protocol | 6 | 6 |
| rather than | 7 | 4 |
| separate* | 15 | 8 |

The two chapters remain substantively coherent. The four-chapter narrative need not be reorganized: external knowledge → online task index → connected textual evidence → query-aware multimodal matching/recomputation is consistently maintained in Chapters1,7,8.

## Integration acceptance — 2026-10-25

Reviewed the AGRAG/MGRAG entries in `planning/review-round2/applied-edits.json`, the current affected method and result passages, the expanded MGRAG algorithm, and the new Chapter 7 controls matrix and accompanying interpretation. **Accepted: no remaining method-fidelity or experimental-condition defect was found in these integrated changes.**

- R2-AM-1 is resolved: `chapter/ch05-agrag.tex:74` calls the pseudo node a “connectivity device”, and the corresponding high-cost connection at line 127 no longer assigns it an unconfirmed indexing lifecycle. The cost remains 10.
- R2-AM-2 is resolved: `chapter/ch06-mgrag.tex:120` says empty output occurs when the search finds no valid correspondence. Its greedy-failure discussion remains present at line 203.
- R2-AM-3 is resolved: the condensed algorithm at `chapter/ch06-mgrag.tex:169–189` now takes query anchor gamma, loops over all evidence counterparts v_a above theta, enumerates mappings satisfying I(gamma)=v_a, validates all query edges, aggregates accepted results, and returns the highest score. This matches the relevant publisher Algorithm 1 outer-loop structure. The renamed v_a avoids collision with the per-edge endpoint v. The adjacent prose retains retrying a different query anchor. No completeness, new fallback, or repaired search procedure was introduced.
- All 17 AGRAG and all 12 MGRAG displayed equation/align blocks were compared byte-for-byte with the saved pre-edit manuscript archive and are unchanged. In particular, AGRAG's sum objective and graph-operator entries, MGRAG's semantic objective/thresholds and recomputation sum remain intact. The 2-approximation remains scoped to initial AGRAG tree construction; MGRAG's condition remains conditional on a valid match. The fixed experimental recomputation budget b remains unknown and symbolic.
- The numeric rank emphasis was removed from the three reviewed files (`agrag-efficiency.tex`, `agrag-ablation.tex`, `mgrag-matching.tex`), resolving the inherited-emphasis issue without needing to change values. This follow-up did not repeat the full table-cell audit, as authorized by the main reviewer; the original numeric audit above remains the substantive source check.
- Source conditions remain present after prose compression: AGRAG main Qwen2.5-14B/A100 80 GB versus low-resource Qwen3-4B/two 2080 Ti; MGRAG Qwen2.5-VL-7B/A100-SXM4 40 GB; different embedding configurations; AGRAG metric denominators and model-assessed accuracy; original multimodal generation inputs; and MGRAG host-pipeline/cache quality-time comparisons. In particular, the inverse GKV addition still increases time from 4.1 to 4.3 hours while increasing accuracy from 0.7372 to 0.7442.
- New `chapter/ch07-discussion.tex:62–63` controls-matrix rows correctly describe AGRAG's fixed corpus graph with query-conditioned selection and its one-passage-per-label classification corpus, and MGRAG's query-specific multimodal construction/matching/recomputation. The rows correctly distinguish Qwen2.5-14B/A100 80 GB from Qwen2.5-VL-7B/A100 40 GB. Accompanying lines 50 and 68 distinguish supervision/evidence state and metric meaning without asserting new shared controls or pooled accuracy.
- The revised cost-accounting sentence in `chapter/ch06-mgrag.tex:347` correctly states that listed module times do not sum to the end-to-end total. It does not invent a residual runtime component or alter the published totals.

The remaining optional defensive-writing reductions listed earlier are editorial suggestions, not unresolved correctness requirements. PDF/layout QA is owned by the main reviewer and is outside this integration acceptance.
