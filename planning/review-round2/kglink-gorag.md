# Round 2 independent review: KGLink and GORAG

Reviewer scope: read-only review of `chapter/ch03-kglink.tex` (413 lines), `chapter/ch04-gorag.tex` (315 lines), all five GORAG table inputs, and KGLink/GORAG framing in Chapters 1, 7, and 8. No chapter, bibliography, or shared verification ledger edited. No filesystem AGENTS.md was found under this project/its parent; the user-supplied AGENTS rules were followed. Prior verification ledgers were not used as proof.

## Evidence used

- Source roots and active source files were located from `planning/source_roots.json` and `planning/SOURCE_MAP.md`.
- Controlling KGLink PDF: `planning/kglink-sources/kglink-author-confirmed-publication.pdf` (PDF page numbers below are physical PDF pages, 1-based). Also read original `KGLink.tex` at the mapped source root, especially method and experimental settings.
- Controlling GORAG PDF: `planning/gorag-source/author-confirmed-publication.pdf`. Also read mapped `WWW/WWW_CR/section/sec-method.tex` and experiment details.
- The source main text controls where source text, formulas, and appendix pseudocode disagree, as instructed. No formula correction, alternative implementation, new approximation guarantee, or interpretation of CAD's literal `03139` was introduced.

## Actionable technical findings

### R2-KG-01 — Restore the reported candidate-type input cap (P2)

**Location:** `chapter/ch03-kglink.tex:126–130`, or the implementation settings around line 160 / lines 245–253.

**Current gap:** The chapter specifies ten retrieved entities per cell, the row budget, 64 tokens per column, and eight columns per encoded table, but never states the reported cap on generated candidate types. Thus its implementation description leaves a model-facing input-selection parameter unspecified.

**Exact evidence:** KGLink controlling PDF p. 9, §IV.B, immediately after the ten-entity retrieval setting: “From the KG entities in each column, we generated up to 3 candidate types per row.” The same sentence appears in the mapped original `KGLink.tex` experimental-settings paragraph. This is an experimental input condition, not an inferred method improvement.

**Proposed fix:** Add: “The reported implementation generates up to three candidate types per row from the KG entities in each column.” Preserve the source's “per row” wording; do not silently turn this into a per-column cap.

### R2-GO-01 — Correct GORAG's language-model role in the synthesis table (P2)

**Location:** `chapter/ch07-discussion.tex:25`, Model role cell of the GORAG row.

**Original:** “Keyword extraction and classification”.

**Defect:** In the table's context, “Model role” describes the language model. Query/support keyword extraction is statistical TF–IDF; the language model generates representative label information and performs classification. The current cell conflates these operations and contradicts Chapter 4's own keyword-extraction description (lines 65–71).

**Exact evidence:** GORAG controlling PDF p. 4, §3.2 Eq. (2), explicitly scores each word or phrase with normalized TF–IDF and retains terms above the extraction threshold. PDF p. 5, §3.4 Eq. (11), gives `K_yi = LLM(p_gen, D^r)` for representative label keywords, and Eq. (12) gives the LLM classification operation. Query keywords are extracted using Eq. (2), as §3.3 explicitly states.

**Proposed fix:** Replace that cell with “Label-description generation and classification” (or “Representative label keywords and classification”). This retains the statistical extraction/LLM generation distinction in the common thesis thread.

### R2-KG-SOURCE-01 — The selected-class 9.70 gain has no unit in the source (source ambiguity; editorial P3)

**Location:** `chapter/ch03-kglink.tex:340`, selected SemTab classes Athlete/Protein/Film.

**Exact evidence:** Visually inspected the controlling KGLink PDF physical p. 12, §V.D. The paragraph says “with an average increase of accuracy of 9.70.” There is no percent sign. Mapped original `KGLink.tex:874` likewise contains `9.70.` with no percent macro or unit. Both sources impose the >10-test-sample class filter. Thus the chapter faithfully transcribes an under-specified source claim; this is not a chapter number mismatch.

