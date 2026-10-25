# Independent review of AGRAG chapter

Review date: 2026-10-24. Reviewer: gorag agent, read-only review of `chapter/ch05-agrag.tex`, `chapter/tables/agrag-*`, `scripts/prepare_agrag_tables.py`, and selected active original source. The chapter was being edited concurrently by its owner; findings refer to the reviewed snapshot, with later fixes to be checked by the main agent. No AGRAG authoring file was edited by this reviewer.

## Second-pass status after author version selection

The author explicitly selected the complete local `AGRAG_GORAG/ICDE2026.pdf` and its source over the incomplete arXiv PDF. The reviewer independently opened this **15-page author-selected complete local version**, SHA-256 `9922cc9633cfd3036e70cf0ffc51348cd790e233e8816ed22b11a1188596d820`, 670,757 bytes (PDF metadata creation 24 April 2026). This resolves which version supplies the chapter's evidence. It is not a claim of successful acquisition from IEEE.

The current chapter snapshot checked in this second pass has SHA-256 `c44a0089f144e249eed67b681fc7290dcefa0d58293d57fcce93b21e1322fc33`. The owner has fixed the opening grammar, added the exact graph operator, explicit expansion acceptance inequality, ROG/COV/FS formulas and source citations, supplied the original running example, and removed several identified defensive sentences. All 23 citation keys used in this snapshot have declarations in the bibliography files. This checks key availability, not all bibliographic metadata.

**A new PDF-to-source comparison matched all 652 numeric entries in Tables III, IV, VI, VII and VIII to the active TeX; a fresh source-to-split comparison again matched all 652.** PDF page11 contains TableVIII beside TableIX; the first low-resource efficiency row was re-extracted using a left-column coordinate crop to prevent the neighboring table from contaminating the cell list. The coordinate crop was for reading only; no adopted research image was edited.

Rendered source pages4–12 were inspected for the displayed equations, original figures, headings, and experimental tables. The four copied figure files are byte-identical to the source assets and visually match local PDF Figures1 (physical p4),2 (p5),3a/3b (p12). The existing JSON asset statuses still say pending; this read-only review records their independently checked status here without editing the owner's manifest.

The main-text formulas are faithfully carried over. The known MCMI/PPR/theory consistency questions are now **source-internal limitations retained in the ledger after the author's main-text-precedence instruction**, not an unannounced alternative implementation. The chapter does not normalize P, change the objective to a ratio of sums, fabricate a cycle-closing operation, or extend the initial-stage approximation to the expanded subgraph. No new numerical transcription error was found in this second pass. Final integrated layout still needs the owner's PDF QA after the latest edits.

## First-pass findings and follow-up history

| Priority | Location | Finding | Evidence and action |
|---|---|---|---|
| RESOLVED by author version choice | Version provenance / main result tables | The author-confirmed arXiv PDF and local ICDE2026 PDF do not contain the same table set. Main-table values cannot yet be called publication-verified solely from the arXiv evidence. | The main agent already identified that arXiv Table II is efficiency while the local PDF includes a dataset Table II and main Table III. Retain SOURCE_CHECKED / VERSION_RECONCILIATION_PENDING until the author settles this difference. Numeric fidelity was subsequently checked against the author-selected complete local PDF as recorded above. |
| FIXED in second pass | Metric interpretation, reviewed line 194 | “The source's ROUGE-L measure” does not state the source's nonstandard denominator, which is material to interpreting the numbers. | Active source `sec-experiment_results_sigmod.tex`, line 165, defines ROG=LCS(G,Y)/|G|. Add this exact formula and define generated/reference sequences; do not silently substitute a standard ROUGE-L F1 implementation. Coverage and faithfulness formulas are also useful source-supported details. Main agent was notified and is adding them. |
| FIXED in second pass | MCMI expansion, reviewed lines 123–131 | “Candidates satisfying the source comparison” leaves the actual acceptance rule implicit. | The source's Eq.(MCMI) accepts c_(MCMI,v)/s_v < r(G_MCMI), with r defined by the sum objective. State that exact inequality and the stop condition. Do not infer monotonic decrease of the sum objective. Main agent was notified and is adding the condition. |
| SOURCE-INTERNAL, exact operator now added | PPR subsection | The recurrence is faithfully reproduced but its p/P definitions are deferred to “specified in the source”; the known normalization/seeding ambiguity is therefore still unresolved. | Source p uses 0/1 membership and P assigns 1/degree on neighbors plus 1/|V| on nonedges. Do not silently replace these with a normalized standard PPR implementation. A complete final method account needs author/code clarification or an explicitly attributed exact source definition. The current chapter avoids inventing a stochasticity theorem. |
| FIXED key coverage in second pass | Citations throughout method/protocol | The reviewed chapter cites only `agrag-paper`; TF–IDF, PPR, Mehlhorn, BM25, Contriever, RAGAS, benchmark and baseline origins should have their primary citations. | `bibliography/agrag.bib` initially contained one own-paper entry. The owner requested a separate related-reference increment, being prepared in `bibliography/agrag-related.bib`; the owner will insert citations and merge shared bibliography. |
| FIXED in second pass | Opening sentence, reviewed line 8 | “can locate ... while still leave” is ungrammatical. | Use “can locate ... while still leaving ...” or “can locate ... yet leave ...”. |
| P3 | Standalone typesetting, reviewed lines 172–173,189–190,233–234 | Four overfull hboxes were observed (5.83,20.52,2.58,2.88 pt). | Rephrase the affected long sentences or address line-breaking in the shared preamble; final integrated compile may change wrapping. Independent output `/tmp/agrag-review-build/agrag-review.pdf` has 23 A4 pages including one bibliography page; cross-chapter labels were stubbed for this isolated review, so its suppressed-link warnings are not final-thesis findings. |

