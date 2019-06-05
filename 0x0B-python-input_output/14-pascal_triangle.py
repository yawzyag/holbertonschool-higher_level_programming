#!/usr/bin/python3
def pascal_triangle(n):

    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    lista = [[1], [1, 1]]

    for l in range(1, n - 1):
        line1 = [1]
        for j in range(0, len(lista[l]) - 1):
            line1.extend([lista[l][j] + lista[l][j + 1]])

        lista.append(line1)
        line1 += [1]

    return lista
