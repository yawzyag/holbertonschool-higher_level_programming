#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, encoding="UTF8") as juanito:
        for line in juanito:
            print("{}".format(line), end="")
