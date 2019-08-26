#!/usr/bin/python3
"""testing comments"""
import requests
from sys import argv

url = argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
