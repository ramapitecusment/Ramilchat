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