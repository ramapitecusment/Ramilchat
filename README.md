# Ramilchat
#Wit Facebook Chatbot for international students

A Python bot, that contains a Flask server designed to be deployed on Heroku. The application uses a bot made using the Python API from Wit.ai and the Facebook Messenger API.

The bot is designed to provide real-time weather updates on Messenger using the pywapi wrapper for the Weather.com API.

# Initial Installation
Fork this repository and clone.

git clone https://github.com/{your_id}/Wit-Facebook.git
cd python-weather-messenger-bot
# Configuration
Setup your wit.ai App
Setup your Facebook Page
Setup your Facebook Page
This code assumes the above have been set up and trained according to the quickstart guide by Facebook.

You can find information on how to set up the above in the Guide by Facebook.

##Launch Server in Heruku

Run heroku create and push to heroku:
heroku create
git push heroku master
# Further Configuration
Setup your Facebook Webhook callback to the heroku app you deployed.
Set the following in your HEroku Config Variables:
WIT_TOKEN = "your wit.ai token"
FB_PAGE_TOKEN = "your facebook page token"
FB_VERIFY_TOKEN = "your webhook verification token"
Finally go to the Facebook page you made and chat to the bot!
