def feeling(entities, entity, values):
    try:
        if entity == 'feeling':
            if 'negative' in values:
                return "I see. Everything will be fine!!!"
            elif 'positive' in values:
                return "That's GOOD!!!"
            else:
                return "I see."
    except:
        pass

def love_q(entities, entity, values):
    try:
        if entity == 'love_q':
            return "Hello from love_q!"

    except:
        pass

def love(entities, entity, values):
    try:
        if entity == 'love':
            return "Hello from love!"

    except:
        pass

def want_you(entities, entity, values):
    try:
        if entity == 'want_you':
            return "Hello from want_you!"

    except:
        pass