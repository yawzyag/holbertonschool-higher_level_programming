#!/usr/bin/python3
"""multipli
    whit numpy

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplin whit numpy
    args
       m_a
       m_b
    """
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    try:
        new_matrix = np.matmul(m_a, m_b)
    except:
        raise
    return new_matrix
