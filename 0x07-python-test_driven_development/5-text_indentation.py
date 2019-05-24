#!/usr/bin/python3
""" This is necesary ?
    I
    dont
    know
"""


def split(s, delim=" "):
    words = []
    word = []
    for c in s:
        if c not in delim:
            word.append(c)
        else:
            if word:
                words.append(''.join(word))
                word = []
    if word:
        words.append(''.join(word))
    return words


def text_indentation(text):
    """function to add two numbers.
       I dont know
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text1 = split(text, ".")
    textt1 = "".join(putsome(text1, "."))
    text2 = split(text, ":")
    textt2 = "".join(putsome(text1, ":"))
    text3 = split(text, "?")
    textt3 = "".join(putsome(text1, "?"))
    print(text3)


def putsome(string, delim):
    textt= []
    for srr in string:
        list1 = list(srr)
        letra = "".join(list1[0])
        if letra == " ":
            list1[0] = ""
        list1[-1] = delim
        textt.append("".join(list1))
    return(textt)
