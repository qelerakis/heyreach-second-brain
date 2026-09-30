# How Gunner from Brij uses multichannel outbound to hit a 60% reply rate

Source: https://www.heyreach.io/outbound-playbooks/multichannel-outbound-for-ecommerce

Summary: How Gunner from Brij uses multichannel outbound and tools like Clay, HeyReach, Smartlead, and Trigify to hit a 60% reply rate

I want to share a detailed breakdown of how [Gunner Park](https://www.linkedin.com/in/gunner-park/) from [Brij](https://brij.it/) built an outbound workflow that combines LinkedIn and email outreach. Including tools such as Trigify, Clay, Smartlead and HeyReach.

The secret sauce is Gunner's powerful Clay table that unlocks deep personalization, allowing his LinkedIn outbound campaigns to hit impressive reply rates of 60% and 23%.

Let me break down the entire process for you, step by step.

**Step 1: Capture engaged prospects**

Gunner starts by using Trigify to gather a list of people who engaged with posts from Brij's CEO, [Kait Stephens](https://www.linkedin.com/in/kait-margraf-stephens/). This creates a warm audience since these people have already shown interest in their content, making it an effective inbound-led campaign.

Next, these leads are sent to Clay where two things happen. First, data like full name, company name, and whether they liked or commented on the post is captured. Gunner also cleans the data of any emojis to have usable tags for outreach.

The way he uses this later is for conversation starters. If the lead left a comment, the copy goes like this:

> Saw you commented on my post about women entrepreneurs sharing insights on brand building.

He then performs two key verification checks:

* Is the lead an existing customer?
* Is the lead a 1st-degree connection with Kait on LinkedIn?

If the answer is yes to either of the questions, the campaign won’t fire off for these leads.

**Step 2: Qualify leads**

This is where it gets interesting. Gunner uses ClayAgent with OpenAI to qualify leads based on two main criteria:

* Decision-maker verification: Checking if they're in a position to make buying decisions
* Department relevance: Making sure they work in departments they typically sell to

This is topped off with the Eligibility Check column that labels qualified leads with "yes" if they match the desired criteria.

One little neat trick is how he captures leads' company revenue data. Instead of paying for ZoomInfo, he uses Clay to scrape Google Search results of company ZoomInfo profiles. This gives him the data point he needs. #supersmart

Here’s the query in Clay:

He then cleans the revenue numbers in a new column from currency signs and commas in case they decide to do lead scoring in the sequence.

Last but not least, Gunner also makes sure to check if the company is selling physical products and if they do across multiple channels. Both extremely important for accurate qualification.

**Step 3: Find work emails**

Since Trigify doesn't allow you to get an email outside their app (for now), Gunner uses a combination of tools:

* Apollo for initial email discovery
* Clay's waterfall feature to try additional email finder tools if Apollo doesn’t find the email
* Get the highest possible hit rate and merge all emails in one column

**Step 4: Deploy market segmentation**

For teams targeting this segment, understanding [CPG analytics](https://alloy.ai/cpg-analytics) can help clarify how consumer brands track sales, inventory, and performance across retail channels. Then, the magic happens.
To begin with, he segments leads into 3 main buckets:

* CPG (Consumer Packaged Goods)
* Durable Goods
* Baby Goods

Then, for each bucket, he maintains a list of similar brands Brij helped. This allows him to make messages more relevant:

We've helped [homegoods] brands like [Carawa] and [Canopy].

As you might have guessed it, words in the brackets are dynamic and change for every lead.

They use location data to create personalized call-outs. For US-based prospects, he mentions local events they’re organizing and sends an invitation. For international prospects, they use more generic but still relevant messaging.

Here’s the difference in the copy:

> We often throw networking events for retail and omnichannel brands in [New York] and would love to invite you to the next one!
>
> or
>
> We throw a bunch of networking events for retail and omnichannel brands and would love to invite you to the next one!

**Step 5: Identify growth signals**

Gunner was very generous to share another one of his Clay tables where he uses RB2B. For those of you who don't know, RB2B can identify your website visitors in the U.S. and send you their LinkedIn profiles.

After qualifying website visitors, Gunner imports them into his Clay table and enriches their data with what he calls ICP's growth signals. Here are some examples:

* Did the company raise funds recently
* Did the company start retail expansion
* Did the company launch a new product recently

A "yes" to any of these questions serves as a powerful sales trigger, since Brij's solution is perfect for scaling companies. This is especially true when leads visit high-intent pages like case studies, which Gunner can mention in his outreach messages.

**Step 6: Send LinkedIn outreach**

They run three parallel LinkedIn campaigns, one for each market segment mentioned above. Since these leads have already engaged on LinkedIn, it's the ideal platform to contact them.

This is his campaign in HeyReach:

It starts off with connection requests that have three different notes attached.

Template 1 (Industry Focus):

> Hey {FIRST\_NAME}! Big fan of {COMPANY} and just wanted to connect. Let me know if I can ever be helpful to you - we do a lot in the {Industry\_Category} space.

Template 2 (Event-Based):

> Hey {FIRST\_NAME}! Big fan of {COMPANY} and just wanted to connect. Let me know if I can ever be helpful to you - {Event\_Invite}

Template 3 (Collaboration):

> Hey {FIRST\_NAME}! Big fan of {COMPANY} and just wanted to connect. Was thinking I could maybe write a post about you guys for my audience, would love to collaborate. Let me know if you're interested!

Once connected, Gunner sends this follow-up:

> Oh - almost forgot, let me know if want to see a sample digital experience. We've built out rebate, sweepstakes and production education experiences for lots of CPG brands, more than happy to show you.

> **🚀 Take action.** [**Send your LinkedIn outreach campaign**](https://app.heyreach.io/account/register) just like this for free - no card required

This message is the same regardless if they accept the connection request or not. The only difference is that if they accept the connection, it’s a regular DM. If they don’t, it’s an InMail.The best part of this campaign are the results. I mean this guy is cooking and building his masterpiece! 🔥

When leads start replying, Gunner said he uses HeyReach’s unibox to handle them.

The way it works is that he can reply to all the leads as Kait, from one place, and without having to log in and out of different LinkedIn accounts. On top of that, it’s easy to use filters and make sure no reply is missed. Making his life fast and simple.

**Step 7: Send cold email outreach**

For email outreach, here are his templates:

Initial Email:

> {{first\_name}} - {{Hook}}
>
> Thought you might be interested in learning more about what Brij can do for {{company\_name}}.
>
> We specialize in bridging the gap between the offline and online, driving revenue from your unknown customers.
>
> We've done this for {{Specific Industry}} brands like {{Similar Brands}} through our digital experiences that leverage rebates and sweepstakes.
>
> Let me know if you'd like to see a few examples or feel free to book a meeting with me.

Follow-up Email:

> Hi {{first\_name}},
>
> Wanted to quickly share a few ways that we've helped other CPG brands facilitate 1st-party collection for their offline customers while also driving retail velocity:
>
> • Chamberlain Coffee brought in over $50,000 in revenue via in-store sweepstakes
> • Health-Ade captured 40,000+ emails through paid media sweepstakes
>
> Curious how we could do this for {{company\_name}}?

Results?

Nothing beyond impressive… including replies such as this:

**Step 8: Scale beyond any limits**

Finally, Gunner pulls out one more trick out of his sleeve to unlock scale in this campaign. He uses Clay to find lookalike prospects and feed them back into the system.

Creating more Clay tables and adding more qualified leads in the process, while the campaign stays almost the same—thus creating an infinite loop.

All I can say after looking over this campaign is → killed it! 🫡
