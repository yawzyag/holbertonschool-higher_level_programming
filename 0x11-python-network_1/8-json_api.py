#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("No result")
    else:
        url = "http://0.0.0.0:5000/search_user"
        payload = {'q': argv[1]}
        r = requests.post(url, data=payload)
        if len(r.json()) > 0:
            try:
                print(
                    "[{}] {}".format(
                        r.json().get('id'),
                        r.json().get('name')))
            except BaseException:
                print("Not a valid JSON")
        else:
            print("No result")
