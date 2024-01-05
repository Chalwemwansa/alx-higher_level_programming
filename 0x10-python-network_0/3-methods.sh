#!/bin/bash
# script that prints the different methods that can be used on the server
curl -Is "$1" | grep -i 'allow' | awk -F ': ' '{print $2}'
