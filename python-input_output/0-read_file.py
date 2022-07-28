#!/usr/bin/python3
"""
function to print text file to stdout without import
"""


def read_file(filename=""):
    """
    read text file and prints stdout
    """
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
