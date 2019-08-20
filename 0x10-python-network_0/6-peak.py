#!/usr/bin/python3
""" adding comentario """


def find_peak(list_of_integers):
    """find a peak"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return 0
    return list_of_integers[findPeakHelper(
        list_of_integers, 0, len(list_of_integers) - 1)]


def findPeakHelper(num, start, end):
    span = end - start
    # span of 1 indicates 2 elements
    if span == 1:
        return start if num[start] > num[end] else end
    mid = start + span // 2
    if num[mid] < num[mid + 1]:
        return findPeakHelper(num, mid, end)
    return findPeakHelper(num, start, mid)
