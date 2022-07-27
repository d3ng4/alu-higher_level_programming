#!/usr/bin/python3
"""
Module contains rectangle class thta inherits the basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class inherits from basgeometry
    """
    def __init__(self, width, height):
        """
        insanitaion of class
        """
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
