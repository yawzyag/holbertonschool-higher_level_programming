#!/usr/bin/python3
"""parse error codes"""
import requests
from sys import argv

if __name__ == "__main__":
    payload = {'search': argv[1]}
    url = "https://swapi.co/api/people"
    req = requests.post(url, params=payload)
    r = req.json()
    num = r.get('count')

    print("Number of results: {}".format(num))
    for i in r.get('results'):
        print(i.get('name'))
        for film in i.get('films'):
            f = requests.get(film).json()
            print("\t", f.get('title'))

    while r.get('next'):
        r = requests.get(r.get('next')).json()
        for i in r.get('results'):
            print(i.get('name'))
            for film in i.get('films'):
                f = requests.get(film).json()
                print("\t", f.get('title'))
