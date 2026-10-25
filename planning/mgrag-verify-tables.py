from pathlib import Path
import pdfplumber,re,json
src=Path('planning/extracted/mgrag-active.tex.txt').read_text()
blocks={re.search(r'\\label\{([^}]+)\}',m[0]).group(1):m[0] for m in re.finditer(r'\\begin\{table\}.*?\\end\{table\}',src,re.S)}
# Crops isolate each published table from the neighbouring column.
locs={
'dataset_statistic':(8,(307,30,610,300)),
'main_exp':(9,(0,30,308,535)),
'efficiency_MGRAG':(9,(308,30,612,400)),
'system_comp':(9,(308,30,612,400)),
'gm_experiment':(10,(0,30,340,470)),
'hop_performance':(10,(330,30,612,275)),
'abl_exp':(10,(330,30,612,350)),
'inv_abl':(11,(0,30,309,330)),
}
result={}
num=lambda x:re.findall(r'(?<![A-Za-z])\d+(?:,\d{3})*(?:\.\d+)?(?:M|k)?|(?<!\S)-(?!\S)',x)
with pdfplumber.open('planning/published/mgrag-pvldb-2026.pdf') as pdf:
 for key,(page,crop) in locs.items():
  extracted=pdf.pages[page].crop(crop).extract_text(x_tolerance=1,y_tolerance=(2 if key=='gm_experiment' else 4))
  Path('planning/mgrag-pdf-table-'+key+'.txt').write_text(extracted+'\n')
  b=blocks['tab:'+key].split(r'\begin{tabular}',1)[1].split('\n',1)[1].split(r'\end{tabular}',1)[0]
  b=re.split(r'\\(?:midrule|hline)',b,maxsplit=1)[1].split(r'\bottomrule',1)[0]
  expected=[]
  for row in re.split(r'\\\\',b):
   if '&' not in row:continue
   cells=row.split('&')[1:]
   vals=num(' '.join(cells))
   if vals:expected.append(vals)
  # Every row's data-token sequence must occur in the corresponding published crop line.
  lines=[num(l) for l in extracted.splitlines()]
  checked=[]
  for i,vals in enumerate(expected):
   matches=[j for j,ls in enumerate(lines) if any(ls[k:k+len(vals)]==vals for k in range(max(0,len(ls)-len(vals)+1)))]
   checked.append({'source_row':i+1,'data_tokens':vals,'pdf_line_matches':[j+1 for j in matches],'status':'PASS' if matches else 'REVIEW'})
  result[key]={'published_page':2480+page,'numeric_or_missing_tokens':sum(len(x) for x in expected),'rows':checked,'status':'PASS' if all(r['status']=='PASS' for r in checked) else 'REVIEW'}
Path('planning/mgrag-cell-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:(v['numeric_or_missing_tokens'],v['status'],[r['source_row'] for r in v['rows'] if r['status']!='PASS']) for k,v in result.items()})
