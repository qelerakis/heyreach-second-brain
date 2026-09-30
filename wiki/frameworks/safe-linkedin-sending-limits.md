# Safe & Scalable Sending: The LinkedIn Deliverability Rule-Set

HeyReach's deliverability doctrine is that **safe scaling is an architecture problem, not a volume problem** — "what gets restricted is HOW you send," not merely how much (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). The rule-set has two halves: a **safety foundation** (cloud sending, per-account limits, warm-up, human-like activity) and a **scaling mechanism** (multiple real sender accounts rotated on one campaign). This article collects the named rules, the sending-limit numbers (with their inconsistencies preserved), the warm-up schedules, and the restriction/recovery model. Everything here reflects LinkedIn's state **as of 2026** and is HeyReach's own guidance — LinkedIn's limits are undisclosed and dynamic, so treat every number as era-bound and vendor-sourced.

## The 8 rules for safe and scalable outreach

HeyReach's canonical checklist splits into a safety foundation (Rules 1–4) and smart outreach (Rules 5–8) (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool"):

1. **Use a cloud-based tool.** Chrome extensions run from your own browser/IP and "click" inside the page where LinkedIn can detect the script; cloud tools send from remote servers, each account on its own secure proxy, and run with the laptop closed.
2. **Stay within connection limits.** Limits are **dynamic** (depend on account age, SSI score, acceptance rate); "for most teams, each person gets roughly 100 connection requests per week," and "each account gets around 200 actions per day" (every profile view, message, like, follow counts as 1 action).
3. **Warm up new/inactive accounts** over a 3-week plan (below).
4. **Make activity look human** — mix smaller actions before "Connect": view profile → like/comment recent post (optional) → after a delay send the request.
5. **Hyper-segmentation** — laser-focused Sales Navigator lists, layered filters, exclude non-ICP.
6. **Write (or skip) connection messages** — the no-note approach works when the profile tells a strong story ("you can't say the wrong thing if you don't say anything"). See [[linkedin-message-formulas]].
7. **Hygiene** — too many pending requests "can quietly limit your reach"; auto-withdraw unanswered ones after a set number of days.
8. **Combine LinkedIn + email** (multichannel) — LinkedIn "response rate can be 5x higher than email," but don't leave email on the table. See [[multichannel-outreach-architecture]].

## The four-factor restriction model

