# Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)

Source: https://www.youtube.com/watch?v=5Ru-r0-ca3c

Let me show you something cool. This message right here, fully personalized, referencing the most recent company news, their integration with clay.com, and one unique contact level insights.

And all of that's generated inside of Clay using just one enrichment. And of course, pushed automatically into a live Heyreach campaign literally just one click. No need for any sort of CSV

exports, no need for copying and pasting any needed information. In the next few minutes, I'll show you how to build this exact system completely from scratch. If we haven't met yet, my name is Tim

Jacobson, and I'm the founder of B2B Boosted and Unlock Clay. Over the last 3 years, I've helped hundreds of founders, agencies, and go-to-market teams to implement Clay, including both a mix of

email outreach and automated LinkedIn outreach as well. And in today's video, I'll show you exactly how you can connect Clay to Heyreach so that you can send truly personalized and relevant

LinkedIn messages at scale. And by the way, don't forget you can always use the timestamps at the bottom of the video to skip over to the parts that you're the most curious about. So, today's video

will cover the following five steps. The first step will be connecting Clay to Heyreach so that the two platforms can talk to each other and so that you can add leads to campaigns seamlessly with a

click of a button straight from Clay. The second step will be all about how you can create a good campaign structure inside of Heyreach before then moving to step three, where we will be generating

a personalized LinkedIn message right inside Clay before in step four then sending across that message from Clay into Heyreach. With the end goal, of course, being step number five, whereby

we can just do some manual quality assurance to make sure that every message looks like we want it to look, and then we can seamlessly launch the campaign inside of Heyreach. Anyways,

enough talking. Let's jump right into the deep end. As I just mentioned, the first step will be all about connecting Clay to Heyreach. So, for this part, it's pretty straightforward. All you

need to do is head into your Clay account, and it should look something like this. As soon as you're inside of your account, just head into your settings in the bottom left-hand corner,

and over here click into connections on the left side of the panel. You can then click on add connection and search for Heyreach as the tool. In this case, you should see Heyreach pop up with a

beautiful logo on the left-hand side over here. And then, as soon as you click into Heyreach, you should be able to see that you can name the connection and then add your API key straight from

Heyreach. So, for the purpose of this, I'm going to keep it simple. I'm just going to call this Tim's API key test. And all we need to do now is just head into Heyreach,

click into the settings icon in the bottom left-hand side of the panel. And over here, after you click into settings, you should be able to see integrations. Inside of integrations,

the second option towards the top should be the Heyreach API, and all you need to do here is click on get API [music] key. Over here, just make sure to click the clipboard sign so that you can copy the

API key into the clipboard. And please remember to treat your API key like a password or like your credit card number. In other words, don't share it with others because you don't want

people to have access to your tools like Heyreach in this case. So, all we need to do is copy the Heyreach API from within Heyreach, go into Clay, and where you added your name to the connection,

all we need to do is click on save and click on test account and save. And you should be able to see that within a couple of seconds, you'll just load up for you and say that this connection was

established. You should now be able to see that this is your connection over here. And the best part is, you only need to do it once. After this is set up, that means that automatically you

can call Heyreach directly from Clay, and I'll explain in a second how we pull this off the rest of the steps. But for the time being, give yourself a tap on the back. You've done really, really

well. You've already connected Heyreach to Clay, and we can now move on to step number two, which is creating a campaign inside of Heyreach. For the purpose of this, it's going to be fairly

straightforward. All we would need to do is head into our Heyreach account and make sure that our LinkedIn account is connected. Now, for the purpose of this one, I'm going to assume that you've

already connected your LinkedIn account. If you have not connected your LinkedIn account to Heyreach, just do me a favor. Go click on the second link in the description down below underneath the

video, and there you will find a tutorial which shows you how [music] to use Heyreach, and it will teach you how to connect your LinkedIn account to Heyreach as well. And as soon as you're

inside of your Heyreach account, assuming that your LinkedIn account is connected, [music] all you need to do is head into the campaigns tab and click on start new campaign in the top right-hand

corner. For the purpose of this one, I'm going to call this sponsorships campaign because I'm actually looking for a sponsor for my newsletter right now, so I'm going to call it sponsorships

campaign, and I'm going to click on create. So, over here on the right-hand side, we might as well just tick all the exclude options so that we exclude any leads that have been contacted in other

