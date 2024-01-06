#!/usr/bin/python3
""" this script takes in an email address and sends
    a POST request to the given server
"""
import requests
from sys import argv

if __name__ == "__main__":
    request = requests.post(argv[1], data={'email': argv[2]})
    print(request.text)
