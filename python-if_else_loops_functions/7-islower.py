#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if value >= 97 and value <= 122:
        return True
    ielif value >= 48 and value <=57:
        return False
    elif value >= 65 and value <= 90:
        return False
