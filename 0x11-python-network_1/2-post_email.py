#!/usr/bin/python3
"""holi"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        email = argv[2]
        data = urllib.parse.urlencode({'email': email})
        data = data.encode('ascii')
        url = argv[1]
        req = request.request.Request(url, data)
        with urllib.request.urlopen(req) as f:
            print(f.read().decode("utf-8"))
    except:
        pass
