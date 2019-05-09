#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        d1 = {key: value * 2}
        a_dictionary.update(d1)
    return a_dictionary
