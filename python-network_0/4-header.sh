#!/bin/bash
# script that takes in URL and sends GET request to URL and displays it
curl -sX "$1" GET -H "X-HolbertonSchool-User-Id: 98" 
