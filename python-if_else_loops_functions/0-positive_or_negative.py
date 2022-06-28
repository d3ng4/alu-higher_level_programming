#!/usr/bin/python3
import random
number = random.randit(-10, 10)
if number < 0:
    print("Negative number")
elif number > 0:
    print("Positive number")
else:
    print("Zero")
