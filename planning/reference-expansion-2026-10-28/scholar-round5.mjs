const fs = await import("node:fs/promises");
const task = await taskSpace(3); const page = task.page("p1");
const titles = ["Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models", "Tree of thoughts: Deliberate problem solving with large language models", "Graph of thoughts: Solving elaborate problems with large language models", "Retrieval augmented language model pre-training", "Atlas: Few-shot learning with retrieval augmented language models", "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions", "Visual Instruction Tuning", "Prototypical Networks for Few-shot Learning"];
const rows=[];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const data=await page.evaluate(()=>({text:document.body.innerText, results:[...document.querySelectorAll("h3")].map(h=>({title:h.innerText, text:h.parentElement.innerText, links:[...h.parentElement.querySelectorAll("a")].map(a=>({text:a.innerText,href:a.href}))}))}));
 rows.push({title,url:await page.url(),...data});
 console.log(JSON.stringify({title,firstResult:data.results[0]?.title,citedBy:data.results[0]?.text.match(/Cited by [0-9,]+/)?.[0],blocked:/unusual traffic|not a robot|recaptcha/i.test(data.text)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(data.text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round5.json",JSON.stringify(rows,null,2));
