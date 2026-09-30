# HeyReach: Features

This is the feature catalog for HeyReach as described on its own product pages, self-reviews, and changelog posts — all first-party vendor descriptions. HeyReach's feature story clusters around five pillars: (1) **unlimited senders + auto-rotation**, (2) the **Unibox** unified inbox, (3) **agency org structure** (workspaces, Master View, roles, white-label), (4) a **conditional Sequence Builder** with personalization and A/B testing, and (5) **analytics** including AI reply-sentiment auto-tagging (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams"; source: "10x your LinkedIn outbound. Unlimited senders, one fixed cost"). Feature-release dates below are tagged where known, because both the UI and the surrounding LinkedIn limits change fast.

## Senders, rotation, and account connection

- **Unlimited LinkedIn senders for one flat fee, with automatic sender rotation** across accounts in a campaign — the headline capability, which the self-review claims makes HeyReach "the only tool" with multi-account rotation (source: "10x your LinkedIn outbound. Unlimited senders, one fixed cost"; source: "HeyReach alternatives: An honest breakdown from the people who built it").
- **Auto lead-splitting across senders:** a large list is divided across selected accounts (e.g., a 10,000-lead list splits ~3,333 across three accounts) and rotated to finish faster (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Account connection options:** "infinite login" (recommended, supports 2FA) or credentials login (email + password) (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial"). The demo calls infinite login the path to "maximum performance" — a vendor claim (source: "10x Your LinkedIn Outbound With HeyReach [Demo Video]").
- **Per-account daily sending limits** are auto-applied and configurable (connection requests, messages, InMails, follows, profile views, post-likes), and HeyReach auto-splits activity across a sender's campaigns without exceeding the cap (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams"). The specific safe thresholds (e.g. ~40 actions/day, 25 connection requests/day) are covered in [[safe-linkedin-sending-limits]].

## Unibox (unified inbox)

The **Unibox** consolidates every sender's campaign replies into one inbox so operators don't log in and out of accounts (source: "10x your LinkedIn outbound. Unlimited senders, one fixed cost"). Key capabilities:

- **Reply on behalf of teammates / take over any conversation**, and record and **send voice notes from desktop** (source: "HeyReach for sales teams"). HeyReach can also turn a script into audio "in the sender's own voice" via AI (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams").
- **Privacy scoping — "keep personal messages private":** only campaign-initiated conversations are shown, so private DMs stay private; the operator can choose to track campaign-only conversations or import all conversations (backfilling the prior 30 days) (source: "HeyReach for sales teams"; source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Tags, favorites, canned messages/templates, and an activity timeline** per conversation (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Bulk Actions (changelog update):** select multiple conversations to Add to list, Add to campaign, Edit tags in bulk, or Export to CRM in one click; a merged **Filters menu** replaced separate Workspaces/Senders dropdowns; conversation-level actions expose the full action set inside each thread; the update also shipped "significantly faster performance" (source: "Unibox just got sharper: bulk Actions, faster inbox & cleaner UI").

See [[manage-replies-and-inbox-at-scale]] for the workflow playbook built on Unibox.

## Workspaces, Master View, roles, and white-label

- **Workspaces** — separate, secure per-client (or per-team) environments with isolated data and controlled access: "Onboard a new client in minutes, not days" (source: "HeyReach for lead gen agencies"). Sales teams can split by sales/marketing/support (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Master View / Masterview** — one unified dashboard (and a **Masterbox** for centralized cross-account replies) spanning all workspaces for KPI monitoring and cross-client reporting (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams"; source: "Expandi vs Dripify: Which LinkedIn automation tool is better for agencies?").
- **Permissions & Roles** — Admin (full access incl. billing, invites, workspace management) vs Member (granular view/edit rights on LinkedIn Senders, Leads, My Network, Campaign, Unibox, Integrations & API; no billing) — e.g. give a VA inbox-only access (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams"; source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **White-label** — "Your logo, your colors, your domain, your sign-in page. Clients see your product, not ours," with multi-brand white-label supported (source: "HeyReach for lead gen agencies"). Included in the Agency tier; multi-brand is an add-on on Unlimited (see [[heyreach-pricing]]).

## Sequence Builder, campaign types, and personalization

- **Conditional ("If Connected") sequences** — drag-and-drop branching that segments current connections from new ones (e.g., skip the connection request if already connected). A typical flow: "connect, like post, wait 3 hours, send message, end on reply or no reply" (source: "HeyReach for growth teams"; source: "10x your LinkedIn outbound. Unlimited senders, one fixed cost").
- **LinkedIn action steps** — connection requests (with or without a note), messages, InMails, profile views, follows, and post-likes; plus email fallback via native integrations or webhook (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Sequence Builder rebuild (changelog):** two entry points — "Build it your way" (blank canvas) or "Start with a template" (real outreach patterns); a redesigned inline action drawer (LinkedIn steps + conditions + multichannel actions in one place, no popups); delays visualized on the canvas; Fit-to-Canvas/zoom navigation (source: "Preview message + new Sequence Builder").
- **Personalization variables** — presets (first name, last name, position, company, location) plus **custom variables pulled from your CSV**, with a required **fallback message** when a variable is missing; HeyReach swaps variables automatically per lead (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Message preview (changelog):** shows exactly how each message renders per lead with variables filled in, and warns when custom data is missing — "No more guessing whether {{first_name}} quietly renders as 'Hey there, .'" (source: "Preview message + new Sequence Builder").
- **Auto-withdrawal** of unanswered connection requests after N days (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams").

For message and sequence design methods see [[linkedin-message-formulas]] and [[outreach-sequence-architecture]].

## A/B testing

HeyReach runs A/B tests natively via **"Add Message Variation"** inside a single campaign (available in the Send Connection Request, Send Message, and InMail steps) — running two separate campaigns on the same sender is *not* a valid test because sender capacity distributes proportionally with priority to whichever launched first (source: "How to a/b test LinkedIn outreach inside HeyReach (and actually trust the results)"). Two variations are recommended (more variations = fewer leads per version = noisier data). Results compare **acceptance rate** and **reply rate**, with dashboard CSV export to a test log. HeyReach's first-party benchmark across **96,051 campaigns** is a median acceptance rate ~21% and reply rate ~22% against qualified-lead lists (source: "How to a/b test LinkedIn outreach inside HeyReach (and actually trust the results)"); see [[linkedin-outreach-benchmarks]].

## Analytics, reporting, and Positive Reply Rate

- **Real-time dashboards** with acceptance rate, reply rate, InMail stats, and progress; filterable by date range, campaign, sender, and team for "clean attribution"; per-step drill-down; leads analytics show failure reasons (source: "HeyReach for growth teams"; source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Positive Reply Rate / "Interested Leads" (feature launch):** HeyReach auto-analyzes the sentiment of every reply and auto-tags leads **Interested / Generic / Negative** across four surfaces — the dashboard (new "Interested Leads" metric), campaign-level analytics, the Unibox (a sentiment tag per conversation), and **webhooks** (new event types Auto-tag Positive/Generic/Negative). The auto-tag is **locked/non-editable "to preserve data integrity,"** though custom tags can be layered on top. "Live for all HeyReach users. No setup required." (source: "Positive reply rate is live: Auto-detect warm leads").
- **HeyReach Analytics 2.0** — positioned as co-built with power users, "campaign insights 10x sharper, without losing the simplicity" (source: "HeyReach webinars").

## Multichannel and enrichment

- **Native email integrations** — Instantly, Smartlead, and EmailBison, with two-way lead-data sync so a reply on either channel auto-pauses steps everywhere ("This prevents the awkward scenario of messaging someone on LinkedIn while simultaneously emailing them the same pitch") (source: "Multichannel outreach, done right").
- **"Find Email" step** — built-in, credit-based email enrichment to identify verified professional emails inside HeyReach: "Drag, drop, sync - no GTM engineer needed" (source: "Multichannel outreach, done right").
- **Enrichment credits** are allocated per sender by tier (100 / 1,000 / 3,000) — see [[heyreach-pricing]] (source: "Unlimited senders, one flat monthly fee").

See [[multichannel-linkedin-email-sequencing]] and [[multichannel-outreach-architecture]] for the sequencing playbook.

## Deliverability, safety, and data controls (the "security" story)

HeyReach's security framing is primarily **account safety and data isolation** rather than formal compliance certification:

- **Dedicated residential proxy per LinkedIn account "that never rotates IP addresses,"** geo-matched to the account's login location (e.g. a Chicago account gets a Chicago proxy); use HeyReach's or bring your own (source: "HeyReach for lead gen agencies"; source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams"). Proxy provision differs by tier (included on Growth; BYO on Agency/Unlimited) — see [[heyreach-pricing]].
- **Exclusion / do-not-contact lists and de-duplication** — campaigns can auto-exclude anyone already contacted by any team member/campaign, plus apply do-not-contact/exclude lists and workspace-level anti-duplication (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial"; source: "The best LinkedIn management tools for scaling outreach without getting banned").
- **Workspace data isolation + granular permissions** (above) and **private-messages-private** scoping in Unibox provide the data-access controls.
- **Gap:** the product pages in this corpus do **not** claim formal security certifications (SOC 2, ISO 27001, GDPR tooling) for HeyReach itself — those appear only for competitors such as Factors.ai and Lemlist (source: "29 Best AI sales tools in 2026 to crush your outreach, not your sales team"; source: "Stop doing it manually: 12 LinkedIn messaging automation tools worth using in 2026"). Treat certification as unstated, not confirmed.

## Integrations, API, and webhooks

- **Powerful API + webhooks** (Postman docs referenced), API key issued in Settings/Integrations (source: "10x your LinkedIn outbound. Unlimited senders, one fixed cost"; source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- **Native HubSpot CRM sync** ("verified by HubSpot") logs every connection, message, and reply as a contact activity; on install it creates a HeyReach property group of **20 properties** and can source campaigns from HubSpot static/dynamic lists (source: "HubSpot integration is live: sync outreach activity automatically"). See [[agency-client-onboarding-and-reporting]].
- **Import sources:** Sales Navigator, LinkedIn free search, groups, events, posts, CSV, plus Clay, RB2B, Trigify, HubSpot, and (on the sales page) Apollo, ZoomInfo, CommonRoom (source: "HeyReach for sales teams"; source: "10x Your LinkedIn Outbound With HeyReach [Demo Video]"). "From lead list to live campaign in under sixty seconds" (source: "HeyReach for growth teams").
- **MCP server, CLI, and Campaign API** as programmatic surfaces — see [[heyreach-mcp-cli-and-api]] and the tools-and-automation category for wiring.

## Related
- [[heyreach-product-overview]]
- [[heyreach-pricing]]
- [[heyreach-mcp-cli-and-api]]
- [[heyreach-positioning-by-segment]]
- [[manage-replies-and-inbox-at-scale]]
- [[safe-linkedin-sending-limits]]
- [[linkedin-outreach-benchmarks]]
- [[multichannel-linkedin-email-sequencing]]
- [[outreach-sequence-architecture]]
