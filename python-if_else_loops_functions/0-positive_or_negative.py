#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is negative number".format(number))
elif number > 0:
    print("{} is positive number".format(number))
else:
    print("Zero")
