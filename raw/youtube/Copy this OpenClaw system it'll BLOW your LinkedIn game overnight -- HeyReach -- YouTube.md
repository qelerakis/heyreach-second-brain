# Copy this OpenClaw system:  it'll BLOW your LinkedIn game overnight

Source: https://www.youtube.com/watch?v=eiWVH5W5ICY

What's up, everyone? Brandon Charleston here. If you're running LinkedIn outbound through Haystack, you know the dashboard is great. But if you're like me, you want to go faster. You want your

agents managing campaigns. You want your data flowing without having to click through any tabs or logins. So, with that, I built Haystack CLI, a full command line tool that covers the entire

Haystack API, which gives your AI agents full control without having to log in anything. You have your campaigns, inbox, lead list, stats, all right from your terminal. And every single command

doubles as an MCP tool, which means your AI agents can run your LinkedIn outreach natively. So, in this video, I'm going to show you how to set it up and how to use it. This just takes all about 60

seconds to install. Let's go ahead and dive in. First and foremost, if you're not already familiar with Open Claw, definitely check it out or you might be still in the closet. I don't know. But

with that said, go to openclaw.ai and get yourself familiar with it. It is basically an AI agent where you can install it in any configuration you want, any chat app. You can put it on a

computer. You can put it on a VPS like Digital Ocean or anything like that. [music] And we are doing this as an agents as a service at top of funnel. So, we are deploying agents all day,

every day, and it is [music] definitely doing a lot of things, very, valuable stuff with businesses when done right. [music] So, I would just say check it out. Definitely check out the

documentation as well so you can get yourself familiar just by clicking here. And if you go to docs.openclaw.ai, definitely get yourself familiar with how to configure it, all of the, you

know, the manual stuff, reading the manual kind of thing. So, that way you're not going to need yourself in any scenarios that you don't want to be in, right? The next part here [music] is

being able to configure it with context and capability. When you give it context, you're actually telling it what [music] it needs to do. You're giving it an identity. You're giving it a context

around your business, right? So, if you're doing growth, sales, and automation, and things like that, you're going to want to give it as much context as possible.

So, that way it knows what tools that it needs to do. Then we give it capabilities, which is where this is where the fun part is. So, if you just go to Top of Funnel, which is our site,

I am always deploying new CLIs all the time, but specific to this [music] use case and video, we're going to go to resources, go to agent tool and CLIs, and then we're just going to scroll

down, and we're just going to click on Haystack. Haystack, basically, as you know, is an automation tool that allows us to scale your social network on LinkedIn. And I did open source it. So,

by all means, if you're developer and you see anything that could be used to improve it, please let me know or submit a pull request and we'll get it figured out. But I intend to open source just

like here to be able to know how people can actually use this better, right? So, we can just continuously share the knowledge and things like that. Very simply, all you need to do is just

install from NPM. So, if you just click on this, there's really just one command line, which is just this right here. And all I do is just copy it, and then you're just going

to go to your agent to be able to, you know, basically run it in the terminal. However you configured your agent, you're usually going to do this from some sort of

terminal base or a agent to set it up. Yes, you have agents setting up [music] agents, right? That's the thing nowadays. Sounds fake, but it's very real.

So, you're going to want to install it, and what this is going to do is actually going to install the code inside of its environment. So, that way, basically, a CLI tool is it gives it the skills,

which you could see right here, and it allows us to know exactly what API endpoints are around like Haystack, and then it's going to wrap them into a tool. So, that way it has the skills, it

has all the tools, and then it's effectively just going to call those tools with high accuracy. So, that way you're not running into bugs or it's not writing scripts and running into all

these edge cases, right? That's the biggest thing here. If you're not signed up for Haystack, by all means, sign up for Haystack. But you'll see this way with this resource here, it provides

insights around why you need it or when to use it, right? So, you can do a number of use cases, which is actually add campaigns, right? You can launch and manage campaigns. You can have access to

your unified inbox. >> [music] >> You can do lead enrichment and tagging, campaign analytics such as how are my campaigns performing? Anything you want

to do on the front end, you can do right from your agent, literally like inside Slack or Telegram or WhatsApp. However you're actually talking to them, right? As I mentioned, you have the install

right here, which this just means NPM install. This means globally, and then we're just calling Haystack CLI, right? And it's going to know what to do from there. If

you even tell your agent just to install it, a lot of times, actually, it'll do it itself cuz a lot of agents will just configure their own environment. But I would say it's up to you and it's at

