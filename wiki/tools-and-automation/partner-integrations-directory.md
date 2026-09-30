# Partner Integrations Directory

A one-stop index of every tool HeyReach connects with across its content, grouped by role in the stack, with a one-line description and a pointer to the deep-dive article. HeyReach's own interfaces (MCP, CLI, Campaign API) are the connection surfaces; everything else plugs in via API key, OAuth, native module, or webhook. This is a HeyReach-first-party corpus (COI) — treat "native," "official," and result claims as vendor claims. Connection method and setup mechanics for each tool are in the linked articles.

## HeyReach's own interfaces
- **MCP server** — natural-language control from any MCP client; free; per-workspace endpoint. See [[heyreach-mcp-server]] (source: "Beginner’s guide to MCP in HeyReach: clean lists and clear inboxes").
- **CLI** — npm-installed tool wrapping all 47 API endpoints, doubling as MCP tools; built by Top of Funnel. See [[heyreach-cli]] (source: "The Best AI Agents for GTM Engineering (Your 2026 Stack Guide)").
- **Campaign / public API** — REST endpoints for campaigns, leads, inbox, analytics, routing (`add-lead` / `pause-lead` / `assign-lead`) + webhooks. See [[heyreach-campaign-api-and-webhooks]] (source: "Introducing HeyReach Campaign API").