Heyreach campaigns, any leads that are messaged by other senders inside of our workspace, and any leads that have been contacted by us in the past. And for the purpose of this, we can click on create

empty list. I'm just going to call this test and click on confirm. And this way, if we click on continue over here, we can now build out the actual [music] structure of our Heyreach campaign. So,

let's just zoom out for a second. What we're trying to do here is create a campaign inside of Heyreach. So, in other words, we want to add a series of actions that will be automatically

performed on our behalf using Heyreach on LinkedIn. So, things like viewing a profile, sending a message, sending a connection request, and so on. So, for the purpose of this, all I'm going to

start with is clicking on the add action button. And over here, the first thing that we would typically do before sending a connection request is view someone's profile. So, in this case, I'm

going to view a profile, and in 5 hours after that, I'm going to click on five over here, switch from days to hours, and click on save. And after 5 hours, let's say, typically I would follow the

profile of a person, and then within day after that, I would most [music] likely send a connection request. And over here, it will offer me to add a connection request. And from my

experience of using LinkedIn to generate leads over the last 4 years, adding a connection request does the opposite to what we intend it to do. So, in other words, I don't recommend you adding a

connection request because most of the time it means that it requires the person to read thoughtfully to click on your profile and review your profile and see if it's worth connecting with you.

So, I wouldn't overthink it. I'm going to click on X over here, and we can see that already we created the skeleton structure of the start of the campaign, whereby we're viewing the profile,

within 5 hours we're following that individual on LinkedIn, and then within a day after that, we're sending a connection request. On the left-hand side over here, we should be able to see

that it's basically giving us the option of within 5 days if the prospect does not accept our connection request, what do we want to do? In this case, I'm going to click on add an action, and I'm

going to like their post. Of course, in some cases this may not be that useful, but for the time being, I'm going to like their post. Then, within 5 days after that, if they still don't connect,

I'm going to end that campaign in case if the connection request is still not been accepted. But on the right-hand side over here, if they have accepted the connection request, I recommend to

not pitch slap them straight away. So, what I mean by pitch slap, I'm sure you understand. A lot of the time you've probably been in that position where you just accept someone's connection request

thinking that it's just pure goodwill, someone just wants to connect with you. But little did you know, they're trying to actually pitch something to you in the messages. So, in this case, I'm

going to give them a 3-day break and click on save, and then after 3 days, I will then send them the initial message. So, for the time being, I'm going to click on add action, and this is when I

can select send message. And I'm just going to put in placeholder over here in both cases. And don't worry about this because later down the line I'll put show you how we can spice up

this message. For the time being, it will just be a placeholder, quite literally. We can also add different message variations later down the line. So, if we click on add message

variation, we can run AB tests on the messaging as well. And for the time being, let's say if within a day the first message was not replied, we may want to click on add action, and in that

case, we may want to send another message. And again, I'm going to call this placeholder. And then, let's imagine for a second that within another 4 days or so, they don't accept your

message, then we're going to try one last time with a third consecutive message that we want that we're going to send to them. So, in this case, I'm going to call this placeholder once

again. So, in a nutshell, what we've done over here so far is that we've built out the skeleton structure for the campaign, and that's step number two of this five-step process that we're going

through in order to push leads from Clay into Heyreach. And for the purpose of this one, now that we are happy with this, after this series of actions ends, all we need to do is just click on end

over there so that we can see that this ends everything. And one thing that I very much recommend for you is just to type in placeholder into all the messages so that it doesn't give you an

error, and then going forward, you can now click on continue. Now, next up, all we need to do is just select the right sender from who we want to send out this Heyreach campaign from. So, in this

case, we can either tick multiple senders or just tick your own profile. And in this case, you should be able to see the daily sending limits here. So, my account will be sending 15 connection

requests, 20 messages, and [music] a maximum of 20 emails per day. Then after we're happy with that, we can click on continue, make sure that we are sending this campaign in the right time zone.

So, in my case, I live in London, so I'm going to be sending it in GMT time. I'm going to be sending it Monday to Friday because I hate working on weekends, and I don't want anyone to [music] reply to

me on weekends as well. So, by the end of this, all we need to do is just click on continue, and then click on resume, and then this will automatically trigger the creation of the campaign. And then,

