#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r+", encoding="UTF8") as juanito:
        listm = []
        for line in juanito:
            listm.append(line)
            if search_string in line:
                listm.append(new_string)
        juanito.seek(0)
        for line in listm:
            juanito.write(line)
