def hello(entities, entity, values):
    try:
        if entity == 'hello':
            return str(values[entities.index(entity)]) + "! How can I help you?"
    except:
        pass


def buy(entities, entity, values):
    try:
        if entity == 'bye':
            return str(values[entities.index(entity)]) + "! I was happy to help you :)"
    except:
        pass

def ok(entities, entity, values):
    try:
        if entity == 'ok':
            return str(values[entities.index(entity)])
    except:
        pass

def mood(entities, entity, values):
    try:
        if entity == 'mood':
            return "I am fine! What about you?"
    except:
        pass