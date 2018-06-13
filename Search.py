def search_g(entities, entity, values):
    try:

        what_to_search = values[entities.index(entity)]
        what_to_search_g = what_to_search.replace(' ', '+')
        what_to_search_a = what_to_search.replace(' ', '_')
        site = list()
        G_search = 'https://www.google.com/search?q=' + what_to_search_g
        A_search = 'http://www.answers.com/Q/' + what_to_search_a
        site.append(G_search)
        site.append(A_search)

        return str(site[0]) + '\n' + str(site[1])

    except:
        pass