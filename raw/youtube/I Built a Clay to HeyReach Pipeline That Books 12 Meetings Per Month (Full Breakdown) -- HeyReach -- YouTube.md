# I Built a Clay to HeyReach Pipeline That Books 12 Meetings Per Month (Full Breakdown)

Source: https://www.youtube.com/watch?v=ggSulNDfM9E

Let me show you what we're building today. It all started as a raw Sales Navigator lead list export. No enrichment, no qualification, no lead scoring, nothing. And now it became a

fully enriched prospect list inside of clay.com AI scored against our ideal client profile. We automatically push those researched prospects from clay into Heyreach. We run a structured

LinkedIn campaign with three messages, manage all of the positive replies through one inbox, and of course, turn all of that LinkedIn outreach into booked meetings. Now, I know what you're

thinking. Pretty much every clay and Heyreach tutorial that I have seen so far skips something. They show you the campaign stats, but they don't show you the exact process to go from start to

finish. Or they show you the actual campaign, but not how you can reply to those interested prospects. Now, don't get me wrong. This video covers everything end-to-end. From raw lead

data all the way through to how you can book calls using Heyreach. No gaps between them. Anyways, let's jump right into it. And by the way, if we haven't met just yet, my name is Tim Jacobsen.

I'm the founder of an agency called B2B Boosted, which implements technologies like clay.com and Claude Code and NA10. And also I run Unlock Courses, which is the fastest way to learn AI and

automation tools like clay.com, NA10, Cursor, Claude Code, and all other tools that you have probably been putting off implementing inside of your own business. I've collected over 50

testimonials from B2B companies over the last 3 years. And in today's video, I'll be showing you the exact workflow we use in order to generate over 12 qualified meetings every single month using

Heyreach. So you can simply replicate it and copy and paste this exact process into your own business. Now, just so that we're on the same page, this will in total require an eight-step process,

the first step of which would be to find lead data. And for that, there are a lot of different options. You could either go to some sort of LinkedIn database, be it LinkedIn Recruiter or LinkedIn Sales

Navigator, or you could go for a more budget-friendly option like Prospector or AI Arc, which I have recently been using a lot. Or if you want to just centralize everything inside of one

platform, look no further than clay.com. Because in clay.com, as soon as you sign up for a free account with Clay, and all you would need to do as soon as you're signed up and logged into your account,

is click on find leads in the top left-hand corner, and over here, if you select people, you should be able to find people that you can reach out to. So, in this case, let's say that we go

into job titles, and we filter for contains, and over here we say it contains founder, owner, CEO, chief executive, and let's say co-founder as well, just in case. And that way, we can

make sure that they're all in the United Kingdom. So, let's say they're all in the UK for the time being, and we can also filter to make sure that the companies that they work at, over here

under company attribute section, are all accounting firms. So, we can filter for accounting, and we can filter for the company sizes to be between 51 and 200 employees. You can see, in total over

here, we'll have 108 results. And here, we can click on continue, save it to a new workbook with a new table. And what that will basically do, if you think about a spreadsheet, you'll just create

a new spreadsheet with a list of all of these prospects over here. For the time being, we can exit the pop-up in the top right-hand corner, and if we now go back to the main Clay interface, you should

be able to see over here this table that has been built for us. So, we have a list of all of these lovely contacts. We get their first name, we get their last name, we get their location name, and we

have their job title and company name as well on top of that. As well as of course their LinkedIn profile. Spoiler alert, all of this completely for free because this find people functionality

inside of clay.com is completely free. You get it even if you're on a free trial with clay.com. So all we need to do now is just make sure that inside of this list we have the LinkedIn profile

on the right hand side. And now before we reach out to the prospects using HeyReach, we need to first of all enrich the leads and qualify the leads. >> [music]

>> So in order to do that, I'm going to click on tools in the right hand corner and I'm going to type in Claygent. And Claygent is what Clay is most renowned for. It's the AI web crawler that is

able to access any open source website and is able to pull any information from the internet. It's able to analyze it, interpret it, and basically replace whatever you're typically doing manually

using this automated AI agent. So all we're doing here is clicking into Claygent and now we're going to describe how we want to enrich and qualify this prospect. Let's say we say something

like this. So far what I typed within just a couple of seconds is as follows. I've said, say ICP if the person does not have an executive assistant working at company name and say not ICP if the

person has an executive assistant working in that company. Now I want the AI web researcher to go and find out if this company has an executive assistant working for this specific founder. So in

this case, what we'd be wanting to do is to pre-qualify this company for the need in an executive assistant and of course if they don't have an executive assistant right now, we'll then reach

