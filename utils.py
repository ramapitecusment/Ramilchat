from wit import Wit
from utils import wit_response
from calculator import calc
from ClassScrapper import classes
from Events import events
from FactsJokes import facts
from FactsJokes import jokes
from Games import games
from HelloAndBuy import hello
from HelloAndBuy import buy
from HelloAndBuy import ok
from HelloAndBuy import mood
from NotablePeople import person
from Search import search
from Tips import tips
from Weather import weather

access_token = "CCBDKWLQI322FY74JTVLURSJWOAEYOXP"
client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(msg = message_text)
    entities = []
    values = []
    dictionary_of_values_and_entities = dict()

    try:
        for entity in list(resp['entities']):
            entities.append(entity)
            values.append(resp['entities'][entity][0]['value'])

        dictionary_of_values_and_entities = dict(zip(entities, values))

    except:
        pass

    return (entities, values, dictionary_of_values_and_entities)

#entities, values, dictionary_of_values_and_entities = (wit_response('Thats ok'))
#print(entities)
#print(values)
#print(dictionary_of_values_and_entities)

response = None

for entity in entities:
    if entity == 'get_class':
        response = classes(entities, entity, values)
        # response = "OK! This are your classes of {}: ".format(str(values[entities.index(entity)]))

    elif entity == 'greetings':
        response = hello(entities, entity, values)

    elif entity == 'bye':
        response = buy(entities, entity, values)

    elif entity == 'mood':
        response = mood(entities, entity, values)

    elif entity == 'tips':
        response = tips(entities, entity, values)

    elif entity == 'fact':
        response = facts(entities, entity, values)

    elif entity == 'joke':
        response = jokes(entities, entity, values)

    elif entity == 'ok':
        response = ok(entities, entity, values)

    elif entity == 'weather':
        response = weather(entities, entity, values)

    elif entity == 'NeedHelp':
        response = NeedHelp(entities, entity, values)

    elif entity == 'no':
        response = no(entities, entity, values)

    elif entity == 'Start':
        response = Start(entities, entity, values)

    elif entity == 'Stop':
        response = Stop(entities, entity, values)

    elif entity == 'event':
        response = event(entities, entity, values)

    elif entity == 'feeling':
        response = feeling(entities, entity, values)

    elif entity == 'game':
        response = game(entities, entity, values)

    elif entity == 'math':
        response = calc(entities, entity, values)

    elif entity == 'love_q':
        response = love_q(entities, entity, values)

    elif entity == 'love':
        response = love(entities, entity, values)

    elif entity == 'want_you':
        response = want_you(entities, entity, values)

    elif entity == 'hobby':
        response = hobby(entities, entity, values)

    elif entity == 'remind':
        response = remind(entities, entity, values)

    elif entity == 'google':
        response = google(entities, entity, values)

    elif entity == 'notable_person':
        response = notable_person(entities, entity, values)

    elif entity == 'datetime':
        response = datetime(entities, entity, values)

    elif entity == 'duration':
        response = duration(entities, entity, values)

    elif entity == 'amount_of_money':
        response = amount_of_money(entities, entity, values)

    elif entity == 'thanks':
        response = thanks(entities, entity, values)

    elif entity == 'SayThanks':
        response = SayThanks(entities, entity, values)

    elif entity == 'local_search':
        response = local_search(entities, entity, values)

    elif entity == 'distance':
        response = distance(entities, entity, values)

if response == None:
    response = "Sorry! I didn't understand your message..."

print(response)