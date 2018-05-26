def hello(entities, entity, values):
    try:
        if entity == 'greetings':
            return "Hi! How can I help you?"
    except:
        pass


def buy(entities, entity, values):
    try:
        if entity == 'bye':
            return "Bye! I was happy to help you :)"
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