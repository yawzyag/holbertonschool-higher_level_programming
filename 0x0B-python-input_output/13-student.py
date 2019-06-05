#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            my_dict = {}
            for item, val in self.__dict__.items():
                for cosito in attrs:
                    if cosito == item:
                        my_dict.update({item: val})
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, val in json.items():
            self.__dict__[key] = val
