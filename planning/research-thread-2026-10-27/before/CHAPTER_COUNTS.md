# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
| 1. Introduction | 1,909 | 58 | 36 | 2,003 | 1–7 | 7 |
| 2. Background and Related Work | 2,698 | 46 | 83 | 2,827 | 8–16 | 9 |
| 3. Knowledge-enriched Table Understanding with KGLink | 3,252 | 88 | 234 | 3,574 | 17–31 | 15 |
| 4. Adaptive Graph Retrieval for Dynamic Classification with GORAG | 2,905 | 73 | 333 | 3,311 | 32–46 | 15 |
| 5. Connected Evidence Selection for Language Models with AGRAG | 3,324 | 90 | 314 | 3,728 | 47–66 | 20 |
| 6. Semantic Graph Matching for Multimodal Reasoning with MGRAG | 4,306 | 116 | 374 | 4,796 | 67–89 | 23 |
| 7. Discussion | 1,090 | 30 | 47 | 1,167 | 90–94 | 5 |
| 8. Conclusion and Future Directions | 491 | 20 | 0 | 511 | 95–96 | 2 |
| **Total** | **19,975** | **521** | **1421** | **21,917** | **1–96** | **96** |

Abstract: 206 English words (limit 300). PDF: 115 pages, comprising 14 preliminary pages, 96 body pages and 5 reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The current prose-editing review is indexed in `planning/STYLE_AUDIT.md`.

PDF SHA-256: `2e0fa332ed7ffd94111d25b45640d4fcf60e24baa97b90d277ae13c9f3941a87`. Machine-readable counts: `planning/qa/final/chapter-counts.json`; raw counter output: `planning/qa/texcount.txt`.
