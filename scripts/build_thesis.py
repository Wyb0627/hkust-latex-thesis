"""Build thesis and reject unresolved references, missing glyphs/assets or overflow."""
from pathlib import Path
import os,subprocess,re,shutil

root=Path(__file__).resolve().parent.parent
os.chdir(root)
env=os.environ.copy()
required=('latexmk','xelatex','biber')
if any(shutil.which(tool,path=env.get('PATH','')) is None for tool in required):
 # GUI processes may omit the active MacTeX installation from their PATH.
 texbin=Path('/Library/TeX/texbin')
 if texbin.is_dir():
  env['PATH']=str(texbin)+os.pathsep+env.get('PATH','')
  print('Added the active MacTeX directory to this build process PATH.',flush=True)
resolved={tool:shutil.which(tool,path=env.get('PATH','')) for tool in required}
missing=[tool for tool,path in resolved.items() if path is None]
if missing:raise SystemExit('Required TeX programs not found: '+', '.join(missing))
for tool,path in resolved.items():print(f'{tool}: {path}',flush=True)
args=[resolved['latexmk'],'-xelatex','-interaction=nonstopmode','-halt-on-error','-latexoption=-no-shell-escape','main.tex']
def build():subprocess.run(args,check=True,env=env)
build()
log=Path('main.log').read_text(errors='replace')
# BibLaTeX can retain an auxiliary rerun flag when Biber's output hash is unchanged.
# A fresh auxiliary build resolves that state without suppressing any warning.
if 'Please (re)run Biber' in log:
 print('BibLaTeX requests another pass: cleaning generated auxiliary state and rebuilding.',flush=True)
 subprocess.run([resolved['latexmk'],'-c','main.tex'],check=True,env=env)
 subprocess.run(args[:1]+['-g']+args[1:],check=True,env=env)
 log=Path('main.log').read_text(errors='replace')
patterns=[r'There were undefined references',r'(?:Citation|Reference) .+ undefined',r'Please \(re\)run Biber',r'Overfull \\[hv]box',r'Missing character:',r'multiply defined',r'destination with the same identifier',r'LaTeX Error:']
issues=[p for p in patterns if re.search(p,log)]
if issues:raise SystemExit('PDF build failed final log check: '+', '.join(issues))
blg=Path('main.blg').read_text(errors='replace')
if re.search(r'\b(?:WARN|ERROR)\b',blg):raise SystemExit('Biber warnings/errors need review; see main.blg')
shutil.copy2('main.pdf','thesis.pdf')
print('Thesis PDF built; references, glyphs, labels and overflow checks passed.')
