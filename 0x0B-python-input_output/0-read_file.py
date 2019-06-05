#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, encoding="UTF") as juanito:
        print("{}".format(juanito.read()), end="")
