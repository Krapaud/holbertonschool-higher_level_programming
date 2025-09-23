#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle inheriting from BaseGeometry.

    This class implements a rectangle with width and height,
    using the integer validation provided by the parent class.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle. Must be a positive
                integer.
            height (int): The height of the rectangle. Must be a positive
                integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