The deeper "why accounts get flagged even within limits" model: two people can send the same 100/week and one is fine while the other is restricted, "because what gets restricted is HOW you send." Four factors beyond volume (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"):

1. **Timing** — 15 requests in one 10-minute burst then nothing looks robotic; the same 15 spread across hours look normal. "Nobody sits down, fires off 15 connection requests in 10 minutes, and then closes their laptop."
2. **Message similarity** — 500 identical messages get flagged; ~80% can stay the same but the **opening line must change**, or leave the connection request empty.
3. **The account must do more than send** — a real person also views profiles, likes, and comments; bake profile-views + post-likes into the sequence so the account isn't a send-only bot.
4. **Tool type** — cloud (server-side, dedicated per-account IP) vs Chrome extension (detectable in-browser clicking).

HeyReach adds an **auto cool-down**: when LinkedIn starts treating an account as suspicious, it pauses sending before a restriction lands (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). The same idea appears as **auto-freeze near the weekly limit + auto-pause at the daily cap** (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool").

## Sending limits (numbers vary by source — preserve all)

LinkedIn's true limits are undisclosed; HeyReach's sources quote different figures depending on account type, era, and default tool settings. **These do not fully reconcile — keep them side by side:**

| Figure | Value | Source |
|---|---|---|
| Per-week connection requests (general) | ~100/week (~20/day) | "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool" |
| Per-week connection requests (established) | ~100/week per profile (~10–15/day) | "How to CRUSH the New LinkedIn Algorithm in 10 Minutes" |
| Per-week connection requests (new vs warm) | ~100–200/week (new ~100, warm ~200) = 20–40/day | "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)" |
| Per-day connection requests (since 2023) | 20–40/day per account | "Outbound ICP signals: How to spot high-intent leads before your competitors" |
| Actions/day (all action types) | ~200/day | "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool"; "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)" |
| Per-month connection requests | ~400–800/month | "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)"; "LinkedIn DM Strategy: What Works After 5,000,000 Messages" |
| InMail/open-profile emails | 50 paid InMail/month; 800 free open-profile/month | "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)" |
| Safe daily default (agency guidance) | 20–25 connections/day | "Stop scaling too soon: a campaign audit framework that actually works"; "How to manage multiple LinkedIn accounts without getting flagged" |
| Tool default per-account caps | 25 CR/day, 40 messages/day, 40 emails/day | "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial" |
| Tool default per-account caps (alt) | 15 CR/day, 20 messages/day, 20 emails/day | "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)" |

Two more inconsistencies to note: the **weekly reset** is cited as **Monday 2 a.m. Pacific** (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool") and as **Monday 2 p.m. Pacific** (source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)"); and the weekly quota **does not bank/roll over** (source: "LinkedIn DM Strategy: What Works After 5,000,000 Messages"). A critical structural rule: **limits are per LinkedIn account, not per campaign** — a sender in multiple campaigns has its cap split proportionally across them (source: "How to manage multiple LinkedIn accounts without getting flagged"; source: "Perfecting your LinkedIn cold messages: Proven tactics for higher engagement and shorter sales cycles").

## Warm-up schedules for new/idle accounts

Two warm-up ramps appear; both start low and build over ~3 weeks:

- **Week 1: 20–30 actions/day → Week 2: 30–50/day (add follows, skill endorsements) → Week 3: 50–70/day**, keeping the profile complete ("training for a marathon") (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool").
- More conservative: new/idle accounts at **10–15 invites/day for the first two weeks**, then build gradually; launch at **20–25/day max**; accounts under 6 months keep pending under 25 (source: "How to manage multiple LinkedIn accounts without getting flagged"; source: "11 LinkedIn connection message templates that people actually accept"; source: "LinkedIn company expansion strategy: Grow and scale your outreach").

A brand-new account firing 100 requests in week one gets restricted "for sure" (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes").

## Pending-request hygiene

- Withdraw unanswered requests after **14–21 days** (gradually), or 1–2 weeks (source: "How to manage multiple LinkedIn accounts without getting flagged"; source: "11 LinkedIn connection message templates that people actually accept").
- LinkedIn **auto-clears pending requests after 6 months**, and a "little-known" rule **blocks resending to the same person for 3 weeks** (source: "11 LinkedIn connection message templates that people actually accept").
- HeyReach can auto-withdraw pending invites after a chosen window; **its minimum withdrawal window is 14 days** (an AI agent could not set it lower) (source: "How I Get Unlimited Leads With Hermes Agent + LinkedIn").

## Multiple-account management (the scaling mechanism)

Because limits are per person, scale comes from **rotating multiple real sender accounts** on one campaign — HeyReach auto-splits the list and rotates which account sends each request, "each lead gets one message from one profile" (source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)"; source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool"). The safety math a HeyReach source uses: **"100 messages from 1 account = high risk/likely ban; 10 messages from 10 accounts = totally safe"** (source: "The ultimate guide to trigger-based outreach"). The empirical reason is the single-account reply-decay curve (12% → 6% → 2%) and the 6–20-sender reply sweet spot in [[linkedin-outreach-benchmarks]].

### The 5-layer multi-account system

For agencies running 5–50+ senders, the rule is **tool-level workspace isolation** (one workspace per client; each sender is a real person's account added as a seat) — **never multiple browser logins or fake/duplicate profiles** (LinkedIn ToS = one account per person; duplicates risk restriction). The system has five layers: **Isolation → Detection → Diagnosis → Rebalancing → Automation** (source: "How to manage multiple LinkedIn accounts without getting flagged").

- **Isolation:** dedicated Chrome profile per account for manual QA (separate cookies/session/fingerprint); tool-side, each account gets a dedicated IP + device fingerprint. Third-party browser-isolation (GoLogin/Multilogin/SessionBox) is for isolation only, "not to automate outreach — most serious agencies use both."
- **Detection (weekly, not daily):** a restricted sender shows **3–5 days of warning signs** (drifting acceptance, piling pending invites, activity creeping toward limits) before restriction — check every Monday. Track WoW % change with a "safe zone" of pending <20 green / 20–30 yellow / >30 red (>25 for accounts under 6 months).
- **Diagnosis — Account Health Matrix (per sender):** 🟢 acceptance decline <15%, pending <25, activity below limits; 🟡 15–20% decline OR pending 25–35 OR nearing 90/wk; 🔴 >20% drop OR pending >35 OR activity >95/wk OR any pacing alert.
- **Rebalancing (seat rotation):** pause the campaign → duplicate it (clones sequence/timing/targeting) → swap the flagged sender for a fresh 🟢 sender → resume; rest the flagged account **5–7 days** and withdraw its oldest 10–15 pending, spaced out. Whole detection-to-rotation loop ~10–15 min.
- **Automation:** alert via CSV→Sheets→Zapier→Slack, or HeyReach API + n8n, or HeyReach MCP + Claude to flag senders with >15% WoW acceptance drop.

## Restriction vs ban, and recovery

A **restriction is not a ban.** LinkedIn usually just temporarily pauses your ability to send connection requests while it reviews (you can still log in and use the account); acceptance rate typically slips for a few days first, so catch it early. If restricted, ease off that account **~5–7 days** (light/manual use) before sending again, then reintroduce at lower limits (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"; source: "How to manage multiple LinkedIn accounts without getting flagged"). Spam reports are "a targeting problem more than a volume one" and follow an escalation path (report → warning → temporary restriction → account loss), with the first two stages recoverable "but slowly" (source: "11 LinkedIn connection message templates that people actually accept").

## Static residential proxies

Each connected account is assigned a **static residential proxy** tied to a chosen country, so outreach appears from the same location as the account's normal login (no location-discrepancy flag) — e.g. a US agency can run a France-based client's account and have it appear from France (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial"). "Cheaper tools are cheaper for a reason" — they relog daily or rotate cheap proxies/VPNs, triggering repeated 2FA/new-location warnings and restrictions (source: "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)"; source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)"). Note this is a HeyReach differentiation claim; see [[safe-linkedin-sending-limits]] cross-links in product-and-positioning.

## Compliance guardrails

The stated compliance posture: **mimic human behavior, respect connection limits, avoid scraping, preserve platform integrity** (source: "LinkedIn prospecting: The only guide you’ll ever need"). "Automate humanly" — auto profile views, post likes, and pauses that imitate a real user rather than a burst-sender (source: "5 LinkedIn best practices to accelerate growth").

## Summary

The deliverability rule-set treats account safety as an engineering discipline: send from the cloud on a dedicated per-account proxy, keep each account under undisclosed dynamic limits (~100/week or ~20–40/day, ~200 actions/day — figures vary by source and era), warm new accounts over ~3 weeks, make activity look human (spread timing, vary opening lines, add non-send actions), keep pending requests clean, and scale not by pushing one account harder but by rotating 6–20 real sender accounts. Restrictions are recoverable with a 5–7-day rest. All limits are HeyReach's own guidance for the 2026 LinkedIn state and drift over time; several key numbers (weekly cap, reset time, per-account defaults) differ between sources and are preserved above.

## Related
- [[linkedin-outreach-benchmarks]]
- [[outreach-sequence-architecture]]
- [[linkedin-message-formulas]]
- [[multichannel-outreach-architecture]]
- [[campaign-audit-and-diagnostics]]
- [[signal-based-outbound-framework]]
