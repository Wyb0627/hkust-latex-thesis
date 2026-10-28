const fs = await import("node:fs/promises");
const task = await taskSpace(3);
const page = task.page("p1");
const titles = ["TURL: Table Understanding through Representation Learning", "WebTables: Exploring the Power of Tables on the Web", "Learning semantic annotations for tabular data", "Language Models are Few-Shot Learners", "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks", "Translating Embeddings for Modeling Multi-relational Data", "Improving Hyper-relational Knowledge Graph Completion", "Lost in the Middle: How Language Models Use Long Contexts"];
const rows = [];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const text = await page.evaluate(() => document.body.innerText);
 rows.push({title, url:await page.url(), text});
 console.log(JSON.stringify({title, text:text.slice(0,3800)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round1.json",JSON.stringify(rows,null,2));
