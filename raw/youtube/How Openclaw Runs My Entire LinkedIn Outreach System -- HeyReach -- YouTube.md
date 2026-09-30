# How Openclaw Runs My Entire LinkedIn Outreach System

Source: https://www.youtube.com/watch?v=a6CfV9JHSPE

If you've ever wished you can run your entire LinkedIn outreach without ever opening the platform, Open Claw is exactly how to do that. At my agency, Top of Funnel, these are the systems we

build out every single day. We deploy fleets of agents for all kinds of use cases, including outreach. So much so that these agents have become reliable employees working collaboratively with

our clients, with our own team. In this video, we're going to go over the entire setup so you can build and launch full LinkedIn campaigns and pretty much run everything on autopilot right from a

single harness. And that harness is Slack or whatever chat app that you like, all just by using natural language and your agent does all the work for you. Let's get into it. First and

foremost, we have Open Claw. So, there's actually several frameworks that I usually use nowadays. There's a lot of them out there. The two biggest ones that I want to cover just for you guys'

high-level and awareness is Open Claw for sure is one that we still use. People still prefer it. It's one of the most popular and it works well and it continues to be iterated and there's

always new changes, right? This is the actual website, so I would recommend that you check it out and look at the documents because things as of this recording are always changing and what I

talk about in this video may change tomorrow. You just never know, right? So, the biggest thing you want to do is go to openclaw.ai and make sure you guys are actually

going to that site. There's a lot of look-alikes there nowadays and then simply go to docs and familiarize yourself with how to use it, you know, getting started, run the onboarding, all

that kind of stuff [music] and you'll be that much better off being more efficient. The second framework that I like to cover, and really a lot of the things are going to be very similar to

this, but you've probably seen it, is called Hermes Agent. Hermes is, in my opinion, one of It's one of the best. It's my favorite, to be honest. There's some pros and cons in using both Hermes

and then Open Claw, but from my experience, Hermes has been one of the better ones because of the memory, especially for business use case, but Open Claw definitely still performs. We

have agents that run an open claw and still generate opportunities, no problem. So, these are the two frameworks and once again, you'll just want to go to Hermes and then go to docs

because again, things change all the time and you just never know. You know, like I said, I could be recording this, I say something and then next thing you know, something else comes along, right?

Uh again, just definitely check it out, open claw and Hermes. The next thing you're going to want to do is you're going to want to think about how you want to set it up. So, frameworks are

one thing, but actually setting it up is a whole different thing. There are two types of ways to actually set up a agent and it really depends on your use case. If it's going to be personal or anything

that you're going to want to talk about business stuff, it could be anything in your life, things like that, it might be beneficial to actually set it up on a computer such as a Mac mini or a Mac

studio or maybe a spare laptop or something that you have laying around. I usually recommend against installing it on your own laptop, your main daily driver, just because you just never

know, you know, based on sandbox, you just never know what it's actually going to do and the last thing you want to do is have your main, you know, workhorse taken down, things like that. But we're

going to cover on a safe way to actually do exactly that, too. So, don't worry, if you're trying to install it on your main machine, there are some people like to take risks, it's just about awareness

and taking those risks carefully, right? The other part about installing a framework such as Hermes open claw is to actually install it on the cloud. We use Digital Ocean, there's also a lot of

other infrastructure cloud services out there. There's a lot of them, you know, they're all great. We usually stand up just a simple Digital Ocean droplet and we'll park it, we'll host it, we'll use

it internally along with our clients and the benefit here is that they run 24/7, right? So, they're always up and we can always remote in. I can just simply SSH into it, which is basically a secure

shell connection to connect into it remotely and be able to configure it and it allows for a lot of security, He for good sandboxing as well and it's not my computer, right? So, I can allow clients

to actually access the agent and do what they need to do completely on their own, let the agents run and just do their thing. So, for the most part, we're actually deploying it usually on

DigitalOcean droplet, so we can manage infrastructure from that. So, there's two types. There's basically on a device, like on prem, such as your own computer, and then there's also the

cloud, which uh is definitely a benefit as well. The other thing is I actually open-sourced quite a while ago, the OpenClaw Mac mini setup guide. I hosted several uh webinars and things like that

on just simply cloning this and how to set it up. You can check out my channel uh for more information on that. But, essentially, you just really, you know, if you're not familiar with GitHub and

