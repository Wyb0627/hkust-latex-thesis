"""Build thesis and reject unresolved references, missing glyphs/assets or overflow."""
from pathlib import Path
import subprocess,re,shutil
args=['latexmk','-xelatex','-interaction=nonstopmode','-halt-on-error','-latexoption=-no-shell-escape','main.tex']
def build():subprocess.run(args,check=True)
build()
log=Path('main.log').read_text(errors='replace')
# BibLaTeX can retain an auxiliary rerun flag when Biber's output hash is unchanged.
# A fresh auxiliary build resolves that state without suppressing any warning.
if 'Please (re)run Biber' in log:
 print('BibLaTeX requests another pass: cleaning generated auxiliary state and rebuilding.',flush=True)
 subprocess.run(['latexmk','-c','main.tex'],check=True)
 subprocess.run(args[:1]+['-g']+args[1:],check=True)
 log=Path('main.log').read_text(errors='replace')
patterns=[r'There were undefined references',r'(?:Citation|Reference) .+ undefined',r'Please \(re\)run Biber',r'Overfull \\[hv]box',r'Missing character:',r'multiply defined',r'destination with the same identifier',r'LaTeX Error:']
issues=[p for p in patterns if re.search(p,log)]
if issues:raise SystemExit('PDF build failed final log check: '+', '.join(issues))
blg=Path('main.blg').read_text(errors='replace')
if re.search(r'\b(?:WARN|ERROR)\b',blg):raise SystemExit('Biber warnings/errors need review; see main.blg')
shutil.copy2('main.pdf','thesis.pdf')
print('Thesis PDF built; references, glyphs, labels and overflow checks passed.')
