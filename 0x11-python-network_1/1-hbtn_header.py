#!/usr/bin/python3
""" script that fetches data from a given url
"""
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as request_data:
        r = request_data.headers
    print(r.get('X-Request-Id'))
