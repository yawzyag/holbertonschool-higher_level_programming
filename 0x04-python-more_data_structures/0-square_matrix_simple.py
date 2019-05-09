#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = copy_matrix(matrix)
    rowsA = len(new_matrix)
    colsA = len(new_matrix[0])
    for i in range(rowsA):
        for j in range(colsA):
            new_matrix[i][j] = new_matrix[i][j] ** 2

    return new_matrix


def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A


def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC
