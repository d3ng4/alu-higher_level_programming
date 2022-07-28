#!/bin/bash
# script that takes URL, send POST request and dsplays response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
