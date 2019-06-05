#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as juanito:
        lineas = 0

        while True:
            line = juanito.readline()
            if not line:
                break
            lineas += 1
        return lineas
