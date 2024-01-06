#!/usr/bin/python3
""" this script takes in a url and sends a request to the url
"""
import requests
from sys import argv

if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        request.encoding = 'utf8'
        print(request.text)
