# How I Get Unlimited Leads Using Claude Code + LinkedIn

Source: https://www.youtube.com/watch?v=9H18NMwXCvI

One of the biggest current crazes in go to market and really all of technology is Claude code, right? Claude has Claude code. And today what I'm going to be showing you is how you can use Claude

code to clean lists, build campaigns in HeyReach, enroll them into campaigns, and run LinkedIn outbound at scale from the terminal. And so, first, to get into this, what even is Claude code, right?

Hopefully a lot of people listening to this, and this is almost certainly the case, don't actually know what Claude code is. They've probably heard about it. They've probably, you know, you're

familiar with like LLMs, you're familiar with the Anthropic. What is Claude code specifically? Well, it's really, really simple. It is code installed on your computer locally, right, on your machine

in a way that it can read files, run commands. It can use tools you connect to it like HeyReach, right? And so, that's what we're going to be showing you today. What it operates off of is

markdown files, right? And so, essentially what happens is your computer locally, right, on your device stores these .md files, markdown files. That is basically a set of text

instructions, right? And so, it's a little bit more than a .text file in that it has formatting, so it has big, you know, headers and smaller headers and bullet points and all that good

stuff. But, this doesn't super matter. You don't need to know a lot about the files, right? If you want to go Google that, awesome, have a good time, but most of you you won't care. And so, what

we're going to do today is we're going to map out a strategy of a campaign, right, conceptually. We're going to use Claude to do it a little bit. We're going to build the campaign buckets and

the copy and we're going to put that inside of HeyReach, right? I'm just going to show you one example, um but as you see, there's sort of this branching logic that I'll talk about in a second.

Then we're going to actually set up Claude code, we're going to run it, we're going to create a campaign, load some contacts into it. So, hopefully that sounds fun. Now, talking

about our strategy first. So, the framework I use for finding message market fit is basically markets, like what is the broad bucket of companies that we're talking about, segments of

those markets, what are ways that we can divide those companies that meaningfully changes how we might talk to them. Then we have personas, who are the CEO of the problem XYZ inside of these companies.

And last, one is our angles or these arguments we're making to them. And so in this case, I have a bunch of family offices, a ton of these, right? Some of them we're going to disqualify. Um some

of them we're going to find the CEO of. Some of them basically some of them are going to have a CEO, some of them are going to be run by partners. And then we're going to disqualify a bunch of the

contacts we find, right? And then for the CEO, we're going to have a personalized campaign where we create copy based on what they do. For the blank, then we're also going to have a

blank connection request campaign. For the partners of these family offices, we're going to have personalized version and blank one, right? And so there's going to be basically four campaign

buckets, either blank connect request and then people do things afterwards or we're going to connect with a personalized message and then we're going to disqualify people that aren't

what we're looking for. Good. Going back to this. So if we wanted like the family offices with only a CEO, and we're going to do the blank connection request, right?

That's going to be this campaign that we're going to run through right now as an example. Right? So the first thing you would do is you'd come into HeyReach, right? You create start new

campaign. We're going to say blank CEO only. I create this campaign. Um we're going to create an empty list, right? List name is blank CEO only.

Confirm, right? Uh I don't have an exclusion list here. Let's say we want to exclude leads messaged by the same sender, right? Inside of HeyReach and then we also want to I'm I'm only that

one, right? So I'm going to hit continue. Now I'm going to build out this campaign. So in this case, it's going to be really really really really really simple. We're going to start with

a connection request. It's just going to be blank, right? So let me go back to this. I'm going to make it so we withdraw this after 14 days if they don't accept it, right? If after 2 days,

let's say, they haven't accepted it yet, maybe we'll go like their most recent post, right? And then 2 days later, we'll just end it, right? It's done. And then if they accept it, right? We'll say

3 hours later, we will go view their profile. 3 hours later, oops.

Hours later, we will then Actually, that's it. It will just end. Right. And so now we would connect a LinkedIn account, right? That would be our sender. I'm going to go back out of this

campaign now. And so you'll see that this exists. Right? Now, [music] we just mapped out the strategy. We built the campaign buckets. There wasn't

really copy, but you saw where the copy would be. Now we're going to set up Cloud Code, right? And so I purposely uninstalled it on this computer of mine, so I can go through this with you and

show you exactly what it looks like, right? And so honestly, what a lot of you should do is just do this. You say, "How do I install Cloud Code on my current computer? It is a

Mac Pro." Right? And so let Cloud do its thing. It's going to spin spin spin, right? We're going to be operating out of create terminal like this, right? And so

um I'm going to be doing something with this in a second. So this is it, right? The easiest way is I'm literally just going to take this. I'm going to terminal. Oops.

I paste it, and as you see, it's doing stuff in the background. So then start by typing Cloud in the terminal, right? And so then we can come into here. Shh. Okay. It's still installing. I'll let it

do its thing. Let me go back to this, right? And so basically I just added Cloud Code, right? So we have Cloud Code now to the terminal. The next thing that I'll need to do is I'll need to get my

Here Each MCP key, right? And so the way I would do that is I would come into Here Each. I'll go into my settings. I'll go to integrations. I would do Here Each MCP server. I'm going to create

this key. I'm going to delete the key before you see this video, so I don't care that you're potentially going to see it, right? I'll grab this. Shh. Let's see. I'm just going to add this to

here. So we'll say key. And then and then URL. And so going back to this, what's going to end up happening is I'm going to

