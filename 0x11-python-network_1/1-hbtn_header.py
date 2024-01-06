#!/usr/bin/python3
""" script that fetches data from a given url
    and prints the value of a given variable
"""
import urllib.request
from sys import argv

request = urllib.request.Request(argv[1])
with urllib.request.urlopen(request) as request_data:
    r = request_data.headers
print(r['X-Request-Id'])
