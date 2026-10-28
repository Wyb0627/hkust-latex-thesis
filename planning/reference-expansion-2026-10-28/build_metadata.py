"""Import inspected primary records while retaining original-library provenance."""
from pathlib import Path
import difflib, json, re, sys
root=Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'scripts'))
from bib_utils import dump,norm

shortlist=json.loads((out/'shortlist.json').read_text())
records={r['key']:r for r in json.loads((out/'primary-verification.json').read_text())}
entries=[];ledger=[]
tokens=['WebTables','TURL','ColNet','TCN','XLNet','SimplE','NeuInfer','HAHE','KnowGPT','H2O','KV','LLMs','LLM','BERT','ColBERT','VQA','BLIP-2','BLIP','InstructBLIP','ViLBERT','TAPAS','TaPas','TableFormer','TriviaQA','FlashAttention','Atlas','Scissorhands','IO','2D']
def protect(title):
    return re.sub(r'\b('+ '|'.join(re.escape(t) for t in sorted(tokens,key=len,reverse=True))+r')\b',r'{\1}',title)
def safe(s): return str(s).replace('&',r'\&')
for candidate in shortlist:
    key=candidate['key'];r=records[key];assert r['status']=='FETCHED',key
    f={};url=r['requested_url']
    if 'crossref' in r:
        c=r['crossref'];title=c['title'][0]
        if c.get('subtitle'):title+=': '+c['subtitle'][0]
        f.update(title=title,author=' and '.join(a['family']+', '+a.get('given','') for a in c['author']),
                 year=str(c['published']['date-parts'][0][0]),doi=c['DOI'])
        container=c['container-title'][0]
        journal=key in ['cafarella2008webtables','deng2022turl','wang2020generalizing']
        typ='article' if journal else 'inproceedings'
        f['journal' if journal else 'booktitle']=container
        for field in ['volume','page','issue']:
            if c.get(field):
                value=str(c[field]).replace('–','--')
                if field=='page':value=re.sub(r'(?<=\d)-(?=\d)','--',value)
                f[{'page':'pages','issue':'number'}.get(field,field)]=value
        f['url']='https://doi.org/'+c['DOI']
        venue= 'CSUR' if key=='wang2020generalizing' else ('VLDB' if journal else ('SIGIR' if key=='khattab2020colbert' else 'WWW'))
    else:
        m=r['meta']
        def first(name,default=''):return m.get(name,[default])[0]
        assert first('citation_title') and m.get('citation_author'),key
        title=first('citation_title').removeprefix('♫ ')
        f.update(title=title,author=' and '.join(m['citation_author']),
                 year=re.search(r'\d{4}',first('citation_publication_date',first('citation_date')))[0],url=url)
        if 'neurips.cc' in url:
            typ='inproceedings';venue='NeurIPS';f['booktitle']='Advances in Neural Information Processing Systems'
        elif 'mlr.press' in url:
            typ='inproceedings';venue='ICML';f['booktitle']='Proceedings of the International Conference on Machine Learning'
            f['volume']=re.search(r'/v(\d+)/',url)[1];f['series']='Proceedings of Machine Learning Research';f['publisher']='PMLR'
        elif 'ojs.aaai.org' in url:
            typ='inproceedings';venue='AAAI';f['booktitle']='Proceedings of the AAAI Conference on Artificial Intelligence'
        elif 'thecvf.com' in url:
            typ='inproceedings';venue='ICCV' if 'iccv' in url.lower() else 'CVPR'
            f['booktitle']=('Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)' if venue=='CVPR' else 'Proceedings of the IEEE International Conference on Computer Vision (ICCV)')
        elif 'jmlr.org' in url:
            typ='article';venue='JMLR';f['journal']='Journal of Machine Learning Research'
        elif 'aclanthology.org' in url:
            typ='article' if key in ['liu2024lost','kwiatkowski2019natural','trivedi2022musique'] else 'inproceedings'
            venue='TACL' if typ=='article' else 'ACL'
            f['journal' if typ=='article' else 'booktitle']=first('citation_journal_title') if typ=='article' else first('citation_conference_title')
            if not f.get('booktitle') and typ=='inproceedings':
                # Official Anthology BibTeX is used for the full proceedings name.
                from bib_utils import parse
                be=parse(Path(r['bib_path']).read_text())[0]
                f['booktitle']=be['fields']['booktitle']
            if typ=='article' and not f['journal']:f['journal']='Transactions of the Association for Computational Linguistics'
        else:raise AssertionError(key)
        for meta,field in [('citation_volume','volume'),('citation_issue','number'),('citation_doi','doi')]:
            if first(meta):f[field]=first(meta)
        if first('citation_firstpage') and first('citation_lastpage'):
            f['pages']=first('citation_firstpage')+'--'+first('citation_lastpage')
    similarity=difflib.SequenceMatcher(None,norm(title),norm(candidate['fields']['title'])).ratio()
    assert similarity>0.94,(key,title,candidate['fields']['title'],similarity)
    assert venue in ['AAAI','ACL','CVPR','ICCV','ICML','NeurIPS','SIGIR','WWW','VLDB','JMLR','TACL','CSUR'],venue
    f={k:safe(v) for k,v in f.items() if v}
    f['title']=protect(f['title'])
    f['author']=f['author'].replace('ichter, brian','Ichter, Brian').replace('koray kavukcuoglu','Koray Kavukcuoglu').replace('DONGXU LI','Dongxu Li')
    entry=dict(type=typ,key=candidate['thesis_key'],fields=f);entries.append(entry)
    ledger.append(dict(key=entry['key'],title=title,year=f['year'],venue=venue,
                       qualification='CCF A conference full paper' if venue not in ['JMLR','TACL','CSUR'] else 'Published journal article',
                       original_source=candidate['source'],original_key=key,
                       primary_url=url,primary_record=r['path'],
                       metadata_source='Publisher citation meta tags' if 'meta' in r else 'Publisher-deposited Crossref record'))
assert len(entries)==56
(root/'bibliography/literature-expansion.bib').write_text('% Primary-verified additions; provenance and claim map in planning/reference-expansion-2026-10-28/.\n\n'+'\n'.join(dump(e) for e in entries))
(out/'reference-ledger.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False))
print('Imported',len(entries),'primary-verified published works.')
print('Original libraries:',sum(r['original_source']!='external-primary-search' for r in ledger),'External:',sum(r['original_source']=='external-primary-search' for r in ledger))