if we go back into the campaigns tab, we can now switch off this campaign for the time being since we don't have any leads in there. We don't [music] want it to start running just yet. So, congrats. By

the end of this step, you would have already created the campaign inside of Heyreach. And that means that we've done 80% of the heavy lifting, and it's just now a matter of us generating a

personalized and relevant message inside of Clay that we can now push from Clay [music] into Heyreach. All right, now comes the really fun part. And step three of this process is to generate the

personalized message as I just mentioned. However, for a lot of us, this may be the toughest part of the process because in order for us to generate the message, first of all, we

need to find a list of companies that fit our ideal client profile, that potentially qualify as a good fit for our product or services. And secondly, not just the companies, we also want to

identify the ICP prospects, the folks that fit our ideal client profile based on the job title, the industry, their time in the role, and anything else that's relevant like a sales trigger,

maybe they're new in the role, or maybe they're the owner or the founder, and for whatever reason they're craving solution now. And this is the hardest part because how do you actually go

about sourcing the right list of prospects and the right list of companies [music] in order to power that outreach. So, for the time being, I'm going to explain a bit of theory, and

then I'll show you how we can pull this off inside of clay.com. So, essentially, the first step, as I just mentioned, is building a company list. Since we're going to be messaging prospects on

LinkedIn, all we basically need is just their full name and their LinkedIn profile. Most folks out there are using a super expensive legacy B2B data provider like ZoomInfo, Cognism, or

apollo.io, for instance. However, my experience with these bigger providers, the big boys in the industry, has not been great. So, for that reason, I'm going to tell you some of the hidden

gems and some of my favorite tools to pull off the company list building and the prospect list building. So, in my case, there are three main tools that I can push you towards. The first tool is

called prospero.io. If we just log into prospero.io, on the left-hand side, we should be able to see it's very similar to LinkedIn Sales Navigator, if you used that before, or it's very similar to

other conventional databases like apollo.io. So, all we need to do over here is just filter for the relevant industries, relevant employee head counts, the locations, and based on

that, we can find the list of companies. We can even filter based on technologies, funding rounds, revenue, buying intents, or if these companies are hiring for a specific set of open

roles. And by the way, this is not just on a company level, also you can find people directly working at a set list of companies, and again, you've got plenty of filters over here. And then, let's

imagine for a second that we're going after and we're going after founders that are based out of the US market. Right now, we found us a list of over half a million prospects. In this case,

all we need to do is just click on apply, and then over here, we can just click on push to and straight away push it into Clay by clicking this button, and it should be pretty straightforward.

So, that's the first tool that I very much recommend called ProsperO. The second option that I recommend is a tool called AI Arc. And if you haven't heard of AI Arc, most of my friends that are

in the Clay agency space right now have switched to AI Arc from some of the bigger providers in the space. And again, he has really good company search filters, people search filters. It does

all sorts of other cool stuff like company lookalikes, people lookalikes, and a bunch of other things, and it comes at a fraction of the cost of other providers like apollo.io. So, I hope by

sharing this information, I gave you a bit of inspiration on some tools that you could use in order to build your company lists or the people lists that you can then import into a Clay table.

So, regardless where you get your company level data from or your people data from, all I expect you to do is head into your Clay account, click on new, click on workbook, and over here,

you'll give you the option to import from CSV, and I'm sure you're familiar with CSVs. So, for the purpose of this video, I'm going to give you the example of me scraping this list of companies

from the Clay website. And this is basically every single data provider that Clay has integrated within the platform. And the idea behind this campaign for me will be to reach out to

every single one of these data providers and beg for a newsletter sponsor sponsorship for my Clay Cult newsletter or for my wider Tim Jacobsen newsletter. By the way, you can subscribe to that.

The second link in the description down below will also feature a bunch of resources like my newsletter links as well as the guides to how to use some of the tools [music] that I just mentioned

like ProsperO and AI Arc as well. So, go check out the second link in the description down below. And essentially, all I'm going to be doing here is just using this file. So, I'm going to

download it from a spreadsheet in CSV format. I'm going to just drag and drop it into Clay. So, now I should have a list of companies that I want to reach out to via LinkedIn.

Okay, so by now, we have just imported all of our companies or prospects into a Clay table using the CSV. In my case, you can see I only have the company names, the functionality of the tool,

