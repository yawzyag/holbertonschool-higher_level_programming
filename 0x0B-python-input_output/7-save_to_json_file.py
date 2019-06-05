#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
