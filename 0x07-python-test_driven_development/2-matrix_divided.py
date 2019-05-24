#!/usr/bin/python3
""" This is necesary ?
    I
    dont
    know
"""


def matrix_divided(matrix, div):
    """function to add two numbers.
       I dont know
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not any(type(matrix) is list and isinstance(el, list) for el in matrix):
        raise TypeError(err)
    n_matrix = []
    temp = []
    row_len = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)
        if row_len is not len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError(err)
            temp = list(map(lambda x: round((x / div), 2), row))
        n_matrix.append(temp)
    return n_matrix
