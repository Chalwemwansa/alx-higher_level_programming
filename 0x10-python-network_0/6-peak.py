#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
    this module consists of a functiion that finds the peak in a list
"""


def find_peak(list_of_integers):
    """the function that find a peak in a list of unsorted integers
    """
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if list_of_integers[1] < list_of_integers[0]:
        return list_of_integers[0]
    if list_of_integers[-2] < list_of_integers[-1]:
        return list_of_integers[-1]

    peak = list_of_integers[1]
    i = 1
    while i < length - 1:
        if list_of_integers[i - 1] < list_of_integers[i] >\
           list_of_integers[i + 1]:
            return list_of_integers[i]
        if list_of_integers[i + 1] < list_of_integers[i]:
            i += 1
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
        i += 1
    return peak
