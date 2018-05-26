import os, sys
from flask import Flask, request,render_template, redirect
from pymessenger import Bot

from utils import wit_response

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAjPlo1AqfoBAOdXX7AJdBZBsnZA20cwklTyRnaZAxoZAA5u7vUZAHjH0MEy8xKx9zhZAXV7zr0eYArvVsreXzYntBlSD6AYsBCFT6StaCBvmND82xS3w4bbISblgcbPse83fLtB7TEjqfIgKqzZAoKlYwN69YZBafTZCE2GUvsDygQZDZD"
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])

def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "ramapitecus":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])

def webhook():
    message = request.get_json() #messages from users are fetched
    log(message)
    print(message)

    if message['object'] == 'page':
        for entry in message['entry']:
            for messaging_event in entry['messaging']:

                #Extracting all IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'NoText'

                    # ECHO
                    response = None

                    entities, values, dictionary_of_values_and_entities = wit_response(messaging_text)

                    for entity in entities:
                        if entity == 'greetings':
                            response = "hello"

                    if response == None:
                        response = "Sorry! I didn't understand your message..."

                    bot.send_text_message(sender_id, response)


    return "ok", 200

def log(message):
    if message:
       print(str(message))
       sys.stdout.flush()
    else:
       print("NULL")
       sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 80)