which is quite specific because I want to mention that when I reach out to the prospects. And then on top of that, I have the enrichments that are available within Clay from all these data

providers. Of course, this is contextual because this is mission-critical in order for my outreach to work and in order for me to find that sponsor of my dreams.

However, one super depressing thing about this Clay table right now is the fact that I have just company names, but I don't have company websites. So, in order for me to find the website of all

of these companies in the first place, all I would need to do is click on actions in the top right-hand corner, and then type in Claygent. And Claygent is the AI web researcher within Clay

that has access to the internet, and it can basically perform such tasks such as finding the website of a company. So, in this case, I'm going to click on Claygent, and over here, if I go into

this generate tab, I'm going to say the input is the company name. The company name equals, and then I'll use the forward slash and select the company name to infer that's, you know, the

company name is in the column on the left-hand side. And I'll say, "Based on this, find and output the website URL and nothing else." And after that, I'm going to click on the generate button so

that automatically this prompt can be improved by Clay for me completely for free. And whilst I turn over here with beautiful sunlight coming in from the outside, you can see in the meantime,

the prompt has been generated, >> [music] >> and Clay will always upsell me to the most expensive model, so the Clay Neon model. In my case, I want to switch this

to GPT-4.0 Mini because it's a lot cheaper. And all I'm going to do now is just click on save and don't run, and just make sure that I'm able to [music] find the website of the company. So, in

that case, I'm going to just click into the first five rows just to make sure that the website of the company is found correctly. And you can see over here, within a couple of seconds, the websites

of all of these companies have been found. So, for example, TrustRadius, SimilarWeb, Semrush, ZenRows, Lead IQ, they have all been found within seconds. And this is what we'll call like an

enrichment, whereby you only have the company name, and we want to find the company website, which we've done successfully. So, all I'm going to do is just click on rename column, and I'm

going to call this step one, find website. Now that we have the name of the company and the website, all we want to do next is find the names of the decision-makers of the company. So, in

this case, I'm going to click on actions again. I'm going to type in Claygent once again. And for the purpose of this, I'm going to write a very quick prompt as well. So, I'm going to say the input

is the company name and website. Based on these, output just the full name and nothing else of one person that could be my main point of contact to the company for any sponsorship, partnerships, or

marketing collaboration requests. And output just the full name of one such person as well as their LinkedIn profile, and make sure that there are just two outputs. The first output is

the full name of the person, and the second output is the LinkedIn profile URL of the person. After I just wrote a rough prompt like that, I can just click on generate again, and right away, Clay

should be able to generate the prompt for me. So, let's give it a couple of seconds to generate in the background. And you can see that Clay just generated a really, really long and impressive

prompt for us. In this case, I'm just going to switch the LinkedIn profile URL from text format over to URL because that's one thing that Clay sometimes gets wrong, and the model is going to be

switched from Neon over to 4.0 Mini. Next up, all I'm going to do is click on save and don't run. And now, I'm going to click into the play icons over here just so that I can see some of these

rows play out to start with before running the entire table. And again, I'm going to rename the column just to stay nice and hygienically clean over here, and I'm going to say find decision-maker

name. Now, at this point, you may be asking, "Why don't you just use one of the typical enrichments, the typical actions inside of Clay like find people, and basically filter for the people that

way?" And yes, you could probably do that by just clicking on find people over here and selecting the relevant job titles and the relevant experience. However, if I'm totally honest with you,

as someone that implements Clay for tens of businesses on a monthly basis, the find people enrichments inside of Clay are not going to be as up-to-date and as good in terms of quality as just using

Claygent in such cases. And you can see, within just a couple of seconds, the output is populated over here with the full names of the main point of contact for sponsorships of these companies

alongside their LinkedIn profiles. So, in this case, we're looking at Natalia, for instance. If I click into her profile over here, I'm taken straight to her profile. I can see that she works at

Semrush. And so now, I have not only just their full names, but also I have their actual LinkedIn profiles, which I can then use for the next step. All right, so let's just take a quick step

back and zoom out. The first step was building a company list. We then found the decision-makers of the company using the Claygent enrichments. And now, it's time to write a personalized message to

each one of those folks that we want to reach out to. For the purpose of this one, I'm going to try to keep it as simple as possible. There are a lot of different ways that you can generate

