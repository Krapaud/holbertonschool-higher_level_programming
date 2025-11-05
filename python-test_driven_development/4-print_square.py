#!/usr/bin/python3
"""Module that prints a square with the character #.

This module contains a function that prints a square.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: The size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
