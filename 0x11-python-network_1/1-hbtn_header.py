#!/usr/bin/python3
"""testing comments"""
import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.info()
    print('{}'.format(headers['X-Request-Id']))
