#!/usr/bin/python3
"""Module for Rectangle class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the Rectangle.

        Returns:
            str: A string representation using print_symbol characters.
                 Returns empty string if width or height is 0.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