you're not technical, literally, you can copy this website right here, or you can go to code and just click the URL right here under code, and you can just basically say, "Hey, help me set up

OpenClaw agent on Mac mini." And it's going to walk you through. The whole goal and the purpose of this is to actually streamline the setup and the onboarding a lot more, especially as it

pertains to GTM or outbound sales, because I have also loaded it when it comes to different skills, like competitive analysis, sales outreach, things like that, contact marketing. So,

there might be some things in here, you know, 5 months, that's not a long time, but that's ages when it comes to AI, right? This is definitely used, I mean, quite a lot for uh some people that want

to, you know, set up a Mac mini agent. Now, this is not going to be for DigitalOcean, that's a different kind of setup, but there's going to be some scenarios where it'll walk you through,

and hopefully, you can uh vibe your way through that, right? But, nonetheless, this is kind of how you set it up and walk in through. Same for the Hermes agent, there's a lot of good onboarding

when it comes to that. Then, the two things here, once you actually get an agent all set up and, you know, basically on your Slack channel uh or Telegram or whatever you want to use, I

recommend Slack because it's the most secure, well, not necessarily the most secure, but it's the most commonly known and secure platform that a lot of businesses use including us. So, it

makes it easy, right? And the experience I think you'll see is uh is quite mature and and good. It's just a really nice polished touch to know that you're doing a high-ticket premium feel. And the

other things that you're going to want to do is two things: context and capability. Context in a way that you're training the agent, right? So, you're training it on your actual business,

maybe how you want to use it, the ways and you want to set up tasks. No different than if you were to train an employee that shows up to work. You say, "Hey, this is what you're doing. This is

the business. Don't screw it up, right? Don't make up stuff. And this is what it is, right?" And your agent on Open Claw or any other one is going to store that into memory, usually in markdown files,

and therefore it's persistent. It will always be injected into the system prompt, therefore it is known and usually it's bound to the memory system, right? The other thing is capabilities.

And this is why we have Hey Reach, uh the CLI right here. CLI is the command line interface. It's no different than the actual terminal. And what it is is a very simple way to actually interact

with the entire Hey Reach platform or really any platform that you actually work with. A CLI tool is uh basically a wrapper where you can actually use any API endpoint or things like that. And

don't worry, if you're not technical, it basically means they give you a a remote control and you can virtually control the entire platform without ever having to log in or click and do all these

things inside of Hey Reach or or any other platform, right? So, basically the whole platform in your terminal. It'll call out these specific commands, and these are what you call flags, but it

will just simply execute right from the terminal and do exactly what you ask it to do. This is an overview on how to use it, as well as how to set it up, but nonetheless, I'm going to walk you

through exactly what to do from here, right? But this is a high-level, again, things change all the time, so I would definitely recommend going to the single source of truth, which is the makers or

the people's website directly. And not a plug at all, I just like to build stuff and ship it, especially open source, but if you go to top of funnel.com and you go to resources, I actually develop

quite a lot of CLI tools as well, so that way you guys can just take and have at it, do what you need to do, and there's a number of different CLI tools including HeyReach to be able to

leverage exactly what it's need to do, right? So, just at a high-level, we have again, your LinkedIn outbound controlled by agents, right? And what it does, it explains, I like to really try to show

like, "Hey, there's a lot of technical things, like break it down for me" kind of scenario, you know what I mean? A lot of sales people are like, "Dude, like this is the reason why there's

developers and then let the sales people do their thing so I can close deals, generate revenue" and that kind of thing, right? Well, basically from here, it's really just to kind of lay the land

a little bit, you know, show some context on what it is, what does it do, how do you control it, how do you navigate it because sometimes with AI, you know, you could throw things and

you're just like, "Wow, like what the hell are you talking about?" right? So, just go through here and you can see this is a way to actually install it. So, if you just simply go npm install

and then {dash}g means global, we'll go into that in a second, but then you'll want to put in HeyReach CLI, right? So, from here, it's going to authenticate, you're going to want to go into

HeyReach, which we'll go through in a second on your actual API key. And really, it's that simple. I mean, you can literally install it in seconds and you basically say, "Hey, you know, I

want to install this, install it" and go from there. So, when you are actually installing it though, if I were to click on install from npm, you can see right here, we have this command right here,

which is npm install {dash}g HeyReach CLI. This is going to be a good command that you can install into your HeyReach or your open cloud setup because if you're sandboxed, the it doesn't matter

