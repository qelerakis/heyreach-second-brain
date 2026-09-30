# HeyReach Campaign API & Webhooks

HeyReach's public/Campaign API gives programmatic control of campaigns, leads, the inbox, analytics, and lead routing — "No tabs. No logins. Just results" (source: "Introducing HeyReach Campaign API"). It is buildable from Claude, OpenClaw, Slack, "or any tool," and complements the [[heyreach-mcp-server]]; the [[heyreach-cli]] wraps its ~47 endpoints. This article documents the API surface, the sequence-node model, the lifecycle rules, the lead-routing endpoints, reply-sending ("Postmaster"), and the webhook catalog. All of this is HeyReach's own product documentation (COI). HeyReach itself cautions: "Campaign API is powerful. Improper usage could affect other areas of the tool" (source: "Introducing HeyReach Campaign API").

## Authentication

All endpoints require an API key from **Settings → API** (also reachable as Integrations → HeyReach API → Get API Key). Auth is a Bearer token: add header `Authorization: Bearer YOUR_API_KEY` (source: "How to connect HeyReach with Zapier"). API keys are commonly generated per-integration/per-workspace (a Clay-specific key, a Make-specific key, etc.), and each workspace scopes which LinkedIn accounts are visible.

## Core campaign endpoints

From the Campaign API reference (source: "Introducing HeyReach Campaign API"):

- **POST /api/public/campaign/Create** — `CreateCampaignApiInputDto`: `name` (1–50 chars), `linkedInUserListId` (must be a USER_LIST), `linkedInAccountIds` (int[], 1–100 sender accounts), exclusion flags (`excludeContactedFromOtherCampaigns` / `excludeHasOtherAccConversations` / `excludeContactedFromSenderInOtherCampaign`), `excludeListId`, `schedule` (defaults Mon–Fri 09:00–17:00 UTC if omitted), and `sequence`. **Create makes a DRAFT** — `StartCampaign` must be called separately to activate.
- **UpdateSettings** — name, lead list, exclusions. The lead list is **locked once a campaign has started at least once**.
- **UpdateSequence** — full replace of the workflow; retrievable via GetCampaignSequence.
- **UpdateAccounts** — **full replacement (not merge)**, 1–100 IDs; removed accounts stop their in-flight leads on a PAUSED campaign.
- **UpdateSchedule** — `startDate` is immutable after the first start.
- **GET GetCampaignSequence** — returns a `PublicSequenceNodeDto` reusable directly in Create/UpdateSequence.

**Lifecycle statuses:** DRAFT, SCHEDULED, ACTIVE, PAUSED, COMPLETED. Most updates are blocked on ACTIVE/COMPLETED; editing a SCHEDULED campaign reverts it to DRAFT; PAUSED sequence updates do a "safe update" remapping lead states (source: "Introducing HeyReach Campaign API").

## The sequence tree

A sequence is a tree of `PublicSequenceNodeDto` nodes with fields: `nodeType`, `unconditionalNode` (the false/next path), `conditionalNode` (the true path, branching nodes only), `actionDelay` (0–100), `actionDelayUnit` (HOUR | DAY), `payload`, and `externalReference` (≤100 chars, for webhook tracking) (source: "Introducing HeyReach Campaign API").

**Node types:** CONNECTION_REQUEST (both branches), MESSAGE (unconditional; a conditional-on-reply must be END), INMAIL, VIEW_PROFILE, FOLLOW, LIKE_POST, FIND_EMAIL (branches = found / not found), CHECK_IS_CONNECTION (both branches), CHECK_IS_OPEN_PROFILE (both branches), SEND_LEAD_TO_INSTANTLY, SEND_LEAD_TO_SMARTLEAD, SEND_LEAD_TO_BISON (EmailBison), and END (leaf). **Validation:** every path ends in END; CONNECTION_REQUEST, CHECK_IS_CONNECTION and CHECK_IS_OPEN_PROFILE require BOTH branches; all other non-END nodes require `unconditionalNode` only (source: "Introducing HeyReach Campaign API").

**Payload constraints (clean values):**
- ConnectionRequest: messages ≤300 chars each (may be blank); `fallbackMessage` required if variables are used; `toBeWithdrawnAfterDays` ≥14 (null = never); supports `{{firstName}}`.
- Message: ≥1 message, ≤8000 chars each.
- InMail: subject ≤200, body ≤1900 chars.
- PostLike: `reactionType` (LIKE / CELEBRATE / SUPPORT / FUNNY / LOVE / INSIGHTFUL / CURIOUS), `randomReaction`, `reactBefore` (DAY1 / DAY3 / WEEK1 / WEEK2 / MONTH1 / MONTH3), `skipDelayIfCannotLike`.
- SendToInstantly: `instantlyResourceId` (UUID), `resourceType` (LIST / CAMPAIGN). SendToSmartLead: `smartLeadCampaignId` (≥1).
- Schedule DTO: `dailyStartTime`/`dailyEndTime` (TimeSpan, max "24:00:00", start < end), `timeZoneId` (IANA, default "Etc/GMT"), Mon–Fri enabled by default / Sat–Sun off, optional `startDate`/`endDate`.