add this address down here, and I guess it has my key. Oh yeah, yeah. This just has my key in it. And so, all I'm going to do is literally paste this into that MCP server once it's

done. Cool. Boom. Let's see if this works. I do not think it did. So, just 1 second. Boom. There you go. This is like a perfect mistake to make on camera. So,

I can't just post that URL in there. I actually need to I guess do this whole thing. So, let's see if this just works. Hold on.

Okay. New terminal window. Paste this in. I'm having an issue. So, I'll come back into here. Here. Cloud me. Will this work?

Hopefully that code will work. So, I'll run this. Now. Okay. So, now I confirm this set up properly. This should work. MCP add. We

went through this together. And now we are going to be successful. Boom. I love it. Okay. So, let me just make sure. Okay. So, dark mode. Let's see. Select

my login method. Let's description. Yes. So, this is going to pull up my Cloud account. Authorize. Authorize. Cool. Boom. Window closed. Pull this

back up. Enter. Cool. Yes. Let's see. Recommended settings for terminal. No, I'll do this later. Okay. Yes, I trust this folder.

Allow. Allow. Wow. Allow full access. Allow. So, we're going to allow it for everything for right now. All right. Now we'll say

/mcp. And as you see, uh yeah, okay, cool. Here each. Yeah, local MCPs. Here each. Perfect. So,

going back to this. Now we know that we have Cloud Code set up. We have Here each's MCP set up inside of Cloud Code. Sorry that took a second. Hopefully you learned something just like I did as

we're doing that. And now we're going to feed it a CSV, right? And so, what I'm going to do is I'm going to go in Oops. Actually, I'm going to say here, "How do I feed Claude

code my CSV to clean?" Okay. So, inside of Claude, we're going to run this. And then, we're going to say, "Clean up the file on my desktop called family off uh let's see

called investor family office leads. I only want the CEOs." All right, that did not work properly. Okay.

So, now inside of Claude code, what I'm going to do is I'm going to say, "Hey, read this CSV in the current directory for showing column names in the first three rows so I can see the structure,

then filter it only rows where the first person is a CEO." So, I'm going to let it go do its thing. All right, Claude's operating in the background, so it's looking at this file that's on my

desktop. It is interpreting what is on the file. It's reading through. Perfect. Right? So, you see we have chief executive, right? And so, these are from different family office. Do do Let's

see. Match count. Yep. Yep. Sh- Just say yes here. All right. And so, here we will now have this list that I just asked for. I'll pull into the screen. What you'll see is it's only the CEOs,

right? >> [clears throat] >> So, now I'm going to say, uh "Can you load those CEOs into the Heritage

campaign for blank CEOs?" Yeah. Cool. So, now it's going to go receive those campaigns. It's looking for them inside of Heritage. Oh. So, it didn't find it initially off of the like very

specific language I gave it, and so it's I I guess broadening the search here. Right. Yes. And so, in the background what's going on is Claude is doing all of the

work of taking our CSV, it's uploading it, it's mapping the columns, all of that good stuff. Right? And so, in a minute I'm going to be able to go into Here Reach. We're going to be looking at

the campaign that I just talked about. Okay, cool. [music] So, I need to go turn it off of drafts in order to load it. Just a sec. Okay. So, now I just set this campaign to be live. And so, thanks

to it being live, I should be able to run again. Please. And so, what's going on right now is uh okay, I see. Shh. Yep, same thing. And so, Claude is on my computer talking

through my systems to the web apps. It's talking to my system like file directory, right? And so, that's how it has a CSV that's on my desktop. Right? It's using Here Reach's MCP in order to

communicate with Here Reach. Yes. Boom. There. Shoutout Prospector. I guess we needed these people's LinkedIn URLs. And so, now we're enriching those, right? And again, this is the benefit of using

tool like Claude Code and [music] having MCP servers connected to it is we can have one single place [music] that we're commanding all of this work out of, right? Just like I am right now. Um this

is technically interacting with Here Reach, Claude Code, LinkedIn, Prospector, my computer itself, right? And so, there's a lot of different factors to this going on. [music]

Perfect. And so, this just told me like, "Hey, I found four of the seven people um using [music] the Prospector call." Some of these people probably just don't work at those companies anymore,

honestly. Nice. Great. And so, these people were added [music] to the campaign. And so, what I should be able to do now is come into here.

I'll go to lead analytics. Let me refresh [music] this. Oh, okay. Cool. Okay. These leads are still getting added in, I guess. Yeah, perfect. Okay. So, see, now going

into this list, here is those founder CEOs inside of those family offices. We did all of this purely off of Claude Code. A little bit of interaction with these other tools, a A of that was just

to show you all how this works. But this workflow is extremely powerful because you can use the same thing to launch email campaigns. You can use the same thing to create content. Working out of

the terminal, right? And becoming comfortable using commands like this. I mean, you saw me make a couple of mistakes, but you saw me get through it, right? This took like 15 minutes. No

problem. Super easy to load. This is the future Heyreach is building to enable stuff like this. I'm super excited to bring videos like this to you. If you have any questions, please reach out.

Again, my name is Calvin Kespere. I'm founder of The Deal Lab. Thank you. If you want to run a setup like this for yourself, you can get started with Heyreach absolutely free. All you need

to do is go to heyreach.io, sign up for yourself. Pick the plan that suits you best. You can get unlimited senders. The MCP server is included in the plans. If you have any at all, please feel free to

reach out. And if you want to see what else you can do with Heyreach, go ahead and watch the video that's about to come on your screen right here.
