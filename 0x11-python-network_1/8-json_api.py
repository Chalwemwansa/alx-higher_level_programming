#!/usr/bin/python3
""" this script sends a letter to a server through a post request
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        value = argv[1]
    else:
        value = ""
    my_data = {'q': value}

    try:
        request = requests.post(url, data=my_data)
        data = request.json()
        if data is None or len(data) == 0:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
