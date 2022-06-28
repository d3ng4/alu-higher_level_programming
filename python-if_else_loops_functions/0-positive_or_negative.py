#!/usr/bin/python3
import random
number = random.randit(-10, 10)
if number < 0:
    print("is negative")
elif number > 0:
    print("is positive")
else:
    print("is zero")
