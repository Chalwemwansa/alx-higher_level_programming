#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        for k, v in a_dictionary.items():
            if k == key:
                del a_dictionary[k]
                break
    return (a_dictionary)
