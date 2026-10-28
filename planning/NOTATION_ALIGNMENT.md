# Thesis notation alignment

The reproduced figures retain their published notation. When a figure uses a
chapter-specific symbol, the surrounding text keeps that symbol or explains its
correspondence. Symbols are defined locally at each displayed formula.

| Concept | Thesis convention and local exceptions |
| --- | --- |
| Query | `q` in background, AGRAG, and MGRAG; `t` in GORAG, following its pipeline figure. |
| Graph, nodes, edges | `\mathcal G`, `\mathcal V`, `\mathcal E`; GORAG adds round `r`, MGRAG distinguishes `\mathcal{QG}_q` and `\mathcal{KG}_q`. |
| Graph node, relation, edge | `u,v`, `r`, `e`; table row `r` and GORAG round `r` are local exceptions. |
| Corpus and chunks | AGRAG uses `\mathcal T,\mathcal T_c`; MGRAG uses `\mathcal D,\mathcal C` and `\mathcal T` for text chunks. These represent different corpus and modality boundaries and retain the source notation. |
| Query and item embeddings | Bold vectors; `\mathcal M` is the text encoder in AGRAG and MGRAG. |
| Graph serialization | `g` in AGRAG and `S_r` in MGRAG, reflecting the source formulations and MGRAG cache figure. |
| Scores and costs | `s` and `c` in AGRAG, consistent with its figure; other scores have task-specific names. |
| Composition and recomputation | KGLink uses `\phi_{comp}`, written `\phi` in its figure; MGRAG uses `\phi(t)` for recomputation, matching its figure. |
| KGLink loss weights | `\sigma_0` weights classification and `\sigma_1` weights DMLM, following the figure. The publication's equation exchanges these indices. |
| Answer and evaluation | `A_q` denotes AGRAG's generated answer and `A_q^{ref}` its reference; `\mathcal A_q` denotes its claim set and `\mathcal E_{ref}` the reference evidence. |
| Counts and budgets | Use descriptive subscripts where the same chapter otherwise reuses a symbol for a set and its size. Other task-specific budgets are defined at use. |

The notation is locally scoped. A shared letter does not imply identical
algorithms, evidence units, distributions, or experimental protocols.
