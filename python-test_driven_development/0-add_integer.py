#!/usr/bin/python3
"""
This module adds two integers and returns sum of two numbers a & b.
"""


def add_integer(a, b=98):
    """ Returns the sum of a and b. """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
