# How I Get Unlimited Leads With Hermes Agent + LinkedIn

Source: https://www.youtube.com/watch?v=Ol9MOzKtdvI

Today I'm going to be showing you how I get unlimited leads with Hermes agent and LinkedIn on autopilot [music] using the workflow that we built and directly through Slack. So by now you've likely

heard of this new AI agent called Hermes, which is something similar to Open Claw, but it's probably something that's the most powerful from any other agent that I've seen so far for one

specific reason, and that's that this agent has its own persistent memory. meaning it has almost like a self-improving loop. Meaning every time you screw up something or the agents

screw up, which happens [music] all the time with all of the agents, it kind of saves that into the memory and make sure that it does not repeat the same mistake next time. Also, when you do something

good, such as define the process of how you want to scrape [music] the leads, enrich the leads, and then send them to your campaigns on LinkedIn, it also does that uh pretty well, and it saves that

into the memory. also builds all of the skills and ensures that every time you run the new campaign, it becomes better and better with it. So today, this is going to be a very practical video where

I'm going to show you exactly how we use Hermes agent to run LinkedIn outreach at high velocity using Kreach, which allows us to basically rotate [music] LinkedIn accounts, connect as many senders as you

want, and really scale this outreach to the [music] point where it really moves the needle for our clients. We're going to pick a specific client and we're going to walk you through the entire

workflow starting with how to set up the agent which is pretty straightforward and simple. It's probably the simplest of all of the agents compared to like open core or anything else. Secondly,

how to basically scrape leads from any place any leads that are not in like traditional [clears throat] databases or directories. How you can basically build that list from scratch. Then moving

forward, how to basically qualify and score each of the prospect on your list against your ICP to make sure you're reaching out to relevant people. How to write [music] all of the sequences with

this agent and how to upload it directly into [music] Harry using their MCP or CLI which is even better where you can create a campaign from scratch, embed all of the sequences, copy and then just

be able to QA and basically run it directly. All of this is going to happen directly from our Slack. There is no reason for us to ever leave Slack. So this is going to be the workflow that

we're going to be showing you today. So starting with the most basic task is how you can set up the agent. So if you just go to Hermes agent, then just punch in the website here or just Google it,

you'll be able to find it. You have a couple of different ways. One is to download the application for desktop. If you're using Mac, it's probably the easiest way. If you're not as technical

and you don't really like the experience, which I don't like it. I don't have coding experience in the background. By nature, go to market person. So, you know, I prefer to

download the app and basically when you download the app, it just looks something like this. Essentially, it guides you through the process as well. You can see basically everything here.

You can chat with your agent directly within the app and you can set up any messaging medium meaning if you use Slack, WhatsApp, Telegram, Discord, any of these, email like our agent for

example has Slack and has its [music] own email. So it has both things. So very easy to manage it from the app. It's my suggestion if you're not as technical starting off the first time.

Just download [music] the app. It's going to be so much easier. Secondly, if you prefer terminal experience, again, still very straightforward. All you have to do is just to copy this URL here, go

to your desktop, click command and space, open your terminal, and then from here you basically just paste the command, hit enter, and the agent is going to prompt you basically step by

step on how you can set up all the things. Either way works. You can even do this and download the app if you prefer to have it that way. So what's important to understand is that once you

install this agent, it's important that if you want your agent to keep running, your computer has to stay awake. It has to be turned on at all times. Otherwise, your agent is not going [music] to work.

So basically, setting up this agent is the first step. It's going to take you maybe 10 minutes to set it up. And once you set it up, basically you can start chatting with it [music] immediately

depending on the medium that you set. You can do desktop app. Again, we have it on Slack. We have our Hermes delivery channel here which we also use for our clients and all of the delivery work. So

um it is pretty easy and straightforward for us to do that. Secondly, once you install your agent, your agent is going to need some tools to work with. It cannot just make up leads from thin air.

Even though it's very good, it [music] cannot send sequences without a tool. So for this purpose, we're going to be using her reach. We use generally here reach for us for all of our clients

outreach and you know just we see great results. It's very easy to set it up when you navigate to your her account. Just go on to settings and then hit integrations. From here there's a bunch

of different options that you can connect. My suggestion here you have the MCP server and you have the CLI. CLI is the better option in my opinion. So all you have to do with your agent is

basically here on her reach click on how to connect. It's going to open a new tab for [music] you and this is a public GitHub repository which you can just basically copy send to your agent and

just say hey please install here each agent install here CLI for me and help me you know authenticate and use it. You will need your API key which you can also grab from here. I'm not going to

click on it because it's going to expose API key but basically once you click on it just copy the API key. Agent will guide you how you can put it in a secure environment so you do not expose it. And

then once you do that very easy to use again this is CLI you can use in cloud code in codec in any of the agents we use it with Hermes and our Hermes agent is connected [music] to our codeex which

I think is the fastest shows the best performance across different tests that we run and generally outperforms every other model and age that we have. The good thing about it is it can be inside

your subscription. So you don't have to use API and you don't have to worry about the API costs if you were for example to use entropic and and use the API key. So that's the first thing that

you will need for our campaign. We will also need clay because it helps us find people do more research and just overall uh achieve better performance. So we do the same thing here under quick start.

Basically there is a GitHub repository. We just copy this give to our agent. It guides us through connects everything with clay and then we have all the tools that we need to really build an

outstanding campaign. So that's setting starting and basically you know setting everything up. Now with our agent we also built a [music] workflow which is a very interactive and kind of guides us

through the campaign which we will do right now. So for this purpose we're going to pick one of our clients little track. Basically, it's an awesome tool that helps creative leaders inside

mostly marketing web design agencies who create websites to basically cut their QA time from probably for like 40 hours a week or per month to be more precise. But in any case, it helps all of these

companies, you know, compare their Figma designs, whether that's a product development or or their web design. It's definitely something that, you [music] know, has a strong value proposition and

you can sign up for the tool to try it out. So it's it's it's pretty good if you're in this space. [music] So in our opinion when we take a look at the client we understand that they probably

work with modern web design agencies. So something like web flow framer or [music] similar would fit the ICP criteria. So what we do here is essentially we're going to go to web

flow partners as our first step and we're going to say let's hire a certified partner here. What we're trying to do right now is how can we get the source? How can we get the leads

that are off the database? Like in other words, these people obviously exist on LinkedIn. We're going to be reaching out to them on LinkedIn. But how can we get to basically companies and make our

outreach relevant? So we're going to click enterprise [music] and premium partners or maybe just enterprise partners if we're going to go on after bigger agencies and we will paste this

URL. We'll come back to our Slack. As you can see, our team already uses this. So we're going to say, hey, our agent names is Stannislav. So we just named it that way. I want to run a new campaign

for a client. Just make sure it knows it's outbound. It's not ads. So, what's going to happen right now? Stannislo here is going to open a new thread [music] which here is going to read our

existing skill. We already preloaded our agent with skill. And by the way, the best way to build skills is to basically establish the process, start doing everything. And then once you have

everything ready, make sure to kind of document that process because again agent will remember it. So it's going to say campaign launcher is here. Let's start a new campaign. So it kind of

opens interactive way for us. So we click start new campaign and it opens the thread for us here. What I'm going to do is I'm just going to open this in a new tab. So here we have our campaign

launch and it says this is the name of the client. Now, it's asking us to add the initial direction for the campaign, which is something that we have to do. So, we're going to click add a direction

and we're going to say something like we want [music] to scrape this directory, find founders, and then clean up the data and write [music] sequences and then send over to her reach. So, for

that, I'm going to be using spoken link here. This is the app [music] that we use to kind of speak to our agents because we just do the work so much faster. So, let's say something like

this. So we're trying to scrape Webflow enterprise partners from the link pasted below. Once we have that, then [music] we will use Clay's CLI to pull founders and CEOs and creative directors of these

companies. Prioritize creative directors and then founders and CEOs afterwards if we cannot find creative directors and then clean up all of the data that we have. We need first name, last name,

company [music] name cleaned and we need LinkedIn profile of the person. And then after that we're going to be writing the [music] copy for LinkedIn outreach through hey reach where we will be

creating the campaign and >> [music] >> uh launching it directly there. Keep this to only 20 companies for now and do not get more than 30 people total

combined. Obviously we just shrink to like smaller number for the demonstration purposes but technically you know if you wanted thousands of leads and just it would do the same

thing. So click save and continue. [music] And basically it's going to ask us how will what is the source of the leads for us. Again this is something that we pre-built. So it's easier for

us. We will do something like custom [music] directory scrape. And then it's going to ask us for the leads. I already kind of told the agent there, but you know, we're going to say 30 save

choices. And then [music] we will also just basically be able to I forgot to paste this here. So I'm just going to have to paste the link in addition to what I said earlier. Once we have that,

then [music] what this is going to do for us, it's basically going to go to Clay and to fetch all of the enrichments and functions that we pre-built to suggest what are the enrichment we

should use to keep [music] our outreach highly relevant and not something that's just super generic. So now we have our agent came back to us once it expected the basically functions and enrichments

