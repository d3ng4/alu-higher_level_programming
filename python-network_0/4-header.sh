#!/bin/bash
# send headers
curl -s -X GET -L -H "X-HolbertonSchool-User-Id: 98" "$1"