your own risk. If you haven't installed it, it's hard to even know if it actually did and worked, right? It, [music] you know, 99% is going to work, but you just sometimes doesn't know the

configuration or it might not have the environment permissions to actually install something, right? So, that's why it's best to kind of surgically go into the back end. But you can install it

right from Slack where auto installs [music] itself, and then you can provide an API key. I can't say and recommend to do that, but I do know that it works and you can

do that. Just know the risks of when you post your API key and it gets tokenized >> [music] >> that you could be at risk. So, I always recommend just basically using it from

the back end. You'll get an authentication, right? It'll ask for API key. And then this gives all your agent campaigns, unified inbox, pretty

self-explanatory, right? So, these are just some simple use cases of create a prospect list, you know, etc., etc., and then this is exactly what it does. This is my intent here to show you. If I were

to prompt the agent and it does the things like what does it actually do, right? These are what you call flags. So, basically, you don't really need to know all that, but this is kind of what

happens under the hood, right? These are all just the very simple use cases. >> [music] >> And I'm basically just going to say this is a my trusted chief of AI staff, Eve.

And if you've seen Wall-E, it's one of our favorite movies for my myself and my family. We're just going to say, "Hey, Eve, how [music]

are my campaigns running with Haystack?" And you can just literally use natural language. You can even, it'll even monitor. I have Eve check my inbox every day to say, "Hey, you connected with

XYZ, you connected with so-and-so. You know, you want me to draft up a reply?" And I could say, "Yeah, draft up a reply." And then >> [music]

>> you just send a message and it literally fires off the messages for you. It's literally right from Slack. So, you could be, you know, out and about on your Slack messaging on your phone,

anything like that. But that's generally, that's how it works. It's pretty simple, right? So, no need to log in or anything like that. All right, perfect. So, I just said,

"Hey, Eve, how are my campaigns running with Haystack?" [music] And she says, "Here's your full Haystack rundown." Gives me all of my active campaigns, paused, finished, okay, things that I

need attention to, [music] right? And it gives me my acceptance rate. All good. And campaign is going through nicely, right? Let me put a little heart there cuz Eve's got a

little personality. Then we'll say, "What messages have [music] I received and who do I need to reach out to?" All right. And again, Eve knows context, she knows

our business, she knows how to use, she has the skills, right? It comes down to two things, context and capability. All right, perfect. And then we just said, "What messages have I received and who

do I need to reach out to?" Eve says, [music] "Here's your inbox breakdown. Need your attention, five people." Okay, these are people that who I have connected with, right? And she's also

saying routine here, no response needed. Okay, 275 unseen conversations. Oh, I need to do some catching up, right? "Want me to draft replies for the top five?" Yes, please draft replies

for the top five, but do not send [music] until I say good to go. All right, perfect. So, I just drafted up some replies. Basically, it's saying, you know, "Hey, Paul, start of the year

has been great, honestly non-stop." True story. And then we have other replies here. Okay, so this is very much drafting a reply, and [music] then she just says, "Let me know which one to

send or if any edits you want." And I can basically say, "Yeah, let's send to so-and-so, let's send to Mike, let's send to Paul." Anything like that. But I'm literally

controlling and doing Haystack actions on LinkedIn right from my Slack. That is exactly what I'm talking about here. This is this is the thing, right? And the I guess the big takeaway here is you

can literally be on Telegram, WhatsApp, Slack, >> [music] >> anything like that. And when you configure an agent such as Eve where you

have full context [music] on the business, everything persists, right? So, you back up memory, things like that. But now she has context [music] and capabilities of actually using

Haystack to connect with people and be able to send them [music] messages and manage and monitor campaigns, and we'll be able to save time and do a lot more productive

human things, right? So, that right there is basically how you install it using your Open Claw agent where I can literally use the CLI, which is inside of Open [music] Claw's environment, and

you can literally do like I mentioned as everything that you want inside of a Haystack platform. If you want to configure as an MCP server, you would essentially do the same thing except you

would do it within your harness like Claude code or cursor or anything [music] like that, and it would basically double as an MCP server with the same amount of tools. So, with that,

that's all for me. I just wanted to, like I said, just share, you know, what I created here with Haystack CLI because it works well for us. We need it for TOFU as well as the

clients that we work with, and I am open sourcing it and hope that you get good value out of it as well. As always, if you see good value, I would appreciate the share and the like and the

subscribe. And [music] again, I'll see you in the next video. Thanks for watching.
