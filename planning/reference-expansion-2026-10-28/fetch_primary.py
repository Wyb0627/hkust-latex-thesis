"""Fetch identified primary records; record failures without substituting sources."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
import hashlib, html, json, re, subprocess, sys

out = Path(__file__).resolve().parent
raw = out / 'primary-records'
raw.mkdir(exist_ok=True)

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.meta = {}; self.links = []; self.text = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta':
            name = a.get('name', a.get('property', '')).lower()
            if name: self.meta.setdefault(name, []).append(a.get('content', ''))
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
    def handle_data(self, s):
        if s.strip(): self.text.append(s.strip())

def get(url):
    result = subprocess.run(['curl','--fail','--location','--compressed','--silent','--show-error',
                             '--max-time','35',url],capture_output=True,check=True)
    return result.stdout.decode('utf-8',errors='replace'), url

def fetch(record):
    key, url = record['key'], record['primary_url']
    row = dict(key=key, requested_url=url)
    try:
        body, resolved = get(url)
        path = raw / (key + ('.json' if 'api.crossref.org' in url else '.html'))
        path.write_text(body)
        row.update(status='FETCHED', resolved_url=resolved, path=str(path), sha256=hashlib.sha256(body.encode()).hexdigest())
        if 'api.crossref.org' in url:
            row['crossref'] = json.loads(body)['message']
        else:
            p = Page(); p.feed(body); row.update(meta=p.meta, text='\n'.join(p.text))
            biburl = None
            if 'aclanthology.org' in url: biburl = url.rstrip('/')+'.bib'
            elif 'neurips.cc' in url:
                biburl = next((link for link in p.links if link.lower().endswith('bibtex.bib')), None)
                if biburl and biburl.startswith('/'): biburl = 'https://proceedings.neurips.cc'+biburl
            if biburl:
                try:
                    bib, _ = get(biburl); (raw/(key+'.bib')).write_text(bib); row['bib_path'] = str(raw/(key+'.bib'))
                except Exception as exc: row['bib_fetch_error'] = repr(exc)
            else:
                m = re.search(r'<pre[^>]*id=["\']bibtex["\'][^>]*>(.*?)</pre>', body, re.S|re.I)
                if m:
                    bib = html.unescape(re.sub('<[^>]+>', '', m[1])); (raw/(key+'.bib')).write_text(bib); row['bib_path'] = str(raw/(key+'.bib'))
    except Exception as exc:
        row.update(status='FETCH_ERROR', error=repr(exc))
    return row

records=json.loads((out/'primary-urls.json').read_text())
if len(sys.argv)>1:
    records=[r for r in records if r['key'] in sys.argv[1:]]
results=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    for future in as_completed([pool.submit(fetch, record) for record in records]):
        row=future.result();results.append(row)
        print(f'[{len(results)}/{len(records)}] {row["key"]}: {row["status"]}', flush=True)
if len(sys.argv)>1 and (out/'primary-verification.json').exists():
    changed={r['key'] for r in results}
    results += [r for r in json.loads((out/'primary-verification.json').read_text()) if r['key'] not in changed]
results.sort(key=lambda r:r['key'])
(out/'primary-verification.json').write_text(json.dumps(results,indent=2,ensure_ascii=False))
print('Complete. Failures:', [r['key'] for r in results if r['status']!='FETCHED'])
