# HeyReach Brain

A distilled, fully-cited **knowledge base of HeyReach's own content** — turned into a navigable
[Obsidian](https://obsidian.md) wiki. It reads the entire public HeyReach corpus and reorganizes
it by *what you'd actually want to know* — playbooks, frameworks, real campaign results, the
automation stack, the product, and HeyReach's point of view — with **every claim linked back to
the exact source it came from**.

Built from **312 sources** scraped on 2026-09-30:

| Source | Count | Folder |
|---|---|---|
| YouTube videos (`@heyreach`) | 69 | `raw/youtube/` |
| Blog posts (`heyreach.io/blog`) | 186 | `raw/blog/` |
| Outbound playbooks (campaign case studies) | 31 | `raw/playbooks/` |
| Certified expert / agency profiles | 16 | `raw/experts/` |
| Product & positioning pages | 10 | `raw/site/` |

## How to use it

- **Browse in Obsidian** — open this folder as a vault and start at [`wiki/INDEX.md`](wiki/INDEX.md);
  follow the `[[wikilinks]]` between articles. The graph view shows how the topics connect.
- **Read on GitHub** — start at [`wiki/INDEX.md`](wiki/INDEX.md) and click through.
- **Chat with it in Claude Code / Claude Desktop** — open this folder and ask, e.g. *"What are HeyReach's
  rules for not getting LinkedIn accounts banned?"* or *"Show me the highest-converting playbooks with
  their numbers."* The [`CLAUDE.md`](CLAUDE.md) here makes it answer grounded in the cited sources.

## What's inside (`wiki/`)

- **playbooks/** — actionable, step-by-step outreach strategies organized by goal.
- **frameworks/** — the named methods, message/sequence formulas, targeting systems and deliverability rules.
- **case-studies/** — real campaigns with their numbers (the outbound playbooks + video/blog results).
- **tools-and-automation/** — the stack: HeyReach + Clay, n8n, Make, enrichment, CRMs, and the HeyReach MCP/CLI/API.
- **product-and-positioning/** — HeyReach the product: features, pricing, agency/sales/growth positioning, comparisons.
- **opinions-and-trends/** — HeyReach's (and its guests') point of view: AI SDRs, safe scaling, 2026 outbound, benchmarks.
- **experts/** — the certified experts & agencies, and the practitioners featured across the content.

## How to trust it

- **Every claim is cited** inline as `(source: "Exact Source Title")`, resolving to a real file in `raw/`.
- **It's HeyReach's own content, so it's marketing** — the wiki keeps that honest: HeyReach's "best/only"
  claims are marked as **vendor claims**, featured practitioners' tactics and results are **attributed to
  them by name** (with their agency noted), and every reply-rate / conversion benchmark is flagged as
  **self-reported** with its context kept.
- **Numbers are verbatim**, cross-source discrepancies are preserved (not silently reconciled), and
  time-bound tactics are **era-tagged** (LinkedIn limits and outreach norms move fast).

## Provenance & rebuild

Scraped from `youtube.com/@heyreach/videos` and `heyreach.io` (blog, outbound-playbooks, experts, and
product pages) on 2026-09-30. The `raw/` files are the verbatim source text. Build method (extraction →
synthesis → citation verification) and the prompts used are in `wiki/_build/`.
