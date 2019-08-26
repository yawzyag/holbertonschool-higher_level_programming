#!/usr/bin/python3
"""parse error codes"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

req = Request(argv[1])
try:
    response = urlopen(req)
except HTTPError as e:
    print('Error code: {}'.format(e.code))
else:
    html = response.read()
    print(html.decode('utf-8'))
