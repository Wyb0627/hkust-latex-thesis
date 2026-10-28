# Citation completion and author-led wording revision

Updated 2026-10-28 (Asia/Shanghai).

## Author changes and editing scope

`author-changes.diff` reconstructs the preceding revision from its saved `before/` files and exact replacement log, then compares that revision with the author's working files at the start of this task. The new author changes were concentrated in Introduction: seven empty citation commands, explicit problem-to-method transitions, searchable relationships, parallel textual/multimodal requirements, and KV reuse. This comparison avoids attributing the entire uncommitted Git diff to the author's latest edits.

The revision preserves that direction. It makes 44 exact replacements across the abstract and eight chapters. `edits.json` records each old/new passage and its reason; `manuscript.diff` contains the complete diff against this task's saved working copy. The backup includes bibliography fragments and current project documentation.

The main wording changes are:

- Introduce the requirement before the method in KGLink, GORAG, AGRAG, and MGRAG; connect the same progression in the abstract, Discussion, and Conclusion.
- Make MGRAG's three motivating challenges parallel: extraction, matching, and repeated computation.
- Replace abstract editorial wording with concrete operations and measured outcomes, including graph serialization, label-node access, caption-dependent ranking, and indexing/querying time.
- Correct `evidences` to `evidence`, `jointed` to `combined`, the classification-task construction, and the ambiguous subject of KGLink's no-linkage result. Combine the repeated statement about question-dependent visual details.
- Define key-value (KV) at its first Introduction occurrence and explicitly retain selective recomputation alongside reuse.

No new experiment, numerical claim, method, or theoretical guarantee was introduced. Scientific conditions and previously documented source discrepancies remain.

## Local bibliography search

`local-bib-inventory.json` records paths, SHA-256 hashes, entry counts, and matching entries from eleven original bibliography files: KGLink, GORAG, AGRAG, MGRAG, FormerGNN, GFM4Graph, KBLink, KBLinkcite, CoT Survey, NIPS2024_Yubo, and LLM_NER. All eleven were parsed successfully. The existing thesis fragments were searched as well.

Six of the seven distinct works selected for the empty positions were already in the thesis bibliography. RECA, MultiModalQA, HippoRAG, incremental few-shot classification, and GraphRAG also occur in the original paper libraries. DPR was already present in the shared background bibliography. One additional paper supplies a direct foundational reference for question-guided visual selection.

## Empty-position citation map

The seven original empty commands become eight nonempty commands because the two claims in position C5 receive separate citations. These commands contain ten citation-key occurrences and seven distinct works.

