#!/usr/bin/python3
"""
Print_square Module:

"""


def print_square(size):
    """
    print_square - prints a square with the character '#'.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    else:
        print("\n".join([
            "".join(["#" for x in range(size)])
            for y in range(size)]))
