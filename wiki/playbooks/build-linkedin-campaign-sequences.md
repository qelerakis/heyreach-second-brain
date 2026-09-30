# Building LinkedIn Campaign Sequences That Don't Die

How to build the multi-step LinkedIn drip in practice: which actions to chain, how long to wait between them, how to branch on acceptance and reply, and how to keep a campaign producing past week two. The recurring rule across the corpus is **fewer, better-timed, human-looking steps** — warm up, connect (usually blank), wait, open with value, follow up once or twice with a *new* angle, then stop. This covers sequence construction; the wording that goes inside is [[write-cold-outreach-copy]] and the volume/safety layer is [[scale-linkedin-outreach-safely]].

## The default sequence shape

The consensus structure that appears in almost every walkthrough:

1. **Warm-up (optional):** view profile → (hours later) like a recent post / follow — so you appear in their notifications and look like a real person before the request (source: "This LinkedIn System Booked Me 80 Qualified Sales Calls in 30 Days"; source: "The Best LinkedIn Outreach Strategy for Agencies in 2026").
2. **Connection request — usually blank** (empty out-accepts noted; see [[write-cold-outreach-copy]]).
3. **Branch on acceptance.** If **accepted**: wait (3 hours minimum, often 1 day) then send message one. If **not accepted**: wait ~5 days, view profile / like a post as a nudge, then end (source: "How I Generate $11M in LinkedIn Pipeline Using This Exact System"; source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)").
4. **Follow-ups:** one or two, spaced 2–4 days (or wider), each adding a new angle; campaign auto-pauses the moment the lead replies.

A representative build that HeyReach reports produced 22.8% acceptance / 42.2% reply / 7 qualified leads: view profile → **empty** connection request → if not accepted, +5 days view again, +2 days auto-like a post *only if newer than 24h*, +5 days end; if accepted, wait 1 day then message → +2 days a single "👋" emoji → +3 days a second nudge, then end (source: "LinkedIn message automation: the playbook that got us a 42% reply rate"; source: "5 LinkedIn best practices to accelerate growth").

## Delays and timing

