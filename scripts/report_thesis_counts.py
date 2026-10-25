from pathlib import Path
import re,json
raw=Path('planning/qa/texcount.txt').read_text()
items={m[4]:(int(m[1]),int(m[2]),int(m[3])) for m in re.finditer(r'^\s+(\d+)\+(\d+)\+(\d+) .*Included file: \./([^\s]+)',raw,re.M)}
pre=json.loads(Path('planning/qa/final/pdf-preflight.json').read_text());chapters=[x for x in pre['outline'] if x['level']==0 and re.match(r'^[1-8] ',x['title'])];refs=next(x for x in pre['outline'] if x['title']=='References')
rows=[]
for i,c in enumerate(chapters):
 f=next(p for p in Path('chapter').glob(f'ch0{i+1}-*.tex'));n,h,cap=items[str(f)]
 prefix={4:'gorag-',5:'agrag-',6:'mgrag-'}.get(i+1)
 if prefix:cap+=sum(v[2] for k,v in items.items() if k.startswith('chapter/tables/'+prefix))
 end=(chapters[i+1]['physical_page'] if i<7 else refs['physical_page'])-1
 rows.append({'chapter':i+1,'title':c['title'][2:],'file':str(f),'narrative_words':n,'heading_words':h,'caption_words':cap,'total_non_cell_words':n+h+cap,'printed_pages':f"{c['label']}–{pre['page_labels'][end-1]}",'physical_pages':f"{c['physical_page']}–{end}",'page_count':end-c['physical_page']+1})
main_start=chapters[0]['physical_page'];body_end=refs['physical_page']-1;front_pages=main_start-1;body_pages=refs['physical_page']-main_start;ref_pages=pre['pages']-refs['physical_page']+1
summary={'pdf_sha256':pre['pdf_sha256'],'pdf_total_pages':pre['pages'],'front_matter_pages':front_pages,'body_pages':body_pages,'reference_pages':pre['pages']-refs['physical_page']+1,'chapters':rows,'total_narrative_words':sum(r['narrative_words'] for r in rows),'total_heading_words':sum(r['heading_words'] for r in rows),'total_caption_words':sum(r['caption_words'] for r in rows),'total_non_cell_words':sum(r['total_non_cell_words'] for r in rows),'abstract_words':items['chapter/front-abstract.tex'][0]}
Path('planning/qa/final/chapter-counts.json').write_text(json.dumps(summary,indent=2))
s='''# Chapter word and page counts

Entry: `main.tex`; PDF: `thesis.pdf`. Counts use TeXcount, including prose in the eight chapter files, headings and captions as separate columns. Numeric and textual table cells, equations, bibliography, front matter and comments are excluded from the narrative column. Table captions from included files are assigned to their parent chapter. TeXcount can classify longtable cell labels as prose; these are deliberately excluded from the narrative budget. Page counts come from the actual PDF bookmarks and page labels, not an estimated words-to-pages conversion.

| Chapter | Narrative | Headings | Captions | Total non-cell English words | Printed pages | Pages |
|---|---:|---:|---:|---:|---|---:|
'''
for r in rows:s+=f"| {r['chapter']}. {r['title']} | {r['narrative_words']:,} | {r['heading_words']} | {r['caption_words']} | {r['total_non_cell_words']:,} | {r['printed_pages']} | {r['page_count']} |\n"
s+=f"| **Total** | **{summary['total_narrative_words']:,}** | **{summary['total_heading_words']}** | **{summary['total_caption_words']}** | **{summary['total_non_cell_words']:,}** | **{chapters[0]['label']}–{pre['page_labels'][body_end-1]}** | **{body_pages}** |\n\n"
s+=f"Abstract: {summary['abstract_words']} English words (limit 300). PDF: {pre['pages']} pages, comprising {front_pages} preliminary pages, {body_pages} body pages and {ref_pages} reference pages. Prose, headings and captions are kept separate from numeric table cells and bibliography entries. The independent full-manuscript review removed duplicated scope explanations; its changes are recorded in `planning/review-round2/`.\n\nPDF SHA-256: `{pre['pdf_sha256']}`. Machine-readable counts: `planning/qa/final/chapter-counts.json`; raw counter output: `planning/qa/texcount.txt`.\n"
Path('planning/CHAPTER_COUNTS.md').write_text(s);print(s)
