# Claude + LinkedIn = Unlimited Leads on Autopilot

Source: https://www.youtube.com/watch?v=svA4AVJB5Vc

We have finally gotten to the point where we can now run the entire LinkedIn lead generation on autopilot using Claude. Now look, having spent the last 5 years running outbounds for over 100

different companies as a part of my own agency business and having worked in numerous VC-backed and bootstrapped startups, I have to admit what I'm about to show you is one of the easiest setups

I have ever used. It's literally just Claude code and the LinkedIn tool and you can set it up literally in just a matter of minutes whilst having me in the corner of the screen guiding you

through everything button by button. Once you do this, this system can clean the lists for you, build your outreach campaigns, handle all of your replies to outreach so you can book something that

feels like an unlimited amount of meetings and do barely any manual work in the process, which is the dream of any salesperson or founder trying to streamline sales in-house. Anyways,

[music] let's jump straight into it and I'll show you how we can pull this off together throughout this video. All right, the first thing that you need to do is connect Claude code to some sort

of LinkedIn outreach tool and the one I like most is called HeyReach. It's one of the safest and most intuitive LinkedIn automation platforms from all the ones that I've used so far and once

Claude code and HeyReach are connected, Claude can essentially go in and run all of this outbound LinkedIn messaging, connection requests, liking of people's posts, and all that fun activity on our

behalf in return for us just prompting it and telling it what to do. The way that you would connect Claude code to HeyReach will be using something called the HeyReach CLI, which gives Claude

code full access to everything within your HeyReach account. For example, creating a lead list, creating a campaign, adding messages [music] to a campaign, or anything of that sort.

Look, I could give you a step-by-step, button-by-button tutorial, but in reality, all it takes is for you to go into Claude and literally just say, "Hey, I want to connect Claude code to

Hay Reach CLI. Tell me the commands I need to paste into the terminal to pull this off." And you can see in this case, Claude or

ChatGPT or Gemini or Croc or any other fancy AI model will automatically research on the internet for the MCP connection and the CLI connection. You will fetch all the information about how

to pull this off. You can see he's basically reading through all of these articles so that you don't have to. And you can see straight away, he comes up with all the steps here. By the way,

I'll be giving away these exact steps inside of a beautiful Notion checklist guide. So, you can see the guide in front of your eyes over here. The first thing you would need to do is open Hay

Reach and go to integrations. So, let's just tick this off and go to Hay Reach. You can get a free Hay Reach account using the first link in the description underneath the video. And the perks of

clicking on that link is of course the tempting 14-day free trial. So, as soon as you're inside, click into settings in the bottom left-hand corner and navigate over to integrations. If you are in

integrations already, you can see over here it says the Hay Reach MCP server, which is connected. I can click into it. You can see the MCP key and the MCP connection URL at the bottom. So, this

time I'm going to click on new MCP key and then just copy [music] that to clipboard and copy the MCP connection URL at the very end of this command over here. So, wherever it says paste your

MCP connection URL here. And this entire command that we created just now, we need to paste into something called the terminal. And the terminal is basically the back-end operating system of your

computer. So, if you type in terminal, you it should pop up on your screen. If you're a MacBook user, you can just paste that command and click on enter. And then as soon as you do that, it

should basically tell you, "Hey, this has been connected." And then after that, to verify that it's installed, again, you can just go into terminal, but this time just click on a new

window, and then click on new window over here, and you can just type in Claude MCP list commands, and then as soon as you click on enter, it will give you a list of all the different MCPs

that are connected on your computer. So, you can see it says, "Checking MCP server health." And it should be giving me a list of all the MCP tools that are connected to my computer. So, you can

see in this case, Make, N A 10, Full Reach, Atium, PayPal, Fireflies, and we can see Hey Reach over here, which is the tool [music] that we've just tried to connect here, and then we have

connected successfully. So again, if you want this guide, all you need to do is just head over to the second link in the description down below. And whilst I have your attention, I'm also going to