**Proposed action:** Do not add `%`, “percentage points,” or “relative improvement.” If retaining the number, make its attribution and source ambiguity explicit once: “For these selected classes, the source reports an average accuracy increase of 9.70 without specifying whether this is an absolute or relative change.” Alternatively omit this under-specified numerical increase while preserving the named classes, selection rule, and qualitative type-mismatch examples. The latter is the more concise final-thesis option if no author clarification is available.

## Checked coverage and non-findings

### KGLink

- Checked the complete graph-to-encoder flow: lexical BM25 retrieval, number/date exclusion and failed-link score zero, cross-column neighborhood union/intersection, maximum cell score and summed row score, ranking before selection, recurring neighborhood support, PERSON/DATE filtering, first-row cell selection and highest-linking entity for feature serialization, padding, multi-column encoding, contextual true-type versus masked inputs, and inference without true-type labels.
- The displayed entity-filter equation, cell/row linking scores, vocabulary projection, DMLM distribution order, cross-entropy, joint uncertainty-weighted loss, and preprocessing expression agree with source main text. The unusual DMLM order is retained correctly. The generic composition function is not silently specified as an unreported architecture.
- Checked all displayed numeric cells in the main, ablation, no-linkage, and row-filter tables against controlling PDF Tables I, II, IV, and V. No transcription mismatch found. Main scores 87.12/85.78 and 96.28/96.07, DeBERTa 87.24/85.81 and 96.98/96.37, and row-filter deltas are accurately described.
- Dataset prose follows source main text: SemTab rounds 1/3/4, 3,048 tables, 7,587 columns, 275 types; multi-column VizNet 32,265 tables, 73,034 columns, 77 types. The source's conflicting VizNet Table III denominator is not silently substituted. The main-text reading of `w/o fv` is preserved despite the source checkmark conflict.
- Checked 7:1:2 class-preserving splits, three runs, AdamW, initial learning rate `3e-5`, epsilon `1e-6`, linear decay/no warm-up, 50/20 maximum epochs, dropout 0.1/0.2, batch 16, Tesla V100, temperature two, top-ten entities, 512-token BERT limit, 64-token column and eight-column limits, default row budget 25, and the source's peculiar “all” = at most 64 rows description.
- No-linkage subset is correctly table-wide: 315 tables, 612 columns, 26 labels, 556 numeric and 56 nonnumeric columns. Selected qualitative classes Athlete/Protein/Film, >10 samples, and average 9.70 increase agree with source; they are not generalized into an all-class gain.
- Runtime labels were checked against the vector figure itself using text extraction: KGLink 16.50/1.53 h, RECA 80.00/9.00 h, Doduo 1.96/0.07 h, MTab inference N/A. The cropped page rendering does not change the source figure's 80.00 label.

### GORAG