personalized outreach messages inside of Clay. However, from my experience, the most beginner-friendly one and the most effective way to do that is using the Twain enrichment. So, in this case, I'm

just going to click on actions, and I'm going to type in Twain, and you should be able to see that over here, it says generate outreach with deep research. So, I'm going to click into that. So,

all you need to do over here is head into Twain, create an account, and you can do that on twain.ai. And then over here, just obviously accept the terms and conditions and click on create

account. And I know it sounds like we're taking a lot of steps here. However, I promise you it'll be worthwhile when you see the copy that Twain is able to generate for us. Over here, to start

with, Twain will ask us to upload some examples of leads. So, in this case, all I'm going to do is head into the Clay table, grab a couple of LinkedIn profiles of the leads over here, [music]

and I'm going to copy and paste them under the add manually option. So, I'm going to click on plus, and then let's just add two prospects really quickly into Twain. After that, I'm going to

click on continue and over here it will ask me to describe my campaign idea. Don't overthink it. I'm sure you have some sort of campaign idea. In my case, because I think I'm really cool, I'm

going to use this tool called Whisper Flow to just speak out my idea and it will just basically transcribe it here because I can't be bothered to write this all out manually word by word. So,

here is how I'm going to pull this off. My name is Tim and I run a newsletter with over 10,000 monthly subscribers across LinkedIn and emails and I already partner with some big tools [music]

in the ecosystem and I'm currently looking for new sponsors for my newsletter. This campaign's goal is to reach out to the main point of contact at my chosen companies that already have

a native clay integration, which means that they're already appealing to the target audience that my newsletter is catered for and my goal is to see if there is an appetite on their side to

sponsor my newsletter or any of the content that I'm putting out across my social media channels. So, you can see straight away this prompt has been typed up over here and in this case I'm now

going to click on continue and essentially for the purpose of this it will just ask me for what my website is. I'm going to type in unlockclay.com. By the way, if you want to learn clay from

beginner to intermediate level, you know where to go. At the bottom over here it will ask us to describe a target job title that we're reaching out to. So, I'll say something like head of

sponsorships, head of marketing, head of partnerships because I assume that's the kind of persona within these software companies that they works with creators like myself. And then after that, I'm

going to click on generate campaign. Now, Twain will think for a couple of seconds. You could see the in the background it will just load for a couple of seconds. By the way, if this

video is valuable so far, please drop a like and drop a nice comment and double check that you're subscribed to the channel because look at me, I'm literally sunburnt, sat in like a winter

garden trying to film this tutorial from a second take. And that's not to mention that this is a real campaign that I'm going to be sending out. I'm not just recording it for the sake of this video.

Okay, so we should now be able to see that inside of our Twain account it's already automatically generated three emails for us, but obviously with HeyReach we don't want to generate

emails, we want to generate LinkedIn messages that sound good. So, for that all we need to do is just scroll to the bottom over here and click on add step. And over here we can choose the channel

to be LinkedIn and in this case >> [music] >> we want the use case to be an introductory message. And then after that, we can click on add step.

>> [music] >> So, for the purpose of this, I'm going to show you how you can set this up inside of Twain for yourself. So, for the time being, I'll just teach you the

principles behind how to pull this off. And of course, you would need to apply this for yourself. So, in this case we just added this step, which will be the LinkedIn step at the bottom. And if we

click on the edit framework pen icon over here, we should be able to see that over here Twain is able to basically generate a personalized and relevant message based on whatever kind of

context we feed it. So, in this case I'm going to wipe all of this out and I'm going to show you how I can go about generating [music] that copywriting completely from scratch. So, in this

case, let's say we want to just greet the person we're reaching out to. So, I'll say something like hi recipient name and going forward we'll be using these curly brackets whenever we want

Twain to research something and make sure that it outputs some messaging instead of the curly brackets. So, as an example here, I could say something like hi first name, I keep on hearing my

Unlock Clay students rave about and then if I put in brackets enrichment name and functionality, then it will just basically replace this with actual details from here because remember I

have the details on the enrichments and the tool functionality, right? Uh so, it should pick up on that pretty easily. And of course, on top of that you may want to add some relevance, you may want

to add a bit of personalization to the opening line. So, in this case we can say something like and I noticed that and then over here we just put observation about the time in the role,

