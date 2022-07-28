#!/usr/bin/python3
"""
Defines a file-appending function
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
