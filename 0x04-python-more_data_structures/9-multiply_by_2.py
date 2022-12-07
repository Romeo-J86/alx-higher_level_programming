#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for x in new_dict.keys():
        temp = new_dict.get(x)
        new_dict[x] = temp * 2
    return new_dict
