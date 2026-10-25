"""Remove source-inherited inconsistent rank emphasis from three reviewed table files."""
from pathlib import Path
import re,json
names=['agrag-efficiency.tex','agrag-ablation.tex','mgrag-matching.tex'];audit=[]
def strip_marks(s):
 pat=r'\\(?:textbf|underline)\{([^{}]*)\}'
 return re.sub(pat,lambda m:m[1] if re.fullmatch(r'[\d.,/\s+\-]+',m[1]) else m[0],s)
for name in names:
 p=Path('chapter/tables')/name;before=p.read_text();after=strip_marks(before)
 after=after.replace('precision and emphasis.','precision.').replace('Original decimal precision and highlighting are preserved.','')
 # Evidence invariance: the complete ordered numeric token stream must stay identical.
 nums=lambda s:re.findall(r'(?<![\w])\d[\d,]*(?:\.\d+)?',s)
 assert nums(before)==nums(after),name
 audit.append({'path':str(p),'numeric_tokens_unchanged':True,'removed_numeric_emphasis':len(re.findall(r'\\(?:textbf|underline)\{[\d.,/\s+\-]+\}',before)),'reason':'Independent review found source-inherited bold/underline marks inconsistent with numeric ranks; keep method-name emphasis and literal measurements.'})
 p.write_text(after)
Path('planning/review-round2/rank-emphasis-changes.json').write_text(json.dumps(audit,indent=2))
# Synchronize the optional generators without regenerating unrelated tables.
p=Path('scripts/prepare_agrag_tables.py');s=p.read_text();s=s.replace('preserve all selected numeric strings/emphasis.','preserve numeric strings; remove inconsistent rank marks in reviewed blocks.')
s=s.replace("def table(title,slug,heads,data,inds,note=''):","def strip_numeric_marks(s):\n return re.sub(r'\\\\(?:textbf|underline)\\{([^{}]*)\\}',lambda m:m[1] if re.fullmatch(r'[\\d.,/\\s+\\-]+',m[1]) else m[0],s)\n\ndef table(title,slug,heads,data,inds,note=''):\n if slug.startswith(('ablation','efficiency')):note=note.replace('precision and emphasis','precision')")
s=s.replace("for r in data:text.append(r[0]+' & '+' & '.join(r[i] for i in inds)+r'\\\\')","for r in data:\n  line=r[0]+' & '+' & '.join(r[i] for i in inds)+r'\\\\'\n  text.append(strip_numeric_marks(line) if slug.startswith(('ablation','efficiency')) else line)")
p.write_text(s)
p=Path('planning/mgrag-build-tables.py');s=p.read_text();s=s.replace('def write_long(name,cols,caption,header,rows):','def write_long(name,cols,caption,header,rows):\n if name==\'matching\':\n  rows=re.sub(r\'\\\\(?:textbf|underline)\\{([^{}]*)\\}\',lambda m:m[1] if re.fullmatch(r\'[\\d.,/\\s+\\-]+\',m[1]) else m[0],rows)\n  caption=caption.replace(\'Original decimal precision and highlighting are preserved.\',\'\')')
p.write_text(s)
# Distinguish the evidence-counterpart variable from a query-edge endpoint.
p=Path('chapter/ch06-mgrag.tex');s=p.read_text();s=s.replace('\\FOR{each $v\\in\\mathcal V_q$ with $\\cos(\\mathbf h_v,\\mathbf h_\\gamma)>\\theta$}','\\FOR{each $v_a\\in\\mathcal V_q$ with $\\cos(\\mathbf h_{v_a},\\mathbf h_\\gamma)>\\theta$}').replace('\\STATE Enumerate candidate mappings consistent with $I(\\gamma)=v$','\\STATE Enumerate candidate mappings consistent with $I(\\gamma)=v_a$');p.write_text(s)
print(audit)
