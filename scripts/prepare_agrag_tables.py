"""Split active AGRAG tables by task; preserve numeric strings; remove inconsistent rank marks in reviewed blocks."""
from pathlib import Path
import re,json
src=Path('/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/AGRAG_GORAG/section/sec-experiment_results_sigmod.tex').read_text()
src=re.sub(r'\\begin\{comment\}.*?\\end\{comment\}','',src,flags=re.S)
src='\n'.join(re.sub(r'(?<!\\)%.*','',l) for l in src.splitlines())
blocks={}
for m in re.finditer(r'\\begin\{table\*?\}.*?\\end\{table\*?\}',src,re.S):
 lab=re.search(r'\\label\{([^}]+)\}',m.group())
 if lab:blocks[lab[1]]=m.group()
records=[]
def rows(label,n,methodcol):
 out=[]
 for line in blocks[label].splitlines():
  cells=line.split('&')
  if len(cells)==n and re.search(r'\d',cells[methodcol+1]):
   cells=[c.strip().removesuffix('\\\\').strip().replace('\\uline','\\underline') for c in cells]
   if any(w in cells[methodcol] for w in ['textbf{Category','textbf{Models','textbf{Model','textbf{Metric','textbf{Dataset']):continue
   out.append([cells[methodcol]]+cells[methodcol+1:])
 return out
def strip_numeric_marks(s):
 return re.sub(r'\\(?:textbf|underline)\{([^{}]*)\}',lambda m:m[1] if re.fullmatch(r'[\d.,/\s+\-]+',m[1]) else m[0],s)

def table(title,slug,heads,data,inds,note=''):
 if slug.startswith(('ablation','efficiency')):note=note.replace('precision and emphasis','precision')
 text=[r'\begin{table}[tbp]',r'\centering\small',r'\setlength{\tabcolsep}{3pt}',r'\caption{'+title+'. '+note+r'}',r'\label{tab:agrag:'+slug+'}',r'\resizebox{\textwidth}{!}{%',r'\begin{tabular}{l'+'r'*len(inds)+'}',r'\toprule','Method & '+' & '.join(heads)+r'\\',r'\midrule']
 for r in data:
  line=r[0]+' & '+' & '.join(r[i] for i in inds)+r'\\'
  text.append(strip_numeric_marks(line) if slug.startswith(('ablation','efficiency')) else line)
 text += [r'\bottomrule',r'\end{tabular}}',r'\end{table}']
 records.append({'label':slug,'rows':[[r[0]]+[r[i] for i in inds] for r in data]})
 return '\n'.join(text)+'\n'
main=rows('tab:main_exp',24,1);assert len(main)==11,len(main)
segments=[('creative','Creative generation',list(range(1,7)),['Novel FS','Novel ACC','Novel COV','Medical FS','Medical ACC','Medical COV']),('summary','Contextual summarization',list(range(7,11)),['Novel COV','Novel ACC','Medical COV','Medical ACC']),('complex','Complex reasoning',list(range(11,15)),['Novel ROG','Novel ACC','Medical ROG','Medical ACC']),('fact','Fact retrieval',list(range(15,19)),['Novel ROG','Novel ACC','Medical ROG','Medical ACC']),('class','Text classification',list(range(19,23)),['WOS ACC','WOS REC','IFS-Rel ACC','IFS-Rel REC'])]
for slug,title,inds,heads in segments:
 Path(f'chapter/tables/agrag-main-{slug}.tex').write_text(table(title+' with Qwen2.5-14B-Instruct','main-'+slug,heads,main,inds,r'Results from the AGRAG main experiment~\cite{agrag-paper}.'))
eff=rows('tab:efficiency',10,1);assert len(eff)==11,len(eff)
t=table('Indexing / querying time in minutes','efficiency',['Novel','Medical','WOS','IFS-Rel'],eff,[1,2,3,4],'Qwen2.5-14B-Instruct; original paired measurements are preserved.')
t+=table('Input / output tokens per query','efficiency-tokens',['Novel','Medical','WOS','IFS-Rel'],eff,[5,6,7,8],'Same source experiment as the preceding time table.')
Path('chapter/tables/agrag-efficiency.tex').write_text(t)
abl=rows('tab:abl_exp',23,0);assert len(abl)==6,len(abl)
t=''
for slug,title,inds,heads in segments[:4]:
 t+=table(title+' ablation with Qwen2.5-14B-Instruct','ablation' if slug=='creative' else 'ablation-'+slug,heads,abl,inds,'Values retain the original source ablation precision and emphasis.')
t+=table('Ablation time and token costs','ablation-cost',['Novel time I/Q','Novel tokens I/G','Medical time I/Q','Medical tokens I/G'],abl,[19,20,21,22],'Time is in minutes. Paired token columns retain the source I/G headings; its caption describes input/output token counts.')
Path('chapter/tables/agrag-ablation.tex').write_text(t)
low=rows('tab:exp_low',19,0);assert len(low)==3,len(low)
t=''
for slug,title,inds,heads in segments[:4]:
 t+=table(title+' in the low-resource setting','low-resource' if slug=='creative' else 'low-resource-'+slug,heads,low,inds,'Qwen3-4B-Instruct-2507 on two 2080 Ti GPUs; values and emphasis preserved.')
Path('chapter/tables/agrag-low-resource.tex').write_text(t)
loweff=rows('tab:exp_low_eff',9,0);assert len(loweff)==3,len(loweff)
t=''
for name,inds in [('Novel',[1,2,3,4]),('Medical',[5,6,7,8])]:
 t+=table(name+' low-resource efficiency','low-resource-efficiency' if name=='Novel' else 'low-resource-efficiency-medical',['Index min','Query min','Input tokens','Output tokens'],loweff,inds,'Qwen3-4B-Instruct-2507 on two 2080 Ti GPUs.')
Path('chapter/tables/agrag-low-resource-efficiency.tex').write_text(t)
Path('planning/agrag-table-cells.json').write_text(json.dumps(records,indent=2))
print('Generated',len(records),'tables; numerical values retained from active source. Publication audit tracked separately.')
