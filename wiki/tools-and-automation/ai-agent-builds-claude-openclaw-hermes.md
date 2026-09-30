# AI Agent Builds: Claude, OpenClaw, Hermes & ChatGPT

Concrete, source-by-source recipes for wiring an AI agent to HeyReach so you can run LinkedIn outreach from a chat window or terminal instead of the dashboard — "You describe the play, Claude runs it for you" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). HeyReach exposes three connection surfaces the agents ride on — the [[heyreach-mcp-server]], the [[heyreach-cli]], and the [[heyreach-campaign-api-and-webhooks]]. This article organizes the builds by agent runtime. Every walkthrough below is from a HeyReach channel/blog and most are delivered by agency practitioners with a COI (they sell services and, in one case, built the tooling); attribute tactics to them, not to HeyReach, and treat all result numbers as self-reported.

## Claude Desktop / Claude via MCP connector

The lowest-friction build connects HeyReach to Claude as a **custom connector** and drives it in plain English. Path: HeyReach → Settings → Integrations → HeyReach MCP server (copy MCP connection URL + a new MCP key); in Claude → Settings → Connectors → Add custom connector → paste the URL + key → set permissions from "custom" to "always allow." This creates a two-way link to perform any HeyReach action and pull stats from the chat (source: "Claude Just Changed LinkedIn Outreach Forever (Tutorial)"). Attribute this build to **Tim (agency B2B Boosted)** — a COI.