## Independent numeric and protocol checks

A separate parser reread the selected active `sec-experiment_results_sigmod.tex`, removed ordinary comments and `comment` environments, located its table blocks by label, and compared each selected source column against `planning/agrag-table-cells.json` and the corresponding split-table layouts. This was independent of running the owner's generator. **18 tables, 652 numerical entries, zero source-to-split mismatches.** Counts include both values in paired time/token cells. This verifies selected-source fidelity; it does not upgrade publication provenance.

- Main result blocks: 11 methods × 22 metric values = 242 numerical entries; the creative/summary/complex/fact/class split indices match the original multicolumn headers.
- Efficiency: 11 methods × 8 paired cells = 176 numerical entries. Time pairs retain indexing/querying order and minute units; token pairs retain input/output order.
- Ablation: 6 variants × (18 quality values + 8 time/token values) = 156 numerical entries. The column labels I/G come from the source; its caption calls them input/output, and the chapter keeps this ambiguity visible.
- Low-resource quality: 3 methods × 18 values = 54 entries.
- Low-resource efficiency: 3 methods × 8 values = 24 entries, with index/query/input/output order correct for Novel and Medical.

The reviewed narrative's quoted main, ablation, low-resource and efficiency numbers match the selected source. Important conditions are preserved: Qwen2.5-14B-Instruct main backbone; Qwen3-4B-Instruct-2507 plus two 2080 Ti GPUs in the low-resource experiment; per-task ACC semantics; one support passage per label for classification; graph-derived candidate labels; model-based relation extraction and raw-triplet filtering. The chapter does not claim that statistical entity extraction removes every LLM operation.

The method retains the source's extraction formula and threshold, semantic edge cost, pseudo-edge cost10, hybrid averaging formula, and passage-score factor0.05. No added experiment, inferred curve value, or globally strengthened approximation result was found. The chapter correctly assigns the reported two-approximation scope to initial MCST connectivity and does not assert it for the expanded MCMI objective.

## Source-supported substantive additions

1. Explicit metric formulas and their denominators, plus the evaluator model and reference evidence units. These make the protocol self-contained.
2. The exact MCMI acceptance/stop inequality, with terminal and candidate definitions. This describes computation instead of paraphrasing the source generically.
3. The original Medical running example can name its mapped facts and the additional answer component shown in the unmodified figure, rather than merely describing an illness/organ scenario abstractly.
4. After version reconciliation, the additional GPT-4o / R1-Searcher result block is a concrete way to discuss backbone dependence if it is present in the authoritative published evidence. The currently selected active source appears to place that block inside an inactive comment environment; do not revive it without provenance confirmation.
5. A task-by-task explanation of GraphRAG-bench query/answer requirements can add useful depth, supported by the benchmark and source evaluation definitions. Avoid adding generic RAG background already assigned to Chapter2.

These additions address actual missing method/protocol details. They are preferable to expanding repeated advice about how results should not be compared.

## Defensive-writing audit

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| Main table captions | “publication-version reconciliation is recorded separately” | D9 | Minor | DEFENSIVE in final thesis | Exposes internal editorial workflow in a research caption | Wants the experiment condition and source | Keep in ledger; delete after the version is settled | “Values and emphasis reproduce [identified original table].” |
| Results, reviewed line211 | “The differences between tasks are expected from their distinct questions and answer formats.” | D4 | Minor | MIXED | Explains score differences without a diagnostic comparison | May read as an automatic explanation for varying scores | State actual protocols without causal reassurance | “The tasks use different query collections and answer formats.” |
| Efficiency, reviewed line219 | “The evidence supports a quality--cost comparison ... rather than a claim that one system minimizes every resource measure.” | D12 | Minor | MIXED | Adds a non-claim after the preceding concrete cost comparison already establishes the tradeoff | Prefers the measured tradeoff directly | Delete the contrast clause | “AGRAG reduces indexing time in these comparisons while its query totals remain above HippoRAG2 on Novel and Medical.” |
| Filtering ablation, reviewed line235 | “They do not require a separate claim that every filtered triple would otherwise cause an incorrect answer.” | D2/D12 | Minor | DEFENSIVE | Answers an imagined universal claim not needed to interpret the ablation | Unnecessary disclaimer | Delete | End after the reported ablation conclusion. |
| Source/PPR/theory interpretation | Precise model, metric, score, and theorem-stage conditions | — | — | NECESSARY_CAVEAT | These conditions determine what was evaluated or guaranteed | Necessary for scientific interpretation | Preserve | Keep conditions local to the associated claim. |

### Paper-level defensive-writing score

First-pass chapter snapshot: **3/10, mild**. Current second-pass text: **2/10**, after removal of the flagged automatic explanation and universal non-claim sentences. The draft is generally direct but contains repeated negative comparison guidance and internal verification language. No whole-thesis score is assigned.

### Highest-priority removals

1. Internal version-reconciliation text from final figure/table captions after resolution.
2. The filtering ablation's universal non-claim sentence.
3. The unsupported “differences are expected” sentence.
4. Repeated “rather than” comparisons that add no condition beyond the immediately preceding measurements.

### Necessary caveats to preserve

Model/hardware changes in low-resource experiments; exact-label ACC versus graded QA ACC; LCS denominator; separate main/ablation measurements; relation/filter LLM use; MCST-only guarantee scope; unresolved PPR/MCMI source semantics; publication version identity.

### Repeated phrase audit

No “We emphasize that”, “It should be noted”, “For a fair comparison”, “We do not claim”, or “Taken together” was present in the reviewed chapter. Multiple “rather than”, “should be compared” and non-claim constructions occur in evaluation discussion. Assess these by meaning, retaining only comparisons that materially distinguish protocols or computational objects.