## AI agent runtimes
- **Claude** (Anthropic) — the most-cited reasoning layer; connects via MCP connector or Claude Code + CLI. See [[ai-agent-builds-claude-openclaw-hermes]] (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").
- **ChatGPT / OpenAI, Cursor** — alternative MCP clients / in-workflow reasoning modules (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").
- **OpenClaw** — third-party agent framework (openclaw.ai) run in chat/VPS + HeyReach CLI (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent").
- **Hermes agent** — third-party agent with persistent memory, Slack-driven (source: "How I Get Unlimited Leads With Hermes Agent + LinkedIn").

## Enrichment & data providers → [[clay-enrichment-and-data-waterfall]], [[data-enrichment-tools-and-providers]]
- **Clay** — enrichment control layer, 100+ sources, Claygent, native "Add Lead to Campaign" (source: "How to integrate HeyReach with Clay?").
- **Persana AI** — enrichment + data orchestration; conditioned "If connection" sequence (source: "How to integrate HeyReach with Persana").
- **Bitscale** — signal-driven GTM platform, waterfall enrichment + BitAgent openers (source: "HeyReach + Bitscale: Turn signals into LinkedIn outreach, automatically").
- **FullEnrich** — LinkedIn-URL-based enrichment with async webhook callback (source: "How to turn website visitors into leads using RB2B and HeyReach").
- **Apollo, Prospeo, Cognism, Lusha, Hunter.io, Ocean.io, Crustdata, ZoomInfo, BetterContact, and more** — provider landscape (source: "Your CRM is only as good as your data: Best B2B data enrichment tools in 2026").

## Signal & intent → [[signal-and-intent-integrations]]
- **Trigify** — real-time LinkedIn/social signal triggers, off-account scraping (source: "How to connect HeyReach & Trigify for smarter LinkedIn outreach").
- **traxy** (traxxi.ai) — LinkedIn listening layer, auto-push active leads (source: "HeyReach + traxy Integration guide").
- **Jungler** — LinkedIn engagement → evergreen HeyReach campaign, no Clay step (source: "HeyReach + Jungler: Turn LinkedIn Engagement Into Booked Meetings, Automatically").
- **Clearcue** — buying-intent intelligence, native or MCP via Claude, signal stacking (source: "HeyReach + Clearcue integration guide").

## Website-visitor identification → [[website-visitor-identification]]
- **RB2B** — person-level de-anonymization (US), native HeyReach integration + hot-lead/hot-page tags (source: "How to turn website visitors into leads using RB2B and HeyReach").
- **IntentStream** — 200M+ identity graph + DSP, multichannel activation (source: "HeyReach + IntentStream integration guide").
- **Factors AI** — intent-triggered workflows, Apollo-enriched, prebuilt HeyReach templates (source: "How to integrate HeyReach with Factors AI").

## CRMs → [[crm-integrations]]
- **HubSpot** — native OAuth integration, 20-property group, activity timeline, reply sentiment (source: "HubSpot integration is live: sync outreach activity automatically").
- **Attio** — community-built app, two-way, up to 12 webhooks (source: "HeyReach + Attio integration guide").
- **Breakcold** — relationship CRM; auto/manual push, reply-sync via webhooks (source: "How to integrate HeyReach with Breakcold for effortless LinkedIn outreach").
- **Alysio** — GTM AI workspace, OAuth, natural-language prospecting (source: "HeyReach + Alysio integration guide").
- **HotHawk** — shared team inbox + CRM, white-label client access (source: "HeyReach + HotHawk integration guide").
- **Salesforce / Pipedrive / Close** — via orchestrators or Alysio (source: "How to connect HeyReach with Zapier").

## Multichannel email & AI copy → [[multichannel-email-and-ai-copy-integrations]]
- **Instantly** — bidirectional LinkedIn↔email, Find Email branching (source: "HeyReach + Instantly integration guide").
- **Smartlead** — native, SmartAgents, agency-oriented (not for white-label users) (source: "HeyReach + Smartlead integration: Complete setup guide").
- **EmailBison** — native, auto-push on no-reply within 3 days (source: "How to Connect HeyReach with EmailBison (Full Integration Guide)").
- **SmartReach AI** — LinkedIn copy generation via `{connection}`/`{follow_up_n}` variables (source: "How to connect HeyReach + SmartReach AI for automated and hyper-personalized LinkedIn campaigns").
- **Twain** — AI personalization layer, `{{var | fallback}}` syntax (source: "How to Integrate HeyReach with Twain to automate personalized outreach").

## Orchestration & notifications → [[n8n-automation-workflows]], [[make-automation-workflows]], [[zapier-albato-and-other-orchestrators]]
- **n8n** — native nodes + community npm node; the deepest orchestration option (source: "How to Integrate HeyReach with n8n (and automate your LinkedIn workflows)").
- **Make** — native modules + scenario library; AI routing + LinkedIn/email logic (source: "How to integrate HeyReach with Make (in under 5 minutes)").
- **Zapier** — no native app; webhook + Bearer-token API (source: "How to connect HeyReach with Zapier").
- **Albato** — 600+ apps, two-way; event types must match (source: "How to connect HeyReach with Albato (and automate outreach like a pro)").
- **Pabbly Connect** — webhook fan-out to Slack/HubSpot/Sheets/Gmail (source: "How to Integrate HeyReach with Pabbly").
- **Cargo** — visual "Plays," data-source → HeyReach pipelines (source: "How to Integrate HeyReach with Cargo").
- **Slack** — native Incoming Webhook notifications (accepted / reply / campaign completed); the standard human-approval channel (source: "How to connect HeyReach with Slack").

## Supporting tools seen in workflows
- **Apify** (scrapers), **Google Sheets/Docs/Drive**, **Airtable**, **Gamma** (AI decks), **Typeform/Tally**, **Google Calendar**, **Notion** — appear across the recipes in [[automation-workflow-templates]].

## Related
- [[heyreach-mcp-server]]
- [[heyreach-cli]]
- [[heyreach-campaign-api-and-webhooks]]
- [[ai-outreach-agent-architecture]]
- [[ai-agent-builds-claude-openclaw-hermes]]
- [[clay-enrichment-and-data-waterfall]]
- [[data-enrichment-tools-and-providers]]
- [[signal-and-intent-integrations]]
- [[website-visitor-identification]]
- [[crm-integrations]]
- [[multichannel-email-and-ai-copy-integrations]]
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[automation-workflow-templates]]
- [[gtm-stack-and-automation-strategy]]
