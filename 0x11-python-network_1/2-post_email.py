#!/usr/bin/python3
"""holi"""
from sys import argv
import urllib.request
import urllib.parse

try:
    email = argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    url = argv[1]
    with urllib.request.urlopen(url, data) as f:
        print(f.read().decode('utf-8'))
except:
    pass
