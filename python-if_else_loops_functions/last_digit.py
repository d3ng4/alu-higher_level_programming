#!/usr/bin/pyhton3
import random
first_number = str(number)
last_number = first_number[-1]
ini_last_number = ini(last_number)
if ini_last_number > 5:
    print("Last digit of, number, is greater than 5".format(number,ini_last_number))
elif ini_last_number == 0:
    print("Last digit of, number and is 0".format(number,ini_last_number))
elif ini_last_number < 6 and ini_last_number !=0:
    print("Last digit of, number and is less than 6 and not 0".format(number,ini_last_number))


