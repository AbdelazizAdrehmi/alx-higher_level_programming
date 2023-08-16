#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    leng = len(new_matrix)

    for i in range(leng):
        new_matrix[i] = list(map(lambda x: x*x, new_matrix[i]))

    return(new_matrix)