Signature moves from that build (all Tim's, COI):
- **Build a company "brain" in Notion** — prompt Claude to write a client onboarding brief mining past chats + website + LinkedIn page for four things (products, persona, pain points, current process), save it as a Notion page with an FAQ so drafted replies match your voice, then: "Go look at HeyReach replies that are unread... then draft replies for all these leads using the Brain in a Notion file" (source: "Claude Just Changed LinkedIn Outreach Forever (Tutorial)").
- **Schedule it as a Claude routine** — "Turn this into a Claude routine whereby you look up unread messages, draft replies and send them to me via Slack DMs every Monday and Thursday morning" (same).
- Claimed benchmark (Tim, unverified): "Almost 90% of the meetings that you book from LinkedIn typically happen after the sixth interaction" (same).

A separate Tim build focuses on **model selection with Claude "Opus 5"/"Sonnet 5"**: use the cheaper Sonnet for low-stakes jobs (cleaning job titles) and Opus for lead research and copywriting; push effort to "max/extra" only when "your job is quite literally on the line." He claims Opus 5 "catches its own mistakes before you ever see its output," re-reading a 500-lead list to self-correct disqualifications (source: "Claude Opus 5 Just Changed LinkedIn Outreach Forever (Tutorial)"). His three core Opus uses: research a lead → write the sub-60-word opener → duplicate the best campaign (~2 min vs ~10 min prior). His stated success benchmarks (unverified): "30% plus connection acceptance rate, a 5% plus reply rate, and an over 50% positive reply rate from the total replies" (same). Note an internal safety-cap discrepancy: this video says "don't send more than 10 to 15 connection requests" per day, lower than the 20–25/day cited elsewhere — see [[safe-linkedin-sending-limits]].

## Claude Code (terminal)

The terminal build connects **Claude Code** to HeyReach via the [[heyreach-cli]] or MCP, then runs whole plays from markdown SOP files. Tim's version: connect Claude Code to the HeyReach CLI ("full account access"), load a "LinkedIn DM SOP" markdown as a skill, import a CSV, then prompt Claude Code to enroll the list in a 3-message campaign using custom variables generated from the first 10 profiles — recommending PLAN mode to scope before executing and a human approval gate ("Pausing here for your go, Tim") (source: "Claude + LinkedIn = Unlimited Leads on Autopilot"). He warns "bypass permissions" mode "is obviously dangerous," preferring "ask before edit." Attribute to Tim (COI); "Unlimited Leads" is title hype.

**Kellen Casey (The Deal Lab)** demos the same pattern end-to-end (name auto-garbled as "Calvin Kespere"): install Claude Code by asking Claude how, add the MCP key with `claude mcp add`, verify with `/mcp`, clean a CSV by prompt, then "load those CEOs into the HeyReach campaign" — a ~15-minute run. His framing: "Claude is on my computer talking through my systems to the web apps... This is the future Heyreach is building" (source: "How I Get Unlimited Leads Using Claude Code + LinkedIn"). COI: The Deal Lab agency. He uses the markets → segments → personas → angles ("CEO of the problem") framework; see [[icp-and-targeting-systems]].

Claude is also the runtime for **automated agency reporting** — see [[automation-workflow-templates]] and the four-layer reporting system that uses HeyReach MCP to "tag leads by performance tier... auto-summarize performance by ICP segment" (source: "Build a repeatable system for agency client reporting with Claude").

## OpenClaw

**OpenClaw** (openclaw.ai) is a third-party AI-agent framework you install in a chat app, on a computer, or on a VPS, then point at the HeyReach CLI. The canonical build is **Brandon Charleson's** (Top of Funnel; he built and open-sourced the HeyReach CLI — double COI). Getting started: sign up for HeyReach → learn OpenClaw → find the HeyReach CLI in Top of Funnel's agent-tools section → `npm install -g heyreach-cli` (install ~60s) → authenticate with your HeyReach API key → give the agent context, then prompt (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent"). His agent "Eve" runs a monitor → draft → review → send loop in Slack, with a standing rule "Draft replies for the top five — but don't send until I say" (same; also source: "Copy this OpenClaw system:  it'll BLOW your LinkedIn game overnight"). His design principle is **"Context + Capability"** and the CLI-as-MCP fact that "every command doubles as an MCP tool."

A deeper Brandon build covers **hosting and fleets**: host on-prem (Mac mini/Studio/spare laptop — not your daily driver, sandbox risk) or cloud (a DigitalOcean droplet, SSH in, 24/7, clients can access); pick Slack or Telegram as the harness for a "premium feel"; store context as persistent markdown injected into the system prompt; install the CLI global for sandboxed setups; and adopt an "agent fleet" model (one agent per client). His command groups exposed by the CLI: campaigns, inbox, accounts, lists, stats, leads, lead tags, webhooks — full lifecycle "create DRAFT (human must launch)" (source: "How Openclaw Runs My Entire LinkedIn Outreach System"). His LLM advice (his opinion): Claude Sonnet is his workhorse; also names Fable, Grok, GPT. Security caveat he raises himself: don't paste an API key into a chat interface — authenticate in the terminal backend.

**Naming caveat:** most sources spell it "OpenClaw" with the URL openclaw.ai, but HeyReach's own MCP page title uses "OpenClaw" while other HeyReach pages reportedly render it "OpenClay" (likely a typo); one video's captions garble it entirely (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). Treat OpenClaw / openclaw.ai as the intended product.

## Hermes agent

**Hermes** is a third-party agent an agency demos for a full Slack-driven build: source off-database leads → enrich → ICP-score → write sequences → push to HeyReach via CLI, all from Slack (source: "How I Get Unlimited Leads With Hermes Agent + LinkedIn"). Its distinguishing claim (the agency's opinion) is **persistent memory + a self-improving loop** — "every time you screw up... it saves that into the memory" — plus a native browser and multi-channel control (Slack/WhatsApp/Telegram/Discord). It connects HeyReach (CLI preferred over MCP) and Clay by pasting a GitHub repo to the agent ("please install HeyReach CLI for me and help me authenticate"). Backend model cited as Codex, "the fastest" (agency opinion, unverified). Practical constraints from the demo: the computer must stay awake or the agent stops; the connection-request withdrawal minimum is 14 days; safety cap "we don't send more than like 20-25 connections per day" per sender. Attribute all of this to the presenting agency (COI); it is not a HeyReach product.

## ChatGPT / Cursor / any MCP host

The HeyReach MCP is client-agnostic: it connects to "Claude, ChatGPT/OpenAI, Cursor, Clay, N8N, Slack, or any other popular MCP" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). The MCP essay adds Cursor for "heavier jobs — run Python scripts, scrape datasets, push normalized data into HeyReach" and notes you can chain multiple MCPs (source: "Beginner’s guide to MCP in HeyReach: clean lists and clear inboxes"). ChatGPT/GPT also commonly appears as the reasoning module *inside* n8n/Make workflows rather than as the top-level chat agent — see [[n8n-automation-workflows]] and [[make-automation-workflows]].

## Cross-cutting build patterns

- **Human approval before send** is standard across every build (draft in Unibox/Slack, human approves).
- **Build campaigns in DRAFT; a human launches** (a recurring OpenClaw/Hermes rule).
- **Context lives in a file** — a markdown SOP, a Notion "brain," or the agent's persistent memory — and is reused across runs.
- **CLI vs MCP:** Brandon and the Hermes agency prefer the CLI ("beats writing custom scripts every time"); the MCP is the no-code, connector-based path. Both wrap the same API.

## Related
- [[ai-outreach-agent-architecture]]
- [[heyreach-mcp-server]]
- [[heyreach-cli]]
- [[heyreach-campaign-api-and-webhooks]]
- [[clay-enrichment-and-data-waterfall]]
- [[automation-workflow-templates]]
- [[manage-replies-and-inbox-at-scale]]
- [[safe-linkedin-sending-limits]]
- [[ai-personalization-at-scale]]
- [[start-and-scale-a-lead-gen-agency]]
