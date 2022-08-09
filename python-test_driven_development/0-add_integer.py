#!/usr/bin/python3
"""
This is the 0-add_integer module
"""


def add_integer(a, b):
    """ Returns the sum of a and b
    float("inf")
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

