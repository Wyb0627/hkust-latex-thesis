# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
| 1. Introduction | 2,111 | 54 | 28 | 2,193 | 1–7 | 7 |
| 2. Background and Related Work | 2,671 | 46 | 83 | 2,800 | 8–16 | 9 |
| 3. Knowledge-enriched Table Understanding with KGLink | 3,257 | 88 | 234 | 3,579 | 17–31 | 15 |
| 4. Adaptive Graph Retrieval for Dynamic Classification with GORAG | 3,020 | 73 | 333 | 3,426 | 32–46 | 15 |
| 5. Connected Evidence Selection for Language Models with AGRAG | 3,386 | 90 | 314 | 3,790 | 47–66 | 20 |
| 6. Semantic Graph Matching for Multimodal Reasoning with MGRAG | 4,350 | 116 | 374 | 4,840 | 67–89 | 23 |
| 7. Discussion | 1,277 | 31 | 47 | 1,355 | 90–94 | 5 |
| 8. Conclusion and Future Directions | 522 | 20 | 0 | 542 | 95–96 | 2 |
| **Total** | **20,594** | **518** | **1413** | **22,525** | **1–96** | **96** |

Abstract: 207 English words (limit 300). PDF: 115 pages, comprising 14 preliminary pages, 96 body pages and 5 reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The current prose-editing review is indexed in `planning/STYLE_AUDIT.md`.

PDF SHA-256: `c33dcf2714d92fd4c62d730feead96561de4a6f401244ca53f649b5374777f26`. Machine-readable counts: `planning/research-thread-2026-10-27/chapter-counts.json`; raw counter output: `planning/qa/texcount.txt`.
