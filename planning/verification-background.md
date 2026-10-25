# Background chapter source and evidence verification

Updated 2026-10-24. Files covered: `chapter/ch02-background.tex`, `bibliography/background.bib`, `figures/hyperkg/decomp_new.pdf`. Status: working chapter and selected evidence checked; integrated thesis PDF checks and remaining reference-metadata corrections belong to the main agent.

## Scope and manuscript status

The chapter follows the accepted seven-section plan: knowledge graphs/language models; table understanding; RAG; graph retrieval; multimodal retrieval/context serving; the author's independent CIKM study; and research-question connections. It distinguishes encoder classification from generative models, retrieval units from index/update units, graph ranking from connectivity, caption representations from original images, and retrieval selection from KV recomputation. It does not claim algorithmic dependencies among the four thesis systems.

Latest check: `texcount -brief chapter/ch02-background.tex` gives **3998 prose + 46 headings + 83 captions**. The dedicated CIKM section gives **966 prose + 18 headings + 66 captions**, within its 900–1400-word budget. The whole chapter is effectively at the lower end of the 4000–5000-word target (two prose words short of exactly 4000); no padding was added. The main agent may expand a substantive point during editing if needed.

## CIKM source identity and use

- Selected source entry is `CIKM_FormerGNN/CIKM2025_CR_new.tex`, with active `main.tex` and `appendix.tex`, as fixed by the plan. Active extracted source is `planning/extracted/hyperkg-active.tex.txt`.
- Reference PDF: `planning/published/hyperkg-author-confirmed.pdf`, arXiv:2508.03280v1, 11 physical pages. The author explicitly confirmed that the arXiv PDFs linked on their site are the formally published versions. Evidence authority is **AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT**. The file was not acquired directly from ACM.
- The arXiv PDF contains legacy conference-header placeholders. They are not used for thesis publication metadata. The published DOI metadata was checked independently against ACM-deposited Crossref data, saved as `planning/background-sources/hyperkg-crossref.json`.
- Publication: Yubo Wang, Shimin Di, Zhili Wang, Haoyang Li, Fei Teng, Hao Xin, Lei Chen, *Understanding the Embedding Models on Hyper-relational Knowledge Graph*, CIKM 2025, pp. 3177–3187, DOI `10.1145/3746252.3761370`.
- The section labels this as the author's own published research and describes its link-prediction task. It does not treat the study as an LM experiment or a module used by KGLink/GORAG/AGRAG/MGRAG.

## Figure and formula

The original decomposition image was visually compared with Fig. 1 on reference PDF physical p. 2. Source and adopted image hashes agree:

`5f80185a1a1659f6f50e314f8f1dafe6ff9b946e211b16f2cf2e054c3314f3a1`

Source: `CIKM_FormerGNN/figures/decomp_new.pdf`. Target: `figures/hyperkg/decomp_new.pdf`, label `fig:background:decomposition`. `planning/background-assets.json` records its original figure number and page. No redraw, cropping, or image-data editing was performed. Prune/Direct/Hyper/reification distinctions were checked against source main.tex Section 3.1 and reference PDF pp. 2 and 6. The hyper-relational-fact formula preserves a main triple and an associated set of qualifier relation--entity pairs, matching the source's Section 2.1.

## Table 6 cell audit

Adopted table: `tab:background:formergnn`, projected from original **Table 6, reference PDF physical p. 8**. The projection retains **all seven model rows** and exactly the **first six metric columns**. It omits Wikipeople/FBAUTO columns to keep the background introduction concise. This projection is declared in the caption. No metric, precision, average, or missing value was inferred.

Column mapping is fixed: metric positions 1–3 are Cleaned JF17k MRR, H@1, H@10; positions 4–6 are WD50k MRR, H@1, H@10. Checked against the rendered p. 8 and selected source main.tex. All **42 numeric cells** match the source and adopted table. The check also confirms original best/second-best bold/underline markings, including NBFNet + Prune's highest H@10 values; FormerGNN is not presented as best on every metric.

