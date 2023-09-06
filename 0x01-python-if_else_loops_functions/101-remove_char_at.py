#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ''
    length = len(str)
    if (n >= length or n < 0):
        return (str)
    else:
        for i in range(0, length):
            if (i == n):
                continue
            str1 += str[i]
        return (str1)
