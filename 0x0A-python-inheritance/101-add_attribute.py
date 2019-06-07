#!/usr/bin/python3


def add_attribute(obj, name, person):
    if hasattr(obj, "__dict__"):
        setattr(obj, name, person)
    else:
            raise TypeError("can't add new attribute")
