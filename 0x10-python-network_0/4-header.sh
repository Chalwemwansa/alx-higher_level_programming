#!/bin/bash
# script that sets a header variable and prints the return of the request
curl -sH "X-School-User-Id: 98" "$1"
