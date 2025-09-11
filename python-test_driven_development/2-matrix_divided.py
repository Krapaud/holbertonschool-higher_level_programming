#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module contains a function that divides all elements of a matrix
by a given number.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If each row of the matrix doesn't have the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix)
            or not all(isinstance(elem, (int, float))
                       for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
