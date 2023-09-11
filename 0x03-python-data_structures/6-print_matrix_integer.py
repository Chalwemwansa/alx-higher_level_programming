#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    max = len(matrix)

    for i in range(0, max):
        max1 = len(matrix[i])
        for j in range(0, (max1 - 1)):
            print("{0}".format(matrix[i][j]), end=" ")
        if (max1 - 1) < 0:
            p = ''
        else:
            p = matrix[i][(max1 - 1)]
        print("{0}".format(p))
