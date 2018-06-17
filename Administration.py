def administration(entities, entity, values):
    try:
        if 'tomorrow' in values:
            site = 'https://almaty.fh-joanneum.at/stundenplan//index.php?submit=Suche&q=' + values[entities.index(entity)]
        elif 'today' in values:
            site = 'https://www.meteoprog.ua/en/weather/Kapfenberg/' + values[entities.index(entity)] + '/?showtomorrow'
        print(site)
        return link_crawler(site, '')

    except:
        pass

def docfind(entities, entity, values):
    try:
        if 'docfinder' in entities:
            return 'Visit https://www.docfinder.at . There you can find the nearest doctor. ' \
                   'I hope you feel better soon!'
    except:
        pass
    
def mensa_hours(entities, entity, values):
    try:
        if 'mensa_hours' in entities:
            return 'Monday to Thursday: 7:30-16:00;\n' \
                   'Friday: 7:30 - 19:00;\n' \
                   'Saturday: 9:30-13:30;\n' \
                   'Lunch menus: Monday to Friday: 11:00-15:00;'
    except:
        pass

def useful_inf_for_inc(entities, entity, values):
    try:
        if 'useful_inf_for_inc' in entities:
            return 'https://www.fh-joanneum.at/en/international/services/orientation-packages/'
    except:
        pass

def fh(entities, entity, values):
    try:
        if 'fh' in entities:
            return 'https://www.fh-joanneum.at/en/'
    except:
        pass

def before_leaving(entities, entity, values):
    try:
        if 'before_leaving' in entities:
            return '1. De-register your residence\n' \
                   '2. De-register for health insurance\n' \
                   '3. Close bank account' \
                   '4. Make sure all payments are done, hand in keys etc.' \
                   'For more information contact: international@fh-joanneum.at'
    except:
        pass