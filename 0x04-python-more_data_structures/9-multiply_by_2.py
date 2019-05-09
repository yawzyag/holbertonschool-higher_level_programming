#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for key, value in sorted(b_dictionary.items()):
        d1 = {key: value * 2}
        b_dictionary.update(d1)
    return b_dictionary
