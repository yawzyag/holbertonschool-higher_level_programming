#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    r = req.json()
    for commit in r[:10]:
        print(
            "{}: {}".format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')))
