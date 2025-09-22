#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method and integer validator"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier positif"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
