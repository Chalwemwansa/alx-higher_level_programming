#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def text_indentation(text):
    """function that leaves two lines after a certain character"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for letter in range(len(text)):
        if text[letter] in ('.', '?', ':'):
            print(f'{text[letter]}')
            print()
            flag = 1
        else:
            if flag == 1:
                while text[letter] == " ":
                    letter += 1
                flag = 0
            else:
                print(f'{text[letter]}', end="")
