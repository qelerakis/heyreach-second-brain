# How to integrate HeyReach with Instantly?

Source: https://www.youtube.com/watch?v=2v4VTMfvtX4

Hey all, so excited to announce the Herich instantly integration. This time birectional. So basically send people from your LinkedIn campaign to your email campaign and send your leads from

your email campaign to your LinkedIn campaign. Let's dive into it. Let me show you around. Um, basically imagine this like you have the multi-rotation of instantly and the rotation of senders

inside of here working together like a charm. Basically have a simple campaign inside of here. Uh once you select the lid list, you select the sender or the senders. Let's do multiple ones. Let's

build out our fresh campaign. So what we want to do, we want to check and find their email address. Now obviously that's a step one. If email is found then great. Well let's

play this a little bit. So we want to send them a connection request over here. And 5 days later if there is no acceptance well this is the fun part. Let's send them to an instantly

campaign. How you do it? You basically connect instantly to hitch using your instantly API key and we will be able to check on your campaigns and you can just select a campaign over here that goes

well these people should receive like obviously that type of message and this cadence like the pointed cadence inside of instant play. um when accepted obviously you can do message one uh

message two and so on and so forth over here but at the end of the day you can again send them to an instantly campaign and this time to a different one so for instance this one can be I tried

reaching you over uh LinkedIn but no response well that's why I'm reaching you out on your email like so and that's pretty much it this is your hey reach instantly campaign vice versa the most

important part is now instantly has dropped a new um pretty much flow which is automations and in this case like you will connect your hyage API key to your instantly uh environment. So how that

looks like it's basically we will just add a new connection. So think of this uh thing working based on triggers and actions. So something has to happen inside of instantly and your email

campaign and obviously it will trigger a different action inside of your H campaign. So let's dive into it. I'm going to add a trigger. So basically check on the built-in and which

triggered. So for instance, if I want to select a person which was u well finished like the campaign actually essentially finished for that lead, I would select that. I would click on

continue. I would can either select uh all campaigns or just um appointed one um campaign ended and the lead did not reply. How often happens that right? Pretty often like 90% of the time. So

I'm [clears throat] going to enroll the ones which did not reply on my email campaign. Click on continue. Not reply true. Campaign ID test step obviously here is the payload [clears throat] and

click on save. Now next step add action. Basically herage is your action now where you need to configure your account. That's pretty straightforward. Select herage. Add an account. I mean

just add your API key. That's pretty much it. Mine is already connected. And I want to select an action. So let's say that I want to send these people to a campaign. So I'm adding leads to

campaign. All good. I can select a campaign as well. I mean I should most definitely to point out to you which one which campaign inside of here I want to send these people to and the data will

be uh prepopulated as well. But then again if you want to check it out you can always check the leads and just like click like so and basically map it out properly. Once we have this we will just

click on continue. We have the last name, the first name, the campaign ID to which you are sending and the LinkedIn URL along with their email address. Click on test. Okay. So once you set it

up, you basically you will have data in, data out and one list updated. Click on save and toggle this on. That's pretty much it. So every lead that not responded on your email campaign will be

enrolled into a LinkedIn campaign conducting like full multi outreach sequence. And remember if they do not respond again to your LinkedIn messages, you can always roll them back to

instantly. Just be cautious because you can go pretty big over email, but LinkedIn has limitations. So just be aware of that. Happy prospecting and thank you for watching this video.
