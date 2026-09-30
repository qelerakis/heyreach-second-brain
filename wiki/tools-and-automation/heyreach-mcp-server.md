# HeyReach MCP Server

The HeyReach MCP (Model Context Protocol) server lets any MCP-capable LLM — Claude, ChatGPT, Cursor, Clay, n8n — drive HeyReach in natural language: launch campaigns, draft messages, analyze performance, and act on warm leads "without touching the app" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). HeyReach positions MCP as "a translator between AI and your outbound tools" built on the open **JSON-RPC 2.0** standard, with the memorable line "AI without MCP is a colleague who's smart but has no access to your systems" (source: "Beginner’s guide to MCP in HeyReach: clean lists and clear inboxes"). This is HeyReach's own product (COI); everything here is vendor documentation. For where MCP sits in the agent stack, see [[ai-outreach-agent-architecture]]; for specific agent builds, [[ai-agent-builds-claude-openclaw-hermes]].

## Setup

Per-workspace and no-config: (1) go to Integrations in your HeyReach workspace; (2) copy your MCP key (each workspace connects through its own dedicated MCP endpoint); (3) paste the key into the tool — Claude, ChatGPT, or Clay. "Deployment is instant, no complex config; runs securely in HeyReach's cloud" (source: "Beginner’s guide to MCP in HeyReach: clean lists and clear inboxes"). Each Workspace has its own **MCP Server URL + MCP Key** (kept separate from the n8n API key), so client/team setups stay isolated (source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook").

For an operator wiring it into an MCP host, HeyReach's guide: HeyReach → Integrations → copy MCP endpoint + API key → add as a custom connector in the host (Claude/Cursor) → use **HTTP streamable transport (SSE being deprecated)** → expose only specific tools; in n8n, add an MCP client and whitelist tools (source: "AI workflow automation agency: The definitive 2026 guide"). The MCP endpoints include built-in authentication and let you "call and merge APIs without any extra setup or dev work" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). Connect at /mcp; it works with a free HeyReach account (source: "HeyReach MCP: Build and launch campaigns end to end").

**Cost:** "How much does HeyReach MCP cost? Nothing, you can use it straightaway" — the MCP is free (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").

## The campaign-building tool set

A product update shipped **8 MCP tools** so an LLM can build and launch a full campaign end to end — "You can now run a full campaign without touching the app" (source: "HeyReach MCP: Build and launch campaigns end to end"):

| Tool | Function |
|---|---|
| `CreateCampaign` | Create a draft campaign |
| `CreateCampaignFromTemplate` | Clone an existing campaign |
| `UpdateCampaignSequence` | Create / replace the whole workflow |
| `UpdateCampaignSettings` | Name, lead list, exclusions |
| `UpdateCampaignSchedule` | Time window, active days, timezone |
| `UpdateCampaignAccounts` | Swap LinkedIn sender accounts |
| `GetCampaignSequence` | Pull the workflow tree |
| `StartCampaign` | Activate a draft live |

These "live automatically for existing MCP users, no update needed." The showcase single-prompt: "Clone my best-performing campaign, swap in this lead list, assign my three warmest senders, set it to send 9-5 CET on weekdays, and launch it" (source: "HeyReach MCP: Build and launch campaigns end to end").

## What MCP is used for (showcases)

HeyReach's beginner guide catalogs the day-one use cases (source: "Beginner’s guide to MCP in HeyReach: clean lists and clear inboxes"):

- **List hygiene** — scan a list, filter by titles/industries, generate a clean version in minutes; a demoed **23k-lead list** was cleaned (keep "Founder/CEO/Owner," exclude interns) "in minutes, no manual review" (credited to HeyReach's own CRO Ilija Stojkovski + GTM engineer Umer Ishaq — a vendor demo, not a customer result).
- **Personalized icebreakers** — read each profile, write a one-line opener, store it on the lead.
- **Generate complete messages** — connection request + first message + follow-up per lead, drafted into the campaign for review.
- **Contacted-check** — verify profile URLs against campaign history before enrichment to skip already-contacted leads and save credits.
- **Inbox tagging with Unibox** — classify replies (positive / not relevant / follow-up later), auto-create tags, draft replies for approval — "Nothing goes out without human review."
- **Seat rotation & rescheduling** — surface seat-usage signals and prompt to rotate accounts before hitting limits.

The MCP can also be **scoped to HeyReach only** and turned into a natural-language interface, e.g. "Retrieve all leads from Sept Leads List... Create a new list 'Clean List – Founders Only'... exclude student/intern" (source: "Best AI sales prompts and role-specific workflows that SDRs and AEs can run today"). You can **chain multiple MCPs** — e.g. Claude → fetch HubSpot contacts → filter → push into HeyReach — and combine with Clay (enrichment tables), n8n (daily analytics → Slack digest), and Cursor (Python jobs) (source: "Beginner’s guide to MCP in HeyReach: clean lists and clear inboxes").

## MCP vs. the API

HeyReach frames the trade-off explicitly: "API = every integration is custom (complexity grows); MCP = one shared standard, any MCP tool connects instantly" (source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook"). The Campaign API "complements the existing HeyReach MCP" for programmatic (dev) control (source: "Introducing HeyReach Campaign API"). The [[heyreach-cli]] wraps the same API and registers each command as an MCP tool, so the three surfaces overlap deliberately.

## Learning resources

The MCP product page links tutorial videos: "AI Agents vs. MCP," "Create custom icebreakers," "Build a campaign that gets replies," "Draft responses to leads who replied," "Filter decision makers in your lead list," and "Analyze sentiment & tag positive replies" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").

## Related
- [[heyreach-cli]]
- [[heyreach-campaign-api-and-webhooks]]
- [[ai-outreach-agent-architecture]]
- [[ai-agent-builds-claude-openclaw-hermes]]
- [[clay-enrichment-and-data-waterfall]]
- [[n8n-automation-workflows]]
- [[automation-workflow-templates]]
- [[manage-replies-and-inbox-at-scale]]
