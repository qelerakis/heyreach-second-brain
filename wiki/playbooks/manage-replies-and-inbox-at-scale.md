# Managing Replies & the Inbox at Scale

How to handle LinkedIn replies across many sender accounts without losing warm leads: consolidate everything into one inbox, triage by intent (not chronologically), respond fast, and route hot replies into a clean SDR→AE handoff. The recurring truth: "starting the conversation is not the issue... keeping it alive in your inbox? That's where deals quietly die," and the biggest funnel drop happens *after* acceptance (source: "Stop losing deals: Build a scalable LinkedIn inbox system with HeyReach"). This is the reply/inbox operations playbook; upstream lead scoring and routing before outreach is [[qualify-and-prioritize-leads]].

## Consolidate into one inbox

The foundational move at scale is a unified inbox (HeyReach's "Unibox") that pulls every reply from every sender/campaign into one place, so a team can work "~10 accounts from one place" without logging in and out or juggling 2FA — and a teammate can reply on a colleague's behalf "without the prospect ever noticing the handoff" (source: "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)"; source: "13 Best B2B lead generation tools to build your stack in 2026"). Core Unibox capabilities used operationally: filter by sender/campaign/tag/message-type/answered-vs-unanswered, apply tags, canned messages/templates, add-to-list, add-to-campaign, export-to-CRM, and (via a later update) bulk actions across many conversations at once (source: "I Sent 5,000,000 LinkedIn DMs: here's what you need to know"; source: "Unibox just got sharper: bulk Actions, faster inbox & cleaner UI"). Feature detail is in [[heyreach-features]].

## Triage by intent, not by timestamp

The core prioritization principle: "the latest reply isn't automatically the most important one" — working the inbox chronologically "leaks pipeline" (source: "Sales prioritization matrix: a 3-step workflow for SDRs to set daily priorities"). Use a small, fixed tag taxonomy so every rep tags the same way. Two near-identical four-tag models recur:

- **Hot Lead / Needs Nurture / Follow Up Later / Low Priority** — Hot = explicit buying intent ("What's the pricing?", "Who's the decision-maker?"); Needs Nurture = interest, no urgency; Follow Up Later = timing objection not rejection; Low Priority = no pipeline value. When torn between Hot and Needs Nurture, pick Hot (source: "Lead prioritization on LinkedIn: Respond to high-intent leads first").
- **Hot / Warm / On-hold / Multi-thread** for SDR→AE inbox systems (source: "Stop losing deals: Build a scalable LinkedIn inbox system with HeyReach").

**Tag → action mapping:** Hot = respond immediately + add to an AE/demo sequence; Needs Nurture = share info + add to a nurture campaign; Follow Up Later = tag only; Low Priority = archive (source: "Lead prioritization on LinkedIn: Respond to high-intent leads first"). Note that adding a lead to a *campaign* (not a list) is how you route them onward for nurture or re-engagement.

## Auto-detect warm leads (sentiment tagging)

HeyReach's Positive Reply Rate feature auto-classifies every reply's sentiment (**Interested / Generic / Negative**) and surfaces an "Interested Leads" count on the dashboard, in campaign analytics, in the Unibox (a sentiment tag per conversation), and as a webhook event — the auto-tag "cannot be edited... it's locked to preserve data integrity," but you can add custom tags on top (source: "Positive reply rate is live: Auto-detect warm leads"). Important nuance: **sentiment is not fixed** — a thread can flip (positive → books call → no-show → "not interested"), so re-analyze the *whole* thread on each new reply, not just the latest message (source: "The AI Agent Every LinkedIn Outreach Campaign Needs"; source: "How to Automate CRM Hygiene in HubSpot Using n8n [Full Workflow Tutorial]").

## The daily triage loop

Run a short, repeatable loop 1–2× per day (morning + afternoon): open Unibox → apply the Unread filter → tag every new reply by intent → switch to the Hot Lead filter → answer all Hot Leads top-down → clear untagged. It takes ~10 minutes; full setup ~20 (source: "Lead prioritization on LinkedIn: Respond to high-intent leads first"). The "sales prioritization matrix" adds a campaign-priority tier on top (scan campaign health first, work the strongest campaigns' replies first) — the campaign-scan half is in [[audit-and-optimize-linkedin-campaigns]] (source: "Sales prioritization matrix: a 3-step workflow for SDRs to set daily priorities"). Task SLAs by tag: Interested → same-hour, Warm → same-day, Not Now → scheduled, Not a Fit → clean and move on.

## Speed-to-lead

Responding fast is the highest-leverage habit — practitioners cite response within **5–10 minutes** to "massively improve your meeting booked rate," because LinkedIn is a social channel people log in and out of (source: "How I’d Generate LinkedIn Leads From Zero (No Network, No Warm Leads)"). HeyReach's SLA bands for a first *human* touch: inbound form ≤5 min, **LinkedIn reply ≤15 min**, referral/intro ≤60 min, with escalation timers (LinkedIn: manager @30, leader @45) and an on-call rotation for after-hours (source: "Sales follow-up workflows: Speed-to-lead benchmarks & SLA templates that win deals"). "Most SDRs lose deals in their inbox, not in their pitch" (source: "Lead prioritization on LinkedIn: Respond to high-intent leads first").

## AI-assisted replies (with a human gate)

AI can draft replies but should not send autonomously. The common pattern: connect an LLM to HeyReach (via MCP or CLI), have it read unread threads, prioritize by intent, and **draft** replies from a company "brain," then approve before send. Tim's Claude workflow builds a Notion "company brain" (products, persona, pains, FAQ, voice) then prompts "look at HeyReach replies that are unread... draft replies for all these leads using the Brain" — with a human approval step, optionally scheduled to deliver drafts via Slack DM on set mornings (source: "Claude Just Changed LinkedIn Outreach Forever (Tutorial)"). Agent versions (OpenClaw/Hermes from Slack): "draft replies for the top five, but do not send until I say good to go" (source: "Copy this OpenClaw system:  it'll BLOW your LinkedIn game overnight"; source: "How Openclaw Runs My Entire LinkedIn Outreach System"). A crucial guardrail from HeyReach's own content: "MCP is the connection protocol, it does not tag, route, or prioritize conversations on its own" — reps keep control (source: "Lead prioritization on LinkedIn: Respond to high-intent leads first"). Some practitioners refuse AI-sent replies entirely — "Once I get a response, I take over and reply myself. No AI-generated replies for my leads" (source: "How to Write a Follow-Up LinkedIn Message & Email [Tactics + Examples]"). The wiring lives in [[heyreach-mcp-server]] and [[n8n-automation-workflows]].

## Inbox management for agencies

At agency scale the inbox needs a system, not willpower (source: "Inbox management for agencies: cut the clutter, close more deals"):

- **"One Touch" rule** (handle a message once) and aim for "inbox *manageable*," not inbox zero — "your LinkedIn inbox isn't a to-do list, it's a communication channel."
- **Time-block** two ~30-min sessions/day with notifications off between; a 4-option decision matrix (Respond if <2 min / Delegate / Archive / Delete).
- **Shared inbox + a trained gatekeeper** filtering twice/day, routing ops questions to Slack and client comms to a PM tool with tags/due dates (Arvind Rongala); Lisa Richards lets the inbox hit 100+ unread for "natural urgency filtration," then answers only messages that match core themes from active profiles.
- Assign inboxes per team member via Workspace roles (e.g. a VA gets inbox-only access).

## Route hot replies into a clean handoff

The final job is getting hot replies to the right person with context. Build the SDR→AE handoff as: auto-alert on a hot reply (HeyReach webhook "Message Reply Received" → keyword/sentiment classify → Slack DM to the owner with lead name, snippet, timestamp, tag), a standardized handoff SOP (SDR captures pain points, budget/timeline, stakeholders, objections, buyer tone), and a CRM sync that pushes Hot/Warm/Booked (skip cold/not-interested) with the thread attached as a note (source: "Stop losing deals: Build a scalable LinkedIn inbox system with HeyReach"). Sync a lead to CRM by first tagging "Meeting Booked" in Unibox, then Export to CRM (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline"). The lifecycle/RACI/SLA detail of handoffs is in [[qualify-and-prioritize-leads]] and the CRM-sync wiring in [[partner-integrations-directory]].

## Related
- [[book-meetings-on-linkedin]]
- [[qualify-and-prioritize-leads]]
- [[audit-and-optimize-linkedin-campaigns]]
- [[signal-based-outreach]]
- [[agency-client-onboarding-and-reporting]]
- [[write-cold-outreach-copy]]
- [[heyreach-features]]
- [[heyreach-mcp-server]]
