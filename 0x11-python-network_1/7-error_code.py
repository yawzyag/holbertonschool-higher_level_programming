#!/usr/bin/python3
"""parse error codes"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        url = argv[1]
        r = requests.get(url)
        r.raise_for_status()
    except Exception as a:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
