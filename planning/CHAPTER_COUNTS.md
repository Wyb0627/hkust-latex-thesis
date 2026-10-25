# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
| 1. Introduction | 2,489 | 58 | 36 | 2,583 | 1–8 | 8 |
| 2. Background and Related Work | 3,892 | 46 | 83 | 4,021 | 9–20 | 12 |
| 3. Knowledge-enriched Table Understanding with KGLink | 4,337 | 88 | 234 | 4,659 | 21–39 | 19 |
| 4. Adaptive Graph Retrieval for Dynamic Classification with GORAG | 4,162 | 73 | 333 | 4,568 | 40–56 | 17 |
| 5. Connected Evidence Selection for Language Models with AGRAG | 4,568 | 90 | 314 | 4,972 | 57–78 | 22 |
| 6. Semantic Graph Matching for Multimodal Reasoning with MGRAG | 5,763 | 116 | 374 | 6,253 | 79–104 | 26 |
| 7. Discussion | 1,907 | 30 | 47 | 1,984 | 105–111 | 7 |
| 8. Conclusion and Future Directions | 725 | 20 | 0 | 745 | 112–114 | 3 |
| **Total** | **27,843** | **521** | **1421** | **29,785** | **1–114** | **114** |

Abstract: 261 English words (limit 300). PDF: 133 pages, comprising 14 preliminary pages, 114 body pages and 5 reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The independent full-manuscript review removed duplicated scope explanations; its changes are recorded in `planning/review-round2/`.

PDF SHA-256: `f44abbdbc4bceb3ba9e73fe42b6b032f22d94aa9ceb40068d3e7280707b40905`. Machine-readable counts: `planning/qa/final/chapter-counts.json`; raw counter output: `planning/qa/texcount.txt`.
