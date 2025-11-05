#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    __size = None

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne l'aire actuelle du carré."""
        return self.__size * self.__size