- Checked cumulative label availability; support labels versus unlabeled query text; observed-corpus statistics; prediction-before-insertion timing; new-keyword-only online insertion; use of predicted labels without supplied query ground truth; and distinction between graph trace and internal model reasoning.
- TF–IDF normalization and threshold 0.5, average complement edge costs, doubled denominator/outer-half label-bridge factors, prompt concatenation, insertion sets, and graph-construction complexity match controlling source expressions. Their source-level oddities are not grounds for silently modifying formulas.
- Checked terminal mapping, auxiliary graph/tree/path expansion, candidate-label intersection, and absence of an invented optimality or approximation guarantee. Main-text-versus-appendix ambiguity remains a source issue; this chapter gives a restrained operational account.
- Independently compared **all 168 adopted WOS/IFS-Rel main-result numeric cells** against the PDF text, reordering original round-major columns into the chapter's separate shot tables: zero mismatches. Checked the 20 ablation values, 20 zero-shot values, 12 token/cost values, and transposed dataset statistics against PDF Tables 1–6. No numerical transcription defect found.
- The five-shot IFS-Rel R4 exception (HippoRAG2 0.5008 versus GORAG 0.4988) is explicitly recognized. The source's bold emphasis is preserved as attributed emphasis, not converted into a false textual best-score claim.
- Formal ablation names remain source-identifiable: KGLink `w/o msk`, `w/o ct`, `w/o fv`, and `DeBERTa`; GORAG `offline&unit`, `offline`, `unit`, and `keyword`. “Offline-and-unit” is only a readable expansion in prose, not a newly defined variant or protocol.
- CAD literal `03139` remains excluded; all quoted CAD values are valid neighboring cells. Main-versus-ablation WOS full rows remain separate result series and are not used as interchangeable controls.
- Checked 1/5/10 shots; Qwen2.5-7B on CAD/WOS; GPT-4o on IFS-Rel; exact label name/number matching; RoBERTa-large Entailment, five epochs, batch 16, learning rate `1e-6`, Adam; LongLLMLingua rates 0.75/0.8/0.85 and selected 0.8; local GraphRAG/LightRAG search; nano-graphrag for GraphRAG/NaiveRAG; Xeon Gold 5220R 2.20 GHz and A100-SXM4-40GB.
- Checked graph-growth endpoints 1,644/1,771/13.3 KB and 5,299/5,503/46.4 KB; the inconsistent intermediate increment is not reproduced as a new verified result. Token prices are correctly historical. Round-generalization curve is correctly described as spliced results from four-, six-, and eight-round partitions, not one eight-round stream. Zero-shot label descriptions are explicitly available information.

### Common thesis thread

The main framing consistently separates KGLink's externally supplied graph + supervised encoder from GORAG's constructed task index + generative classifier. Neither study is falsely described as performing textual answer generation. The Chapters 1/8 numerical summaries for these two studies agree with their chapter tables. The concrete inconsistency is the Chapter 7 model-role cell above.

## Defensive/repetitive writing audit

Applied `/Users/ybwang/.codex/skills/academic-defensive-writing-auditor/SKILL.md`. Most conditions below are necessary scientific scope statements. The following are optional editorial reductions, not correctness blockers.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| ch04:204, 210, 214, 217 | “The tables should be read by comparing methods under the same dataset, round, support size, and backbone”; “Comparing the fourth-round ten-shot score to the first-round one-shot score would mix these conditions”; “Comparisons use methods evaluated under the same round and support conditions”; pooled-improvement discussion | D12 repeated scope signaling | Minor | MIXED: first scope statement and backbone distinction are necessary; repetitions add little | The text repeatedly instructs readers how not to compare already labeled table columns | The result interpretation may feel more procedural than analytical | Retain the first scope statement; remove the hypothetical invalid comparison in line 210 and the repeated final sentence in line 214 | Keep line 204's controlled comparison, then report WOS/CAD values directly. Keep line 217's dataset/backbone distinction if needed for synthesis. |
| ch04:295 | “This case illustrates the operation of retrieval for one text. The accuracy tables quantify the decisions over the test collections, and the ablation table measures the contribution of changing specific pipeline components. These evidence types answer different questions.” | D11/D12 repeated evidence-type explanation | Minor | DEFENSIVE/redundant; no extra scientific limitation | It explains elementary distinctions already established in the results/ablation sections | The case-study section pauses to defend what a case can show | Shorten to the case's specific evidential contribution | “The example shows how the selected keyword connections place the insult label in the classifier's input.” |
| ch03:119 | “Its effect is an empirical question because the score measures linkage rather than the semantic diversity of the selected values.” | D12 | Minor | MIXED: linkage score definition is useful, speculation about diversity is optional | It introduces an unmeasured alternative objective before the row-filter evidence | Reader may expect a diversity analysis that is never used | Keep only the link to the actual experiment | “The row-filter experiment compares linkage ranking with original row order under the same input limit.” |

**Paper-level defensive-writing score (reviewed scope only): 3/10.** Mild repetition; no rebuttal-like passage or need to remove necessary scientific boundaries. The whole thesis was not scored.

