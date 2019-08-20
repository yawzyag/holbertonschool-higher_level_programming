#!/usr/bin/python3
""" adding comentario """


def find_peak(list_of_integers):
    """find a peak"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return 0
    return list_of_integers[find_recursive(
        list_of_integers, 0, len(list_of_integers) - 1)]


def find_recursive(arr, start, end):
    """function recursive"""
    num_m = end - start
    if num_m == 1:
        return start if arr[start] > arr[end] else end
    mid = start + num_m // 2
    if arr[mid] < arr[mid + 1]:
        return find_recursive(arr, mid, end)
    return find_recursive(arr, start, mid)
