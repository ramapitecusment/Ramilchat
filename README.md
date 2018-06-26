# Ramilchat
#Wit Facebook Chatbot for international students

A Python bot, that contains a Flask server designed to be deployed on Heroku. The application uses a bot made using the Python API from Wit.ai and the Facebook Messenger API.

The bot is designed to provide real-time weather updates on Messenger using the pywapi wrapper for the Weather.com API.

# Initial Installation
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