that we could run. So we have a couple of different potential angles [music] that we can run. The first one is cut enterprise website QA cycle before launch and position dual check as a

faster way for web flow enterprise [music] partners to compare approved Figma designs to live client pages. Identify visual mismatches [music] and avoid repeated functions. This is the

persona and this is the trigger. Then the second one is protect agency margins. The third one is reduce design to develop and handle friction and then add QA [music] capacity during delivery

growth. We're just going to pick the first one for now. And then here we're going to be able to basically select some enrichments. It basically suggested a couple of these to us. This is the

company enrichment from website. Find open jobs. Find latest news. Find people at the company which we will need in any case. And then company employee count. So what we will select here is multiple.

We'll [music] say we will want to find people at the company. We will want to find to do company enrichment. And that's typically sufficient for us because we have the rich data from

there. Now we click review. select the strategy and [music] the agent is basically going to ask us to just approve the strategy. So all we have to do is just [music] click approve and

it's actually going to start visualizing how everything looks for us. In our case that's strategy source sample list build enrichment QA copy sequencer draft and then launch. Now here all we have to do

[music] is just for approval for the agent to be able to spend the credits. We're just going to paste this here and it's going to start. By the way, what I'm showing here again, we have an

existing workflow that we built, but technically you could just chat with your agent on Slack or WhatsApp directly [music] and it would still achieve the same output. We just standardize it

because we have different approval gates that we run for our clients. But it doesn't have to look this way. You can simply just, [music] you know, chat with your agent. One great thing about Hermes

agents is you will be able to see what are the actions that it performs. So, right now it read our skill. It started basically going into the [music] URL that we pasted. It's reading the client

context. We already have our client context pre-built here. So, it understands what the client does. [music] It helps him with the content, with sequences, copyrighted later on,

and so on. So, it basically does all [music] of the work for us without us having to use a lot of different tools. The agent can figure everything on its own to be able to basically perform all

of these actions for us that normally we would have to have scrapers or do it manually or figure out a third way to kind of stitch multiple CSVs and tools together. [music] So now our agent here

actually pulled all of the unique web flow enterprise partners. It [music] did recognize that we asked only for 30 for this use case. Now it will find people and it shows us the estimated spending

credits and it's going to reach the companies and basically [music] allow us to have everything ready. So from here all we have to do is [music] just click approve and it's actually going to start

building this out for us. Now although you don't really have to leave Slack for anything if you really wanted to have some visibility into how everything works because we are using now clay for

the enrichment you can see that the function actually runs here with the inputs and it basically does the company research enrichment for [music] us. It says what is the ICP of this company? Do

they have any funding? These are agencies so most of [music] them will not have uh who they sell to. What is the company description? All of this context including the services and

products that they offer is going to be of paramount importance to the agent to be able to perform the [music] scoring against the ICP and really assess if this is a fit for us to reach out

[music] or not. That way you avoid reaching out to competitors. You stay much more relevant. You can really stay relevant with the copy and you can personalize the copy that doesn't scream

AI or something weird that you've seen on their LinkedIn or something similar. So it is very important to run these types of enrichments with whatever tools you're using and then be able to use

that information to feed the agent to score against the ICP before you actually send anything to your sequences for any kind of automated outreach. So now we can see here that after a couple

of minutes our agent basically researched 30 of 30 company profiles. It selected contacts and cleaned the contacts. We have everything that's ready here. Some of them failed. List

[music] quality is A+ and nothing is uploaded yet. So what we have to do is basically just to click approve um list QA meaning like it will basically just audit our list. And then after that

because it's already scored, it [music] already has the context on our client. It will upload the lists directly into her reach where we will run LinkedIn outreach using multiple senders for our

clients to [music] basically maximize the coverage and ensure that we're as relevant as possible. Now what the agent says here is basically finalist is confirmed. [music] Now this is the

suggestion from the agent. We're going to send a blank connection request or with a note. We're going to likely go for blank. Number of follow-up messages. What is the core wording? What is the

proof point? What is the CTA that we want? What is the personalization service so on? And what is the preferred [music] delay? So basically it's going to create one representative sequence

and then it's going to automatically upload [music] everything into here. So what we'll do here, we're going to say to our agent something like this. So we will send a blank connection request and

then we [music] want the first message after 3 hours. Then we want one more follow-up after 2 days and then the third follow-up after 4 days. If we aren't accepted, then we want to wait 5

days to basically follow them. Two more days to like their latest LinkedIn post. And then after 10 days, if we are still not accepted, we can withdraw the connection directly. CTA is going to be

