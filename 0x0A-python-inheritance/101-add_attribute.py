#!/usr/bin/python3


def add_attribute(obj, name, person):
    if isinstance(obj, (int, str, list, tuple, dict,
                        bool, float, complex)) or obj is None:
        raise TypeError("can't add new attribute")
    obj.name = person
