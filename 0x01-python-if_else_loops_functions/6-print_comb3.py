#!/usr/bin/python3
for j in range(10):
    for i in range(j, 10):
        if j != i and j != 8:
            print("{:d}{:d}".format(j, i), end=", ")
        elif j == 8 and j != i:
            print("{:d}{:d}".format(j, i))
