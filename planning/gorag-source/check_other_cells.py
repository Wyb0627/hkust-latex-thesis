from pathlib import Path
import re,csv
# Independent transcription from author-confirmed publication-equivalent PDF pp6,8 inspected in text and rendered page8.
checks={
'dataset':{'CAD':['154','240','4','60','3','286','3','231','3','817'],'WOS':['200','2,417','32','2,842','53','2,251','30','1,886','18','9,396'],'IFS-Rel':['105','640','16','640','16','640','16','640','16','2,560']},
'ablation':{'offline&unit':['0.2979','0.2287','0.2645','0.2249'],'offline':['0.3063','0.2302','0.2455','0.2156'],'unit':['0.4706','0.4394','0.4407','0.3899'],'keyword':['0.4746','0.4606','0.4455','0.4030'],'GORAG':['0.4862','0.4649','0.4814','0.4210']},
'token':{'GPT-4o':['634.6','0.005'],'LongLLMLingua':['2771.3','0.021'],'NaiveRAG':['4537.4','0.034'],'LightRAG':['7866.3','0.059'],'GraphRAG':['9296.3','0.070'],'GORAG':['557.5','0.004']},
'zero':{'GPT-4o':['0.9219','0.5109','0.4063','0.5936'],'LongLLMLingua':['0.9281','0.5297','0.4234','0.5806'],'LightRAG':['0.6718','0.3047','0.2135','0.0977'],'GraphRAG':['0.5625','0.1875','0.1458','0.0938'],'GORAG':['0.9328','0.5406','0.4375','0.6063']}}
results=[]
for table,rows in checks.items():
 lines=Path('planning/gorag-'+table+'-table.tex').read_text().splitlines()
 for name,values in rows.items():
  if table=='ablation':
   target=next(l for l in lines if ('\\textit{'+name.replace('&','\\&')+'}' in l if name!='GORAG' else '& \\textbf{GORAG}' in l))
  else:target=next(l for l in lines if name in l and '\\\\' in l and len(l.split('&'))>len(values))
  cells=target.split('&')[-len(values):]
  # escaped ampersand in ablation row's method is before numeric cells.
  for j,(cell,pdfvalue) in enumerate(zip(cells,values)):
   cell=cell.split('\\\\')[0]
   v=re.search(r'\d[\d,]*(?:\.\d+)?',cell).group()
   assert v==pdfvalue,(table,name,j,v,pdfvalue)
   results.append([table,name,j+1,v,pdfvalue,6 if table=='dataset' else 8,'MATCH_AUTHOR_CONFIRMED_PUBLICATION_EQUIVALENT'])
with Path('planning/gorag-other-cell-ledger.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['table','row','column_index','source_value','pdf_value','pdf_page','status']);w.writerows(results)
print('Other tables checked:',len(results),'cells.')
