#!/bin/bash
# script that displays only the exit code
curl -so /dev/null -w "%{http_code}" "$1"
