const fs = await import("node:fs/promises");
const task = await taskSpace(3); const page = task.page("p1");
const titles = ["XLNet: generalized autoregressive pretraining for language understanding", "LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression", "Improving language models by retrieving from trillions of tokens", "H2o: Heavy-hitter oracle for efficient generative inference of large language models", "Role-aware modeling for n-ary relational knowledge bases", "Link prediction on n-ary relational data", "Generalizing tensor decomposition for n-ary relational knowledge bases", "Simple embedding for link prediction in knowledge graphs"];
const rows=[];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const data=await page.evaluate(()=>({text:document.body.innerText, results:[...document.querySelectorAll("h3")].map(h=>({title:h.innerText, text:h.parentElement.innerText, links:[...h.parentElement.querySelectorAll("a")].map(a=>({text:a.innerText,href:a.href}))}))}));
 rows.push({title,url:await page.url(),...data});
 console.log(JSON.stringify({title,firstResult:data.results[0]?.title,citedBy:data.results[0]?.text.match(/Cited by [0-9,]+/)?.[0],blocked:/unusual traffic|not a robot|recaptcha/i.test(data.text)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(data.text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round3.json",JSON.stringify(rows,null,2));
