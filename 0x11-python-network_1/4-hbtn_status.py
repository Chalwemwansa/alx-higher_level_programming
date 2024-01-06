#!/usr/bin/python3
"""this script fetches data from a given url and
    prints it using requests module
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