the free signup and then personalization is basically if we can pull their case study as an example to kind of mention some of the great work that they did and to ask them how they currently QA the

process and position the solution that would be great and I already described all [music] of the delays. So essentially what we did here is I recorded to to the agent [music] what

are the things that we want and I even added something additional. I said, let's also grab the case studies from these companies [music] to use that as a personalization point. Meaning, you

know, we will be more relevant. People like to be complimented [music] when we reach out to them. So essentially, we're doing this for like 30 50 leads right now, but if you had

hundreds or thousands of leads, you could technically just perform the same process and the outcome would be the same. It's also pretty quick as long as it's hooked up to something like Codex.

It's going to take a couple of minutes for the agent to kind of wrap up everything, but as you can see, it actually is using a native browsing experience and the browser that's built

in into Hermes agent to kind of research every company here [music] and pull case studies. So, you can use that here. And you can see it's only allow us to say, yeah, we can withdraw at least 14 days,

which is fine. We can still [music] still do that. And here we can see that our agent basically drafted a proposal for the sequence. It's a blank connection request. And then we have

here like, hey, your [music] whatever project really stood out, which I don't like as an opener. So, we can change that. But it is relevant. It says, especially how the site pairs with bold

visual identity, why Web Flow build. So, it kind of acknowledges that it's already built on web flow. How does your team currently QA live build against the approved Figma client handoff? Then 2

days later, it says this is the reason why I asked where we kind of pitched [music] the platform. And then 4 days after it again just kind of reiterates that obviously the messaging can be

better but as long as the list is relevant we're reaching out to right people with a good solution I think like these are just minor differences and cop even doesn't matter that much so for

[music] the sake of of this presentation I'm going to say looks good so it can continue otherwise I would say just you know please change this which again we can [music] do something later on and

and tweak if we need it but basically that's uh you know decent enough to to move forward. So now when the copy is approved here it will say we have to approve it and after that it's going to

need the exact sending accounts use both active senders. Again with [music] her reach you can have unlimited senders. So if you have 5 10 15 people within your company that can do the outreach for one

fixed price or cost you can basically scale the outreach to like really something like a really scalable channel that [music] will consistently bring you pipeline. So daily connection requests

per volume per sender that's already default. We don't send more than like 20 25 connections per day just to kind of keep everything you know in limits where I don't think we're risking any of the

accounts. So right here then we'll see that basically both active senders are assigned has been published yet. It created a campaign uh inside here for us and basically contacts are not uploaded

yet. [music] So what all we have to do is basically to approve the sequencer draft which I think we can do directly from here and then just say done. So our [music] agent is actually going to

upload the leads and then we can check it out how it actually looks inside here reach. So we actually hear that it uploaded all the contacts for us 42 and 27 companies the campaign is in draft.

It did not find [music] emails or something similar. So if I go over to Kreach to check this, we can see that it actually respected the structure that we described. So connection request and

then 7 days wait to like the post and then wait a little bit more before kind of ending the sequence. Withdrawal is being handled automatically by hey reach if it's not accepted within the certain

period of time. And then if we're accepted, wait 3 hours and send the first message. Obviously if somebody replies, it automatically stops the sequence. then wait two days for the

follow-up message and [music] then wait another 4 days before you send the final follow-up message here. So basically our agent created a campaign for us, sourced the leads and just uploaded everything

[music] directly inside hey reach and it actually looks quite good. So now that you've seen how you can source the leads from any directory, enrich, score the data, get all of the information, write

the copy and upload it directly to Harach to run very scalable and high quality LinkedIn outreach. You can build this on your own. Two things that you have to do is sign up for her reach

using the link below where you can have unlimited senders for one fixed cost and it already comes with MCP CLI and all of the other integrations. And also make sure to install the Hermes agent which

is going to allow you to perform something like this directly from your Slack. So at Frreak we basically follow this process for all of our clients. That means that we can be somewhere else

drinking the coffee while we can actually launch campaigns directly from our mobile phone just by chatting up with our agents on Slack. And what's the best part about the agent again when

paired with the right tools like Kreach? [music] It also has a persistent memory. So now we can say to our agent, every morning 9:00 a.m. find me 30 more of these

companies like this and perform the same process. So even without me chatting to my agent, it's actually going to perform this process on a schedule and every day you can basically generate as many leads

as you want and run scalable, personalized, and relevant outreach using a combination of hair reach and Hermas. [music] And if you made it to the end of this

video, by now you probably know that LinkedIn outreach is about to change forever with the tools and AI we have around us. So, just make sure to check out the next video here because it

breaks down the exact process.
