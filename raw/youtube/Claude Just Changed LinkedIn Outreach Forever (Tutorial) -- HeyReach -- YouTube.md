# Claude Just Changed LinkedIn Outreach Forever (Tutorial)

Source: https://www.youtube.com/watch?v=4eG0MFS7vDQ

We're entering a completely new era of LinkedIn lead generation. In order to actually book meetings in the past, you had to have endless back-and-forth conversations with each individual

prospect. And that's the exact part of outreach that nobody could automate in the past. Oh, until now, of course. Since I literally run cold outreach for a living over the last 3 years, the

positive replies stack up, and now we finally built a system that enables us to automatically handle each individual positive reply and convert them into meetings. So, in the next few minutes,

I'm going to give you a full tutorial of the exact system that I use in order to run my entire LinkedIn outreach together with Claude. And of course, I'll cover how to train Claude codes to become your

best salesperson, how to let it read every single conversation that you are having on LinkedIn, and how to get it to draft replies to book meetings into your [music] calendar. Anyways, let's jump

straight into it. All right. So, first things first, almost 90% of the meetings that you book from LinkedIn typically happen after the sixth interaction with the prospect. So, you always need to

keep in mind that a deal that you can only convert a prospect into a meeting on the back of five or six message exchanges, which is obviously way past just the initial cold outreach message

that you would send to the prospect. And that's why most of the people that I know that are most effective at booking meetings using LinkedIn tend to just endlessly be on their phone replying to

the messages, asking open questions, and trying to have a back-and-forth conversation with each individual prospect, which obviously takes a lot of time and is super, super manual. You

don't need me to tell you that there are automation tools like HeyReach that allow you to send connection requests and messages, for example. But the one thing that I bet you didn't know in the

past is the fact that you can actually reply to those positive replies from your prospects instead of having to answer the same FAQs, the same kind of objections every single time in your

LinkedIn inbox. Now, to start off with, I will quickly show you how we manage over 10 different LinkedIn accounts all within one workspace whereby just one person can manage all of the positive

replies that are coming in. For the purpose of this, I'll be using a tool called HeyReach, and if I quickly sign into my account, you should be able to see on the left-hand side I have over 99

different conversations inside of the UniBox. So, if I click into the UniBox on the left-hand side of the panel, I can now filter for the relevant sending accounts because we have a lot of

different senders and a lot of different clients connected into HeyReach. So, for example, if I only wanted to filter for my own replies, I can select myself as the sender over here and then click on

apply. And that way, let's imagine for a second that a prospect replies over here, I can just quickly assign a tag to it so I can, let's say, add a tag here and just call this interested, just as

an example. And then, on the back of that, we can then navigate across to leads on the left-hand side of the panel. And that way, next time, if I want to find all the leads that are

interested in my services, again, I can just filter based on the tag being interested. I can click on apply and I'll see a couple of people over here that I have just marked as interested.

So, not only are we sending connection requests and sequences inside of HeyReach, automating a lot of the activities that we are otherwise performing like connection requests and

messaging, we also connect all of the replies inside of the platform. And in a second from now, I will be showing you how you can connect it directly to Claude so that Claude can read the full

conversation, draft the next message for each person, and so that we can finally add a human-in-the-loop step, which enables you to approve the message before it's sent out to the

prospect. So, the first thing that you have to do is head into your HeyReach account. For the purpose of this, I'll sign into it, go into the settings in the bottom left-hand side of the panel,

navigate across into integrations, and then over here you should be able to see the HeyReach MCP server. So, if you see this, it will generate you an MCP key and also an MCP connection URL. For the

purpose of this, all I want you to then do is head into your Claude account. Inside of Claude, navigate into your name in the bottom left-hand corner, and if you navigate across into settings,

you should be able to see connectors, and then over here you will be able to click on add in the top right-hand corner and click on add custom connector. So, in this case, all we need

to do is now just give it a name. I'm just going to call this HeyReach 2. We're going to copy the MCP connection URL that's at the bottom over here straight into the remote's MCP server

URL. And all we need to do is just copy the MCP key, which you can see at the top here, straight into the top field over here where it says remote MCP server URL. That also passes through

your key, which is a secret key, so please keep it safe. And for the time being, we're just now going to click on add, and you should then be able to see HeyReach pop up amongst the list of

connectors. It's a very similar way. And by the way, if you have not tried using connectors yet, I recommend for you to connect any tool that you use on a day-to-day basis straight into Claude.

That way you will be able to perform actions within that tool just by prompting Claude in real time. So, in this case, all I'm doing is I'm going to now click into HeyReach. You can see

that the permissions are now set to custom, so for the time being, I'm going to switch that to always allow, of course, assuming that you're happy to allow all of these permissions. And if

we just look at all of these end points or all of these actions that we're able to perform using this MCP, it's all pretty straightforward. We can create campaigns, we can delete campaigns, we

can add leads, we can add messaging, we can do all of that good stuff as long as everything is connected here. But essentially, all we have done right now is we have established a two-way

connection between HeyReach and Claude, meaning that now you can perform any actions inside of HeyReach directly from the Claude chat, and also we can pull up any stats from HeyReach on top of that.

So, most of the manual activities that you would have otherwise been doing inside of HeyReach, you don't need to do anymore because Claude can perform those actions on your behalf. If I'm totally

