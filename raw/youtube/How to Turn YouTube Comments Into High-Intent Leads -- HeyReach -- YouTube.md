# How to Turn YouTube Comments Into High-Intent Leads

Source: https://www.youtube.com/watch?v=Fh8jr24sP9E

In this video, I'm going to show you how you can automatically turn your YouTube commenters into qualified LinkedIn connections without even lifting a finger. I'm using this workflow myself

and the more I post on YouTube, the more I profit. And to be honest, this is probably one of the most, if not the most underutilized lead genen strategies currently. So, if you implement this

early, I can almost guarantee you that you will have an advantage over everyone else. So the context is let's say we're regularly publishing videos on YouTube and some people will comment on our

videos and whenever that happens YouTube will notify us through notifications and we can go into the comment section have conversation with these people. But what if we're able to get all the information

about the people their YouTube profiles so we can save them in a storage and maybe analyze them later. And also not only that, but what if we can get all social media URLs that they've posted on

their YouTube profile and whenever someone has LinkedIn URL, we can add this person on LinkedIn. Of course, we can do this manually, but it will take forever. Instead of that, we can use

this cool workflow that allows us to do that and even more. First of all, this workflow will run on a schedule because when we publish a video on YouTube, some people will comment right away, some

people will comment later. So we want to continuously to run this workflow so we always check for new comments and new people. So let me quickly run this for you and to show you what we're building.

So we're fetching URLs from a spreadsheet and we're saving people and information about them in another sheet. It's pretty straightforward is going through everything and at the end if we

find some LinkedIn profiles we are going to push those to hey reach. Here is our input sheet and this is what we're getting at the end. As you can see, we have a lot of information. All of those

comments, YouTube videos on which people commented, YouTube profiles and some URLs that they have. Let's dive into the details. First of all, as I've mentioned, schedule trigger, it's up to

you if you want to run those workflow every day, every few days. In my opinion, this is not that time-sensitive because some videos will be watched many many times by many people in in months

to come. Then we have this get YouTube urls from this first sheet here. So by ID, name or whatever you prefer, we have four rows that we got at the output. Next, we are going to use two ampify

actors. The first one is going to be for YouTube comments. This is the one that I've used. This one is working well and it's super super affordable and it gives us a lot of information. What is

important when using actors to pick run an actor and get data set which means not just run an actor because that will run actor on ampify but get data set means wait for the actor to finish and

send back the data set. So we pick the actor and based on the documentation we've gave it um the input the URL and what we got here are the comments. So if we analyze this the type is it comment

is it reply the page URL a reply count vote count and those kind of things. I've pinned this information here just for me to use because it takes a while for everything to be scraped. We can see

here when we switch to JSON view all the comments that we can analyze. If you want to skip the manual setup and just want to clone this entire workflow, you can in literally 60 seconds. And I've

made that available for free at the first link in the description. Just pop in your email and we'll send instant access to this complete template with everything preconfigured. Grab it before

you forget about that. Then come back and I'll show you how to finish setting everything up. The next thing is filter out comments and replies by me. In this case, hey reach account. How I did that

is I could have just done if type is reply just skip those. But then I found cases where people replied to an existing conversation and I want to scrape those people as well. I'm just

saying if author is someone else than this profile or this profile or this profile those are two of my profiles on on YouTube keep the rest. What is happening now from 77 comments 46 pass

this criteria that are not originating from me or hey reach and at this step we have another app ampify actor and this is YouTube profile scraper that is actually scraping this part of a profile

and returning all the information that we want to have. So we can see here all scraped and some people will have this section links some people will not if they haven't published any links but if

they do we can analyze these links in a second. Now a piece of code. So basically here we are getting an object that contains a lot of things. So I've just added some properties to this

object because of uniformity of all objects all profiles. So, LinkedIn, Instagram, X, threads, Facebook. And I'm just checking if a link that comes in this array contains LinkedIn, push it to

this property, LinkedIn. If it has threads, push it to threads. At the end, every single profile will have these properties. LinkedIn, Instagram, X, threads, Facebook, etc. So, this is

going to be uniform. Now, here we are updating or inserting new rows. This is super important. So we don't want to just duplicate everything every single run but I'm using append or update row

and I need to set based on which column should be checked to see is it a new row or is it an existing value and I said ID we are getting this ID from the actor for the YouTube profile. So this is a

unique value and then I'm just dragging and dropping all of these fields. YouTube profile this is a free form. You can do whatever you like here. This is not set in stone. These columns are

something that made sense for me. So basically the ID this column will be used by the Google spreadsheet note to compare whether this data value is a new one or is an existing one. So it can

update or add to rows. YouTube video where the comments originated, the comment itself, YouTube profile and this breakdown based on LinkedIn, Instagram threads x, Facebook and all the links,

the array of all links because some people have like their website and those kind of things. So I'm preserving these links as well so I can see later on if I want to do something with them. After

that I'm filtering out only people that have value in the LinkedIn property. And in this case, we have six, but one is a duplicate. Otherwise, we have two company profiles and that's fine. So, we

ended up with three people here, which is okay if you ask me. And this is a simple example what we can do with this campaign. So, push to this campaign and we can say, "Hey, thanks for commenting

on my YouTube video. Would love to connect." So, this can start an interesting conversation because it's completely automated. We don't have to invest time into this and we can start

building a relationship with these people. Alternatively, a small upgrade to the whole system if you like could be to introduce maybe an AI agent that will take the context about the YouTube video

this person commented on and say thanks for commenting on my YouTube video about fill in the blank. Would love to connect or something like that. You can play with that if you want. But this is a

workflow that can actually monitor your desired YouTube videos and continuously scrape comments, scrape people their social media URLs and keep adding them on LinkedIn. If you want to take this a

step further and completely automate your LinkedIn outreach with just a few tools, then click on the video in the overlay to check out the next one where we walk through everything step by step

so you can start booking qualified appointments while you Sleep.
