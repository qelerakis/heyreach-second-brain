# How to Generate Unlimited Leads Using LinkedIn and Make.com (2026)

Source: https://www.youtube.com/watch?v=pF_XbIpMct4

Recently, I discovered one of the most powerful ways to generate leads on LinkedIn. And the best part is that it's very simple to implement. And the reason why this method is so amazing is because

it leverages Hey Reach, Clay, and Make.com to send personalized lead magnets at scale. So, I found a guy called Michael Suja online and he's absolutely killing it. And he did this

exact same method using instantly. And we're going to do it right now with Hey Reach. So, by the end of this video, you're going to be able to implement it for yourself and generate thousands and

thousands of leads. Now, this works so well because it completely flips the script on how lead magnets have been done in the past. Previously, you would send out what I would call a generic

lead magnet. And a generic lead magnet is essentially some sort of cookie cutter template that you would send out to everyone, but because it was a generic lead magnet, it wouldn't convert

as well and we would have to assume what the current situation of the prospect was. On the other hand, we could have done a personalized lead magnet, but that was incredibly timeconuming. it

would require a full-time VA or a full-time SDR to essentially create personalized resources to send. And so we would generally reserve that for the end of the sales process when we were

making customized proposals or customized quotes. Now, the new way completely flips it on its head because it now lets us do personalized lead magnets at the beginning of the sales

and marketing journey. Imagine being able to send every lead a personalized resource that converts at such a higher rate and that makes them feel seen and heard by your marketing. And so on a

high level, this is exactly how it works. First, we're going to start with Hey Reach. Hey Reach is a LinkedIn outreach tool and it has an awesome feature called a uni box which basically

lets us see inside the inbox of LinkedIn accounts. Now with that uni box, we can then tag a conversation and then when that conversation is tagged, send that lead into a clay table. Now clay is

almost like Google Sheets with AI powered on top of it. Now, when that lead goes into Clay, we're going to use AI to basically create personalized elements and variables, which we're

going to use for our lead magnet. We're then going to send the output from Clay into Make.com, which is going to create a Google doc for us, which is the personalized lead magnet, and it's going

to be stored inside Google Drive. So, let's kick it off. I'm going to show you how to do step one. First, we got to go into Hey Reach and create a campaign so that we can start speaking to

individuals. So, all we got to do is head over to Hey Reach. This is what the dashboard looks like. We're going to click on campaigns. We're going to click start new campaign and we're going to

give it a name and in this case I'm going to do hey reach clay make test then click create. Now when you're in this page you can then add a bunch of leads that you want to reach out to. So

I've already uploaded a bunch of leads to hey reach which was super super easy and then I'm going to click continue and then I can select the accounts I want to send messages from. Now hey reach is

really cool because it will let me use multiple accounts for the same campaign. So now I can 3x my connection volume with three accounts. I click continue. I click continue again and then I'm going

to do a simple campaign which says if there a connection and if we're not connected I'm going to send a connection request. It's going to be blank for now and then I'm going to click add message

after they've accepted. And for this video I'm going to assume that I'm a YouTube agency so I'm trying to get YouTube agency clients and the message I'm going to write I'm going to write

first name over here so I can add some personalization with hey reach. Hey first name I saw you have some awesome case studies. You could easily generate a couple new clients just by posting

that to YouTube. I've taken one of them and created a strategy around it. Can I send the doc over? And this works so well because one is I'm not trying to ask for a meeting. I'm actually offering

value outright. And that value is going to be my personalized lead magnet. So I can expect a high reply rate. And all I've got to do is copy this over to the fallback message and remove the

variable. And then I'm just going to click save and click continue. And then I can launch this campaign and get going. Now the next step happens after about a day when you start getting

responses. And I guarantee you this campaign will get responses because it has such irresistible value. Now I can head over to the uni box and when I get that positive reply, all I need to do is

open up a conversation and add a tag to it. And that's a way of me signaling that this conversation, this lead needs a personalized lead magnet. Now I've created a tag name already. I've called

it Amen. So I'm just going to search it. And that's what I would do in practicality. The next step is to make sure that when this tag is added, this data is sent over to Clay. So I'm going

to head over to integrations on Hey Reach. Now what I'm going to do is click on integrations, click on web hook under the connections number, and click create web hook. For the web hook name, I'm

going to write Amen hey reach clay. For the event type, I'm going to choose lead tag updated. And then I need to get a web hook URL. And this is when I go into clay. So this is the table that I have

already over here. And what I've done is I've created a table that captures from a web hook. And I'll show you how to create that too. Now when you're in clay, you got to go click new, click

workbook, and then you need to click all sources. And then we're going to search for web hook. You're going to click on that one. And this is now going to create us a URL that we're going to put

into Hri. So, we can copy this one and we're going to go back into Hey Reach and we're going to paste that as the web hook URL and click create web hook. And there you go. Heyach is now connected up

to Clay. So, every time a conversation gets added with a tag, it will send it directly to that table in clay.com. Now, I've already had this connected up for some time. So, I'm going to show you

what I did. When the web hook comes in, it looks like this. And you can click on the web hook. And then you can add a column for all this information about the lead. And so, I added a column for

the lead's first name, for the lead's last name. I also added it for the company name, the company URL, and the profile URL. I also added the tag over here because I need to do something

quite important. I need to filter for the tag that I care about. So, I'm going to click filters over here. I'm put where the tag is equal to and I'm going to write the tag name that I used. And

so, now only the conversations which have the tag that I just applied and I created inside here make it to this table. So, the next step is to create all the personalized variables I want

