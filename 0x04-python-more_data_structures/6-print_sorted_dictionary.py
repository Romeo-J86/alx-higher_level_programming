#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    tmp = list(a_dictionary.keys())
    tmp.sort()
    for i in tmp:
        print("{}: {}".format(i, a_dictionary[i]))
