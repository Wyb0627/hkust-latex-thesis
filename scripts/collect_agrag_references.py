from pathlib import Path
import re,json
p=Path('/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/ICDE2026.bib')
s=p.read_text();entries={}
for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,',s):
 depth=1;i=m.end()
 while i<len(s) and depth:
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
  i+=1
 entries[m[2]]=s[m.start():i]
keys=['tfidf','haveliwala2002topic','robertson2009probabilistic','mehlhorn1988faster','izacardunsupervised','ragas2024','xiang2025use','qwen2025qwen25technicalreport','kwon2023efficient','bge_embedding','kowsari2017hdltex','xia-etal-2021-incremental','lin2004rouge','edge2024local','guo2024lightrag','gutiérrez2025ragmemory','sarthi2024raptor','zhang2025sirerag','he2024g','liu2025mixrag','fastgraphrag','jiang-etal-2024-longllmlingua']
out=[]
for k in keys:
 if k not in entries:raise SystemExit('Missing '+k)
 out.append(re.sub(r'(@\w+\s*\{\s*)'+re.escape(k)+',',r'\g<1>agrag-'+k+',',entries[k],count=1))
Path('bibliography/agrag-related.bib').write_text('% Source entries from selected AGRAG bibliography; metadata checks in central audit.\n\n'+'\n\n'.join(out)+'\n')
Path('planning/agrag-related-reference-map.json').write_text(json.dumps({k:'agrag-'+k for k in keys},indent=2,ensure_ascii=False))
print(len(out),'references collected')
