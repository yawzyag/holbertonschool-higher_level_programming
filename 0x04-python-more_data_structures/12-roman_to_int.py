#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
            val = ro[roman_string[i]]
            if (i + 1 < len(roman_string) and ro[roman_string[i + 1]] > val):
                num -= val
            else:
                num += val
    return num
