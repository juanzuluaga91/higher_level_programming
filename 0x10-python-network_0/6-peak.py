#!/usr/bin/python3
"""Function find_peak"""


def find_peak(list_of_integers):
    """Finds a peak """
    l_int = list_of_integers
    l = len(l_int)
    if l == 0:
        return
    x = l // 2
    if (x == l - 1 or
        l_int[x] >= l_int[x + 1]) and\
            (x == 0 or l_int[x] >= l_int[x - 1]):
        return l_int[x]
    if x != l - 1 and l_int[x + 1] > l_int[x]:
        return find_peak(l_int[x + 1:])
    return find_peak(l_int[:x])
