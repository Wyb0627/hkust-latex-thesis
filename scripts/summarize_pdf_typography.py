"""Summarize actual PDF fonts/geometry and retain original image-resolution limits."""
from pathlib import Path
import json,re,statistics
import pdfplumber
out=Path('planning/qa/final');j=json.loads((out/'pdf-preflight.json').read_text())
fonts=(out/'pdffonts.txt').read_text().splitlines()[2:]
records=[re.search(r'\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$',x).groups() for x in fonts]
rasters=[]
for l in (out/'pdfimages.txt').read_text().splitlines()[2:]:
 a=l.split()
 if len(a)>=16:rasters.append({'page':int(a[0]),'type':a[2],'width':int(a[3]),'height':int(a[4]),'ppi':[int(a[12]),int(a[13])]})
main=next(x for x in j['outline'] if x['title']=='1 Introduction')['physical_page']
with pdfplumber.open('thesis.pdf') as pdf:
 p=pdf.pages[main];ys=sorted(set(round(c['top'],2) for c in p.chars if abs(c['size']-11.955)<.02 and c['top']<775));ds=[round(b-a,2) for a,b in zip(ys,ys[1:]) if 18<b-a<24]
report={'pdf_sha256':j['pdf_sha256'],'pages':j['pages'],'all_A4':all(x['size']==[595.28,841.89] for x in j['page_map']),'all_unrotated':all(x['rotation']==0 for x in j['page_map']),'embedded_font_count':len(records),'all_fonts_embedded':all(r[0]=='yes' for r in records),'all_fonts_subset':all(r[1]=='yes' for r in records),'fonts_without_unicode':sum(r[2]=='no' for r in records),'raster_min_ppi':min(min(r['ppi']) for r in rasters),'raster_instances_below_300ppi':[r for r in rasters if min(r['ppi'])<300],'body_baseline_median_pdf_points':statistics.median(ds),'body_size_pdf_points':11.955,'margin_violations_excluding_centered_page_numbers':j['text_outside_approx_25mm_body'],'empty_text_pages':[p['physical_page'] for p in j['page_map'] if p['text_length']<15]}
(out/'typography-summary.json').write_text(json.dumps(report,indent=2))
assert report['all_A4'] and report['all_fonts_embedded'] and not report['margin_violations_excluding_centered_page_numbers'] and not report['empty_text_pages']
print(json.dumps(report,indent=2))
