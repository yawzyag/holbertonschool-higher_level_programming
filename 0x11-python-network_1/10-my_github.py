#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    req = requests.get(url, auth=requests.auth.HTTPBasicAuth(argv[1], argv[2]))
    r = req.json()
    num = r.get('id')
    print(num)
