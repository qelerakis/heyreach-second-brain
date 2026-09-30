# This lead scoring system doubled our conversion rate

Source: https://www.heyreach.io/outbound-playbooks/free-trial-qualification-system

Summary: Let me walk you through one of the key tactics we implemented that helped double our conversion rate from free trial to paid.

In the summer of 2024, I had a meeting with our CEO and CMO (ex-Growth Consultant at that time). There were a few very important things said during that call, one of them being:

"We shouldn't care about total number of free trials. What we should care about is the total number of qualified free trials."

After the call, I stepped out to grab a smoke and had a brainwave. What if we could:

1. Qualify every free trial signup
2. Segment it across user tiers
3. Tier 1 and 2 signups are pushed into Customer Success campaigns (human-led onboarding)
4. Tier 3 are pushed into Marketing campaigns (self-serve onboarding)

Data is already in HubSpot, we just have to push it to Clay and enrich it.

I called [Macklin](https://www.linkedin.com/in/macklin-buckler/), our Clay expert, and explained the flow. Within a few weeks, he implemented the new system and got it running smoothly.

This became one of the key factors that helped boost our conversion rate from free trial to paid to 20%+. For comparison purposes, we started at 10%.

Let me walk you through our Clay table setup:

The first step handles the basic data collection. When someone starts a free trial, we enrich their profile with essential information: names, company details, LinkedIn URLs, and contact information through Apollo.

Note: We only run Apollo enrichment for contacts who have an Account Owner in HubSpot, which helps us save credits and not waste it on those we don’t need emails for.

For teams with multiple users, we streamlined our approach by only reaching out to Admins and Power Users, not Team Members. This prevents overwhelming teams with duplicate messages.

Next, we pull information from their website and company's LinkedIn page to understand their business and target market. Specifically, we focus on their ICP's job titles and industry to create custom sentences for our campaigns.

Clay table with Job Titles

Here's an example of the prompt we use to generate clean job titles for our campaigns:

> Format the job titles listed in [FIELD] to fit within the sentence structure: "I’ve done some research and noticed your team is targeting [Titles], [Titles], and [Titles]." Output just the job titles, not the rest of the sentence:
>
> Follow these rules:
>
> 1. Pluralize any singular job titles.
> 2. For titles with a "/", remove the "/" and one title.
> 3. Apply the format: "Title" for one, "Title and Title" for two, and "Title, Title, and Title" for threeor more, using "and" only once before the last title.
> 4. Remove any abbreviations in parentheses.
> 5. Ensure proper capitalization for all titles. Output the formatted titles as text.
> 6. Do not include a period at the end of the sentence.
> 7. Only output the job titles, do not write "I’ve done some research and noticed your team is targeting"
>
> Lives are on the line. If no titles Job\_Titles (Do Not Use) are provided or it says "insufficient data to identify job titles", output "ZZZ" Make sure to format the job titles correctly.

Then we qualify each signup into the right user tier. HeyReach's primary users are lead gen agencies, sales teams, and GTM experts. Each represents a separate tier, with a few additional tiers completing our segmentation.

We use criteria like industry, ICP, organizational size, and other key data points to accurately qualify each lead. This qualification determines whether they receive self-serve or concierge onboarding.

For instance, larger agencies and sales teams typically need direct support from our team to discuss complex needs like multi-client onboarding, whitelabeling, and custom API connections. That's when our Customer Success team steps in.

While we actually needed several Clay tables to do all this proper lead scoring—not just one—that's exactly why we have Macklin. Thank God for that!

Finally, in HubSpot, we assign each lead to a CS team owner and route them to the appropriate campaign. For outreach, we take a multichannel approach using Smartlead for emails and HeyReach for LinkedIn messages (duh 😀).

Here’s how our cold email template looks like:

> Hi [NAME],
>
> [CS NAME] here, your dedicated Account Manager. Think of me as Robin to your Batman. 💪
>
> I’ve done some research and noticed your team is targeting Operations Managers, Logistics Managers, and E-commerce Managers.
>
> If you’re up for it, I’d love to give you a personal walkthrough of HeyReach and help you build high-converting LinkedIn campaigns.
>
> We could cover things like:
>
> - Building GTM playbooks
> - Sourcing leads from anywhere, capturing social signals, and enriching your leads with any data points you need
> - Connecting HeyReach with your GTM stack (Clay, HubSpot, Common Room, Trigify, etc)
>
> Want me to share some LinkedIn strategies that always work?
>
> Happy hunting,
> [CS NAME]

LinkedIn message is example the same.

As for the LinkedIn outreach sequence, here’s how that looks::

LinkedIn Outreach Sequence

The campaign begins by segmenting LinkedIn contacts into two groups: those we're already connected with and those we aren't. For existing connections, we send a LinkedIn message, like one of their recent posts, and follow up if they don't reply initially.

For those we're not connected with, we first send a connection request. If they accept and reply, we send our message. If they don't respond to the connection request, we send an InMail instead. We use the same initial message regardless of how the lead responds.

Prior to implementing this campaign structure, we used a simpler version. The improvements you see now were added based on our learnings.

One feature of the HeyReach API I love is how easily it handles sender assignment. You can run a single campaign where the sender automatically matches each lead's HubSpot owner—their LinkedIn profile becomes the sender. One campaign, three senders, all automated, done!

Here are the results: 99 requests, 47 accepted, 20 responses

The cold email results were less impressive but still generated meetings: 48 messages sent with 6 replies from one CS account. We did not track opens and clicks for deliverability purposes.

Overall, these results are very good.

It's creating a powerful loop - as our marketing team continues to crush user acquisition, we'll see more and more free trial signups. No pressure marketing! 😅

Best of all, we now have everything in place to track performance comprehensively across all user tiers and campaigns.
