"""Fresh-build the current archive, and record text and compiled-input identity."""
from pathlib import Path
import hashlib,json,subprocess,tempfile,zipfile

archive=Path('deliverables/thesis-project-2026-10-25.zip')
out=Path('planning/qa/final')
def digest(data):return hashlib.sha256(data).hexdigest()
def is_input(path):
 return path in ['main.tex','Makefile','thesis-references.bib'] or path.startswith(('chapter/','figures/','bibliography/','template/','scripts/'))
with zipfile.ZipFile(archive) as z:
 manifest=json.loads(z.read('hkust-cse-phd-thesis/PACKAGE_MANIFEST.json'))
 for entry in manifest:
  assert digest(z.read('hkust-cse-phd-thesis/'+entry['path']))==entry['sha256'],entry['path']
 inputs=[{'path':e['path'],'sha256':e['sha256']} for e in manifest if is_input(e['path'])]
 fingerprint=digest(json.dumps(inputs,sort_keys=True,separators=(',',':')).encode())
 for e in inputs:assert digest(Path(e['path']).read_bytes())==e['sha256'],e['path']
 with tempfile.TemporaryDirectory(prefix='thesis-round2-build-') as tmp:
  z.extractall(tmp)
  project=Path(tmp)/'hkust-cse-phd-thesis'
  (project/'thesis.pdf').unlink()
  with (out/'package-build.txt').open('w') as log:
   result=subprocess.run(['make'],cwd=project,stdout=log,stderr=subprocess.STDOUT)
  assert result.returncode==0,'See planning/qa/final/package-build.txt'
  delivered=subprocess.check_output(['pdftotext','-layout','thesis.pdf','-'])
  rebuilt=subprocess.check_output(['pdftotext','-layout',str(project/'thesis.pdf'),'-'])
  info=subprocess.check_output(['pdfinfo',str(project/'thesis.pdf')],text=True)
  pages=int(next(line.split(':',1)[1] for line in info.splitlines() if line.startswith('Pages:')))
  expected=json.loads((out/'chapter-counts.json').read_text())
  assert pages==expected['pdf_total_pages']
  assert delivered==rebuilt,'Rebuilt PDF text differs'
  report={'review_date':'2026-10-25','archive':str(archive),'build_exit_code':result.returncode,'page_count':pages,'delivered_pdf_sha256':digest(Path('thesis.pdf').read_bytes()),'pdf_text_matches_delivered':True,'delivered_text_sha256':digest(delivered),'rebuilt_text_sha256':digest(rebuilt),'compiled_input_manifest_sha256':fingerprint,'compiled_inputs':inputs,'verification_scope':'Fresh temporary-directory extraction; all manifest hashes checked, reading PDF removed, make from no generated auxiliary files; identical extracted PDF text and page count. Later archive updates may add documentation only; compiled-input fingerprint must remain unchanged.'}
(out/'package-build-verification.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='compiled_inputs'},indent=2))