*Note: the raw API doc contains OCR/placeholder artifacts (a lorem-ipsum row, "SEND_LEAD_TO_BISONt" typos, a duplicated node) that are not real API semantics; the node/payload names above are the clean values (source: "Introducing HeyReach Campaign API").*

## Lead-routing endpoints (add / pause / assign)

For orchestration, HeyReach's lifecycle guide names the three most-used public actions (source: "Your lifecycle strategy is leaking revenue — Here’s how to patch it"):

- **POST /campaign/add-lead** — add a lead to a campaign (requires a valid LinkedIn URL + Campaign ID).
- **POST /campaign/pause-lead** — pause a lead (e.g. when a human replies, or a "closed won"/opt-out fires).
- **POST /campaign/assign-lead** — assign a lead / Unibox sender.

These can be triggered by an orchestrator (n8n/Make/Zapier), by the MCP ("let an AI agent trigger these same actions"), or the CLI. One caveat (as of the article's writing): **"Assigning Unibox senders isn't supported natively in HeyReach or n8n"** — you must use an HTTP module against the API, or fall back to a shared sender/tag (source: "Your lifecycle strategy is leaking revenue — Here’s how to patch it").

The key distinction practitioners flag: **"Add Lead to Campaign" vs "Add to List"** — a *finished* campaign ignores leads added to its list, but adding to the *campaign* re-triggers it for the new leads (source: "I Built an AI Agent in n8n That Books Sales Calls For You"; source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook").

## Sending replies (Postmaster) & reading threads

To send a reply programmatically, HeyReach's "Postmaster" send takes a JSON body of `message, subject, conversationId, linkedInAccountId, senderId` with the API key in headers and `Content-Type: application/json` (source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook"; source: "How to automate LinkedIn outreach using Clay, HeyReach and n8n"). To read a whole thread, call the **"get chat room"** endpoint with the account ID + conversation ID (both delivered in the reply webhook) to return all messages in the thread (source: "The AI Agent Every LinkedIn Outreach Campaign Needs"). Reply payloads arrive as an **array of messages**, each with a creation time, text, and an `isReply` boolean (false = you sent it, true = the prospect replied) (source: "How to Get Unlimited Leads on LinkedIn Using N8N + Clay.com + HeyReach").

## Webhooks

Webhooks are configured under **Integrations → Webhooks / View/Create Webhooks**, bound per-campaign and per-event. The event catalog across HeyReach's integration guides:

| Event | Cited in |
|---|---|
| Connection request accepted | Slack, Zapier, Albato, Pabbly, Attio |
| Message / InMail reply received | Slack, Pabbly, Albato |
| First message reply received (legacy) | (older, single-fire) |
| Every message / InMail reply received (new) | The AI Agent Every LinkedIn Outreach Campaign Needs |
| Message sent | Albato, Attio |
| Lead tag updated | HotHawk, "personalized lead magnets" workflow |
| Campaign completed | Slack |
| Connection request sent | N8N + Clay video |

Sources for the catalog: (source: "How to connect HeyReach with Slack"; source: "How to connect HeyReach with Zapier"; source: "How to Integrate HeyReach with Pabbly"; source: "The AI Agent Every LinkedIn Outreach Campaign Needs"). The community Attio app **auto-creates up to 12 webhooks** (one per event type) on connect (source: "HeyReach + Attio integration guide"). The newer "every message/inmail reply received" event (vs the old "first message reply received") is what enables whole-thread re-analysis on each reply (source: "The AI Agent Every LinkedIn Outreach Campaign Needs").

**Native n8n nodes** expose the API without hand-rolling HTTP: Campaigns, Unibox, Lists, Stats, Webhooks (source: "How to Integrate HeyReach with n8n (and automate your LinkedIn workflows)") — see [[n8n-automation-workflows]].

## Constraints quick-reference

Name 1–50 chars; connection note ≤300 chars; message ≤8000 chars; InMail subject ≤200 / body ≤1900 chars; `externalReference` ≤100 chars; 1–100 sender accounts per campaign; `toBeWithdrawnAfterDays` ≥14; `actionDelay` 0–100; default schedule Mon–Fri 09:00–17:00 UTC (source: "Introducing HeyReach Campaign API"). A recurring **hard product rule**: HeyReach rejects old-style LinkedIn URLs containing `/pub/` — use the standard `linkedin.com/in/username` format or the lead fails (source: "HeyReach + Attio integration guide").

## Related
- [[heyreach-mcp-server]]
- [[heyreach-cli]]
- [[ai-outreach-agent-architecture]]
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[multichannel-email-and-ai-copy-integrations]]
- [[automation-workflow-templates]]
- [[outreach-sequence-architecture]]
