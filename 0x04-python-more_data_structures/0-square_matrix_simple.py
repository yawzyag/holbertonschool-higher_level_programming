#!/usr/bin/python3
def calculateSquare(n):
    return n*n


def square_matrix_simple(matrix=[]):
    n_matrix = []
    temp = []

    for row in matrix:
        for x in row:
            temp = list(map(lambda x: calculateSquare(x), row))
        n_matrix.append(temp)

    return n_matrix
