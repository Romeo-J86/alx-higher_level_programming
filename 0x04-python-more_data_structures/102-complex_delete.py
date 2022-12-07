#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None or value == "":
        return a_dictionary
    for i in list(a_dictionary.keys()):
        tmp = a_dictionary.get(i)
        if tmp == value:
            a_dictionary.pop(i)
    return a_dictionary
