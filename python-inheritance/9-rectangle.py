#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method and integer validator"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier positif"""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectange class with herited by BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the Rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the Rectangle.

        Returns:
            str: A string representation using print_symbol characters.
                 Returns empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__width, self.__height))