out to them and propose our executive assistant services. So for the time being, because this was a really lazy way to write a prompt, I can click on that generate button and it will now say

sculpting and that will improve my prompt. It will add all of the details for the AI agents like the LinkedIn profile, the company domain, and all of those other fields that are essential.

And you can see it writes out a really sophisticated prompt for us containing like the company name, the last name, the domain, and so on. And throughout this process, I'm going to untick all of

these toggles so that it doesn't become a bottleneck if we don't have one of these data points available for the prospect. So, now all we're going to do is to switch this model from Neon

because it will cost us two credits like this all the way through to a cheaper model like GPT 5.1 because it does the same job but for a bit cheaper. Click on save and run 10 rows. And this way, we

can use this AI agent now to do the research and to qualify these prospects under our ICP. Worth noting, it's very similar to this, you could give it like five or 10 different bits of criteria.

For example, you could say based on head count, geography, colleagues, in departments, like how many sales reps they have in the UK, you know, something like that. You can do all of that. And

in this case, you can see most of these folks would fit our ideal client profile because none of them have executive assistants. For the time being though, I'm going to just run a few more rows

just to hopefully get some examples of where these leads would be disqualified. So, let's say we do it for the first 50 rows. Now, all I'm going to do is just click into the play button and run 50

empty or out-of-date rows. Now, occasionally we may want to score the leads. So, for example, we could then use add column, click on formula, and say, "Give five points if this thing

contains" and then we use the forward slash to refer to the contact response over here. And we could say, "Is ICP, right?" So, in this case, we will score five points to this specific prospect if

they do not have an executive assistant. So, over here, you can see we now score the leads [music] as well. Going forward after this, let's assume that we already used Clay in order to source those

leads, qualify them, and to score them very briefly. The next step after that will be to click on tools, and now [music] we can just type in HeyReach, and over here it gives us the option to

add a lead into a campaign. All we need to do now in order to pull this off is to sign up for free account with HeyReach or to log into our existing accounts.

And within the account, head into the integrations and click on get API key under the Heyreach API and just copy this API key back into Clay where it says add account and all I would need to

do is just paste the API key and name this connection. I'll just say Tim test as an example and then now we can test the account and save this specific API key. More than that, this would require

for us to then create a campaign inside of Heyreach and then over here we can just select the sender. So in this case I'll select myself as the sender and you can see automatically all of the fields

have been mapped out for me. Now as you can see on the screen right now, this campaign beta we ran over the last 3 months generated over 47 positive replies for our client and in this case

they booked in over 15 sales demos on the back of this Heyreach campaign. So what I'll be showing you now is how we can go and imitate the copy for this exact campaign using this underrated

tactic that I've not seen too many people share in this space before. So the first thing that we'll be doing is we're going to be heading into ChatGPT and using this specific prompt. So the

prompt is as follows. Identify the top 10 events happening in London or in whatever location where your prospects are currently based in and we're going to say between April and July the 1st

because it's the next 3 months or so and in this case we're going to say and this has to be an event where accounting firms are highly likely to attend. The events must be well known, high quality

or globally recognized, similar level awareness to Y Combinator or Web Summit. They should attract density of B2B accounting firm founders, operators of VC-backed startups. For each event,

provide the event name, the expected timing and a short explanation of why this would attract our ICP. So in this case I'm going to replace SAS founders with accounting businesses and what we

want is for ChatGPT to do its research and for the purpose of this one it's pretty straightforward. All I want you to do is go click on the second link in the description down below, copy and

paste the prompt from the guys that I share there, and just fill in the exact ICP of the target audience. And based on this, we can then run outreach referencing this super super common

industry event, and we can ask them if they're attending. And that's just a nice little touch, which hopefully creates a little opening. The person replies to us, and then we can carry the

conversation from there as well. Um and we've seen this work really really well ahead of a huge event called Legal Week in New York, and we had two clients that have attended that event, and they were

over the moon with the results and the reply rates of this specific campaign that we ran over the last 3 months in a run up to the event. So, essentially, we're going to do that. You can see it's

now researching and just making sure that it finds all the relevant accounting events. So, let's give it a couple of seconds. In the meantime, we're going to just push these contacts

into HeyReach. All we need to do here is at the very bottom where it says only run if, we need to click on use AI and say only run if, and then we could just say this reply is ICP, because we want

to only push ICP leads into the campaign. And then we'll say save formula. What we can do from this point onwards is pretty straightforward. All we need to do is just select a campaign.

