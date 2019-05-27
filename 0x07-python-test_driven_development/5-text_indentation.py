#!/usr/bin/python3
""" This is necesary ?
    I
    dont
    know
"""


def text_indentation(text):
    """function to add two numbers.
       I dont know
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delimiters = [":", "?", "."]
    for deli in delimiters:
        text = text.replace(deli, deli + "\n\n")
    print("\n".join(txt.strip() for txt in text.split("\n")), end="")
