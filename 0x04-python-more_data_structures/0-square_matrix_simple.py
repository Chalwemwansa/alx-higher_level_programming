#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[matrix[i][j] ** 2 for j in range(len(matrix[i]))]
            for i in range(len(matrix))]
    return (new_matrix)
