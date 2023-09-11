#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        char1 = "None"
    else:
        char1 = sentence[0]
    new_sentence = ((length), char1)
    return (new_sentence)
