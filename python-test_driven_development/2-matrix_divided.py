#!/usr/bin/python3
""" matrix_divided divides all elements of matrix """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    verify list is int/float
     if each list are the same size
    checks if "div" is an int/float or is 0
    """
    matrix1 = "matrix must be a matrix (list of lists) of integers/floats"
    matrix2 = "Each row of the matrix must have the same size"
    result_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(matrix2)
        another_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(matrix1)
            else:
                another_list.append(round(items / div, 2))
        result_matrix.append(another_list)

    return result_matrix