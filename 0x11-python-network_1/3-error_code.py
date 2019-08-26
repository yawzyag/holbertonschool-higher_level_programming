#!/usr/bin/python3
"""parse error codes"""
import urllib.request
from urllib.error import HTTPError
from sys import argv

try:
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html.decode('utf-8'))
except HTTPError as e:
    print('Error code: {}'.format(e.code))
except:
    pass
