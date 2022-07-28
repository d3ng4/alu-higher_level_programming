#!/bin/bash
# send headers
curl -s -L -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"
