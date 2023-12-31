#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list = []
filename = "add_item.json"
if os.path.exists(filename):
    list = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    list.append(sys.argv[i])
save_to_json_file(list, filename)
