"""Validate citations with the project's brace-aware reader and preserve research content."""
from pathlib import Path
from collections import Counter
import difflib
import json
import re
import sys

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'scripts'))
from bib_utils import parse

out = Path(__file__).resolve().parent
entries = parse((root / 'thesis-references.bib').read_text())
keys = {}
for e in entries:
    for key in [e['key'], *e['fields'].get('ids', '').split(',')]:
        if not key:
            continue
        assert key not in keys, key
        keys[key] = e['key']
    required = {'article': ['author', 'title', 'journal', 'year'],
                'inproceedings': ['author', 'title', 'booktitle', 'year'],
                'book': ['author', 'title', 'publisher', 'year']}.get(e['type'], ['title'])
    assert all(e['fields'].get(k) for k in required), e['key']

def cites(text):
    return Counter(k.strip() for group in re.findall(r'\\cite\{([^}]*)\}', text)
                   for k in group.split(',') if k.strip())

def noncomments(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)

def content_numbers(text):
    text = re.sub(r'\\(?:cite|ref|label)\{[^}]*\}', '', noncomments(text))
    return re.findall(r'\d+(?:[.,]\d+)*', text)

report = {}
diff = []
all_citations = Counter()
for p in sorted((out / 'before/chapter').glob('*.tex')):
    file = Path('chapter') / p.name
    old, new = p.read_text(), (root / file).read_text()
    before, after = cites(old), cites(new)
    all_citations.update(after)
    assert not before - after, (file, before - after)
    checks = {'numeric_tokens': content_numbers(old) == content_numbers(new),
              'labels': re.findall(r'\\label\{[^}]*\}', old) == re.findall(r'\\label\{[^}]*\}', new),
              'references': re.findall(r'\\ref\{[^}]*\}', old) == re.findall(r'\\ref\{[^}]*\}', new),
              'inline_math': re.findall(r'(?<!\\)\$[^$]*\$', old) == re.findall(r'(?<!\\)\$[^$]*\$', new)}
    for env in ['equation', 'align', 'algorithm', 'figure', 'table', 'tabular', 'longtable']:
        pattern = r'\\begin\{' + env + r'\*?\}.*?\\end\{' + env + r'\*?\}'
        checks[env] = re.findall(pattern, old, re.S) == re.findall(pattern, new, re.S)
    assert all(checks.values()), (file, checks)
    assert not re.search(r'\\cite\{\s*\}', new), file
    report[str(file)] = dict(checks=checks, added_citations=dict(after-before))
    diff.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                   fromfile='before/'+str(file), tofile=str(file)))

# Include citations from every active included table, not only narrative files.
for p in (root / 'chapter/tables').glob('*.tex'):
    all_citations.update(cites(p.read_text()))
missing = sorted(set(all_citations) - set(keys))
assert not missing, missing
report['bibliography'] = dict(unique_works=len(entries), aliases=len(keys)-len(entries),
                              cited_keys=len(all_citations), missing_keys=missing,
                              required_fields='PASS',
                              parser='scripts/bib_utils.py; brace-aware; BibLaTeX ids supported')
(out / 'source-checks.json').write_text(json.dumps(report, indent=2))
(out / 'manuscript.diff').write_text(''.join(diff))
print(json.dumps(report['bibliography'], indent=2))
print('Research-content preservation: PASS in all nine narrative files.')
