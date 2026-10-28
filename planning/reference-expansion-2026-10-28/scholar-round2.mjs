const fs = await import("node:fs/promises");
const task = await taskSpace(3); const page = task.page("p1");
const titles = ["Colnet: Embedding the semantics of web tables for column type prediction", "Tcn: Table convolutional network for web table interpretation", "Exploring the limits of transfer learning with a unified text-to-text transformer", "Generalizing from a few examples: A survey on few-shot learning", "Chain-of-thought prompting elicits reasoning in large language models", "Dynamic few-shot visual learning without forgetting", "Incremental few-shot learning with attention attractor networks", "KnowGPT: Knowledge Graph based Prompting for Large Language Models"];
const rows=[];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const data=await page.evaluate(()=>({text:document.body.innerText, results:[...document.querySelectorAll("h3")].map(h=>({title:h.innerText, text:h.parentElement.innerText, links:[...h.parentElement.querySelectorAll("a")].map(a=>({text:a.innerText,href:a.href}))}))}));
 rows.push({title,url:await page.url(),...data});
 console.log(JSON.stringify({title,results:data.results.slice(0,1),blocked:/unusual traffic|not a robot|recaptcha/i.test(data.text)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(data.text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round2.json",JSON.stringify(rows,null,2));
