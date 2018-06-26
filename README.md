# Ramilchat
#Wit Facebook Chatbot for international students

For years, in-person meetings and phone calls were the dominant means of communication in society and business. Nowadays, with the rise of the internet, a multitude of new options became available (email, social media, mobile apps or filling out a form on a website and waiting for a follow-up). However, recently, the rise of real-time messaging has led to a fundamental shift in how people prefer to communicate with one another.

Chatbots are staring to become more and more popular, even more now that they can study, and answer questions in a shorter time. Our group is composed by international students, and we want to use this technology to support future international students in FH Joanneum, because we understand all difficulties living in a different country with different traditions. We conducted a survey between international students and we found that the biggest difficulties are:
	
1.	Timetable changes;
2.	Administrative questions;
3.	Contacts of international office;
4.	Working hours of Mensa;
5.	Working hours of international office;
6.	Additional information for incoming students;
7.	Upcoming events;
8.	How to find Moodle and Official website of FH Joanneum;
9.	Currency of EUR;
10.	Weather changes;
11.	Etc.;

Our main goal is to create a chatbot to make it easier for new students to adapt in a new environment. Therefore, we decided to implement most of the features mentioned above as well as simple conversation with users.

In the future, the chatbot can be developed, trained, educated in a way that it will be able to answer almost every question of the student (not only incoming ones) and notify all students of FH Joanneum about:

  1.	Exam dates;
  2.	Deadlines;
  3.	Grades;
  4.	And other academic issues;


A Python bot, that contains a Flask server designed to be deployed on Heroku. The application uses a bot made using the Python API from Wit.ai and the Facebook Messenger API.

# Initial Installation

BEFORE STARTING CREATING THE CHATBOT WATCH [THIS VIDEO TUTORIAL](https://www.youtube.com/watch?v=uU4pjtcbFeg&index=1&list=PLyb_C2HpOQSC4M3lzzrql7DSppTeAxh-x) !!!

Fork this repository and clone.

```bash
git clone https://github.com/{your_id}/Wit-Facebook.git
cd Ramilchat
```
For local development make sure you install the development requirements:

```bash
pip install -r requirements.txt
pip install -e .
```

# Configuration
Setup your wit.ai App
Setup your Facebook Page
This code assumes the above have been set up and trained according to the quickstart guide by Facebook.

You can find information on how to set up the above in the [Guide by Facebook](https://developers.facebook.com/quickstarts/?platform=web).

## Launch Server in Heruku

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```bash
$ heroku login
```

Clone the repository
Use Git to clone ramilchat's source code to your local machine.

```bash
$ heroku git:clone -a ramilchat
$ cd ramilchat
```

Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
```bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
# Further Configuration
Setup your Facebook Webhook callback to the heroku app you deployed.
Set the following in your HEroku Config Variables:
```bash
WIT_TOKEN = "your wit.ai token"
FB_PAGE_TOKEN = "your facebook page token"
FB_VERIFY_TOKEN = "your webhook verification token"
```
Finally go to the Facebook page you made and chat to the bot!

# Results of the ChatBot:


