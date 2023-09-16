#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or (len(a_dictionary) == 0):
        return (None)
    else:
        score = next(iter(a_dictionary))
    for k, v in a_dictionary.items():
        if a_dictionary[score] < v:
            score = k
    return (score)
