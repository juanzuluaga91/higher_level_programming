#!/usr/bin/python3
"""
Create the class MyInt
"""


class MyInt(int):
    """ Sub class of int """
    def __new__(cls, *args, **kwargs):
        """ A new instance of the class """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Equals to operator"""
        return int(self) != other

    def __ne__(self, other):
        """The not equals operator"""
        return int(self) == other
