#!/usr/bin/python3
""" This is necesary ?
    I
    dont
    know
"""


def spliter(strin, deli):
    temp = []
    texto = strin.split(deli)
    for txt in texto:
        temp.append(txt.strip())
    return(temp)

def text_indentation(text):
    """function to add two numbers.
       I dont know
    """
    delimiters = '.:?'
    for srr in delimiters:
        txt = spliter(text, srr)
        text = (srr + "\n\n").join(txt)
    print("{}".format(str(text)), end="")

    if len(text) > 0 and text[-1] in delimiters:
        print("")
        print("")
