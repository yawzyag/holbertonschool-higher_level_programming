#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF8") as juanito:
        lineas = 0
        while lineas < nb_lines or nb_lines <= 0:
            line = juanito.readline()
            if not line:
                break
            lineas += 1
            print("{}".format(line), end="")