So, for the time being, I'll just select a random test campaign. We're going to save and run the first 10 rows. You can see that now the leads have been added directly into the HeyReach campaign. And

of course, this assumes you already know how to use HeyReach, that you've already headed across into the campaigns, started a new campaign by typing in the name of a campaign here, created it. And

by the way, if this sounds overwhelming, don't worry, because as the second link in the description underneath the video, I'll be giving you a guide which contains the tutorial for how to use

every single feature inside of HeyReach so that you can set up the campaigns and launch them within just a couple of minutes every single time. However, just to keep things short, typically we

always start with the first action being viewing the profile of a prospect. So, in this case, I will select view profile. I typically give it a day or two, and then after that, we add the

next action, which is sending a connection request. Because if you think about how you do this manually, you would typically check out the page of a person and only then you'll send across

a connection request. Um just in order to then continue with this process, you may also click on add action again and then as the next step, you may also like their post for example. Here, if their

profile is open within just let's say like 3 hours or 4 hours over here, we can now go ahead and send them an in mail. Now, on other side of the campaign over here, let's imagine for a second

that the connection request has been accepted. In that case, we can click on add action, we can click on send message and we can copy and paste a templated pre-event outreach message. So, by the

way, I'll be giving away a guide with the exact templates, screenshots of campaigns and messages so you can just copy and paste this all into your existing sequences and campaigns inside

of Heyreach. But essentially, it all starts with the first message containing something like, "Hey first name, are you at this event this week, this month, in a couple of months, in a couple of

weeks, or whenever basically this specific event is that we just researched. And then we're going to say something like, "I'm going to be at that event all week. Would you want to find

15 minutes to compare notes?" And for context, most of the time your ICP will say, "Oh hey, I know that this event is happening. However, I'm not able to attend. Could we catch up?" In this

case, we can see that we've just opened up by saying, "Hey John, are you coming to Legal Week this year?" They said, "Yeah, we're coming." In some other cases, it actually goes a lot further

than that as well. So, for example, over here we're referencing the exact same event and then it says, "Unfortunately, I'm not coming. However, my colleague is and they basically put us in touch with

their colleague in a separate thread thereafter. Or in this case for instance, Jason replies and says, "Yes, we will be there. Are you going to be there as well?" And you can see that all

of these prospects fit the ideal client profile of our clients, in which case it's a really nice campaign to have running on autopilot in the background because there are endless events

happening all the time. Chances are your ICP audience would not hang out and attend every single one of these events, but it creates a nice little conversation topic, a nice little

non-awkward opener. You don't need to pitch them anything. You're just opening the conversation thread for future conversation to then be initiated over time as well. And the best part about

this, you can just have it on autopilot. So, you can literally just keep on sending connection requests every single day. Or for instance, in this case, Renee over here said, "Yes, I will reach

out once I'm there at the event." And this is really good because in some cases, don't get me wrong, if they say, "Oh, hey, I'm actually going to this event." you're pretty screwed because

you can't make it. And you can always make that excuse pretty much last minute. Oh, sorry, had to take care of business, can't make it to the event. But I think it's one of those campaigns

that is super underused. If you want to have a look at some of the most underused plays, for example, pre-conference outreach messages, post-conference outreach messages,

outreach to first-degree connections that have the relevant sales triggers, or if you want to tap into the followers of your competitors, all of these templates will be added as the second

link in the description underneath this video. So, go check it out in your own time. And needless to say, after we launch the campaign live inside of HeyReach, we have this Unibox feature.

And this way over here, we're able to sit and just wait for all of those positive replies to come in. And we can even filter it based on senders. So, for example, we have my own account, we have

Jasmine's account. And if you're not familiar with Jasmine, it's a colleague of mine who runs the GTM engineering part inside of my business. And the Unibox just enable jump into some of

these conversations. You can refresh the messages by clicking on refresh here. You can edit tags. For example, you can create a tag and call this like interested as an example, right? And

then you can just click on create tag. You can also find their emails if you want to. And you can also add those leads into different lists so that your sales team can follow up later on as

well. So, in a nutshell, we talked about a lot of this already. I showed you a free way to find people inside of clay.com. I showed you how to use their AI agents in order to qualify those

leads. I showed you how you could go about scoring your leads based on different criteria and how you can then push them into say reach before then creating your campaign and tracking the

replies coming in inside of your Heyreach Unibox. Now, of course, if you enjoyed this video, consider clicking on the video here which shows you how to master the Heyreach and Clay integration

and how you can personalize every single cold outreach message that you send out. Anyways, I'll see you in that video. Have a good one in the meantime. Cheers.