real with you guys, if you use Claude or any sort of large language model as fanatically as I do, your Claude will already know a lot about you. So, in my case, I'm going to be super bold and I'm

going to just paste this prompt into the chat and say, "Create a client onboarding brief for B2B Boosted done-for-you GTM engineering agency." So, in this case, I'm just literally

going to say, "Hey, go and create a client onboarding brief for my business, which is called B2B Boosted. Make it based on past knowledge of what myself and my company is all about." And on the

basis of this, I trust Claude to look up all of the past chats that it had with me and to research my business via my website and via my LinkedIn company page and various other social medias. And on

the basis of that, I expect it to learn four [music] main things. I expect it to understand the products that we're selling or the products or services that we're selling. I expect it to understand

the persona that we're selling to, the pain points that we're looking to solve, and also our current process for that. So, essentially we just want to cover end-to-end the business, specifically

from a GTM perspective of who do we want to go after, what do we sell, what are the pain points that we want to scan for, and what's our existing process for that. And on the basis of this, they

should create a quick form for us, which we can then use in order to train up Claude and in order to perform numerous actions inside of HeyReach on our behalf. So, you can see really quickly

on my side, it went ahead and it created a quick high-level playbook. So, in this case, it says that we're clay-powered GTM engineering agency. We work with SaaS companies who are working on their

outbound and go-to-market stuff. It talks briefly about the offer, about the kind of tools that we use, all that good stuff. And essentially, what I'm going to do now is I'm going to say, "Create a

Notion page with all of this info." Worth keeping in mind that the way that this has access into Notion is the same way as it has access into our HeyReach. All I needed to do in order to establish

that connection is head into settings, head into connectors on the left-hand side of the panel, and then over here, if I click on add and browse connectors, I can just select Notion, and I can add

that very similarly to how we added HeyReach already. In the meantime, you can see over here it says, "Done. The Notion page is now live." So, I'm going to click into this Notion page, and I'm

going to rename it to B2B Boosted Brain for HeyReach. So now, all I'm going to say is, "Great. Go look at HeyReach replies that are unread or not replied to in HeyReach using the HeyReach MCP,

then draft replies for all of these leads using the Brain in a Notion file, and show me on the screen for how you do that just for one prospect, just so I can show you a quick teaser." And for

the purpose of this, after I submit this prompt, you can see it now says that you will pull HeyReach conversations, and it will find unread or unreplied conversations. On the basis of that,

you'll then load up, and you can see over here the HeyReach logo pops up. So, of course, it's using the HeyReach MCP in order to pull this [music] off. Whilst it does its job, worth noting

that you can also teach it to add certain tags. So, for example, you can ask the MCP to add a tag like interested in a meeting or something of that sort, so you can sort through your list inside

of the HeyReach unify box. And you can see right now, at the time of me recording this video, we have 103 messages that are marked as unread and require reply because we have numerous

agency clients who are connected into HeyReach, so we do get positive replies on most days of the week. And in this case over here, we can see we have this specific campaign retargeting people

that attended a specific tech conference. And in this case, we have two draft replies to their reply to us. And And this case, we have the first reply, which reads, "Hi Rick, appreciate

the reply and no rush given the travel. Next week works well." Then we basically praise this prospect because apparently they were talking about time zones and how you know, we need to find a mutually

convenient time to speak. And you get the idea. You can basically draft the entire message and you have two options here. The first option is that you can just do that on a manual basis all the

time. Or alternatively, what you can do as well is you can go into the chat and you can say something like, "Turn this into a Claude routine whereby you look up unread messages, draft replies and

send them to me via Slack direct messages every Monday and Thursday morning." So that way this will work completely on autopilot in the background without you having to even

chat with Claude. He will just send you all of those as notifications and you just need to basically sign off on the replies and how you want to handle them. Again, if you want to learn a bit more

about Claude routines, I'll make sure as the second link in the description down below to add a separate video which I have done on Claude routines. But spoiler alert, it's pretty

straightforward. You basically just go into the schedule section on the left-hand side of the panel inside of Claude and then you can click on new task and create it with Claude using the

previous chat that you had with Claude already. And I highly recommend that inside of that Notion brain that you created for your own company, you have the FAQ section which you can pull up by

just getting Claude to visit your website. So based on things like how does your service delivery work, what's your pricing like, how long does it take for a customer to onboard or something

of that sort, you just need to put it into an FAQ directory, add it into your brain and that way your replies by Claude will mimic the kind of replies that you would be sending out manually

otherwise as well. Now guys, don't get me wrong, there is so much that we covered throughout this video already and if you want to set this up for yourself so that you can stop worrying

about having to manually reply to every single individual lead, you can go and get started completely for free using He Reach which will be using the first link in the description underneath the video.

Once it's connected to Claude, every reply in your inbox gets drafted, and you can be notified on a daily on a weekly basis to check some of these replies and to approve them for sending,

or you can even do that every single morning. So, again, go check out the HeyReach link, which will be the first link in the description down below. More than that, we're giving away a 14-day

free trial, meaning that you can try it out completely risk-free for 2 weeks. And by the way, in case if you want to learn the most important things from millions of dollars made with LinkedIn

outreach, then check out this video popping up on your screen right now.
