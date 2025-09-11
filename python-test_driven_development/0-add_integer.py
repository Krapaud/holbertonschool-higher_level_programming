#!/usr/bin/python3
"""Module that adds two integers.

This module contains a function that adds two integers or floats
after casting them to integers.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: first integer or float
        b: second integer or float (default: 98)

    Returns:
        The addition of a and b as integers

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
