#!/usr/bin/python3
""" Defines matrix divides """


def matrix_divided(matrix, div):
    """ Divides each element of a matrix by di """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not isinstance(matrix[0], list)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for row in range(0, len(matrix)):
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError(
                    "Each row of the matrix must have the same size")
        for value in matrix[row]:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    return ([[round(x/div, 2) for x in row] for row in matrix])
