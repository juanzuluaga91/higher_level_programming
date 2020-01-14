
"""add_integer method."""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
       a & b: both are integers or floats.
    If errors
        TypeError: if a, b are not int, float.
    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
