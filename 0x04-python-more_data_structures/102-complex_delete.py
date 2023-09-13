#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for k, v in a_dictionary.items():
        if v == value:
            new_list.append(k)
    for i in range(len(new_list)):
        del a_dictionary[new_list[i]]
    return (a_dictionary)
