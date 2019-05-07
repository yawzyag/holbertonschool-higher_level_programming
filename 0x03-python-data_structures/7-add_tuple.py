#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) is 2 and len(tuple_b) is 2:
        t = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return t
    elif len(tuple_a) is 2 and len(tuple_b) is 2:
        t = 0, 0
        return t
    elif len(tuple_a) is 1 and len(tuple_b) is 1:
        t = tuple_a[0] + tuple_b[0], 0
        return t
    elif len(tuple_b) is 0:
        return tuple_a
    elif len(tuple_a) is 0:
        return tuple_b
    elif len(tuple_b) is 1:
        t = tuple_a[0] + tuple_b[0], tuple_a[1] + 0
        return t
    elif len(tuple_a) is 1:
        t = tuple_a[0] + tuple_b[0], tuple_b[1] + 0
        return t
