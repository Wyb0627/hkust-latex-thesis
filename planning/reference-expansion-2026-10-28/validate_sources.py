"""Count actually cited independent papers and preserve scientific source content."""
from pathlib import Path
from collections import Counter
import difflib, json, re, sys
root=Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'scripts'))
from bib_utils import parse,norm

def citation_counter(s):
    return Counter(k.strip() for group in re.findall(r'\\cite\{([^}]+)\}',s) for k in group.split(','))
def index(entries):
    result={}
    for e in entries:
        for k in [e['key'],*e['fields'].get('ids','').split(',')]:
            if k:
                assert k not in result,k
                result[k]=e['key']
    return result
entries=parse((root/'thesis-references.bib').read_text())
oldentries=parse((out/'before/thesis-references.bib').read_text())
keys,oldkeys=index(entries),index(oldentries)
oldc,currentc=set(),set()
checks={};diff=[];chapter_counts={}
for before in sorted((out/'before/chapter').glob('*.tex')):
    f=Path('chapter')/before.name;a,b=before.read_text(),(root/f).read_text()
    ca,cb=citation_counter(a),citation_counter(b)
    assert not ca-cb,(f,ca-cb)
    la,lb=Counter(re.findall(r'\\label\{[^}]*\}',a)),Counter(re.findall(r'\\label\{[^}]*\}',b))
    row=dict(original_citations_retained=True,original_labels_retained=not bool(la-lb),
             no_duplicate_labels=all(v==1 for v in lb.values()))
    for env in ['equation','align','algorithm','figure','table','tabular','longtable']:
        pat=r'\\begin\{'+env+r'\*?\}.*?\\end\{'+env+r'\*?\}'
        row[env+'_unchanged']=re.findall(pat,a,re.S)==re.findall(pat,b,re.S)
    row['inline_math_unchanged']=re.findall(r'(?<!\\)\$[^$]*\$',a)==re.findall(r'(?<!\\)\$[^$]*\$',b)
    if before.name not in ['ch01-introduction.tex','ch02-background.tex']:row['byte_identical']=a==b
    assert all(row.values()),(f,row)
    assert not re.search(r'\\cite\{\s*\}',b),f
    checks[str(f)]=row
    oldset={oldkeys[k] for k in ca};newset={keys[k] for k in cb}
    oldc.update(oldset);currentc.update(newset)
    chapter_counts[str(f)]={'before':len(oldset),'after':len(newset)}
    diff.extend(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='before/'+str(f),tofile=str(f)))
for p in (root/'chapter/tables').glob('*.tex'):
    cs=citation_counter(p.read_text());oldc.update(oldkeys[k] for k in cs);currentc.update(keys[k] for k in cs)
new=currentc-oldc
expected={e['key'] for e in entries if e['key'].startswith('lit-')}
assert new==expected and len(new)==56

# Conservative paper count: these six retained references do not add independent papers.
excluded={
    'agrag-tfidf':'Encyclopedia entry, not a research paper',
    'agrag-ragas2024':'Software repository; the separate RAGAs paper is counted',
    'agrag-fastgraphrag':'Software repository',
    'kglink-hassanzadeh_oktie_2019_3518539':'Dataset release',
    'mgrag-tech-report':'Supplementary report for the already counted MGRAG paper',
    'mgrag-nanographrag':'Software repository',
}
assert set(excluded)<=currentc
paper_count=len(currentc-set(excluded))
assert len(oldc)==73 and len(currentc)==129 and paper_count==123
assert paper_count>120

ledger=json.loads((out/'reference-ledger.json').read_text())
for row in ledger:
    row['locations']=[]
    for name in ['chapter/ch01-introduction.tex','chapter/ch02-background.tex']:
        text=(root/name).read_text()
        for paragraph in text.split('\n\n'):
            if row['key'] in paragraph:
                row['locations'].append(dict(file=name,line=text[:text.index(paragraph)].count('\n')+1,paragraph=paragraph))
    assert row['locations'],row['key']
    assert row['qualification'] in ['CCF A conference full paper','Published journal article']
    e=next(e for e in entries if e['key']==row['key']);f=e['fields']
    assert f.get('author') and f.get('year') and f.get('url'),e['key']
    assert 'findings' not in f.get('booktitle','').lower(),e['key']
(out/'reference-ledger.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False))
report=dict(baseline_cited_unique=len(oldc),current_cited_unique=len(currentc),new_cited_unique=len(new),
            independent_paper_count=paper_count,excluded_from_paper_count=excluded,
            merged_database_entries=len(entries),uncited_database_entries=sorted({e['key'] for e in entries}-currentc),
            chapter_counts=chapter_counts,checks=checks,
            new_sources={'original_libraries':sum(r['original_source']!='external-primary-search' for r in ledger),
                         'external_primary_search':sum(r['original_source']=='external-primary-search' for r in ledger)})
(out/'source-checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
(out/'manuscript.diff').write_text(''.join(diff))
print(json.dumps({k:report[k] for k in ['baseline_cited_unique','current_cited_unique','independent_paper_count','new_cited_unique','new_sources']},indent=2))
print('All preserved scientific content checks: PASS.')
