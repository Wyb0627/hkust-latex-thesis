# GORAG verification and chapter handoff

Last updated: 2026-10-24. Responsible agent: gorag. Chapter status: complete working research chapter at `chapter/ch04-gorag.tex`; independent compile/visual QA underway. **The author has confirmed that the linked arXiv PDF is equivalent to the formal publication. The record uses `AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT`, not publisher-download provenance.**

## Frozen source and publication identity

Selected entry: `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/WWW/WWW_CR/GORAG_WWW.tex` (SHA-256 `65dcf96c814476a4d1929817a40d80876a8775749d5a947f20793748c2116a75`). Active inputs are `sec-introduction.tex`, `sec-related_work.tex`, `sec-method.tex`, `sec-experiment_results.tex`, `sec-conclusion.tex`, and `sec-appendix.tex` in this entry's own `section/` directory. Comments and `comment` environments have been excluded from working inspection copies under `planning/gorag-source/`.

Official publication metadata is corroborated by the [HKUST Research Portal](https://researchportal.hkust.edu.hk/en/publications/gorag-graph-based-online-retrieval-augmented-generation-for-dynam/): Yubo Wang, Haoyang Li, Fei Teng, Lei Chen; *Proceedings of the ACM Web Conference 2026*, pp. 9148–9159; DOI `10.1145/3774904.3793011`; publication date 12 April 2026. The portal distinguishes publication date from rescheduled conference dates (29 June–3 July 2026). Thesis bibliography need not repeat event dates.

On 2026-10-24, `https://dl.acm.org/doi/pdf/10.1145/3774904.3793011` and `/doi/epdf/` returned HTTP 403 through web access; direct `curl -L --fail` also returned 403. The official portal exposes no separate manuscript download. **Neither local PDF is designated publisher-authoritative:** `GORAG_WWW.pdf` was compiled 31 January 2026; `GORAG_WWW_CR.pdf` was compiled 29 January 2026. Both are 12-page author-built acmart PDFs with DOI text. DOI text alone does not establish publisher provenance. No arXiv or mirror was substituted for publisher evidence.

## Author clarification and acquired comparison PDF

During the parent session, the author confirmed that the arXiv versions linked on the personal website are the formal published PDF versions and directed conflicts to follow the paper's main text. On this basis, the agent downloaded `https://arxiv.org/pdf/2501.02844` to `planning/gorag-source/author-confirmed-publication.pdf`. Its first page identifies arXiv:2501.02844v4, 29 January 2026; it carries the WWW '26 DOI and reference block. File SHA-256 is `22bedc758e8714d6634a8dd394d0f31265741b084f3055cf8ed9fa500d0ad4dc`, size 1,344,543 bytes, 12 pages. The ACM HTTP403 result remains part of the acquisition history. This author-confirmed equivalence enables source/PDF comparison; no claim is made that the PDF was downloaded from ACM.

Main text governs method exposition. The chapter follows terminal mapping, auxiliary-graph construction, its MST, path expansion, and label intersection. It does not transplant the appendix pseudocode or silently invent a new shortest-path implementation. The main text itself also conflates original-graph shortest paths and an MST. The chapter does not assert the disputed approximation transfer or add a proof.

## Material issues and their handling after author clarification

| ID | Evidence in selected source | Interpretation / action |
|---|---|---|
| G1 | `sec-method.tex` retrieval prose says a Mehlhorn-based algorithm achieves “2-Approximate”; `sec-appendix.tex`, Algorithm 2 line 1 computes an MST of the original graph, line 5 finds terminal paths **in that MST**, and lines 10–11 expand auxiliary-tree edges using paths in the MST. | A terminal-connecting Steiner problem differs from an ordinary spanning-tree problem. The stated algorithm first restricts paths to an original-graph MST. Its quoted two-approximation does not follow merely by citing the standard Mehlhorn algorithm. Await publication comparison / author clarification; do not silently replace paths with shortest paths in the original graph or state a global two-approximation theorem. |
| G2 | Active main table `tab:main_exp`, CAD/GORAG/Round 4/10-shot is `\\textbf{03139}`. The Jan29 local PDF also renders `03139`. | Invalid as a fractional accuracy; do not silently change to 0.3139. Retain exact source in internal ledger; omit this table cell from final quantitative interpretation until confirmed. |
| G3 | `tab:memory_cost`: Nodes at 25% are 1644; at 50% are `3238 (+1394)`. | The displayed increment differs from subtraction (1594). Do not correct the original annotation or repeat it as verified. Publication / author resolution needed. |
| G4 | Main WOS/GORAG 1-shot row is 0.4866/0.4790/0.4736/0.4420. Ablation WOS/GORAG row, described as 1-shot Qwen2.5-7B, is 0.4862/0.4649/0.4814/0.4210. | Tables may reflect different runs, but no active source explanation identifies run/seed/protocol differences. Preserve them as separate reported experiments and avoid deriving an ablation delta against the main table. Ask author for experiment provenance before finalizing conditions. |
| G5 | Equation `eq:tfidf_ke` divides frequency by text length and by log(corpus size+1), multiplies by IDF; prose extracts terms with score >0.5. | Normalization and threshold require implementation/publication confirmation. Do not replace the score with conventional TF–IDF or invent a scaling step. |
| G6 | Label-bridge weight has outer 1/2 and inner denominators `2*|M_y|`. | Preserve exact formula; do not simplify to an ordinary mean under a verbal “weighted average” description. |
| G7 | Active Appendix complexity prose says “weighted adjacency matrix” takes O(|E|) space. | Storage form and claimed bound do not match ordinary dense adjacency-matrix accounting. Avoid restating the bound as a verified implementation property. |

The author instructed main-text precedence. The chapter applies that instruction, retains exact main-text formulas and parameters, separates main and ablation result series, and excludes the invalid CAD result block and inconsistent graph-growth annotation. The invalid literal is preserved only in `planning/gorag-working-cad-table.tex` and the cell ledger. No corrected measurement is manufactured. G1 remains an internal algorithmic consistency issue rather than an asserted thesis theorem.

## Source/PDF-checked protocol facts (author-confirmed publication equivalent)

- Each round adds new labels; the current label universe is their cumulative union. Few-shot settings use 1, 5, or 10 labeled examples per class.
- Graph nodes are extracted keywords and labels. Keyword–label edges reflect occurrence in labeled text; label-bridge edges are also introduced when merging rounds. There are no exemplar nodes in this source's graph definition.
- Query keywords already represented in the graph become retrieval terminals; unseen keywords are retained for online insertion.
- Classification prompt concatenates query text, its extracted keywords, retrieved candidate labels, and representative label keywords/descriptions where label names are available.
- Online insertion occurs **after** classification. New query keywords connect to the **predicted** label, not the query's ground-truth label. Query ground truth remains evaluation information.
- CAD and WOS main results use Qwen2.5-7B; IFS-Rel main results use GPT-4o. Do not pool their runtime or accuracy as one backbone setting.
- Classification is correct only for exact match to a ground-truth label name/number. Four-round main results use cumulative label sets; six/eight-round WOS experiments are additional split variants. The composite curve uses rounds 1–4 from the four-round split, 5–6 from six-round split, and 7–8 from eight-round split, **not one continuous eight-round run**.
- The source's macro-recall/hallucination tables occur inside inactive comment environments and must not be revived as published evidence. An active Hardware Settings subsection at the end of the appendix reports Intel Xeon Gold 5220R @ 2.20GHz and one NVIDIA A100-SXM4-40GB; a separate earlier hardware paragraph is inactive.
- Zero-shot IFS-Rel graph initialization uses label names and LLM-generated label descriptions, with no labeled text. This is a separate protocol from few-shot graph initialization.

## Intended evidence mapping

| Thesis topic | Source | Publication locator | Verification status |
|---|---|---|---|
| Dynamic few-shot task and rounds | `sec-related_work.tex`, DFSTC Task; `DFSTC_task.pdf` | Figure 1 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |
| Offline/retrieval/online pipeline | `GORAG_pipeline_example_new.pdf` | Figure 2 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |
| Dataset statistics | `sec-method.tex`, `tab:data_stat` | Table 1 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |
| Full main accuracy | `sec-experiment_results.tex`, `tab:main_exp` | Table 2 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; G2 block excluded |
| Runtime | `runtime_wos.pdf`, `runtime_cad.pdf` | Figure 3 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |
| Graph growth | `tab:memory_cost` | Table 3 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; G3 annotation excluded |
| Token and historic USD cost | `tab:token_cost` | Table 4 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; historical price only |
| Ablations | `tab:exp_abl` | Table 5 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT; separate result series |
| Zero-shot IFS-Rel | `tab:0_shot` | Table 6 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |
| Four/six/eight-round split study | `wos_4_round_1.pdf`, `wos_4_round_5.pdf` | Figure 4 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |
| Qualitative CAD example | `new_case.pdf` | Figure 5 in local author PDF | MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT |

Seven original PDF assets have been copied unchanged to `figures/gorag/`, SHA-256 checked against their source files, and visually compared with the author-confirmed PDF. Figures 1–5 correspond to PDF physical pages 1, 4, 7, 8, and 12. The two-panel figures preserve all original subfigures; legends in the second panels are retained and their scope is stated in captions. Manifest: `planning/gorag-figure-manifest.json`.

`planning/gorag-main-cell-ledger.csv` records 252 original main-table cells. An independent row extraction from PDF Table 2 matched all 252 texts; the one invalid literal `03139` is explicitly marked and its entire CAD block is withheld from the integrated table. WOS/IFS-Rel data preserve all 168 cells and original bold/underline formatting. The chapter additionally reports only undisputed CAD values in prose. `planning/gorag-other-cell-ledger.csv` records 82 checked cells from Table 1 dataset statistics (30), Table 4 tokens/costs (12), Table 5 ablations (20), and Table 6 zero-shot (20). Each cell matches the source and the PDF. Original units, decimal precision, and historical USD costs are preserved.

One substantive claim correction is necessary when transcribing prose: the original statement that GORAG is best in every main-table condition is contradicted by IFS-Rel R4 five-shot (HippoRAG2 0.5008; GORAG 0.4988). The chapter reports the exact values and does not repeat the universal ranking. This is a source-internal discrepancy, not a newly calculated result.

## Formulas and quantitative claim checks

- Correlation score: thesis Eq. `eq:gorag:correlation` matches publication Eq. (2), PDF p.4, using a clearer local corpus symbol `T_{<=r}`. The reported threshold 0.5 is retained without inventing a normalization step.
- Keyword edge mean: thesis Eq. `eq:gorag:weights` matches publication Eq. (4), p.4.
- Label-bridge expression: thesis Eq. `eq:gorag:labelbridge` retains both outer 1/2 and inner factor-two denominators of Eq. (7), p.5.
- Query keyword partition and candidate intersection follow Sec.3.3, p.5; no rewritten NP-hardness proof or global approximation theorem is introduced.
- Prompt construction and predicted-label online insertion match Eqs.(10)–(13), pp.5–6.
- Abstract graph-construction count matches Appendix D, p.11. The inconsistent dense-matrix/O(E) storage claim is not adopted.
- Backbone, exact-match metric, few-shot sample sizes, prompt compressor rates, hardware, zero-shot label-description initialization, and combined split-curve conditions were checked against Secs.4.1–4.4 and Appendix E.
- Narrative scores are direct table entries; no relative percentage improvements or derived significance claims were introduced.

## Citation verification

Own-paper title/authors/DOI/year/pages checked against HKUST Research Portal. CAD, Entailment, LongLLMLingua and LightRAG entries replaced with the official ACL Anthology BibTeX records (2021.naacl-main.182, 2021.naacl-main.106, 2024.acl-long.91, 2025.findings-emnlp.568). HippoRAG2 title/authors/venue/pages checked against PMLR volume 267, pp.21497–21515. Mehlhorn title/author/volume/pages/DOI checked against the publisher record (10.1016/0020-0190(88)90066-X). The GORAG source bibliography's extra `and` in LongLLMLingua authors and duplicate year/wrong venue wording in LightRAG were not inherited. An invalid optional ISBN supplied by ACL's LightRAG BibTeX was omitted after Biber's validation warning; no replacement ISBN was guessed. WOS/GraphRAG/TF-IDF/GPT-4o metadata remain source-transcribed (not all fields independently checked); these records are distinguishable from the primary-source-verified subset.


## Chapter build and layout QA

- Independent entry: `planning/gorag-source/chapter-smoke.tex`; HKFoggyU v0.11.6 class with TeX Gyre fonts and chapter counter set to 3. Main thesis files were not modified.
- Command: `latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=planning/gorag-build planning/gorag-source/chapter-smoke.tex`; Biber was run through latexmk and once explicitly after bibliography cleanup. Last checked build succeeds, A4, 20 PDF pages (19 chapter pages plus one independent references page), with no undefined citations/references and no overfull boxes. Class-name/path, unused-option and siunitx/physics warnings originate in the class configuration; no missing asset warning.
- Inspected rendered physical pages 1,4,6,8,10,12,14,17,18,20 in the current standalone layout, plus original publication pages 1,4,7,8,12 and every adopted source figure. Formulas, image proportions, page-bottom numbering, datasets, split tables, legends, case example and bibliography are legible. Initial 13-column main tables were split by dataset and shot to retain natural-size `small` text; all 168 adopted main cells remain present. Dataset statistics were transposed without changing values. Small tables use natural text size instead of being enlarged to full width. Latest final prose edits require a final integrated build by the main agent; no source formula or table changed after this visual inspection.
- TeXcount command/output: `texcount -sum -inc chapter/ch04-gorag.tex`, saved in `planning/gorag-wordcount.txt`. Main text is approximately 5,000 words; headers/captions are separately counted. This excludes table numbers and bibliography.
- The standalone chapter is ready for main-agent integration and independent factual review. The final integrated PDF still needs inspection; this record is not final-thesis preflight.

## Defensive-writing audit (chapter only)

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| Zero-shot interpretation, working draft | “Their accuracy values should therefore be presented with those sources visible, rather than interpreted as a controlled subtraction of a particular number of support examples.” | D12 | Minor | MIXED | Addresses an imagined comparison instead of stating the evaluated difference | Wants the initialization conditions directly | Replace with positive scope statement | “The zero-shot and few-shot comparisons therefore evaluate different graph initialization sources.” |
| Final case caption, working draft | “The offensive text is retained as part of the original dataset illustration.” | D9 | Minor | DEFENSIVE | Explains a routine reproduction choice already apparent from the figure attribution | Unnecessary commentary in a research caption | Delete | Caption directly identifies the contextual-abuse example and source figure. |
| Round generalization | Four/six/eight-round points are taken from separate split versions | — | — | NECESSARY_CAVEAT | Changes interpretation of the plotted trajectory | Needs this protocol detail | Preserve | Explicit positive statement of which split supplies each point. |
| Online update | Newly observed terms attach to the predicted label after classification | — | — | NECESSARY_CAVEAT | Distinguishes available information and error propagation | Needs the true/predicted label boundary | Preserve | “After the prediction, each keyword ... is inserted into the graph and connected to y*.” |
| Main/ablation series | The full-method rows differ between the two original tables | — | — | NECESSARY_CAVEAT | Prevents unsupported cross-table effect subtraction | Needs provenance to interpret component comparisons | Preserve once and track run provenance internally | Component comparisons use the full-method row from the same ablation table. |

### Paper-level defensive-writing score

Chapter-only score: 2/10 after cleanup. Whole-thesis score is not assigned by this subtask.

### Highest-priority removals

1. Removed a reviewer-facing instruction about how zero-shot scores should not be compared.
2. Removed the caption's procedural explanation for retaining the original example text.
3. Did not inherit source claims of universal superiority, overfitting explanations without diagnostics, or space-limit justifications.

### Necessary caveats to preserve

Predicted-label online insertion; query-stream state dependence; exact-label metric; Qwen2.5-7B versus GPT-4o conditions; the split-curve construction; distinct main/ablation result series; historic USD pricing; graph memory versus model memory; the actual terminal-connecting algorithm conditions.

### Repeated phrase audit

The checked chapter has zero instances of “We emphasize that”, “It should be noted”, “We do not claim”, “For a fair comparison”, “Together, these”, “Taken together”, “robust”, “promising”, or “encouraging”. Remaining negative/contrastive technical statements distinguish the evaluated objects and information boundaries. A whole-thesis phrase audit remains the main agent's responsibility.

## Integrated table locations

Current compiled table inputs are `chapter/tables/gorag-{dataset-table,main-tables,ablation-table,token-table,zero-table}.tex`. Their corresponding `planning/gorag-*.tex` intermediates are retained for provenance; the two one-shot captions now read “one support example”. No numerical cell changed during relocation.


## Independent round-two integration — 2026-10-25

Discussion Table7.1 now correctly assigns label-description generation and classification to the language model; lexical query/support keyword extraction remains statistical. Source extraction versus label-generation equations were rechecked. Retrieval prose is shorter but retains terminals, auxiliary graph, spanning-tree/path expansion and candidate-label intersection. Support/query timing, prediction-derived updates, cumulative labels, exact-label assessment, Qwen/GPT dataset split, description-based zero-shot input, separate main/ablation series and stitched round partitions remain explicit. All8 displayed math blocks and all external result-table numerical streams are unchanged. No Mehlhorn/source-appendix conflict was reclassified as resolved.

Current PDF/counts and visual findings are in `FINAL_QA.md`; prior chapter audit counts remain historical. Full dispositions: `review-round2/REVIEW_SUMMARY.md`. No new experiment was run.
