#!/usr/bin/python3
"""
Import the class BaseGeometry and creates a subclass named rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
