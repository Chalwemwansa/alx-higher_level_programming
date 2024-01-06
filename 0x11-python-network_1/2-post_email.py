#!/usr/bin/python3
"""script that takes in url and an email the sends a POST request
    to a given url
"""
import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    value = {'email': f'{argv[2]}'}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf8')
    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as request_data:
        r = request_data.read()
    print(r.decode('utf8'))