| Row | main.tex source line | Cleaned JF17k MRR / H@1 / H@10 | WD50k MRR / H@1 / H@10 | Status |
|---|---:|---|---|---|
| StarE | 823 | 0.381 / 0.284 / 0.577 | 0.346 / 0.268 / 0.494 | 6/6 visual and ordered source/target matches |
| QUAD | 824 | 0.402 / 0.305 / 0.602 | 0.349 / 0.275 / 0.487 | 6/6 matches |
| HAHE | 826 | 0.405 / 0.310 / 0.585 | 0.360 / 0.288 / 0.496 | 6/6 matches |
| HyperFormer | 827 | 0.425 / 0.328 / 0.613 | 0.372 / 0.293 / 0.522 | 6/6 matches |
| NBFNet + Prune | 828 | 0.415 / 0.313 / 0.630 | 0.360 / 0.271 / 0.530 | 6/6 matches |
| CompGCN + Hyper | 829 | 0.389 / 0.294 / 0.590 | 0.350 / 0.277 / 0.488 | 6/6 matches |
| FormerGNN | 831 | 0.432 / 0.335 / 0.624 | 0.377 / 0.299 / 0.527 | 6/6 matches |

The machine-readable records are `planning/background-table-cells.json` (42 records). An independent read-only check matched each model's six adopted numbers to both that JSON and the first six numeric entries of the selected TeX source row. Conditions in chapter text preserve link prediction, the two named datasets, A100-40GB hardware, the source's original-repository/grid-search parameter policy, and the Transformer replacement for CompGCN's decoder.

The complete source contains an FBAUTO entity-count inconsistency (dataset table 2,094 versus prose “over 8000”). No FBAUTO entity count is adopted. This does not affect the projected numeric table. The source Table 6 results on the two omitted datasets are not combined into a new summary statistic.

## Literature and metadata checks

Only primary scholarly/author sources are used to support descriptions of external methods. Most references were already cited by the five thesis papers. The exact evidence used for the background is listed below; this is not a claim that every cited paper has undergone a line-by-line full-text audit.

