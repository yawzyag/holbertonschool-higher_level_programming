#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        try:
            value = roman[roman_string[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(roman_string) and roman[roman_string[i+1]] > value:
                num -= value
            else: num += value
        except:
            return None
    return num
