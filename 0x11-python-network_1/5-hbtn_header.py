#!/usr/bin/python3
"""testing comments"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
