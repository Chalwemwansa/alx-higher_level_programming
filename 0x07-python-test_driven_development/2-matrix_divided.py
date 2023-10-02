#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def matrix_divided(matrix, div):
    """function divides a matrix by a given value"""

    size = 0
    new_mat = []
    if isinstance(div, int) or isinstance(div, float):
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for j in matrix[0]:
        size += 1
    for i in range(len(matrix)):
        temp = 0
        row = []
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], float):
                row.append(round(matrix[i][j] / div, 2))
            if isinstance(matrix[i][j], int):
                row.append(round(matrix[i][j] / div, 2))
            else:
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
            temp += 1
        if not (size == temp):
            raise TypeError("Each row of the matrix must have the same size")
        new_mat.append(row)
    return (new_mat)
