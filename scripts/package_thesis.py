"""Create a portable, locally buildable thesis bundle with compact audit evidence."""
from pathlib import Path
import zipfile,json,hashlib
paths=set()
def add(p):
 p=Path(p)
 if p.is_file():paths.add(p)
def glob(pattern):
 for p in Path('.').glob(pattern):add(p)
for p in ['main.tex','thesis.pdf','Makefile','README.md','thesis-references.bib','THESIS_WRITING_PLAN.md']:add(p)
for pat in ['chapter/ch*.tex','chapter/front*.tex','chapter/tables/*.tex','figures/**/*','bibliography/*.bib','planning/*.md','planning/*.json','planning/*.tsv','planning/*.csv','planning/published/*.pdf','planning/references/*','planning/background-sources/*.json','planning/kglink-sources/*.json','planning/gorag-source/*.bib']:glob(pat)
for p in ['planning/kglink-sources/kglink-author-confirmed-publication.pdf','planning/gorag-source/author-confirmed-publication.pdf']:add(p)
for name in ['LICENSE','README.md','hkustthesis.cls','hkustthesis.dtx','hkustthesis.ins','release.json']:add('template/hkust-thesis-v0.11.6/'+name)
for name in ['build_thesis.py','bib_utils.py','merge_bibliography.py','report_thesis_counts.py','inspect_thesis_pdf.py','check_thesis_assets.py','summarize_pdf_typography.py','package_thesis.py','verify_thesis_package.py']:add('scripts/'+name)
for pat in ['planning/qa/final/*.md','planning/qa/final/*.json','planning/qa/final/*.txt','planning/qa/texcount.txt','planning/qa/style-phrase-counts.json','planning/qa/build-current.txt']:glob(pat)
for pat in ['planning/review-round2/*.md','planning/review-round2/*.json','planning/review-round2/*.txt']:glob(pat)
manifest=[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(paths)]
Path('deliverables/package-manifest.json').write_text(json.dumps(manifest,indent=2))
with zipfile.ZipFile('deliverables/thesis-project-2026-10-25.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(paths):z.write(p,Path('hkust-cse-phd-thesis')/p)
 z.write('deliverables/package-manifest.json','hkust-cse-phd-thesis/PACKAGE_MANIFEST.json')
print(len(paths),'files packaged')
