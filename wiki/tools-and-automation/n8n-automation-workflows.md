# n8n Automation Workflows

n8n is the orchestration layer HeyReach's content reaches for most — the "coordinator" in the six-layer agent model ("n8n is the coordinator") (source: "AI outreach agent: From sequences to systems that think") and the "glue" between platforms that lack native integrations (source: "How to Get Unlimited Leads on LinkedIn Using N8N + Clay.com + HeyReach"). HeyReach ships **native n8n nodes** and a per-workspace API key, and its blog/channel publish numerous copy-ready n8n templates. The GTM-agents roundup profiles n8n at 162,000+ GitHub stars, 230,000+ users, 500+ integrations, execution-based billing (Business €800/mo) (source: "The Best AI Agents for GTM Engineering (Your 2026 Stack Guide)"). This article covers setup, the node set, and the standard n8n patterns; the full end-to-end recipes live in [[automation-workflow-templates]]. HeyReach authors most of this (COI); named practitioners are flagged.

## Setup: native nodes (web + desktop)

Get the key in HeyReach: Integrations → n8n → **Connect Now → Generate New n8n (API) Key** (unique per workspace, so client/team setups stay separate; each workspace also has its own MCP Server URL + MCP Key) (source: "How to Integrate HeyReach with n8n (and automate your LinkedIn workflows)"). Then:
- **n8n Web:** Add first step → select HeyReach API as trigger → install the required nodes → create a Webhook → new Credential (paste the n8n key) → set Resource, Operation, Event Type → Execute (green = success). Confirm in HeyReach → Integrations → Webhooks.
- **n8n Desktop:** Community nodes → Install a Community node → npm package **`n8n-nodes-heyreach`** → I agree.

Installing the nodes unlocks HeyReach actions grouped as **Campaigns, Unibox, Lists, Stats, Webhooks** (source: "How to Integrate HeyReach with n8n (and automate your LinkedIn workflows)"). The first workflow is usually "Add leads to campaign" (Campaign Actions → Add leads to campaign → paste key → set "Allow HTTP Requests Domain to All" → Execute). For actions without a native node, use an HTTP Request node against the API (see [[heyreach-campaign-api-and-webhooks]]).

## The standard reply-handling pattern

The most-repeated n8n build captures every HeyReach reply, classifies sentiment, and syncs a CRM. Canonical shape (source: "The AI Agent Every LinkedIn Outreach Campaign Needs"):

1. **Webhook trigger** on the reply event (payload includes message text, timestamp, isReply, conversation ID, campaign, sender, lead, list, event type). Use the newer **"every message/inmail reply received"** event, not the legacy "first message reply received," so you re-analyze on each reply.
2. **Set-variables** node holds the HeyReach API key.
3. **HTTP call to the "get chat room" endpoint** (account ID + conversation ID from the webhook) → returns the full thread.
4. **Code node** flattens the JSON message array into labeled plain text (each line "me" vs the correspondent + timestamp + body).
5. **AI sentiment agent** (an LLM node — sources use GPT-4o mini, O3 Mini, or GPT-4.1 mini) reads the whole thread and outputs one value (positive / negative / neutral / unsure).
6. **Write to CRM** (HubSpot custom properties, or Attio via HTTP), plus a **Slack** alert / approval gate.

Key insight repeated: sentiment "is not set in stone" — it flips message-to-message (interested → ghost → "push to next quarter"), so re-analyze the WHOLE thread on every new reply (source: "The AI Agent Every LinkedIn Outreach Campaign Needs"). To send a reply back, POST to HeyReach's Postmaster with `message, subject, conversationId, linkedInAccountId, senderId` (source: "How to automate LinkedIn outreach using Clay, HeyReach and n8n").

## Reliability patterns

HeyReach's guides bake in guardrails (source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook", author Umer Ishaq — COI, books his own calls):
- **Slack "send message and wait for response"** node with Approve/Decline buttons and a ~10-minute timeout as the human gate; Decline loops the agent to regenerate.
- **Global error workflow** → Slack `#ops-outbound`; auto-throttle if ≥3 errors in 10 minutes (pause + ping Slack).
- **If nodes** branch on event_type / sentiment / message-contains-a-time.
- Weekly metric targets: fallback hit rate >10% → fix variable mapping; Slack approval turnaround <10 min; errors per 100 webhooks <1.
- GDPR: log lawful interest + opt-out, suppress "stop/unsubscribe."

The reporting-automation guide adds five common n8n mistakes: forgetting "Always output data" when creating a weekly sheet; using dynamic sheet names directly in nodes; API rate-limit "too many requests" when looping campaigns in the same second (enable retry-on-fail with a ~2-second delay); pulling Gmail fields from the wrong branch; and treating an empty weekly reply tab as an error (source: "Automate your LinkedIn outreach campaign reports").

## Add to CAMPAIGN vs. add to LIST

A critical n8n gotcha: use **"add leads to campaign," not "add to list"** — a *finished* campaign ignores leads added to its list, whereas adding to the *campaign* re-triggers it for the new leads (source: "I Built an AI Agent in n8n That Books Sales Calls For You"; source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook"). The Add-Lead-to-Campaign endpoint is also "re-activation safe."

## Testing LLM steps

Because "LLMs are a bit like a black box," test them. n8n **evaluations** connect a Google Sheet of test rows (e.g. "messages" + "expected sentiment"), run them through the agent, and compare — "light" evaluations while building, "metric-based" for production (source: "The AI Agent Every LinkedIn Outreach Campaign Needs"). A JavaScript fallback (`$json.body exists ? real data : hard-coded`) lets you test with real content vs a trigger's dummy data (source: "I Built an AI Agent in n8n That Books Sales Calls For You"). A recurring AI-copy rule across these builds: "Do not use m dash symbol" to avoid an AI tell.

## Where the full recipes live

n8n powers most of the end-to-end plays — sentiment-triage inbox, automated Monday reports, YouTube-comments→LinkedIn, signal→enrich→outreach, CRM hygiene, and lead routing. Rather than duplicate them here, see [[automation-workflow-templates]]. HeyReach maintains a template library at /n8n-templates.

## Related
- [[make-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[heyreach-campaign-api-and-webhooks]]
- [[heyreach-mcp-server]]
- [[clay-enrichment-and-data-waterfall]]
- [[automation-workflow-templates]]
- [[crm-integrations]]
- [[signal-and-intent-integrations]]
- [[ai-outreach-agent-architecture]]
- [[manage-replies-and-inbox-at-scale]]
- [[agency-client-onboarding-and-reporting]]
