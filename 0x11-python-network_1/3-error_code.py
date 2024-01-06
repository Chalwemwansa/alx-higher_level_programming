#!/usr/bin/python3
""" this script sends a request to a url and displays the body
    of the response
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(request) as request_body:
            r = request_body.read()
        print(r.decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
