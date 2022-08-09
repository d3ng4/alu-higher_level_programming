#!/usr/bin/python3
"""
Write a function that adds 2 integers.
"""


def add_integers(a, b=98):
    """
    add_integer: Check input if correct, cast both into ints and return sum
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))
