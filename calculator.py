import math

def calc(entities, entity, values):

    try:
        if '+' in values[entities.index(entity)]:
            value = str(values[entities.index(entity)]).split('+')
            return float(value[0]) + float(value[1])
        if '-' in values[entities.index(entity)]:
            value = str(values[entities.index(entity)]).split('-')
            return float(value[0]) - float(value[1])
        if '/' in values[entities.index(entity)]:
            value = str(values[entities.index(entity)]).split('/')
            if float(value[1]) == 0:
                return 'division by zero!'
            else:
                return float(value[0]) / float(value[1])
        if '*' in values[entities.index(entity)]:
            value = str(values[entities.index(entity)]).split('*')
            return float(value[0]) * float(value[1])
        if '^' in values[entities.index(entity)]:
            value = str(values[entities.index(entity)]).split('^')
            return math.pow(float(value[0]), float(value[1]))

    except:
        pass