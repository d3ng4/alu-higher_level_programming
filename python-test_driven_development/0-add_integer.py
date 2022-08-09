#!/usr/bin/python3
"""
This module adds two integers and returns sum of two numbers a & b.
"""


def add_integer(a, b=98):
    """ Returns the sum of a and b
     a must be an integer or float, and,
    b must be an integer or float
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
