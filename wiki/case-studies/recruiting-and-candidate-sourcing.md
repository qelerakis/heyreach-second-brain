# Recruiting & candidate-sourcing with outbound tooling

One playbook in the library uses the same LinkedIn outbound stack (Sales Navigator → Clay → HeyReach → Make) for **recruiting** — sourcing and screening candidates — rather than for sales. It is worth isolating because its impressive numbers are **hiring-funnel metrics, not sales-outreach benchmarks**, and shouldn't be compared against the reply/meeting rates elsewhere in these case studies. (Note the terminology trap: the separate "hiring campaign" playbook in [[buying-and-intent-signal-campaigns]] is the *opposite* — targeting companies that are *hiring* as a buying signal, not sourcing candidates.)

## Nikola Sokolov (Influencers.Club) — 800 connections, 571 replies in 2 weeks

**Who:** **Nikola Sokolov**, founder of **Influencers.Club** (influencers.club), a creator-economy data provider — his company is the COI, and the piece is a HeyReach "Outbound Outliers"-style feature (source: "800 Connections, 571 Replies, 2 Weeks: A Recruiting Masterclass").

**Context:** Rapid growth created a hiring crisis "that would make most people reach for the whiskey" — he couldn't manually vet hundreds of candidate profiles but couldn't afford wrong hires. The premise: Sales Navigator can filter by title/company size but **can't** filter for nuance like "won't job-hop after 12 months" or "has diverse growth experience" — that lives in the profile timeline (source: "800 Connections, 571 Replies, 2 Weeks: A Recruiting Masterclass").

**What he did:** Pull 500–1,000 LinkedIn profiles per search → dump the URLs into a **Clay** table → build an **AI red-flag scoring system** encoding the patterns his recruiter kept flagging (a "living checklist"). Candidates over the threshold enter a HeyReach outreach campaign. A **Make** automation processes every reply into a pipeline, tagging each with campaign source, reply date, **sentiment analysis**, and the Clay quality score — so the recruiter sees at a glance who replied, whether they're excited vs polite, whether they fit, and their stage. It mirrors a sales pipeline, but for hiring (source: "800 Connections, 571 Replies, 2 Weeks: A Recruiting Masterclass").

**The scoring weights (verbatim):**

| Red flag | Points |
|---|---|
| Job tenure under 18 months | −5 |
| No SEO experience | −1 |
| Not in growth / demand / product roles | −3 |

(source: "800 Connections, 571 Replies, 2 Weeks: A Recruiting Masterclass")

**Numbers (self-reported):** **800 accepted connections + 571 replies in 2 weeks.** Context: the company **scaled $10K → $160K MRR in five months** (the growth that triggered the hiring crisis). In-DM company marketing claims: **"$110K ARR in Jan to $1.8M ARR now," 150k monthly visitors (mostly organic)**, and that the data powers Amazon, L'Oréal, and TikTok. Searches pull 500–1,000 profiles (source: "800 Connections, 571 Replies, 2 Weeks: A Recruiting Masterclass").

**His conclusion / limits:** The AI scoring "wasn't perfect, but it was fast and consistent. Good enough to separate 'definitely not' from 'maybe worth a conversation.'" Founder's takeaway: "this system saved his life." **Caveats to preserve:** this is a **recruiting** use case — do **not** file the 800/571 as sales-outreach benchmarks; and the in-DM ARR/traffic/logo claims are Influencers.Club's own marketing copy, unverified (source: "800 Connections, 571 Replies, 2 Weeks: A Recruiting Masterclass").

## Related
- [[buying-and-intent-signal-campaigns]] — the "hiring campaign" that targets companies that hire (opposite meaning)
- [[heyreach-first-party-campaigns]] — reply-processing pipelines and lead scoring in a sales context
- [[personalization-and-message-experiments]] — AI scoring/qualification tradeoffs
