#!/usr/bin/python3
"""
This module adds two integers and returns sum of two numbers a & b.
"""


def add_integer(a, b=98):
    """ Returns the sum of a and b
    a must be an integer or float, and,
    b must be an integer or float
    """
     values = []
    for x, param in [(a, 'a'), (b, 'b')]:
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(param))

    return sum(values)