where if it's global or user. You want it to be able to be accessed across any project that it wants to do. However, if you are installing it on your computer, then it's different. You're going to

want to install this on an actual project, and you know, similar to like Cloud Code or Code X or things like that, where you have like an actual project. For the purpose of this video,

I would recommend you continue to install on the global level, and you're going to want to uh install it right from the sandbox environment. go from there, okay? And then, you're going to

go to Hey Reach, okay? So, Hey Reach, obviously, you want to set up an account, and links in the description as far as getting all squared away there. Once you get your account all set up,

you're going to want to go to settings, and then go to integrations, and then simply get your API key, right? So, you're going to want to get an API key, and it's going to display. You'll just

simply copy that, provide that to your agent. You want to verify and authenticate and make sure that it actually works. And then, it's time to start going, right? All right, so we're

back in Slack, okay? So, everybody, a lot of people use Slack, a lot of our clients use Slack, and honestly, it's one of the most popular ways, and in my opinion, my favorite way to interact

with the agents. You'll see right here, we have just a snapshot of some of the agents that we have in our fleet. A lot of them are internal. We also have agents across every single client that

we work with, because again, the goal here is to collaborate with humans and agents, because the agents can actually effectively do pretty much 100% of your job nowadays. And I know that's scary to

say, but think about it. I mean, they go faster, they're smarter when trained right, and if you can really just leverage it, and you're on Slack in the first place, this is where humans become

less of the operator and more of the orchestrator or the supervisor. And with that, you're doing two things. You're verifying for quality and accuracy. And this is really a pivotal shift, if you

think about it, because this is one of the biggest things that humankind has ever seen. Now, without going on a tangent when it comes to that stuff, let's just get right into it. So, we're

just going to chime in with my one of my go-to agents, Roz, who's from the Wild Robot. I'm going to say, "Hey, Roz, I am showing my fellow outreach LinkedIn folks on how to do outreach. Validate

and tell me if you have a Reach CLI." So, we already have see the HeyReach CLI here. Roz is going to pop right up here. Another cool addition is Slack just recently started to do a lot more agent

enrichment. So, it just pops right up and can actually, you know, just enhance the experience from there. I've noticed it just going from a simple app to an actual agent. You can actually do

sidebar chats, you can do a whole lot of stuff. So, you can see right here, I can actually start chatting with a whole lot of different agents that we all have right there. So, that's awesome. Got to

confirm. Quick Let's see, by the end of time. The command is HeyReach. Okay, so it's just going to call HeyReach. We're going to say, "Perfect. What are you able to do?" And just, you know, ask the

agent, "What are you able to do? What are some of the endpoints or some of the taskers that you can actually do from here?" So, available commands, we have campaigns, inbox, accounts, lists,

stats, leads, lead tags, webhooks, things like that. A lot of this stuff we don't really need to chime in. The biggest thing is creating campaigns, right? Setting up outreach, things like

that. And you can see just right here, we have campaigns. So, it can list campaigns, it can get campaigns, it can create a draft, although you got to launch it yourself, which is fine. You

want to verify for quality, right? You can start, pause, resume, full life cycle management. And then from here, we can add leads, okay, get leads. I mean, you get you get my drift here. Inbox, we

can actually list out messages. We can have the agent reply to it. Now, one of the biggest things that I personally like to do, since it is our own LinkedIn account, is I like to be notified and

then it the agent will just prompt me to say, "You know, they said this. What do you want to say?" Or, "I would recommend saying this." And I'll be like, "All right, cool." Now, it depends on how

risky you want to take it and how far you want to go, but once it has enough context and you can reliably say like, yes, you know, you just want to make sure that the agent's not going to say

anything that isn't potentially embarrassing, right? Or fake. But we have accounts, okay, cool. We have lists, leads, and tags. We have stats, webhooks, all that kind of stuff. So,

end to end, I can build a lead list, launch a campaign, check stats, reply to inbox conversations, all from the terminal. Per our workflow rule, I always show the outreach copy sequences

for your approval before hitting start on anything. Okay, great. Okay, great. Show me the inbox messages that I have to reply to. And I'm just going to chime in. I'm not again, I'm not logged into

Heyreach. Well, I'm logged in, but I'm not on the interface. And really, it's just that simple. You just put in Heyreach CLI, install, get your API key, and it sounds that simple, but once you