give away my LinkedIn DM SOPs. This is the exact markdown file with all the instructions that you need to plug into your Claude code system so that you can write relevant and personalized LinkedIn

DMs at scale. And you can build on top of those custom instructions, but you can think of them as the recipe, and you can have your own interpretation of this wider recipe. So again, if you want this

markdown file, it'll be linked in the second link in the description down below, alongside a lot of other cool resources on Hey Reach, including how to use Hey Reach, every single button

within the tool, how to connect [music] to other platforms like clay.com, and a bunch of other videos that I have done about Hey Reach, as it's one of my favorite outbound tools at the time of

recording this video right now. Okay, so now everything is connected, Claude code, we have the LinkedIn custom instructions markdown file all loaded inside of Claude code. All we need to do

next is just go into Hey Reach, go on the left side of the panel where it says leads, and click on add leads. For the purpose of this one, I'm just going to import some leads from a CSV, so let's

click on continue here, and I'm going to upload a huge CSV with every single person that follows clay.com on LinkedIn. If you want access to this lead list and a lot of other cool lead

lists, as well as courses on Open Cloud Code, Any Ten, Clay.com, and a bunch of other emerging AI tools that are super super important that hardly anyone teaches from affordable price

points. Head over to unlockgtm.com and just check out the range of courses that we have available there. All in return for just one sensible monthly subscription fee. So, anyways, worth

noting the course launches on the 1st of July. So, if you're watching this before the 1st of July, I'll make sure to drop the wait list link as the third link in the description down below. And you can

see here we've just imported the CSV file. The most important things that we need to map are the LinkedIn profile URL fields, the first name, the last name, and the location, and the company name.

We have done that. We can click on create empty list, and I'll call this Tim Tuesday 8:00 a.m. because I'm recording this at 8:00 a.m. in the morning. And now you can see there are

51,000 leads that we've imported. So, I've just clicked on import. Obviously, this will take quite a while because there are quite a few leads in that lead list. And you can see now that 1,000 of

those leads have been created as a part of this lead list. So, all I'm going to do next is head over into Cloud Code and say, "I have a lead list inside of Heyreach titled Tim Tuesday 8:00 a.m.,

and I want you to enroll it in a new campaign that I want you to create for me. Just three messages inside the campaign spread out by three days each, and each message should contain custom

variables that we generate based on the first 10 leads leads's LinkedIn profiles using the LinkedIn DMs SOP." And I'll call this skill as well. "Use the Heyreach CLI in order to pull this off."

And my favorite line for this is to say, "Ask clarifying questions before actioning because I hate it whenever AI does stuff that I have not asked it to do." And in this case, I'm going to

switch from edit automatically over to plan mode. Obviously, the plan mode just enables us to scope the deal without before actually executing it. That way, we spend less time on troubleshooting

late down the line as well. You can see here, Claude code immediately replies saying, "I'll explore the relevant skills context." And he reached tooling before asking clarifying questions. Let

me launch parallel explore agents, and you can see it's reading the HeyReach CLI to understand how that works. Okay, guys, really quickly, as you can see I'm inside of Claude code right now. I

basically started a new session over here, and I'm inputting a super simple prompt. Bearing in mind that the Claude code system is already trained on all of my HeyReach SOPs. And again, you can get

them in the guide, which will be the second link in the description of the video. So, all I'm saying is use the HeyReach CLI to add the leads to a newly created campaign titled 10 LinkedIn DMs

for Tim. The leads are in my desktop. Just as a quick example here, you can see that it's set to bypass permissions, which is obviously dangerous. So, I highly advise for you to keep it at edit

automatically or at ask before edit mode instead. And you can see in real time, it's checking the HeyReach CLI and the SOP files. And you can see that it hardly even thought here. It literally

took about 10 seconds end-to-end for it to say that it's added the 10 LinkedIn DMs to a fresh HeyReach campaign. So, we started off with just 10 leads to start with. You can see each one of these

