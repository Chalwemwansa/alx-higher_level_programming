#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) or not (len(a_dictionary) == 0):
        score = next(iter(a_dictionary))
    else:
        return (None)
    for k, v in a_dictionary.items():
        if a_dictionary[score] < v:
            score = k
    return (score)
