#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    maximo = -100000000
    for i in a_dictionary.keys():
        temp = a_dictionary.get(i)
        if temp is None:
            return None
        if temp > maximo:
            maximo = temp
            key = i
    return key
