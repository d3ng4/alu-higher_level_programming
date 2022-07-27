#!/usr/bin/python3
"""
Module containing the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Function returns True or False
    """
    return(isinstance(obj), a_class) and type(obj) is not a_class
