#!/usr/bin/python3
"""
Import the class Rectangle and creates a subclass named Square.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area of square Method.'''
        return self.__size ** 2

    def __str__(self):
        """ String reepresentation of the square """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
