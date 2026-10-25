"""Verify copied research graphics without modifying image data."""
from pathlib import Path
import json,hashlib,csv
files=['kglink-assets.json','gorag-figure-manifest.json','agrag-assets.json','mgrag-assets.json','background-assets.json']
rows=[]
for name in files:
 for a in json.loads((Path('planning')/name).read_text()):
  src=Path(a.get('source',a.get('source_path','')));dst=Path(a.get('target_path',a.get('target','')))
  sh=hashlib.sha256(src.read_bytes()).hexdigest();dh=hashlib.sha256(dst.read_bytes()).hexdigest()
  rows.append({'manifest':name,'source':str(src),'target':str(dst),'recorded_sha256':a['sha256'],'source_sha256':sh,'target_sha256':dh,'status':'PASS' if a['sha256']==sh==dh else 'FAIL'})
Path('planning/qa/final/asset-hash-verification.json').write_text(json.dumps(rows,indent=2))
assert all(x['status']=='PASS' for x in rows)
print(f'{len(rows)} original research assets: all source/target/manifest hashes match')
