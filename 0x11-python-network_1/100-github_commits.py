#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    r = req.json()
    for i in range(10):
        print(
            "{}: {}".format(
                r[i].get("sha"),
                r[i].get("commit").get("author").get("name")))