for my personalized lead magnet. And so, I need to create what this personalized lead magnet will look like. This is one I've created already and it's basically saying this is first names custom

strategy for brand names. So this might be hey this is Martin's custom strategy for Semrush and I say we booked 20 calls from YouTube with a similar strategy and I go through some text about what we do

and then I say and now you can do it too and this is where the personalized variables come in. I say step one ideation I saw your case study on and then I'm going to have double double

brackets case study URL. So I'm going to pull that as a custom variable from clay. I said based on that case study we can create videos with potentials like case study title. That's something I'm

going to generate inside Clay and the outline of the video would be as follows. I'm going to give an outline too. Want to give it a go? Let me know on LinkedIn and I'll send you some more

resources to kick off. So in this template I have five custom variables. First name, brand name, case study URL, case study title and outline. And honestly I could have only one and I

could also have 100. It doesn't actually matter as long as we're putting them in curly brackets. So now I need to create these variables so I can send them to make.com which will then fill out this

Google doc. And so this is how I did it. I basically used a bunch of collagents. So I'm going to walk you through now how I created each of those variables. So the very first variable I got was the

first name and the brand name which I already have from hey reach. That's first name and company name over here. The next variable I wanted was the case study URL. And so I created a column on

clay. So click edit column. You'll see exactly what I did. I have I'm using open AAI GPT 4.1 model and I wrote a prompt over here. I said context. You're tasked with finding a company's website

and identifying the best case study available on that website. I'm not going to read through all of it but the whole objective is to find and return a URL of the best case study. And so it gives

instructions over on how to do that. It has an example and then the output should look like a case study URL. And as a result, when a lead comes in, it will literally create and find the case

study URL for me there and there. And so for example, when I ran this on Mariana's account at Hey Reach, it pulled up this case study about how they booked in 15 sales calls in a single

week. Now with this case study URL, I added a new column which was designed to create a YouTube title which followed the same format as the best way to get result. And so this was able to create

me YouTube titles like the best way to 2x your demos with rewards or the best way to 30x leads with outbound. And finally, I created another prompt which said given the URL and the YouTube

title, create me a outline of the video. And here's the prompt over here. And I'll scroll through so you can see it and capture it. And as a result, I got awesome outputs that looked like this.

Now I have all the personalized variables inside Clay. I now need to send them to make.com. So you got to head over to make.com and create this scenario. So, all you have to do is

click add module and we're going to click and search there web hooks and we're going to do custom web hook exactly the way I've done it below and then you can add a web hook or you can

use an existing one. You can click add over here and click save. And as a result, you'll get a URL that looks like this. Now, I've done this already so I'm not going to do it again. But basically,

I'm going to copy this URL and I'm going to put it inside Clay. And this is how I configured the column that sends the data from Clay to Heyach. You click edit column over here. You choose post method

and you paste the endpoint URL. And now you need to add all the variables that you want to send across. Now the way to do this is in a JSON. So it's really simple. You can copy the format over

here, but essentially it's a curly bracket and it's question mark and the variable name that you want to give it. And that's the same variable name and it's the variable name that you want to

give it. Ideally, you keep it the same as we had in the templates. And then you just match the columns accordingly. So we have first name to first name column. We have brand name to company name

column, case URL to case URL column and so forth. And all we got to do then is click save. Now, in practice, what you should do is click on this web hook and click redetermine data structure. And

then you should play this cell over here so that that information goes to make and then make understands what you're going to be sending across. And so we can use those variables in the next

module. And so you'll probably see something that says successfully determined. The next thing you're going to do is use this module, which is create a document from a template. Click

add module. You're going to click the plus sign there. You're going to click Google Docs and you're going to say create a document from a template which is over here. Now again, I'm not going

to do it because I've done it already, but this is what mine looks like. I connect up my Google Drive. I choose by drop down my drive. I make sure I use the exact folder structure that I have.

So it's in the hey reach clay make test folder under template. And all those variables are sent. I'm going to map it over one by one. I'm going to give a title to my Google doc which is going to

be first name hyphen brand name. And then I'm going to click save. I'm going to save this scenario. I'm going to toggle immediately as it arrives. And that's it. It's all done. And so let's

try the whole flow out. I found a lead. His name is Daniel and he runs an agency in Germany. So, I'm going to literally add a tag to his name, which is Ammon. So, I've added the tag Ammon. I'm going

to go over to Clay and see how it comes through. So, I can see that his title has come in today on the 15th July, Daniel at top ads.io. And I'm now waiting to have it come through, Clay.

So, it's found a case study, which is over here. And this is the URL over here. It's in German, though. So, let's see how the AI handles it. And it's done a pretty good job cuz it's translated

and worked out the title, which should be the best way to 10x ad research with filters, which is great. It's then working on the YouTube outline right now and it's created an outline which is

over here. And now it's created status code 200 which means it's sent. So it's now gone into make.com. It started over here. It's created a Google doc from the template. Now if I open a Google folder

where my template is stored, I should see Daniel topaz.io. And if I double click on that and I open up that Google document, I have my template with the filled out variable. So Daniel for

topaz.io and it's all over here. Now all I got to do is click share general access. Anyone can view. And I'm going to copy that link and head over back to hey reach. Paste the URL and send it to

the lead. And there you go. I was able to go from Hey Reach into Clay into Make.com and then create a personalized lead magnet. Now, this is only one specific way to get leads on LinkedIn.

But if you want this to be really sustainable and longterm, there's a few other things you have to do. So, click here to check out the next video where you can look at the full LinkedIn lead

generation strategy to help your business grow leads, revenue, and sign more clients. See you in the next one and thank you for watching.
