# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
| 1. Introduction | 2,345 | 58 | 36 | 2,439 | 1–8 | 8 |
| 2. Background and Related Work | 3,620 | 46 | 83 | 3,749 | 9–19 | 11 |
| 3. Knowledge-enriched Table Understanding with KGLink | 4,034 | 88 | 234 | 4,356 | 20–37 | 18 |
| 4. Adaptive Graph Retrieval for Dynamic Classification with GORAG | 3,790 | 73 | 333 | 4,196 | 38–53 | 16 |
| 5. Connected Evidence Selection for Language Models with AGRAG | 4,148 | 90 | 314 | 4,552 | 54–75 | 22 |
| 6. Semantic Graph Matching for Multimodal Reasoning with MGRAG | 5,315 | 116 | 374 | 5,805 | 76–100 | 25 |
| 7. Discussion | 1,670 | 30 | 47 | 1,747 | 101–106 | 6 |
| 8. Conclusion and Future Directions | 682 | 20 | 0 | 702 | 107–109 | 3 |
| **Total** | **25,604** | **521** | **1421** | **27,546** | **1–109** | **109** |

Abstract: 206 English words (limit 300). PDF: 128 pages, comprising 14 preliminary pages, 109 body pages and 5 reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The current prose-editing review is indexed in `planning/STYLE_AUDIT.md`.

PDF SHA-256: `08d701b5b070ec8ec9c226d632882a0e9f80c44edbc370618bc763244559e8fc`. Machine-readable counts: `planning/qa/final/chapter-counts.json`; raw counter output: `planning/qa/texcount.txt`.
