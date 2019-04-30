#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c not in [101, 113]:
        print("{}".format(chr(c)), end="")
