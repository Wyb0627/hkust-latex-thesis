from pathlib import Path
import re
src=Path('planning/gorag-source/sec-experiment_results.tex').read_text()
methods=['Entailment','NaiveRAG','LongLLMLingua','GraphRAG','LightRAG','HippoRAG2','GORAG']
rows={k:[] for k in ['CAD','WOS','IFS-Rel']}; dataset=None
for line in src.splitlines():
 if '\\multirow{7}{*}{\\textbf{CAD}}' in line:dataset='CAD'
 if '\\multirow{7}{*}{\\textbf{WOS}}' in line:dataset='WOS'
 if '\\multirow{7}{*}{\\textbf{IFS-Rel}' in line:dataset='IFS-Rel'
 cells=line.split('&')
 if dataset and len(cells)==15:
  model=next((m for m in methods if m in cells[2]),None)
  if model:
   values=[re.sub(r'\\\\.*','',v).strip() for v in cells[3:]]
   rows[dataset].append((model,values))
 if '\\end{table*}' in line and rows['IFS-Rel']: break
out=[]
for d in rows:
 assert len(rows[d])==7,(d,len(rows[d]))
 content='''% Exact active-source transcription. Author-confirmed publication-equivalent PDF comparison recorded in ledger.
\\begin{table}[p]
\\centering
\\caption{Classification accuracy on DATASET under the four-round protocol. BACKBONE is the RAG backbone. Each round lists 1-, 5-, and 10-shot results in that order. This is the DATASET block of the original main table.}
\\label{tab:gorag:main-LABEL}
\\resizebox{\\linewidth}{!}{%
\\begin{tabular}{l|ccc|ccc|ccc|ccc}
\\hline
Method & \\multicolumn{3}{c|}{Round 1} & \\multicolumn{3}{c|}{Round 2} & \\multicolumn{3}{c|}{Round 3} & \\multicolumn{3}{c}{Round 4}\\\\
 & 1-shot & 5-shot & 10-shot & 1-shot & 5-shot & 10-shot & 1-shot & 5-shot & 10-shot & 1-shot & 5-shot & 10-shot\\\\
\\hline
'''.replace('DATASET',d).replace('BACKBONE','GPT-4o' if d=='IFS-Rel' else 'Qwen2.5-7B').replace('LABEL','ifs' if d=='IFS-Rel' else d.lower())
 for m,vals in rows[d]:content+=m+' & '+' & '.join(vals)+' \\\\\n'
 content+='\\hline\n\\end{tabular}}\n\\end{table}\n'
 if d=='CAD':
  content+='\\noindent\\textit{Working-draft audit note.} The selected source prints \\texttt{03139} in the final GORAG cell. This transcription preserves that text; the cell is excluded from thesis quantitative interpretation pending author clarification.\n'
  Path('planning/gorag-working-cad-table.tex').write_text(content)
 else:out.append(content)
Path('planning/gorag-main-tables.tex').write_text('\n'.join(out))
# Reuse complete other source tables with faithful data/format; remove only spacing commands.
source_method=Path('planning/gorag-source/sec-method.tex').read_text()
for name,label,ss in [('dataset','tab:data_stat',source_method),('ablation','tab:exp_abl',src),('token','tab:token_cost',src),('zero','tab:0_shot',src)]:
 tables=re.findall(r'\\begin\{table\*?\}.*?\\end\{table\*?\}',ss,flags=re.S)
 t=next(t for t in tables if '\\label{'+label+'}' in t)
 t=t.replace('table*','table')
 t=re.sub(r'\\vspace\{[^}]+\}','',t)
 t=re.sub(r'\\cite\{([^}]+)\}',lambda m:'\\cite{'+','.join('gorag-'+k for k in m.group(1).split(','))+'}',t)
 t=t.replace('\\label{'+label+'}','\\label{tab:gorag:'+name+'}')
 Path('planning/gorag-'+name+'-table.tex').write_text('% Exact active-source transcription, numerical values retained.\n'+t+'\n')
# CSV ledger of each main cell (including disputed CAD literal).
import csv
with Path('planning/gorag-main-cell-ledger.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['dataset','method','round','shot','source_cell','comparison_status'])
 for d,rr in rows.items():
  for m,vs in rr:
   for j,v in enumerate(vs):w.writerow([d,m,j//3+1,[1,5,10][j%3],v,'PENDING_PDF_CHECK'])