| Position | Claim and resulting citation | Local provenance and primary verification |
|---|---|---|
| C1 | Missing context or evidence distributed across sources: `bg-reca`, `bg-mmqa` | RECA in KGLink/KBLink; MultiModalQA in MGRAG. [RECA, PVLDB 16(6), pp. 1319–1331](https://www.vldb.org/pvldb/vol16/p1319-sun.pdf), Introduction; [MultiModalQA author project](https://allenai.github.io/multimodalqa/) and [ICLR paper PDF](https://openreview.net/pdf/f3dad930cb55abce99a229e35cc131a2db791b66.pdf), abstract. |
| C2 | Selecting evidence while retaining relationships: `bg-hipporag` | GORAG/AGRAG/MGRAG libraries. [HippoRAG, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract-Conference.html), abstract and linked paper. |
| C3 | External information must relate to the task: `bg-reca`, `bg-dpr` | RECA original libraries and existing shared DPR entry. [RECA](https://www.vldb.org/pvldb/vol16/p1319-sun.pdf) selects schema-similar/topic-relevant tables; [DPR, EMNLP 2020](https://aclanthology.org/2020.emnlp-main.550/) learns question–passage retrieval. The general sentence synthesizes these task-specific examples. |
| C4 | New labels with few examples: `gorag-xia-etal-2021-incremental` | GORAG/AGRAG libraries; alias retained. [Xia et al., NAACL 2021](https://aclanthology.org/2021.naacl-main.106/), abstract and Introduction. The citation is attached specifically to new labels arriving with few examples; the absence of a suitable external KG remains the thesis's design motivation. |
| C5 | Joint supporting facts: `bg-hipporag`; complementary facts for a summary: `bg-graphrag` | GORAG/AGRAG/MGRAG libraries. [HippoRAG](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract-Conference.html) studies multi-hop QA; [GraphRAG v1](https://arxiv.org/abs/2404.16130v1) builds community summaries and aggregates partial responses for comprehensive query-focused summaries. |
| C6 | Joint reasoning over text and images: `bg-mmqa` | MGRAG library. [MultiModalQA author project](https://allenai.github.io/multimodalqa/) and [ICLR paper](https://openreview.net/pdf/f3dad930cb55abce99a229e35cc131a2db791b66.pdf). The revised sentence states the supported cross-modal requirement directly. |
| C7 | Questions determine relevant image details: `bg-stacked-attention` | New external addition, after checking the local libraries. [Yang et al., CVPR 2016, pp. 21–29](https://openaccess.thecvf.com/content_cvpr_2016/html/Yang_Stacked_Attention_Networks_CVPR_2016_paper.html); [author-deposited arXiv record](https://arxiv.org/abs/1511.02274), abstract. The model uses the question to locate relevant image regions. |

Existence, author lists, year/venue, and the cited mechanism or task were checked against these primary sources. The CVF page and PDF were available through indexed primary-source search but direct fetch returned 403; its author-deposited arXiv record was opened successfully. The OpenReview forum presented a browser challenge; the author project and official hosted paper PDF supplied verification. No third-party summary was used as claim evidence.

## Bibliography changes

- Add `bg-stacked-attention` to `bibliography/background.bib`, with all five authors, CVPR 2016, pages 21–29, and the official proceedings URL.
- Preserve the existing GraphRAG 2024 reference and eight-author list by explicitly pinning its URL and note to version 1. Version 2 has a changed author list and revision date; the two versions were not mixed.
- Protect Graph RAG, MultiModalQA, and RECA capitalization.
- Correct the existing Faiss preprint entry in `bibliography/mgrag.bib` from `article` to `misc` and link its [2024 version](https://arxiv.org/abs/2401.08281v1). Preserve its authors, title, year, and identifier.
- Regenerate `thesis-references.bib` through the existing merge script: 106 fragment entries, 75 unique works, and 31 retained aliases.

## Validation and tooling diagnostics

`validate_sources.py` uses the project's brace-aware `scripts/bib_utils.py`, including BibLaTeX `ids`. `source-checks.json` confirms required fields, all 100 cited keys resolving, seven empty citations removed, and preservation of every pre-existing nonempty citation occurrence. It also confirms unchanged numerical tokens, labels, references, inline math, equation/align environments, algorithms, figures, and tables in all nine narrative files. Included table citations are checked as well.

The skill's generic structural checker was run as:

```sh
python3 /Users/ybwang/.agents/skills/latex-paper-en/scripts/verify_bib.py thesis-references.bib --output planning/citations-wording-2026-10-28/bib-structure-check.json
```

It returned exit code 1. Its regex parser counted 74 rather than 75 records and reported missing authors for Sherlock, Sato, Doduo, and VizNet because their names contain nested LaTeX accent braces. The project parser confirms that those fields exist. Its Faiss missing-journal finding was a real entry-type issue and was corrected above. Generic IEEE recommendations about preprint volume/pages, optional DOI fields, and author truncation are retained in the raw report; they are not claims of missing citations. The generic checker was not modified or its result relabeled as a pass. The project's existing parser and final Biber compilation provide the independent checks.

Initial compilation completed successfully with:

```sh
python3 /Users/ybwang/.agents/skills/latex-paper-en/scripts/compile.py main.tex --compiler xelatex --recipe latexmk
```

After the Faiss metadata change, an incremental run of the same command returned exit code 12 because `main.bcf` was absent. `compile-final.log` preserves the failure. The same skill entry point was then used with `--clean`, followed by `--compiler xelatex --recipe latexmk`, to regenerate auxiliary state without changing the TeX engine or enabling shell escape. `compile-rebuild.log` records both commands and their output.

The first PDF-dependency probe, `/opt/anaconda3/bin/python -c 'import pypdf,PIL; print("PDF inspection dependencies available")'`, returned exit code 1 because that older installation lacks pypdf. The existing `/Users/ybwang/anaconda3/bin/python` installation passed the identical import probe and is used for inspection. No dependency was installed or substituted in the manuscript build.

The final PDF checkpoint, page counts, visual inspection, and compiler diagnostics are recorded in `../FINAL_QA.md` and the local `pdf-qa/` directory. Earlier review records are historical checkpoints.

The capitalization-only incremental run repeated the missing-BCF failure (`compile-case-final.log`, exit 12). A final clean rebuild passed (`compile-case-rebuild.log`, exit 0), followed by a fresh full render and inspection. An optional page-stream localization probe incorrectly treated the truth value of pypdf ContentStream objects as proof that a stream was absent; it was discarded and no unchanged-page claim is based on it. Final QA relies on the complete rendering and actual text/font/bounding-box checks.
