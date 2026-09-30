# Deliverability & Ban-Avoidance Beliefs

HeyReach's deliverability worldview can be summed up in one claim: **LinkedIn restrictions are driven less by raw volume than by *how* you send — the behavioral fingerprint of the account.** Two people can send the same 100 requests a week and one gets flagged, because "what gets restricted is HOW you send." From that belief flow the rest of its convictions: use a cloud tool (never a Chrome extension), give every account its own residential proxy in a consistent location, warm accounts up, distribute volume across many "governed" senders instead of pushing one hard, do more than just send (views/likes/comments), and treat a restriction as a recoverable warning rather than a ban. This is the POV/belief layer; the actual thresholds live in [[safe-linkedin-sending-limits]]. Everything here is a vendor position — the safety architecture HeyReach describes is also exactly what it sells, and the specific limits are era-bound to 2026.

## Belief 1: "It's not volume, it's HOW you send"

The centerpiece: "even accounts that don’t get close to the weekly limit are getting restricted" (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). That video names four restriction factors beyond volume — **timing** (all requests in one 10-minute burst looks robotic: "nobody sits down, fires off 15 connection requests in 10 minutes"), **message similarity** (500 identical messages get flagged; keep ~80% but vary the opener, or send empty requests), **non-send activity** (an account that only sends is easy to flag, so build profile-views and post-likes into the sequence), and **tool type** (see Belief 2). The behavioral-simulation view appears on the product side too: micro-delays, randomized message spacing "90-150 seconds," and a message-validation layer that scans for spam words (source: "AI outreach agent: From sequences to systems that think"). "Make activity look human" is Rule 4 of (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool").

## Belief 2: Cloud tool > Chrome extension

A firm architectural conviction: browser-extension tools "physically click inside your browser" where "LinkedIn can see a script clicking on your computer," whereas a cloud tool sends from its own servers with the laptop closed (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). Rule 1 of the 8-rules post is "Use a cloud-based tool" for exactly this reason (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool"), and PhantomBuster is singled out as carrying "LinkedIn ban risk (runs through session cookie)" (source: "Best GTM tools of 2026: build a stack where everything works together"). This is a HeyReach differentiation claim as much as a safety belief.

## Belief 3: Dedicated proxies and location consistency

Each account should log in from its own stable, country-appropriate residential IP — "never share proxies" (source: "The best LinkedIn management tools for scaling outreach without getting banned"). Cheap tools that relog daily or rotate IPs trigger repeated new-location/2FA warnings (source: "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)"), hence "cheaper tools are cheaper for a reason." HeyReach assigns a static residential proxy matched to the account's chosen country so outreach "appears from the same location as your phone/browser login."

## Belief 4: Governed senders — distribute, don't push one account

The safety math HeyReach preaches: 100 messages from one account is "high risk/likely ban," while "10 messages from 10 accounts = totally safe" (source: "The ultimate guide to trigger-based outreach"), where the slogan is "Safety is performance." The corollary is that pushing a single working account backfires because "an account's performance actually drops the more you send from it" (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). Even distribution has a ceiling of credibility, though — "even 500/day across 10 accounts is risky" (source: "The best LinkedIn management tools for scaling outreach without getting banned"). This "governed senders" belief connects directly to [[quality-over-volume-philosophy]] and the "6–20 senders" sweet spot in [[how-they-read-the-benchmarks]].

## Belief 5: Warm up new accounts

A fresh account "sending 50 connection requests/day looks like a bot" (source: "The best LinkedIn management tools for scaling outreach without getting banned"), so new/inactive accounts get a multi-week ramp — framed as "training for a marathon" in the 3-week plan of (source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool").

## Belief 6: A restriction is a warning, not a death sentence — be proactive

HeyReach insists restrictions are usually temporary pauses, not bans, and that they telegraph themselves: an account shows "~3–5 days of warning signs" (drifting acceptance, piling pending invites) before LinkedIn acts. "Every restricted sender I have seen had a week of warning signs behind it," so "Look at the numbers every Monday and you find the sender before LinkedIn does" (source: "How to manage multiple LinkedIn accounts without getting flagged"). Its stance is anti-reactive: don't wait for the auto-freeze; catch the slide, pause, rotate to a healthy account, and rest the tired one 5–7 days.

## Belief 7: Never use fake or duplicate accounts (the ethics line)

The safe-scaling model is "one workspace per client; each sender = a real person's LinkedIn account," explicitly *not* multiple browser logins or fake/duplicate profiles, since LinkedIn's ToS is one account per person (source: "How to manage multiple LinkedIn accounts without getting flagged"). HeyReach's public ethics stance is that it "never crosses LinkedIn messaging/InMail/connection limits, no fake accounts, no shady shortcuts, no data misuse" (source: "Quick update from Nick (CEO @HeyReach)").

## Belief 8: Being deplatformed is "part of the game"

When LinkedIn removed HeyReach's company page and several exec profiles, the CEO framed it as a rite of passage: "This is part of the game, and honestly, we saw it coming," and "LinkedIn can't detect who uses HeyReach" (source: "Quick update from Nick (CEO @HeyReach)"). The argument leans on precedent — LinkedIn has done this to "Apollo, Seamless, Evaboot, Lemlist, LGM" and "None of them skipped a beat" — and claims "zero impact" on users. Treat "zero impact" and "can't detect who uses HeyReach" as **vendor claims about an enforcement action against HeyReach itself**, not verified fact; the same letter cites self-reported "$13M ARR."

## Era caveats and internal inconsistency

These beliefs are heavily time-bound. The 2026 framing cites a January 2026 "Depth Score" algorithm update and an "Entity Alignment" update, "up to 30% reach reductions" for AI-generated content, and external links increasingly flagged in DMs (source: "LinkedIn outreach strategy for 2026: How to build campaigns that don’t die after week two"). And HeyReach's own numbers don't fully agree — its "~100 connection requests/week per account" guidance (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes") conflicts with "~200/week" cited in other videos; LinkedIn publishes no official limits, so all of these are HeyReach's inferred, changeable guidance. The reconciled thresholds are catalogued in [[safe-linkedin-sending-limits]].

## Related
- [[safe-linkedin-sending-limits]]
- [[quality-over-volume-philosophy]]
- [[how-they-read-the-benchmarks]]
- [[ai-sdr-augmentation-vs-autonomy]]
- [[2026-outbound-predictions]]
- [[scale-linkedin-outreach-safely]]
- [[manage-replies-and-inbox-at-scale]]
