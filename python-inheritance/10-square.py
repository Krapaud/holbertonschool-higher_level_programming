#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherited from BaseGeometry"""

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
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
