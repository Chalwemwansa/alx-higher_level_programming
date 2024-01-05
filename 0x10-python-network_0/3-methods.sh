#!/bin/bash
# script that prints the different methods that can be used on the server
curl -Is 0.0.0.0:5000/route_4 | grep -i 'allow' | awk -F ': ' '{print $2}'
