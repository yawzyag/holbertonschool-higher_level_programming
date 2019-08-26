#!/usr/bin/python3
"""testing comments"""
import sys
import urllib.request

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])
except:
    pass
