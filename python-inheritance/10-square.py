#!/usr/bin/python3
"""
inherits from subclass
"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Recatngle):
    """
    class represntation of a asquare
    """

    def __init__(self, size):
        """
        class instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
