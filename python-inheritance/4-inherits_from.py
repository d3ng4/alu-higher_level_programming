#!/usr/bin/python3
"""
module containing the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    function returns True or False
    """
    return(isinstance(obj), a_class) and type(obj) is not a_class)
