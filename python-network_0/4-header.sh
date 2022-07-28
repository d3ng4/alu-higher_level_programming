#!/bin/bash
#script that takes in URL and sends GET request to URL and displays it
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id:98"
