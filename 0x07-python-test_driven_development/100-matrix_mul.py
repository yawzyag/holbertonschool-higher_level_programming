#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def matrix_mul(m_a, m_b):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not any(isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if not any(isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(len(list(el)) is 0 for el in m_a):
        raise ValueError("m_a can't be empty")
    if any(len(list(el)) is 0 for el in m_b):
        raise ValueError("m_b can't be empty")

    err2 = "m_a should contain only integers or floats"
    err3 = "m_b should contain only integers or floats"

    for row in m_a:
        for x in row:
            if not isinstance(x, (float, int)):
                raise TypeError(err2)

    for row in m_b:
        for x in row:
            if not isinstance(x, (float, int)):
                raise TypeError(err3)
    list1 = []

    row_lena = len(m_a[0])
    row_lenb = len(m_b[0])
    for i in range(0, len(m_a)):
        if row_lena is not len(m_a[i]):
            raise TypeError("each row of m_a must should be of the same size")
    for i in range(0, len(m_b)):
        if row_lenb is not len(m_b[i]):
            raise TypeError("each row of m_b must should be of the same size")

    if row_lena is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(0, len(m_a)):
        temp = []
        for j in range(0, len(m_b[0])):
            result = 0
            for k in range(0, len(m_a[0])):
                result += m_a[i][k]*m_b[k][j]
            temp.append(result)
        list1.append(temp)

    return list1
