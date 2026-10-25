"""Read-only PDF preflight, structural page map and contact sheets."""
from pathlib import Path
import json,hashlib,subprocess,re,collections,math
from pypdf import PdfReader
import pdfplumber
from PIL import Image,ImageOps,ImageDraw
root=Path('.');out=Path('planning/qa/final');out.mkdir(parents=True,exist_ok=True)
for pattern in ['thumb-*.png','contact-*.png','page-*.txt']:
 for old in out.glob(pattern):old.unlink()
pdf=Path('thesis.pdf');reader=PdfReader(pdf)
labels=reader.page_labels
pages=[];font_counts=collections.Counter();outside=[]
with pdfplumber.open(pdf) as pp:
 for i,p in enumerate(pp.pages):
  txt=p.extract_text() or ''
  # Exclude page number from body extent check; leave figure labels included.
  chars=[c for c in p.chars if c.get('text','').strip()]
  bad=[c for c in chars if (c['x0']<69 or c['x1']>526.3 or c['top']<69 or c['bottom']>775) and not(c['top']>780 and 280<c['x0']<320)]
  if bad:outside.append({'physical_page':i+1,'label':labels[i],'text':''.join(c['text'] for c in bad)[:200]})
  for c in chars:font_counts[(c['fontname'],round(c['size'],2))]+=1
  pages.append({'physical_page':i+1,'label':labels[i],'size':[round(p.width,2),round(p.height,2)],'first_lines':txt.splitlines()[:4],'figures':re.findall(r'Figure\s+\d+\.\d+[^\n]*',txt),'tables':re.findall(r'Table\s+\d+\.\d+[^\n]*',txt),'text_length':len(txt),'rotation':p.rotation})
  (out/f'page-{i+1:03}.txt').write_text(txt)
outline=[]
def walk(xs,level=0):
 for x in xs:
  if isinstance(x,list):walk(x,level+1)
  else:
   try:idx=reader.get_destination_page_number(x)
   except Exception:continue
   outline.append({'level':level,'title':x.title,'physical_page':idx+1,'label':labels[idx]})
walk(reader.outline)
report={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(reader.pages),'encrypted':reader.is_encrypted,'page_labels':labels,'outline':outline,'page_map':pages,'fonts_by_character_count':[{'font':k[0],'size_pdf_points':k[1],'characters':v} for k,v in font_counts.most_common(30)],'text_outside_approx_25mm_body':outside}
(out/'pdf-preflight.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
subprocess.run(['pdfinfo',str(pdf)],stdout=(out/'pdfinfo.txt').open('w'),check=True)
subprocess.run(['pdffonts',str(pdf)],stdout=(out/'pdffonts.txt').open('w'),check=True)
subprocess.run(['pdfimages','-list',str(pdf)],stdout=(out/'pdfimages.txt').open('w'),check=True)
subprocess.run(['pdftoppm','-r','45','-png',str(pdf),str(out/'thumb')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=True)
thumbs=sorted(out.glob('thumb-*.png'))
for start in range(0,len(thumbs),20):
 sheet=Image.new('RGB',(5*390,4*580),'#c8c8c8');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(thumbs[start:start+20]):
  im=Image.open(p).convert('RGB');im.thumbnail((378,548));x=(j%5)*390+(390-im.width)//2;y=(j//5)*580+24
  sheet.paste(im,(x,y));d.text(((j%5)*390+12,(j//5)*580+5),f'PDF {start+j+1} / {labels[start+j]}',fill='black')
 sheet.save(out/f'contact-{start//20+1}.png')
print(json.dumps({'pages':len(pages),'outline_chapters':[x for x in outline if x['level']==0],'outside':outside},ensure_ascii=False))
