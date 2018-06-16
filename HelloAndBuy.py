from ClassScrapper import classes

def hello(entities, entity, values):
    try:
        if 'mood' in entities:
            return "I am fine! What about you?"
        elif entity == 'greetings':
            if 'get_class' in entities:
                return str(classes(entities, 'get_class', values))
            else:
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
        if 'mood' in entities:
            return "I am fine! What about you?"
        elif entity == 'ok':
            return str(values[entities.index(entity)])
    except:
        pass

def mood(entities, entity, values):
    try:
        if entity == 'mood':
            return "I am fine! What about you?"
    except:
        pass

def needhelp(entities, entity, values):
    try:
        if entity == 'NeedHelp':
            return "How can I help you?"
    except:
        pass

def no(entities, entity, values):
    try:
        if entity == 'no':
            return "Ok."
    except:
        pass

def hobby(entities, entity, values):
    try:
        if entity == 'hobby':
            return "I like chatting."
    except:
        pass

def thanks(entities, entity, values):
    try:
        if entity == 'thanks':
            return "You're welcome!"
    except:
        pass

def saythanks(entities, entity, values):
    try:
        if entity == 'SayThanks':
            return "Thank you!"
    except:
        pass

def because_a(entities, entity, values):
    try:
        if entity == 'because_a':
            return "I see."
    except:
        pass