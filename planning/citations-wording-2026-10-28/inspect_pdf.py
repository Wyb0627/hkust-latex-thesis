"""Inspect the revised reading copy with pypdf and Poppler; render review sheets."""
from pathlib import Path
import collections
import hashlib
import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

from pypdf import PdfReader
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parent / 'pdf-qa'
out.mkdir(exist_ok=True)
log = (root / 'main.log').read_text(errors='replace')
issues = [p for p in [r'There were undefined references',
    r'(?:Citation|Reference) .+ undefined', r'Please \(re\)run Biber',
    r'Overfull \\[hv]box', r'Missing character:', r'multiply defined',
    r'destination with the same identifier', r'LaTeX Error:'] if re.search(p, log)]
assert not issues, issues
assert not re.search(r'\b(?:WARN|ERROR)\b', (root / 'main.blg').read_text())
shutil.copy2(root / 'main.pdf', root / 'thesis.pdf')
pdf = root / 'thesis.pdf'
reader = PdfReader(pdf)
labels = reader.page_labels
outline = []

def walk(items, level=0):
    for item in items:
        if isinstance(item, list):
            walk(item, level + 1)
        else:
            page = reader.get_destination_page_number(item)
            outline.append(dict(level=level, title=item.title,
                                physical_page=page + 1, label=labels[page]))

walk(reader.outline)
pages = []
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ''
    pages.append(dict(physical_page=i+1, label=labels[i],
                      size=[round(float(v), 2) for v in page.mediabox[2:]],
                      rotation=page.get('/Rotate', 0), text_length=len(text),
                      first_lines=text.splitlines()[:4]))

for command, filename in [('pdfinfo', 'pdfinfo.txt'), ('pdffonts', 'pdffonts.txt')]:
    with (out / filename).open('w') as stream:
        subprocess.run([command, str(pdf)], stdout=stream, check=True)
subprocess.run(['pdftotext', '-bbox', str(pdf), str(out / 'words.html')], check=True)
tree = ET.parse(out / 'words.html')
outside = []
ns = {'x': 'http://www.w3.org/1999/xhtml'}
for i, page in enumerate(tree.findall('.//x:page', ns)):
    bad = []
    for word in page.findall('x:word', ns):
        x0, x1, y0, y1 = [float(word.attrib[k]) for k in ('xMin', 'xMax', 'yMin', 'yMax')]
        footer = y0 > 775 and 280 < x0 < 320
        if not footer and (x0 < 69 or x1 > 526.3 or y0 < 69 or y1 > 775):
            bad.append(''.join(word.itertext()))
    if bad:
        outside.append(dict(physical_page=i+1, label=labels[i], words=bad))

report = dict(pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
              pages=len(pages), page_labels=labels, outline=outline,
              page_map=pages, encrypted=reader.is_encrypted,
              text_outside_approx_25mm_body=outside,
              extent_method='Poppler pdftotext word bounding boxes, footer excluded')
(out / 'pdf-preflight.json').write_text(json.dumps(report, indent=2))
subprocess.run(['pdftoppm', '-r', '45', '-png', str(pdf), str(out / 'thumb')],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
thumbs = sorted(out.glob('thumb-*.png'))[:len(pages)]
for start in range(0, len(thumbs), 20):
    sheet = Image.new('RGB', (1950, 2320), '#c8c8c8')
    draw = ImageDraw.Draw(sheet)
    for j, path in enumerate(thumbs[start:start+20]):
        im = Image.open(path).convert('RGB')
        im.thumbnail((378, 548))
        x = j % 5 * 390 + (390 - im.width)//2
        y = j // 5 * 580 + 24
        sheet.paste(im, (x, y))
        draw.text((j % 5 * 390 + 12, j // 5 * 580 + 5),
                  f'PDF {start+j+1} / {labels[start+j]}', fill='black')
    sheet.save(out / f'contact-{start//20+1}.png')
print(json.dumps(dict(pages=len(pages), outside=outside,
    chapters=[x for x in outline if x['level']==0]), ensure_ascii=False))
