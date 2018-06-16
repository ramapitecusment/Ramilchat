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