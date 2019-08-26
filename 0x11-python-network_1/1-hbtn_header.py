#!/usr/bin/python3
"""testing comments"""
import sys
import urllib.request

try:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])
except:
    pass
