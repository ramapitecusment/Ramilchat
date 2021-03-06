import os, sys
from flask import Flask, request,render_template, redirect
from pymessenger import Bot
from utils import wit_response
from Administration import docfind
from Administration import mensa_hours
from Administration import useful_inf_for_inc
from Administration import fh
from Administration import before_leaving
from AmountOfMoney import amount_of_money
from calculator import calc
from ClassScrapper import classes
from Distance import distance
from Duration import duration
from Events import events
from FactsJokes import facts
from FactsJokes import jokes
from Feel import love_q
from Feel import feeling
from Games import games
from HelloAndBuy import hello
from HelloAndBuy import buy
from HelloAndBuy import ok
from HelloAndBuy import because_a
from HelloAndBuy import mood
from HelloAndBuy import needhelp
from HelloAndBuy import no
from HelloAndBuy import hobby
from HelloAndBuy import thanks
from HelloAndBuy import saythanks
from LocalSearch import local_search
from NotablePeople import person
from Remind import remind
from Search import search_g
from StartStop import start
from StartStop import stop
from Tips import tips
from Weather import weather

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAjPlo1AqfoBAHFu5hCqUmfq5HyOsZCyDeFRGkSQlBpgfaqwUMVBBAQ3KrOTNWToUKWPP7WoXlM0oYySRyYhTd1ZB5pRfUdMJSV1C9VmYIZC3V0zblzOddZAaejehJbr6FYSzuBnEiAiqZBJvSQsfE7ws360nUBt04O2HdZAObkgZDZD"
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
                        if entity == 'get_class':
                            response = classes(entities, entity, values)
                            if response == None:
                                response = "Sorry! I can not find this course..."
                            # response = "OK! This are your classes of {}: ".format(str(values[entities.index(entity)]))

                        elif entity == 'feeling':
                            response = feeling(entities, entity, values)

                        elif entity == 'mood':
                            response = mood(entities, entity, values)

                        elif entity == 'greetings':
                            response = hello(entities, entity, values)

                        elif entity == 'bye':
                            response = buy(entities, entity, values)

                        elif entity == 'currency_1':
                            response = amount_of_money(entities, entity, values)

                        elif entity == 'docfinder':
                            response = docfind(entities, entity, values)

                        elif entity == 'mensa_hours':
                            response = mensa_hours(entities, entity, values)

                        elif entity == 'useful_inf_for_inc':
                            response = useful_inf_for_inc(entities, entity, values)

                        elif entity == 'fh':
                            response = fh(entities, entity, values)

                        elif entity == 'before_leaving':
                            response = before_leaving(entities, entity, values)

                        elif entity == 'tips':
                            response = tips(entities, entity, values)

                        elif entity == 'because_a':
                            response = because_a(entities, entity, values)

                        elif entity == 'fact':
                            response = facts(entities, entity, values)

                        elif entity == 'joke':
                            response = jokes(entities, entity, values)

                        elif entity == 'ok':
                            response = ok(entities, entity, values)

                        elif entity == 'weather':
                            response = weather(entities, entity, values)

                        elif entity == 'NeedHelp':
                            response = needhelp(entities, entity, values)

                        elif entity == 'no':
                            response = no(entities, entity, values)

                        elif entity == 'Start':
                            response = start(entities, entity, values)

                        elif entity == 'Stop':
                            response = stop(entities, entity, values)

                        elif entity == 'event':
                            response = events(entities, entity, values)

                        elif entity == 'game':
                            response = games(entities, entity, values)

                        elif entity == 'math':
                            response = calc(entities, entity, values)

                        elif entity == 'love_q':
                            response = love_q(entities, entity, values)

                        elif entity == 'hobby':
                            response = hobby(entities, entity, values)

                        elif entity == 'remind':
                            response = remind(entities, entity, values)

                        elif entity == 'google':
                            response = search_g(entities, entity, values)

                        elif entity == 'notable_person':
                            response = person(entities, entity, values)

                        elif entity == 'duration':
                            response = duration(entities, entity, values)

                        elif entity == 'amount_of_money':
                            response = amount_of_money(entities, entity, values)

                        elif entity == 'thanks':
                            response = thanks(entities, entity, values)

                        elif entity == 'SayThanks':
                            response = saythanks(entities, entity, values)

                        elif entity == 'local_search':
                            response = local_search(entities, entity, values)

                        elif entity == 'distance':
                            response = distance(entities, entity, values)

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