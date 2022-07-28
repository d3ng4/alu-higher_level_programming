#!/bin/bash
# script that takes url and displays all HTTP methods server will accept
curl -sI "$1" | grep "ALLOW:" | sed 's/ALLOW: //'
