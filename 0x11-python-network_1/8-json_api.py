#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        payload = {'q': ''}
    else:
        payload = {'q': argv[1]}

    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, payload)
    try:
        r = req.json()
    except BaseException:
        print("Not a valid JSON")
    else:
        if r:
            print("[{}] {}".format(r.get('id'), r.get('name')))
        else:
            print("No result")
