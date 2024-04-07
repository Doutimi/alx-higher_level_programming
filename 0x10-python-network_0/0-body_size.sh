#!/bin/bash
#a Bash script that displays the size of the body of the response for a URL request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
