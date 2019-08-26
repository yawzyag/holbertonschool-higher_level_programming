#!/usr/bin/python3
"""parse error codes"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

try:
    req = Request(argv[1])
    response = urlopen(req)
except HTTPError as e:
    print('Error code: {}'.format(e.code))
except:
    pass
else:
    html = response.read()
    print(html.decode('utf-8'))
