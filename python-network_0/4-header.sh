#!/bin/bash
# script that takes in URL and sends GET request to URL and displays it
curl -sX -X GET -H "X-HolbertonSchool-User-Id:99" "$1"
