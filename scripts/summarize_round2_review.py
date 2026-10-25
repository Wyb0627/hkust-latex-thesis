"""Record review deltas and exact invariance checks against the pre-review manuscript."""
from pathlib import Path
import re,tarfile,json,hashlib,collections
out=Path('planning/review-round2');files=[Path('chapter/front-abstract.tex'),*sorted(Path('chapter').glob('ch*.tex'))]
patterns={'reported':r'\breported\b','published':r'\bpublished\b','rather than':r'\brather than\b','should':r'\bshould\b','protocol':r'\bprotocol\b','does not':r'\bdoes not\b','we do not claim':r'\bwe do not claim\b','for a fair comparison':r'\bfor a fair comparison\b','it should be noted':r'\bit should be noted\b','taken together':r'\btaken together\b'}
clean=lambda s:re.sub(r'(?m)(?<!\\)%.*$','',s)
with tarfile.open(out/'before-manuscript.tar.gz') as tar:
 before='\n'.join(clean(tar.extractfile(str(p)).read().decode()) for p in files)
 after='\n'.join(clean(p.read_text()) for p in files)
 counts={k:{'before':len(re.findall(p,before,re.I)),'after':len(re.findall(p,after,re.I))} for k,p in patterns.items()}
 formula=[]
 for p in files[1:]:
  a=tar.extractfile(str(p)).read().decode();b=p.read_text();math=lambda s:[m[0] for m in re.finditer(r'\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}',s,re.S)]
  ma,mb=math(a),math(b);assert ma==mb,p;formula.append({'file':str(p),'formula_blocks':len(ma),'formula_blocks_byte_identical':True})
 tables=[]
 for p in sorted(Path('chapter/tables').glob('*.tex')):
  a=tar.extractfile(str(p)).read().decode();b=p.read_text();num=lambda s:re.findall(r'(?<![\w])\d[\d,]*(?:\.\d+)?',s)
  assert num(a)==num(b),p;tables.append({'path':str(p),'numeric_token_stream_identical':True,'tokens':len(num(b))})
report={'review_date':'2026-10-25','before_pdf_sha256':json.loads((out/'before-hashes.json').read_text())['thesis.pdf'],'after_pdf_sha256':hashlib.sha256(Path('thesis.pdf').read_bytes()).hexdigest(),'formula_blocks':sum(x['formula_blocks'] for x in formula),'formula_checks':formula,'table_file_count':len(tables),'table_checks':tables,'result':'PASS; all original formula blocks and table numeric token streams unchanged; restored anchor-loop exposition checked separately against publisher Algorithm1'}
(out/'invariance-check.json').write_text(json.dumps(report,indent=2));(out/'phrase-counts.json').write_text(json.dumps(counts,indent=2))
# A label inventory excludes cleveref companion labels.
aux=Path('main.aux').read_text();extract=lambda prefix:[x for x in re.findall(r'\\newlabel\{('+prefix+r':[^}]+)\}\{\{([^}]+)\}\{([^}]+)',aux) if not x[0].endswith('@cref')]
Path('planning/qa/final/table-figure-labels.json').write_text(json.dumps({'tables':extract('tab'),'figure_labels':extract('fig')},indent=2))
print(report['formula_blocks'],report['table_file_count'],counts)