**Highest-priority editorial removals:** (1) hypothetical cross-condition comparison at ch04:210; (2) repeated comparison instruction at ch04:214; (3) generic evidence-type paragraph at ch04:295. These are optional and rank below the two technical findings.

**Necessary caveats to preserve:** true-type labels are training-only in KGLink; MTab's label-definition difference/missing F1; no-linkage subset is table-wide; GORAG prediction-before-update and predicted-label error propagation; different backbones across datasets; main/ablation result rows differ; historical cost scope; zero-shot label descriptions; round-generalization curve uses distinct partitions; selected graph paths describe index provenance rather than internal LLM computation. These change interpretation materially.

**Repeated phrase audit:** Case-insensitive whole-word/phrase counts, excluding TeX comments but including captions, in the two complete chapter files: `reported` 29/15 (KGLink/GORAG), `evaluated` 7/5, `protocol` 6/8, `rather than` 4/9, `should` 2/9, `does not` 5/8, `different` 11/20, `separate` 5/6. Counts are screening information only; source attribution and protocol statements are not defects merely because they recur.

## Review limits

This pass checked scientific content and source fidelity, not compiled-page layout, bibliography resolution, or a rerun of the original experiments. No new run/seed provenance was inferred for unexplained source result differences. Source-level contradictions are noted only to explain decisions already required by the author; they are not presented as newly discovered chapter defects.

## Targeted post-edit acceptance check — 2026-10-25

Read current edited KGLink/GORAG passages and Chapter 7's new controls matrix. No new full numeric-table recheck was requested or performed.

**Accepted changes:**

- `ch03:70` now reproduces the source cap accurately: up to three candidate types **per row**, from KG entities in each column. It does not silently change this to a per-column limit.
- `ch03:339` removes the source's unitless 9.70 while retaining Athlete/Protein/Film, the largest-increases selection, and the >10-test-sample eligibility rule.
- `ch07:25` now assigns GORAG “Label-description generation and classification.” This resolves R2-GO-01 and agrees with the separate TF–IDF extraction operation.
- GORAG retains cumulative labels (`ch04:33–40`, 172), supplied support labels versus predicted query associations (`ch04:19`, 40), new-keyword-only insertion after prediction (`ch04:141–149`), error propagation, zero-shot label descriptions (`ch04:247`), composite round-split curve interpretation (`ch04:253`), and distinct main-versus-ablation WOS series (`ch04:216`). Cutting repetitions has not removed these material information boundaries.
- New Chapter 7 main-model/hardware cells correctly give BERT/Tesla V100 and Qwen2.5-7B CAD/WOS versus GPT-4o IFS-Rel/A100 40 GB. The caption explicitly calls hardware the reported local setup and identifies GPT-4o as a service, avoiding an inference that GPT-4o ran on that A100. The GORAG 1/5/10 support examples, cumulative labels, prediction-dependent index state, and exact-label metric are correct. KGLink percentage-scale accuracy/F1 and three-run averages agree with its reported evaluation.

**Two local clarifications recommended (P3; no numerical defect):**

1. `ch03:70`: Inserting the three-type-cap sentence between the ten-entity setting and “This limit bounds the candidate sets that enter the subsequent neighborhood operations” changes the latter's immediate antecedent. Candidate types are generated after the neighborhood/filtering operations, whereas the ten retrieved entities bound their inputs. Move the new cap sentence to the candidate-type subsection/experimental settings, or change the following sentence to “The ten-entity retrieval limit bounds the candidate sets that enter the subsequent neighborhood operations.” The cap itself is accepted.
2. `ch07:60`: “7:1:2 labeled-column split” can imply column-level partitioning. The controlling KGLink PDF p. 9 states train/validation/test proportions and preservation of class proportions, but does not specify the split unit in that passage. Use “7:1:2 train/validation/test; external KG; three-run averages” (optionally “class proportions retained”). This removes an unsupported split-unit implication while preserving every verified condition.

No other new condition error found in the targeted KGLink/GORAG changes.