| Reference | Primary evidence checked | Use |
|---|---|---|
| Wikidata | [ACM DOI](https://doi.org/10.1145/2629489); Crossref snapshot | Explicit structured facts and qualifiers; author metadata |
| BERT | [ACL paper record](https://aclanthology.org/N19-1423/) | Bidirectional representations and task-specific output layer |
| Transformer | [NeurIPS record](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) | Attention architecture; complete eight-author metadata is required |
| Sherlock | [Author project](https://sherlock.media.mit.edu/) | Column features and semantic type prediction |
| Sato | [PVLDB paper](https://www.vldb.org/pvldb/vol13/p1835-zhang.pdf) | Table context, topic modeling, structured prediction |
| Doduo | [Author implementation/citation](https://github.com/megagonlabs/doduo) | Multi-column PLM annotation; DOI 10.1145/3514221.3517906 |
| HNN | [IJCAI paper record](https://www.ijcai.org/proceedings/2019/289) | Table features and KB-derived property information |
| RECA | [PVLDB DOI](https://doi.org/10.14778/3583140.3583149); Crossref snapshot | Related-table evidence; metadata |
| BM25 | [Publisher DOI](https://doi.org/10.1561/1500000019) | Sparse retrieval; confirms only Stephen Robertson and Hugo Zaragoza as authors |
| DPR | [ACL record](https://aclanthology.org/2020.emnlp-main.550/); Crossref snapshot | Dual-encoder passage retrieval; table retrieval unit |
| Original RAG | [NeurIPS record](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html) | Retrieved nonparametric evidence and generative prediction |
| GraphRAG | [Authors' paper](https://arxiv.org/abs/2404.16130) | Entity graph/community summaries for query-focused summarization |
| HippoRAG | [NeurIPS record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract-Conference.html) | KG plus personalized PageRank; authors and year |
| LightRAG | [ACL record](https://aclanthology.org/2025.findings-emnlp.568/); Crossref snapshot | Dual-level graph/vector retrieval, incremental updates; corrected venue to Findings of EMNLP 2025 |
| MMQA | [Authors' repository](https://github.com/allenai/multimodalqa); [ICLR record](https://openreview.net/forum?id=ee6W5UgQLa) | Cross-modal evidence and question answering |
| MRAMG | [Authors' repository](https://github.com/MRAMG-Bench/MRAMG) | Text-plus-image output task; source benchmark identity |
| CacheGen | [Author-hosted SIGCOMM PDF](https://cs.stanford.edu/~keithw/sigcomm2024/sigcomm24-final1571-acmpaginated.pdf); Crossref snapshot | Cache compression and transfer; complete author metadata |
| CacheBlend | [Author paper](https://arxiv.org/abs/2405.16444); [EuroSys accepted-paper list](https://2025.eurosys.org/accepted-papers.html); Crossref snapshot | Selective recomputation when composing cached chunks |
| StarE | [ACL record](https://aclanthology.org/2020.emnlp-main.596/); Crossref snapshot | Qualifier/triple semantic roles and WD50K |
| CompGCN | [Authors' repository](https://github.com/malllabiisc/CompGCN) | Composition-based graph representations; corrected publication year from imported 2019 to ICLR 2020 |
| NBFNet | [NeurIPS record](https://proceedings.neurips.cc/paper/2021/hash/f6a673f09493afcd8b129a0bcf1cd5bc-Abstract.html) | Path aggregation formulation; four authors, NeurIPS 34 (2021) |
| HyperFormer | [Coauthor institution record and accepted manuscript](https://www.research.ed.ac.uk/en/publications/hyperformer-enhancing-entity-and-relation-interaction-for-hyper-r/) | Qualifier integrator identity; five authors, CIKM 2023, pp. 803–812, DOI 10.1145/3583780.3614922 |
| Four thesis publications | Corresponding chapter source ledgers and chapter-local BibTeX | High-level interfaces and research-question mapping |

The NBFNet primary abstract describes its node-pair representation as a generalized sum of path representations; this supports the chapter's path-information description. HyperFormer's author-institution record confirms its entity-neighbor and relation-qualifier modules and the imported title/author/year/pages. Direct ACM access returned 403, which does not affect the independently checked author-institution metadata.

Eight DOI metadata responses are saved under `planning/background-sources/`. Chapter descriptions introduce established method roles without carrying over external headline improvement numbers. The retrieval-organization table is descriptive and does not combine heterogeneous benchmark scores or imply a shared experiment.

## Remaining corrections found during independent review

1. **Transformer bibliography entry is incomplete.** `bibliography/background.bib` and the current merged `thesis-references.bib` contain `author={Vaswani, A}` for `bg-transformer`; the primary NeurIPS record lists Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin. Replace with the complete author list and volume 30. The main agent owns shared bibliography integration.
2. **BM25 imported author placeholder.** The source-derived entry has “and others”; the publisher lists only Robertson and Zaragoza. Remove the placeholder. The currently migrated publisher landing page has inconsistent volume/page metadata relative to the original 3(4):333–389 record, so do not blindly overwrite the established volume/pages from that HTML.
3. Integrated PDF QA for the original decomposition figure and projected result table is not certified by this source audit. The main agent is compiling/rendering the full project.

## Defensive-writing check

Chapter prose was reviewed for claims about retrieval and information preservation. The HyperKG section retains a single explicit scope statement that its evidence is KG link prediction. It uses the actual H@10 counterexample instead of claiming universal superiority.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| End of §2.6 | “The selected table illustrates the result associated with the main discussion of graph reception and qualifier integration; it is not an average over the four datasets.” | D12 | Minor | MIXED | Repeats a projection already declared in the caption | Reader already knows which datasets are shown | Prefer positive scope on final editing | “The selected columns report the link-prediction results on Cleaned JF17k and WD50k.” |
| §2.6 opening | “Its experiments concern KG embedding models, while the four research chapters examine language-model augmentation.” | — | — | NECESSARY_CAVEAT | Separates different experimental objects | Prevents false attribution of LM evidence | Preserve once | Current statement |

Chapter-level score: **2/10**, not a full-thesis score. Highest-priority edit is the repeated table-scope non-claim above. Necessary conditions to preserve are the actual benchmark/task distinction, model configuration, metric-specific rankings, and source-projection declaration. No “we emphasize,” “it should be noted,” “for a fair comparison,” “we do not claim,” or promotional compensation is needed in this chapter.

## Main integration resolution — 2026-10-24

The bibliography corrections flagged above have been applied. Primary evidence and exact corrections are in `planning/bibliography-primary-corrections.md`; Contriever’s author-linked arXiv v4 PDF explicitly confirms TMLR 08/2022 and all seven authors. Transformer and BM25 author records are corrected; HyperFormer DOI is supplied. Integrated pagination and final visual findings are recorded separately in `planning/FINAL_QA.md`; historical chapter counts remain checkpoint counts.
