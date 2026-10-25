from pathlib import Path
import csv,re
# Keep faithful first-pass layouts for audit; authoring layouts below preserve every adopted cell.
for name in ['main-tables','dataset-table','ablation-table','token-table','zero-table']:
 p=Path('planning/gorag-'+name+'.tex');f=Path('planning/gorag-source/original-layout-'+name+'.tex')
 if not f.exists():f.write_text(p.read_text())
rows=list(csv.DictReader(open('planning/gorag-main-cell-ledger.csv')))
out=[]
for dataset,label,backbone in [('WOS','wos','Qwen2.5-7B'),('IFS-Rel','ifs','GPT-4o')]:
 for shot in [1,5,10]:
  suf='' if shot==1 else '-'+str(shot)+'shot'
  t='''\\begin{table}[tbp]
\\centering
\\caption{DATASET classification accuracy with SHOT support examples per label. BACKBONE is the RAG backbone. Values and emphasis reproduce the corresponding columns of GORAG's main table.}
\\label{tab:gorag:main-LABELSUFFIX}
\\small
\\begin{tabular}{lrrrr}
\\hline
Method & Round 1 & Round 2 & Round 3 & Round 4\\\\
\\hline
'''.replace('DATASET',dataset).replace('SHOT',str(shot)).replace('BACKBONE',backbone).replace('LABEL',label).replace('SUFFIX',suf)
  for method in ['Entailment','NaiveRAG','LongLLMLingua','GraphRAG','LightRAG','HippoRAG2','GORAG']:
   vals=[x['source_cell'] for x in rows if x['dataset']==dataset and x['method']==method and int(x['shot'])==shot]
   assert len(vals)==4
   t+=method+' & '+' & '.join(vals)+' \\\\\n'
  t+='\\hline\n\\end{tabular}\n\\end{table}\n';out.append(t)
Path('planning/gorag-main-tables.tex').write_text('% Layout split by shot; all 168 adopted WOS/IFS main cells retained.\n'+'\n'.join(out))
# Transpose dataset statistics to keep natural-size text, all 30 numeric cells preserved.
rr=list(csv.DictReader(open('planning/gorag-other-cell-ledger.csv')))
d={n:[x['source_value'] for x in rr if x['table']=='dataset' and x['row']==n] for n in ['CAD','WOS','IFS-Rel']}
labels=['Average text tokens','Round 1 test texts','Round 1 new labels','Round 2 test texts','Round 2 new labels','Round 3 test texts','Round 3 new labels','Round 4 test texts','Round 4 new labels','Total test texts']
t='''\\begin{table}[tbp]
\\centering
\\caption{Dataset statistics for the four-round experiments, transposed from the original table. IFS-Rel has 40 test samples per label. Round label counts refer to newly introduced labels.}
\\label{tab:gorag:dataset}
\\small
\\begin{tabular}{lrrr}
\\hline
Statistic & CAD & WOS & IFS-Rel\\\\
\\hline
'''
for j,stat in enumerate(labels):t+=stat+' & '+' & '.join(d[n][j] for n in ['CAD','WOS','IFS-Rel'])+' \\\\\n'
t+='\\hline\n\\end{tabular}\n\\end{table}\n';Path('planning/gorag-dataset-table.tex').write_text(t)
for name in ['ablation','token','zero']:
 p=Path('planning/gorag-'+name+'-table.tex');s=p.read_text()
 s=s.replace('\\resizebox{\\linewidth}{!}{','\\small')
 s=re.sub(r'(\\end\{tabular\})\s*\}',r'\1',s)
 p.write_text(s)
