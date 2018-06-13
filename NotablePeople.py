def person(entities, entity, values):
    try:

        what_person = values[entities.index(entity)]['external']['wikipedia']
        what_person = what_person.replace(' ', '_')
        #print(values[entities.index(entity)]['external']['wikipedia'])
        site = 'https://en.wikipedia.org/wiki/' + what_person
        return site

    except:
        pass