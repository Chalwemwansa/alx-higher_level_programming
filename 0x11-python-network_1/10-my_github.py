#!/usr/bin/python3
""" this script takes arguments and connects to the github api
    then outputs the id of the user
"""
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    url = f'https://api.github.com/users/{argv[1]}'
    header = {'Authorization': f'Bearer {passwd}'}

    request = requests.get(url, headers=header)
    print(request.json().get('id'))
