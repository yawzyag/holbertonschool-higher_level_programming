#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    payload = {'search': argv[1]}
    url = "https://swapi.co/api/people/"
    req = requests.get(url, payload)
    r = req.json()
    num = r.get('count')

    print("Number of results:", num)
    for i in r.get('results'):
        print(i.get('name'))
