#!/usr/bin/python3
""" script that fetches data from a given url
"""
import urllib.request
import sys

request = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(request) as request_data:
    r = request_data.headers
print(r['X-Request-Id'])
