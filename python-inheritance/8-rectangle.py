#!/usr/bin/python3
"""
Module defining BaseGeometry and Rectangle classes.

This module contains a base class for geometric shapes
and a concrete implementation for rectangles.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.

    This class provides a base interface for all geometric shapes
    with methods to calculate area and validate integer parameters.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method must be implemented by subclasses.

        Raises:
            Exception: Always, as this method is not implemented
                      in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter to validate.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
