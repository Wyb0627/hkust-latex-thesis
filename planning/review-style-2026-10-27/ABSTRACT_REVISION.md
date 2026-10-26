# Abstract revision following the author's review

Reviewed on 2026-10-27 (Asia/Shanghai). The author asked to simplify the abstract, especially its final paragraph, by removing specific metric values and backbone names/sizes and referring to other HKUST CSE doctoral abstracts.

## References examined

| Thesis | Source inspected | Relevant writing choice |
|---|---|---|
| Yushi Sun, 2025, *Innovative Approaches to Data Curation and Retrieval-Augmented Generation* | [HKUST Research Portal abstract](https://researchportal.hkust.edu.hk/en/studentTheses/innovative-approaches-to-data-curation-and-retrieval-augmented-ge/) | Organizes the thesis through its research problems and contributions, then summarizes evaluation against existing approaches without listing benchmark scores or backbone sizes. Same department and supervisor. |
| Zihao Wang, 2025, *Querying Neural Graph Databases* | [HKUST Research Portal abstract](https://researchportal.hkust.edu.hk/en/studentTheses/querying-neural-graph-databases/) | Describes research questions, theoretical properties and technical advances without listing benchmark scores or implementation backbones. |
| Tianqing Fang, 2024, *Commonsense Knowledge Base Population and Reasoning for Inferential Knowledge* | Local full thesis, printed pp. xv–xvi, [author-hosted PDF](https://tqfang.github.io/files/Tianqing_Ph_D__thesis.pdf) | Explains contributions and qualitative downstream improvements. Includes an annotation dataset size, but no benchmark metric values or backbone configurations. |
| Yu Peng, 2012, *Understanding and Utilizing User Preferences* | Local full thesis, printed pp. xii–xiii, [source archive](https://home.cse.ust.hk/~raywong/PGGuideline/defense/Thesis-Template.zip) | Describes the problems and algorithms, and summarizes effectiveness, efficiency and scalability. The numerical approximation factor is a theoretical property, not a benchmark score. |

These examples inform the editorial choice; they do not establish a departmental rule against numbers. The revised abstract follows the author's preference and the problem/contribution/result emphasis in these examples. Phrasing was written for this thesis, not copied from the references.

## Applied edits

Paragraph 1 is unchanged. Paragraph 2 now states the four methods' principal contributions with less component-level detail. Paragraph 3 removes dataset names, score values and backbone configurations. Its result statement describes improved effectiveness over established baselines and efficiency gains in indexing and context processing. It does not assert that every method leads every effectiveness and efficiency measure. The related HyperKG study retains one short information-preservation sentence.

[REVISED: Paragraphs 2 and 3]

### Before

```text
Language models depend on the evidence supplied to their prediction and generation processes. Tables can omit information needed for semantic annotation, classification labels can evolve under limited supervision, and answers can require relationships distributed across textual and visual sources. This thesis investigates how explicit knowledge structures can organize and select evidence for these settings.

The thesis develops four methods. KGLink combines knowledge-graph information with a pre-trained language model for column type annotation. Cross-column graph filtering, candidate types, and a contextual representation objective relate external knowledge to the target annotation vocabulary. GORAG maintains weighted keyword--label relations for dynamic few-shot classification. Its connected retrieval and online indexing adapt candidate evidence to the input and the information available across rounds. AGRAG selects connected textual evidence using query-conditioned node influence and semantic edge costs, then combines the selected graph with hybrid passage retrieval. MGRAG incrementally constructs query-specific multimodal graphs, matches query relations to semantic paths, and uses graph features to guide selective recomputation of cached model states.

Evaluations cover annotation on SemTab and VizNet, dynamic classification on CAD, WOS and IFS-Rel, textual retrieval and generation, and multimodal question answering. KGLink obtains weighted F1 of 96.07\% on VizNet. GORAG reaches fourth-round WOS accuracy of 0.4929 with ten examples per label and Qwen2.5-7B. AGRAG obtains Medical summarization coverage of 0.690 with Qwen2.5-14B-Instruct. MGRAG reaches MMQA accuracy of 0.7442 with Qwen2.5-VL-7B-Instruct. Ablations examine knowledge enrichment, index maintenance, connected context, semantic matching, and context recomputation. A separate hyper-relational knowledge-graph study analyzes information preservation. The studies identify how explicit relationships guide evidence representation, retrieval, and computation for language models.
```

### After

```text
Language models depend on the evidence supplied to their prediction and generation processes. Tables can omit information needed for semantic annotation, classification labels can evolve under limited supervision, and answers can require relationships distributed across textual and visual sources. This thesis investigates how explicit knowledge structures can organize and select evidence for these settings.

The thesis develops four methods for structural augmentation. KGLink integrates knowledge graphs with a pre-trained language model to enrich column representations and bridge differences between graph types and annotation labels. GORAG supports dynamic few-shot classification through connected label retrieval and an online graph index that evolves with the task. AGRAG selects connected textual evidence by combining query-dependent node influence, semantic edge costs, and hybrid passage retrieval. MGRAG constructs query-specific multimodal graphs, matches query relations to semantic paths, and uses graph structure to guide the reuse and recomputation of cached model states.

Experiments across table annotation, dynamic classification, textual generation, and multimodal question answering show improved effectiveness over established baselines and efficiency gains in graph indexing and context processing. Ablation studies verify the contributions of the structural components. A related study of hyper-relational knowledge graphs examines information preservation. These studies demonstrate how explicit relationships improve evidence representation, retrieval, and computation for language models.
```

## Manual abstract diagnosis

| Element | Status | Evidence |
|---|---|---|
| Background | PRESENT | First paragraph identifies incomplete tables, evolving labels and distributed textual/visual evidence. |
| Objective | PRESENT | First paragraph explicitly states the investigation of knowledge structures for organizing and selecting evidence. |
| Methods | PRESENT | Second paragraph identifies KGLink, GORAG, AGRAG and MGRAG with their central operations. |
| Results | PRESENT | Final paragraph summarizes effectiveness improvements and indexing/context-processing efficiency gains. |
| Conclusion | PRESENT | Final sentence identifies evidence representation, retrieval and computation as the common use of explicit relationships. |

The heuristic `analyze_abstract.py` exits 0 but labels the diagnosis FAIL. It misses the existing background/objective wording and asks for numerical results. The first paragraph explicitly contains both elements; numerical details were omitted at the author's request. No metric was reintroduced to satisfy that heuristic. Full output: `abstract-check.txt`.

## Validation

- Abstract word count is 206, reduced from 261. The three-paragraph abstract has no numerical results, named backbone configurations, rhetorical colons or sentence-level dashes.
- XeLaTeX + latexmk compilation passed with shell escape disabled. Strict project checks for undefined references, duplicate labels, missing glyphs, overflow and Biber diagnostics passed.
- PDF remains 128 pages. Only physical page 2 has changed character content/layout. All other 127 pages retain identical text, character bounds, sizes and actual font names. Automatically generated six-letter font-subset prefixes are excluded from font-name identity comparison.
- The new abstract page was rendered and inspected. Current PDF geometry, embedded-font, margin and empty-page checks passed. Body tables, equations, algorithms and references remain unchanged.
- `abstract-verification.json` records the comparison; `abstract-build.txt` records compilation. PDF SHA-256 is `08d701b5b070ec8ec9c226d632882a0e9f80c44edbc370618bc763244559e8fc`.

The preceding 107-edit body review remains documented in `REVIEW.md`; its statement that the abstract was then unchanged refers to the earlier stage, before this author-requested follow-up.
