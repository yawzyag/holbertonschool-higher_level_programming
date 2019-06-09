#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        listm = []
        if list_objs is not None:
            for info in list_objs:
                listm.append(info.to_dictionary())

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as write_file:
            write_file.write(cls.to_json_string(listm))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            text = cls(1, 1)
        elif cls.__name__ == "Square":
            text = cls(1)
        cls.update(text, **dictionary)
        return text

    @classmethod
    def load_from_file(cls):
        listm = []
        filename = "{}.json".format(cls.__name__)

        with open(filename, "r") as read_file:
            listm = cls.from_json_string(read_file.read())
        for i, j in enumerate(listm):
            listm[i] = cls.create(**listm[i])
        return listm