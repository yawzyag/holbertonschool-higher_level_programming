#!/usr/bin/python3
""" testing comments """
from sys import argv
import urllib.request

url = argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.info()
    print('{}'.format(headers['X-Request-Id']))
