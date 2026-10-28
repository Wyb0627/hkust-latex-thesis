# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
| 1. Introduction | 2,190 | 54 | 28 | 2,272 | 1–8 | 8 |
| 2. Background and Related Work | 4,264 | 57 | 83 | 4,404 | 9–22 | 14 |
| 3. Knowledge-enriched Table Understanding with KGLink | 3,256 | 88 | 234 | 3,578 | 23–37 | 15 |
| 4. Adaptive Graph Retrieval for Dynamic Classification with GORAG | 3,017 | 73 | 333 | 3,423 | 38–52 | 15 |
| 5. Connected Evidence Selection for Language Models with AGRAG | 3,384 | 90 | 314 | 3,788 | 53–72 | 20 |
| 6. Semantic Graph Matching for Multimodal Reasoning with MGRAG | 4,352 | 116 | 374 | 4,842 | 73–95 | 23 |
| 7. Discussion | 1,282 | 31 | 47 | 1,360 | 96–100 | 5 |
| 8. Conclusion and Future Directions | 531 | 20 | 0 | 551 | 101–102 | 2 |
| **Total** | **22,276** | **529** | **1413** | **24,218** | **1–102** | **102** |

Abstract: 213 English words (limit 300). PDF: 125 pages, comprising 14 preliminary pages, 102 body pages and 9 reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The current prose-editing review is indexed in `planning/STYLE_AUDIT.md`.

PDF SHA-256: `11951828b2f94db09b2b8ceefb5c0b61c3bb30ab4a388a20b86ecec2ac556d82`. Machine-readable counts: `planning/qa/final/chapter-counts.json`; raw counter output: `planning/qa/texcount.txt`.
