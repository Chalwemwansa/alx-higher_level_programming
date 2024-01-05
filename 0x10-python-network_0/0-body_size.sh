#!/bin/bash
# the script makes a get request to a remote server

curl -w "%{size_download}\n" "$1" -so /dev/null
