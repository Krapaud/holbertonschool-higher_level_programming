#!/usr/bin/python3
"""Module defining the BaseGeometry class.

This module contains the BaseGeometry class that serves as a base class
for geometric shapes with integer validation.
"""


class BaseGeometry:
    """Base class for geometric shapes.

    This class provides the basic methods for managing geometric
    shapes, including area calculation and integer validation.

    Attributes:
        No specific attributes.
    """

    def area(self):
        """Calculates the area of the geometric shape.

        This method must be implemented by child classes.

        Returns:
            float: The area of the geometric shape.

        Raises:
            Exception: Always raised because this method is not implemented
                      in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        This method verifies that the provided value is indeed an integer
        and that it is strictly positive (> 0).

        Args:
            name (str): The name of the parameter to validate
                       (used in error messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