if the person is new in the role or any sorts of other research or insights that we have about the person that suggests that they may be in the market

looking for creators or partnerships with newsletters or clay related communities. And after just a couple of seconds of prompting just the opening line here, if I click on update step, I

should now be able to see how Twain generates a personalized message, which uses all of our context and all of the research that we put in curly brackets over here. And you can see in this case

from Natalia it generated this message saying hi Natalia, I keep on hearing my Unlock Clay students raving about the Semrush integration for connecting prospect data with search and traffic

insights and I noticed that you lead market research and partnerships at Semrush and that the enterprise partner program from October 2025 puts more weight on co-marketing, which suggests

you might be exploring more sponsorships with outbound heavy audiences that already build campaigns in clay. Again, this is really good, right? From the first prompt, it just came up with this

message and as you just saw, I didn't even prepare this prompt in advance. >> [music] >> So, if you want to research a specific thing about like the time in the role,

the name of a colleague or you want to like acknowledge a bad review or a good review that this company has or this prospect has on Glassdoor, Tripadvisor or whatever

other website, >> [music] >> you can call them out with that in the opening line. So, I very much recommend that you keep it nice and short. In this

case, at the bottom you can also add some instructions. So, I'll say keep this short and sharp. [music] Each sentence no more than 12 words. And the other thing with LinkedIn, just

remember that it's supposed to be a networking platform. So, we probably want to make the tone a bit less formal and we want to space out the messaging. So, in this case I will just keep this

all in one string of text where it's like hey first name exclamation mark and then just a quick opening line, which obviously is just like a nice little compliment over here and then after that

a quick observation followed by a quick open question, which hopefully like lubricates and starts a conversation. And look, I've run all sorts of automated LinkedIn campaigns in the past

and one thing that I can tell you for sure that nothing beats the structure of this type of message, whereby we start with just a greeting and an opening line, which is relatively personalized

and or relevant following on with some sort of observation or trigger that shows to the prospect that you've done a tiny bit of research and then you can follow up with some sort of open

question. The main idea behind [music] asking a question is first of all to initiate a conversation and to encourage like a two-way conversation rather than you just trying to pitch slap the

prospect straight away. And preferably that question should prompt the prospect to be slightly curious about your product and or service. And you may have heard of this concept of poke the bear

questions. So, for example, instead of you saying >> [music] >> hey, we have a payment gateway that can accept payments in over 20 currencies,

instead you can create a poke the bear question that that probes the prospect to think about their pain points. For example, saying something like how do you know that you're not being

overcharged with your exchange exchange rates and transaction fees on your current transactions with Stripe? And you can see the difference between this is one message is very transactional,

very sales heavy and it just makes you not want to reply to it and the other message suggests you to think about the problem and based on that it pushes you to logically think hey, I probably need

a solution to this problem and typically this is where the company comes in that's sending us the poke the bear question. And by the way, for the purpose of this, you can go into ChatGPT

and just feed it this magic prompt, which I will be giving away as the second link in the description underneath the video and it basically trains ChatGPT on what a poke the bear

question is and then after that we can just feed it some context on your business and based on that it will generate some poke the bear questions for you. So, in this case I'm feeding it

some context on my newsletter and then based on that you could see it generates some poke the bear questions at the bottom here. And something like this could be cool where you say something

like how do you know that operators building the workflows in clay are even aware your tool integrates with it? Or something like this, how do you know that the clay nerds inside of my

community are using your enrichment over your direct competitor? >> [music] >> Right? And it would be pretty cool if we can name drop a direct competitor. So,

and I totally realize that I went on a slight tangent there, but the main idea here is to click on edit framework and to add some sort of question [music] at the end of this initial message. And in

my case, it's very important to ask a qualifying question right away. So, I'm going to be super direct here and say curious, do you sponsor YouTube videos and or newsletters? Question mark. And

I'm going to click on update step and I should then be able to see that the message gets generated at the bottom over here. So, we can read it again. I keep on hearing my students rave about

the Semrush integration. I noticed that you work with market research plus your enterprise partner program and content sponsorships. And on top of that, your Semrush enterprise partner program, you

know, stands out. You're likely fielding more collabs and creator requests than before. Curious, do you sponsor YouTube videos and or newsletters? Now, in my opinion, just sending that one opener in