get that all set up, I'm telling you like, this is this is the unlock. All right, that query pulled raw data. Let me filter it down what actually needs a reply. Last message from them, not you.

All right, so it's drafting it up. All right, so here's your inbox. We have 25 conversations on the latest page of 9,000, all right, conversations in the workspace where they replied last and

you haven't responded yet. High priority, real content, not just a nice to meet you. Okay, so we have Jared right here, who's basically asking an interested question. And so what Roz

did, she actually went through my inboxes and she filtered through all of the hey, great to connect with you, too, and all the fluff and all that kind of stuff. And she actually prioritized the

ones that actually need my attention, right? So, she's like, high priority, real content, like get back to these people as far as, you know, engaging, right? So, then we have another another

lead right here, complimenting on, you know, content, things like that. McKenzie, okay, sweet. So, we have leads that are literally replying to me and connecting and reaching out to say like,

hey, like they're waiting for my response. Well, this is where timing comes in, right? So, you can be like, yeah, let's go ahead and just engage with them, right?" You can then reply

exactly and it will automatically reply with a lot less clicks and types or anything like that. No, this is just a page of one of 100 results. The full inbox, okay, it looks like I need to be

getting back to some people. But, you get my gist here on being able to reach out as well as use it for inbox. Now, with campaigns, great. Now, are you able to create a campaign? And the thing is

is I know I can create campaigns, but let's see if we can actually demonstrate and go in there and create a campaign. Got back to me saying, "Yes, full campaign life cycle. HeyReach campaigns

create." Here's what that looks like in practice, what I can build. Create a fully configured campaign in draft status where we have name, sender account, slate list, message sequence,

etc., etc. Okay, update any piece here. We can start it, draft, resume, leads up to here, okay? Monitor. My guardrail per our standing rule, I build the campaign and sequence in draft, okay? I basically

want to verify for quality and accuracy. Walk me through the live sequence, okay? So, at least the sender account. Sure, let's let's set up a campaign. So, it's going to set up a campaign for me and

we're going to see what that actually looks like. All right, so it says, "Good, I can see your workspace. Before I build the draft, I need a few quick decisions since this is going live in

front of your audience." So, we have lead list, okay, we have different lists that I'm working with and then we can pull a fresh list from my TAM super base. You can also do Clay. There's a

lot of different, you know, lead sources where you're going to need to upload a list or and get it to actually do an outreach, right? So, we have sender accounts, okay, and it starts to do

everything from here. We're just going to do this. Let's go ahead and do a fresh pull from Superbase. And it's going to be for me, which is Brandon, [music]

and target the ICP for founders and CEO. And we're also going to say time zone is going to be PDT, which is Pacific. All right, so it ran through for quite a bit where my computer actually went in night

mode, but you can see right here as we have Superbase TAM. Okay, so we store all our leads on a Superbase for millions and millions of rows for any lead that comes across because single

source of truth for that. And from here, the company's table 99 target companies, cool. No actual people yet. Since HeyReach needs individual LinkedIn profile URLs, okay, so we started to go

into another tool that we're using, which is Prospect. So we're going to do a person search, okay, so we're trying to get some fresh leads here. Real founder CEOs coming back from Prospect.

We'll match against our Superbase TAM domains. Let me pull the full result, okay. 124 founders, all 124 pulled. Let's Let's consolidate. So you can see it kind of goes through here and then

what I actually live built, okay. We queried it, so we have some targeted companies, ran a real person search using Prospect, which is a great data provider. Pulled five pages, okay, so we

pulled a very small sample set right there. And from here, you can see where it's where I stopped, okay. I was midway through it and created copy. Okay, nothing has been sent or launched. Next,

create a HeyReach list. All right, draft a campaign. Yes. Yes, let's continue. While this cooks, another thing that I want to mention as well, which is kind of nuance, but I think it's worth

describing, is, you know, with all the LLMs that are coming out nowadays, we have some pretty massively capable LLMs, mainly Anthropic has Sonnet 5, you know, you have Fable, you now have Grok 4.5,

GPT 5.6. I think it's worth considering the use case for how you want to actually use the agent. Not all agents need to be on Fable. Not all agents need to be on Grok 4.5. But I will say one of

the common workhorse ones that I personally love to have it on is Sonnet, namely Sonnet 5, at least as of this recording, because even raw ones and a lot of the agents that we have, you

