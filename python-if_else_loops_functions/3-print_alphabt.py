#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    joak = chr(i)
    if joak not in "qe":
        print("{:s}".format(joak), end="")