most cases could get a reply. However, if it doesn't, we're going to click on add step again and in that case we can just select LinkedIn and then select follow up and then we can just select

the auto framework and then just click on add step. We can make it super short as well just to make sure that we're not [music] wasting too many characters and so that it's it's a lot easier to read

inside of prospect's inbox. And then I'm going to click on add step and you should be able to see that the follow-up message to that is generated automatically. [music] And you can see

the beauty of Twain is that it really knows your product inside out assuming that you share a lot of information about your product over here. And this follow-up message is pretty good, so

I'll just continue by clicking on add step again with another follow-up and I'm going to make this really short as well and then click on add step again. >> [music]

>> And for the purpose of that, we should now have three consecutive HeyReach messages generated over here, which we can then generate natively inside of clay. So, inside of clay as a quick

reminder, all we need to do now is click on actions, type in Twain and as soon as we see Twain pop up over here, all we need to do is just copy and paste. And inside of Twain, all we need to do is

just head it over on the left-hand side where it says campaigns, click on copy ID, head back into our Clay account, and then over here we're able to copy and paste that campaign ID. And the only

thing that we need to pass through is the LinkedIn profile of your relevant individual. And more than that, over here where it says prospect extra info, we can just map some of the columns that

we have in the existing data set. So, I'll say something like, here is what the tool does. And then I'll just select {forward-slash} [music]

tool functionality. Here is the enrichments that it offers [music] inside Clay, and then I'm going to just select the enrichments. And then for the

purpose of this one, I'm then going to just click on save and don't run. You can see that it will cost you 12 Clay credits per row, but I guarantee you they'll be worthwhile after we check the

kind of quality of messages that's being generated. So, over here I'm just going to click into the first five rows, and we should be able to see that for the first four people where we have their

LinkedIn profile, it'll say queued, and it'll basically automatically call Twain over here, [music] and it'll automatically basically pull this copywriting that we've just applied

inside of Twain, and we should be able to see it reflected inside of Clay within just a couple of seconds. In the meantime, I'll take my time to rename this. So, I'll say step three, Twain

copy generation. And you can see straight away it says sequence generated. So, where it says sequence generated, we can click into messages. And this is the reason that I absolutely

love using Twain alongside HeyReach, because if you click into the persona, you can see what persona this fits. You can see all the messages that have been generated. So, these are all six

messages, including three emails and three LinkedIn messages over here. So, not only can we use this for HeyReach [music] outreach, we can also use this for SmartLead outreach as well, or

Instantly, if you use any of these tools for email automation at the same time. It also provides you with research insights, both on a person level, on a company level, and with some basic other

research factors over here. And >> [music] >> each research factor has a reference as well. So, if you ever want to manually double-check and make sure that the

research that Twain has done in order to generate the email copy. And if you ever want to just check the references to make sure that whatever things we use as research inside of our messaging is

correct, all you need to do is just click into references, and it gives you the URL, so you can click into it and just read this article for yourself, so that you're up to speed on all the

insights about each individual prospect and company. So, you can see all of those over here. And more than that, it even generates subject line for you [music] if you're sending an email. And

more than that, it has the warnings over here in cases when Twain thinks that this person does not actually fit your ideal client profile. So, for the purpose of this, I know that messages

three, four, and five are the three messages that we'll be sending via LinkedIn, because they're the back of this Twain [music] steps over here that we have generated. So, I'm just going to

click into the messages. So, message, and I'm going to click [music] on add to column. So, I'm going to do that for this one as well. So, message two, create column, and I'm going to click

into message three >> [music] >> and create column as well. And you should now be able to see that this fully personalized LinkedIn message has

now been generated, whereby we open up with recent news insights that are symptomatic of this prospect being on the lookout for a solution that they're offering. So, here we are. Up to this

point, we have generated a series of three separate messages inside of Clay using the Twain enrichment. And if we take a step back for a second, we've already done all of these fun steps,

like finding the decision maker names, enriching their LinkedIn profiles, writing the personalized message inside of Twain. [music] And now we're onto step number five, which is finally

pushing those leads into HeyReach. This is the simplest part of the process. All we need to do now is click on actions in the top right-hand corner, type in HeyReach, and we should be able [music]

