#!/usr/bin/python3
def uppercase(str):
    str1 = ''
    length = len(str)
    for i in range(0, length):
        num = ord(str[i])
        if (not (num >= 65 and num < 91)):
            if (num >= 97 and num < 123):
                str1 += chr(65 + (num - 97))
                continue
        str1 += str[i]
    print("{}".format(str1))
