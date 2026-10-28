# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
| 1. Introduction | 2,130 | 54 | 28 | 2,212 | 1–7 | 7 |
| 2. Background and Related Work | 2,660 | 46 | 83 | 2,789 | 8–16 | 9 |
| 3. Knowledge-enriched Table Understanding with KGLink | 3,256 | 88 | 234 | 3,578 | 17–31 | 15 |
| 4. Adaptive Graph Retrieval for Dynamic Classification with GORAG | 3,017 | 73 | 333 | 3,423 | 32–46 | 15 |
| 5. Connected Evidence Selection for Language Models with AGRAG | 3,384 | 90 | 314 | 3,788 | 47–66 | 20 |
| 6. Semantic Graph Matching for Multimodal Reasoning with MGRAG | 4,352 | 116 | 374 | 4,842 | 67–89 | 23 |
| 7. Discussion | 1,282 | 31 | 47 | 1,360 | 90–94 | 5 |
| 8. Conclusion and Future Directions | 531 | 20 | 0 | 551 | 95–96 | 2 |
| **Total** | **20,612** | **518** | **1413** | **22,543** | **1–96** | **96** |

Abstract: 213 English words (limit 300). PDF: 115 pages, comprising 14 preliminary pages, 96 body pages and 5 reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The current prose-editing review is indexed in `planning/STYLE_AUDIT.md`.

PDF SHA-256: `5adbc3791bd69d19ebf85ba6ed3d20d53f7446dcfd4a4ae4320b49456cd19d32`. Machine-readable counts: `planning/citations-wording-2026-10-28/pdf-qa/chapter-counts.json`; raw counter output: `planning/citations-wording-2026-10-28/texcount.txt`.
