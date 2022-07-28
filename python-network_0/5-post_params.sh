#!/bin/bash
# script that takes URL, send POST request and dsplays response
curl -sd "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