- **Don't pitch-slap.** Never send the opener the instant a request is accepted — use a delay (Tim Jacobson gives a **3-day break**; HeyReach guides suggest **24–48h**) so it doesn't read as automated (source: "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)"; source: "Sales sequence automation: Fewer steps, more replies").
- **3 hours is the minimum** post-accept delay in the tool (source: "The Best LinkedIn Outreach Strategy for Agencies in 2026").
- **Space follow-ups 2–5 days apart**, wider on LinkedIn than email because message history is permanent (source: "The Best LinkedIn Lead Generation Strategy for 2026").
- **Withdraw unanswered connection requests.** Set auto-withdrawal (many use 14 days; the tool's stated minimum is 14 days in some notes; others use 7–21) so stale pending invites don't drag down acceptance and reputation (source: "How I Generate $11M in LinkedIn Pipeline Using This Exact System"; source: "How to manage multiple LinkedIn accounts without getting flagged").

## Keep sequences short

Longer is not better. Guest Stan: "we don't suggest sending more than four messages. I would even do three" (source: "LinkedIn Outreach is About to Change Forever (and nobody even realises)"). HeyReach's own guidance: "A fifth extra step rarely recovers what a weak second step lost," and to consider stopping after the second follow-up (source: "Sales sequence automation: Fewer steps, more replies"; source: "The Laziest Way to Book Meetings on LinkedIn"). Follow-up restraint is also a deliverability move — over-following *lowers* reply rates because LinkedIn is a social space, not an inbox (source: "LinkedIn Follow-Up Message: A Signal-Based System (+ Examples)").

## Branching, variables and fallbacks

- **Conditional steps** ("If Connection" / accepted vs not-accepted) let warm 1st-degree contacts skip the request and get a direct message while cold leads get the full request-then-message path (source: "How to turn post reactors into a high-converting lead list in 30 minutes").
- **Custom variables + a mandatory fallback.** If a message uses variables (first name, company, or CSV/Clay fields), you must set a fallback message for when a variable is empty — otherwise it sends "Hey first name, ." (source: "The ONLY LinkedIn Lead Generation Video You Need"; source: "How to Send Automated Personalized Pitch Decks on LinkedIn (Step-by-Step)").
- **A/B message variations** rotate two or more openers and report the winner — test one variable at a time (source: "How I Generate $11M in LinkedIn Pipeline Using This Exact System"; source: "I Sent 2,400 LinkedIn Messages in 30 Days (Real Results + What Actually Worked)").
- **Preview before launch.** HeyReach's message preview renders each lead's message with variables filled and warns on missing data (source: "Preview message + new Sequence Builder").

## Warm-up steps share your daily budget

A subtle failure mode: profile-view and post-like warm-up actions consume the *same* per-account daily limit as connection requests, so a heavy warm-up can throttle later steps in the sequence. Fix by raising the limiting step's cap or reordering, and note that sending limits are per LinkedIn account, distributed proportionally across a sender's active campaigns — not per campaign (source: "Why automation fails in sales sequences: 8 early-warning signs of outbound drift"; source: "LinkedIn automation for outbound agencies: A zero-chaos system"). Full limit numbers live in [[safe-linkedin-sending-limits]].

## InMail for open profiles and senior titles

For prospects who don't accept, or open profiles, an InMail step can be added — but InMail uses limited credits (often only returned when the recipient replies) and performs better for senior titles/verticals, so use it as a fallback rather than the first touch (source: "LinkedIn message automation: the playbook that got us a 42% reply rate"; source: "I Built a Clay to HeyReach Pipeline That Books 12 Meetings Per Month (Full Breakdown)"). Note-on-connection-request at scale only works well with Sales Navigator; regular accounts are limited to ~5–10 noted requests/day before they send empty (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").

## Build campaigns that don't die after week two

Every campaign follows a **performance curve**: acceptance peaks in the first ~10 days, then plateaus, then enters a fatigue zone — so plan for day 11/23/47, not day-one reply rate (source: "LinkedIn outreach strategy for 2026: How to build campaigns that don’t die after week two"). Winners' moves:

- **Segment the list into 3–5 micro-segments** by trigger so the whole list doesn't fatigue at once; launch the highest-intent segment first and rotate the next in as performance plateaus (source: "LinkedIn outreach strategy for 2026: How to build campaigns that don’t die after week two"). See [[signal-based-outreach]].
- **At the plateau, don't blast more volume.** Rotate in fresh senders, A/B a new *angle* (not new wording), push non-responders to email, and shift send timing (Tue–Thu reported to beat Mon/Fri).
- **In the fatigue zone: kill and relaunch.** You **cannot edit sequence *steps* in an active campaign** (you can edit message copy), so duplicate the campaign, exclude already-contacted leads, add fresh senders and a new angle, and launch against a new micro-segment; or revive with a repositioned breakup message (source: "LinkedIn outreach strategy for 2026: How to build campaigns that don’t die after week two"; source: "LinkedIn campaign monitoring that scales").
- **Reuse by duplication.** HeyReach's "lazy" reuse: duplicate a working campaign and change just three things — the lead list, the first message, and when it runs (source: "The Laziest Way to Book Meetings on LinkedIn").

Campaigns under 30 days consistently under-perform in HeyReach's benchmark data, so give a campaign time before judging it (source: "LinkedIn Message Automation: The 2026 Guide to Automated LinkedIn Messaging").

## Templates and cloud sending

HeyReach ships built-in sequence templates (its "Import from templates" / 7 built-in templates such as Value-first outreach, New connection nurture, Comment follow-up) plus a rebuilt drag-and-drop Sequence Builder with template-vs-blank entry points (source: "How to set up LinkedIn drip campaigns that actually generate leads"; source: "Preview message + new Sequence Builder"). Set the sending window once — the campaign spreads actions across that slot, runs from the cloud (computer can be off), and auto-stops messaging anyone the moment they reply (source: "The Laziest Way to Book Meetings on LinkedIn"). Full day-by-day drip templates (e.g. Sönke Venjacob's connection → +2d like post → +3h message → +4d follow-up) are catalogued in "The ultimate guide to drip campaigns" and "How to set up LinkedIn drip campaigns that actually generate leads."

## Related
- [[write-cold-outreach-copy]]
- [[book-meetings-on-linkedin]]
- [[scale-linkedin-outreach-safely]]
- [[signal-based-outreach]]
- [[multichannel-linkedin-email-sequencing]]
- [[manage-replies-and-inbox-at-scale]]
- [[audit-and-optimize-linkedin-campaigns]]
- [[safe-linkedin-sending-limits]]
- [[heyreach-features]]
