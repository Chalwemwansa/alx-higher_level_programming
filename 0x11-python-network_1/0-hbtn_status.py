#!/usr/bin/python3
"""this script fetches a url and prints the body of the returned body
"""
import urllib.request

request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(request) as response_obj:
    r = response_obj.read()

#  output the data that has been returned
print(f"Body response:\n\t- type: {type(r)}\n\t- content: {r}\
\n\t- utf8 content: {r.decode('utf8')}")
