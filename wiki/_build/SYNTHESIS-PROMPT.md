# HeyReach Brain — Synthesis Prompt (one agent per category)

**Read `D:\HeyReach Brain\wiki\_build\SYNTHESIS-CAVEATS.md` FIRST** — it governs COI handling,
attribution, citations, and voice. Then synthesize your assigned category.

## Input
The extraction notes: `D:\HeyReach Brain\wiki\_build\notes-batch-*.md`. They total a lot of text —
**do NOT read all of them into memory at once.** Work topic by topic:
1. Survey what exists: `grep -h '^## ' notes-batch-*.md | sort -u` (all source titles) and
   `grep -h '\*\*topics:\*\*' notes-batch-*.md` (topic tags).
2. For each article you plan, `grep -rin "<keywords>" notes-batch-*.md` to find the relevant note
   blocks, read those blocks, and synthesize. Repeat per article.

## Output
Write articles to `D:\HeyReach Brain\wiki\<YOUR_CATEGORY>\<kebab-slug>.md`. Every article:
- Opens with a one-paragraph summary.
- Merges across ALL sources touching the topic (video + blog + playbook + product + expert), one
  article per coherent topic — NOT one per source.
- Cites every claim inline `(source: "Exact Title")` (byte-exact; see caveats). Multiple: `(source: "A"; source: "B")`.
- `[[wikilinks]]` related articles liberally; end with a `## Related` footer of links.
- Uses tables for thresholds/pricing/benchmarks where it helps. Numbers verbatim.
- Applies the COI / attribution / self-reported-benchmark / era-tag discipline from the caveats.

**Return** a markdown list of every article you created: `- [[slug]] — one-line description`
(goes verbatim into INDEX.md), plus a count and anything notable you couldn't place.

---

## Category boundaries (stay in your lane; link across to the others)

### playbooks/  (actionable strategies, organized by GOAL)
The step-by-step "how to run X" material. Likely goals: book meetings on LinkedIn; scale outreach
WITHOUT getting accounts restricted; multichannel LinkedIn+email sequencing; AI personalization at
scale; build & enrich targeted lead lists (ICP, signals, lookalikes); LinkedIn profile + content for
inbound; managing replies / the inbox at scale; agency client onboarding & reporting; writing cold
outreach copy that gets replies. Give the CURRENT approach where advice evolved.
**Send to others:** named methods/formulas → `frameworks/`; numbered result stories → `case-studies/`;
stack wiring → `tools-and-automation/`; feature specifics → `product-and-positioning/`; debates/
predictions → `opinions-and-trends/`.

### frameworks/  (their NAMED methods, formulas, systems, rule-sets)
Message/copy formulas, sequence architectures, targeting/ICP systems, the deliverability/safety rule-set
(sending limits, warm-up, sender rotation), and any benchmark framework (e.g. the 96,051-campaign
benchmark set and how to read acceptance/reply rates). Per item: definition, steps as taught, when to
use, thresholds, results attributed. Group tiny related ones together.

### case-studies/  (documented campaigns, numbers verbatim)
The 31 outbound playbooks plus any video/blog case data. Per study: WHO (named practitioner/agency +
their COI), context (ICP/vertical/list size), what they did, the exact numbers, their conclusion, and
the limits. Preserve cross-source discrepancies. Never present a self-reported number as verified.

### tools-and-automation/  (the stack + workflows)
How HeyReach is wired with the rest of the GTM stack: Clay/Claygent enrichment, n8n / Make / Zapier
orchestration, data providers, CRMs (HubSpot/Salesforce), and HeyReach's own MCP server, CLI, and
Campaign API. Cover the AI-outreach-agent architectures (execution layer vs reasoning/enrichment layer)
and concrete automation workflows/templates. Organize by tool/integration and by workflow.

### product-and-positioning/  (HeyReach the product)
Features (unified inbox / Unibox, unlimited & rotating senders, workspaces, A/B, campaign types,
analytics, whitelabel, proxies, security), pricing tiers & the flat-fee-vs-per-seat wedge, the
for-agencies / for-sales / for-growth positioning, and competitor comparisons. Everything here is a
vendor claim — frame it as such; keep the competitor-comparison numbers as HeyReach's own table.

### opinions-and-trends/  (POV & themes)
HeyReach's and its guests' stances, organized by theme: AI SDRs (augmentation vs full autonomy; why
"spin up a bot army" fails), the safe-scaling / quality-over-volume / anti-spam philosophy, deliverability
& ban-avoidance beliefs, 2026 outbound predictions, "is LinkedIn outreach still worth it," and how they
read the benchmarks. Short verbatim quotes (≤15 words). Note where a guest disagrees with HeyReach.

### experts/  (the certified experts & featured practitioners)
A directory + profiles of the 16 HeyReach-certified experts/agencies (name, specialty, ICP, stack,
any results — all self-reported/COI) and the notable practitioners featured across the playbooks and
videos. Make it a useful "who's who" that the case-studies and playbooks can link into. Include a
short index article listing all of them.
