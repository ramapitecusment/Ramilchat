from wit import Wit
from AmountOfMoney import amount_of_money

access_token = "CGWUZCDKZRYBJ5UWGZI5C45N3VSAP5G7"
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

#entities, values, dictionary_of_values_and_entities = wit_response("100 USD in EUR")
#for entity in entities:

#print(response)