leads has automatically been enriched. In my case, I use separate providers like AI Arc and Prospector to enrich all those profiles so we can pull all of the details from their LinkedIn profiles

directly. And each sequence is built on my five message framework, which starts off with a greeting, a controlled compliment with five out of 10 level of enthusiasm, followed by an authority

observation, and a curiosity question, and a resonance line. So, if you're wondering what that looks like, let's just have a look at a couple of examples in front of our eyes over here. So, to

start off with, we have Joe Leto. Right now, he doesn't have a name of his company. In brackets, it just says "Own things." So, I guess he's just in stealth mode or something of that sort.

And here is the five messages that you will receive. Hey Joe, we clearly both live in the clay corner of LinkedIn, haha. You running your own thing at the minute? {question mark} The outbound

space is moving so fast right now. I do a lot with Claim Claude and put it out on YouTube. Plus, I'm also in a group with some of the outbound guys like Eric Nowoslawski. Genuinely hard to keep up

with the clay releases lately. Is clay a big part of what you're building or more of a side interest for now? And then my favorite is the resonance line, which is the fifth line we send out. You out in

Ashburn, heard it's basically the data center capital of the world right now. Mad how much of the internet quietly runs through there. Now, you may call me out at this point and be like, "Tim,

this is absolute garbage. I'd never reply to that." But let's be real, you don't need every single person's reply to these kind of messages. All it takes is one in 50 people, one in 30 people,

and you're generating one lead a day if you know how to use HeyReach properly to the full capacity. Again, if you want to get our HeyReach tutorial for 2026, it will be the second link in the

description underneath the video. So, go check it out. In the meantime, you can see the examples for all the other prospects here as well. So, all of the copy in my opinion is pretty sharp. And

bearing in mind that I can also go through the QA process of quality assurance, I can rewrite it in cold code in real time. I can teach it that I can that way train cold code to make the

copy even better. And at scale of sending over 50 over 100 messages a day, I back myself to get positive replies from this campaign alone. Now, if we scroll all the way down, it says, "All

of these leads loaded into the new campaign, 10 LinkedIn DMs for Tim." And it says, "Pausing here for your go, Tim. Do you want me to send those across?" Basically, do you want Do I want cold

code to launch this campaign live? And if I go into the campaign over here, I can basically click on edit campaign. And then if I go all the way through to continue, I can see that it's basically

manned out of five messages. So, the first message over here. And in this case we're splitting the messages by 1 day. We're realistically you can switch that to as low as 3 hours as well. So,

I'm just going to set it to change this to 3 hours. We can send them a message every 3 hours if we wanted. Bearing in mind that all of these messages are very light, so it's a very easy read for the

prospect. I hope you found this stuff useful, guys. If you have, as I mentioned a million times already, you can steal the entire SOP, the entire skill library behind LinkedIn outreach

as the second link in the description underneath the video. And just remember that at first attempt, the outreach copy will not be the best. You do need to give it feedback. You do need to rewrite

it in your own tone. And only based on that will Claude Code learn from it. It will update its memory.md file. And next time, the speed to launch your campaign will be way, way faster. Now, if you

want to run this exact setup yourself, I will leave a link for HeyReach as the top link in the description underneath the video, where you can try out HeyReach completely for free. And of

course, once you are signed up, you can connect it to Claude Code and let it handle your lead list cleaning, the build out of your campaigns, and sorting out the replies just like you saw in the

video earlier today. And more than that, you can even tidy up and sort all of the replies to the interested prospects, so that you can spend your time on what only you can do, which is closing the

deals, of course. So again, you can go and get started with HeyReach, top link in the description down below. Go click on it and redeem that free trial. And if you're exploring different AI tools, and

you want to see how Open Claw how Open Claw can run your LinkedIn outreach for you, and how you can use Open Claw in order to run your entire LinkedIn outreach, then check out the video

popping up in your screen right now.