know, they're very commonly and very good workhorses. So I would, you know, recommend something like Sonnet 5 has been my favorite, but I will say that we've had multiple agents that do okay

on Grok, right? So, Grok 4.3 at least at the time was great, but Grok 4.5, we're still uploading or updating and testing it, but I can tell you Anthropic has always been the goat when it comes to

actual OpenClaw. So, from here, we're going to say, "Okay, let's create the list." All right, it's gone through. Okay. Hey, okay, so it's coming up with a draft here. All right, full

transparency on grounding a real funding stage. Okay, so here we go. Approve as is. So, let's just go ahead and check just to see if we have done anything when it comes to those campaigns. All

right, it has not yet created it. We're just going to say, "Draft the campaign as is. Then, I will have you add more leads down the road. I just want the campaign created

for now in status." Another nice touch is clearly it shows, well, eyeballs to know like if something was done, and then when it is done, it checks with a green check mark. I think that's a nice

touch. So, that way you're going in. And by the way as well, you can see we're in a thread, so it has full context around our conversation. Whereas if I were to say, "What LM are you running?" This

would be another way where I can actually Ross can immediately respond as well while I can continue continue the context of this one as well. So, we have right here, "I'm running Claude Sonnet

5, provider Anthropic." Okay, shows right there. So, then from here I can switch back and go. Okay, "Campaign created sitting in draft." Very good. So, we're going to go ahead and refresh,

and we're going to see Let's see what it is. There it is. So, Tofu founder CEO 726. Okay, seven So, we got right here, we have sequences. All right, wait 3 hours send message. So, right here,

"Thanks for connecting." Okay, "Put your GTM stack compounding more reps." This is awesome. All right, so then let's see if it types in here. Okay, "Saw company name is Past Growth Stage Mark. Here's

how you think. All right. So, this has completely filled out the whole thing. I didn't even do a single thing. You see out here right in front of me live. Well, as of this recording, you're not

live any longer. But, you can see what I've done this basically in real time to create a campaign in Haystack from start to finish. And then literally, I can just add leaves and have it respond to

messages. And I can even query every day. Another note, too, is you can actually have it every day remind you and say like, "Hey, you know, I've noticed this." Or you can instead up

basically it's called a heartbeat or cron jobs where you can set up, you know, triggers to have it throughout the day say like three times a day to say like, "Hey, you actually got a message.

Like, do you want me to respond?" Things like that. So, you're really leveraging automation and agentic workflows in such a way where it's all coming back to the chatbot, which is in this case Slack,

right? So, a lot of times even for our clients when we deploy an agent such as this, we have literally agents where on channels they will be talking to agents in the wee hours of the night or in

another country or while I'm sitting here doing other things like building or going, you know, enjoying time with family and stuff like that where there's they're literally getting work done and

we are collaborating with agents to actually do the thing, right? And then if something goes wrong or we need to do an additional context layering or capability such as a new CLI tool or

maybe an update, then that's where we come in obviously and help with that. So, that said, I mean, this is basically in a nutshell how you set up Open Claw from start to finish. Again, one of the

biggest things you're going to want to do is go to the single source of truth for whatever agent frameworks that you want to actually get to be familiar with. Consider how you set it up,

whether it's on the cloud, on a DigitalOcean droplet, or something similar, or if it's actually on your computer. And check out the open source repo that I have right here. And of

course, reach out if you have any questions. But, one of the biggest things here is we're just in a beautiful time now that we have never seen in our entire lives, which is being able to

leverage things like this to actually grow your business. And as you know, LinkedIn is a social media network where you can establish connections with real humans. And this is the biggest thing is

here you are watching this video. We're working on the computer, okay? We have the internet. You can work in a global capacity, but at the end of the day, you're actually connecting to another

human in order to solve a problem or just build a relationship, right? This is where using agents comes in a real context and real leverage because it can actually do a lot of things where some

things you just don't know and what you do know, you just always wonder how much better you can improve it, right? So, what I would say is just like I said, get to get be get familiar with OpenClaw

and Hermes. Definitely check out Hermes as well. As far as HeyReach is concerned, sign up, you know, it's basically automation platform as you know here you are watching the channel,

but get yourself familiar with the CLI to get it installed. Once you get that installed, then you can start to set up your outreach things like that. If you reached up to this point, I just really

appreciate you watching. Please like and subscribe and I'll see you in the next video.
