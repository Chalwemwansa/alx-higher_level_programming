#!/bin/bash
# script that sends content to a script in json format
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