to see where it says add leads to campaign. In this case, we just need to make sure that we select our API key and select the relevant campaign. So, in my case, it will be [music] the

sponsorships campaign that we've just created. I'm going to select the LinkedIn sender's [music] account. So, in this case, it'll be my own account, so I'm going to select my own name. And

now we just need to be very careful with the way that we map the field names. So, in this case, the first name we can map from Twain, because Twain typically does the persona-level research. So, [music]

if we go into research person, we should be able to see first name, and we should be able to see last name. [music] So, if we just type in last name. And the main things that we need to send across into

HeyReach is the custom fields at the bottom. So, the way that we'll do we'll go about this is we'll click on custom fields, we'll click [music] on add a new custom field name and custom field value

pair. We'll call this message one, message two, [music] and message three. And then all I'm going to do is just use the {forward-slash} in order to refer to these columns, and I'm going to transfer

them one by one from Clay into HeyReach. So, in this case, I've just selected all three messages, >> [music] >> and now I can click on save and don't

run. And again, just click into the first cell just to make sure that the lead has been added to our campaign. We can see that now it says added to campaign. So, this is the perfect time

for us to head into our HeyReach account, into that exact campaign. And since we add that data right from Clay already, we can now click on edit campaign, head into the branches where

we've got all of this lovely stuff here. And then where it says send a message, we can then replace the placeholder with message [music] one. And only in exceptional circumstances, you may need

a fallback message. So, I'll just say, "Hi, how are you?" in the fallback message, just because, you know, I I don't want to just leave it as a placeholder here. And then I'm going to

click on save. And then the same thing for the second message, I'm going to click on send message, [music] and then over here just select message two. And then here I just need to think of a

fallback message. So, I'll say something like, "Heard good things [music] about your Clay integration. Do you have a creator program?" {question mark} and then I'm going to click on save. And

then the same thing for message number three, I'm going to again just select message three. Worth noting that these message one, message two, and message three custom variables will only be

visible inside of HeyReach after you transfer something from Clay. So, that's why we transferred this one lead already. And in this case, I'm just going to have a fallback where it's let

where it says, "Let me know." and I'm going to click on save. And then I'm good, I can click on continue, continue, [music] continue, and then we can resume the campaign. At the point at which

you're 100% confident in this campaign, all you need to do is just click in the top left-hand corner, select all, and then click on actions and run all the rows. Now, you probably don't want to be

manually adding all of these leads into a HeyReach campaign every time, >> [music] >> and you don't want to always have to click on actions and type in HeyReach

and go through that process all over again for every new campaign that you set up inside of Clay, right? In order for you to save this as a template, all you need [music] to do is just click

into the add lead to campaign enrichment, click on edit column, and then over here you can click on save as template, and we'll call this add lead to HeyReach. And over here we can just

say add lead to HeyReach again and save it as a template. [music] And that way, next time that you're inside of your actions inside of Clay, you can just type in add lead to HeyReach, and

automatically you will have this pre-built [music] template ready for you. So, all you need to do is just click into it and just drop the first name column, the last name, the company

name, and the messages across, and it will automatically create that enrichment and add the lead into the campaign. All right, as we wrap up the video, let's do a quick recap. The first

thing that we covered is how you can connect your HeyReach API over to Clay. The second thing that we covered is how you can go about building out the campaign structure inside of HeyReach.

The third thing that we covered is how you can use a mix of Clay and Twain in order to generate a personalized and hopefully relevant message for your HeyReach campaigns. And one extra golden

nugget I want to share is the fact that Twain obviously provides you with the email copy as well as the LinkedIn outreach copy, so you can also >> [music]

>> go into HeyReach and add the go multi-channel option, whereby you can add a lead to automatically receive emails using SmartLead or Instantly, so that you can use that Twain credit to

also generate the email copy for [music] your emails as well as your LinkedIn copy as well. And of course, we also covered how you can push the data from Clay. And of course, after we generated

this lovely personalized and relevant outreach message, we also covered how to push it back into HeyReach. And of course, if you're serious about outbound infrastructure, do me a favor and watch

the HeyReach and Sales Navigator video next, which will be popping up over here. That's where we go a lot deeper into campaign strategy. Anyways, I'll see you in that video. Make sure to

double-check that you're subscribed to the channel, like this video if you've made it this far, and I'll see you in the next one. Cheers.
