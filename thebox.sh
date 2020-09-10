#!/bin/bash

url=$1
option=$2

curl "$1" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*"| grep mp4 | sort -r > .tmp
link=`cat ./.tmp | head -$option | tail -1`
name=`basename $1`
echo "name=$name"
curl $link > $name.mp4
echo "Done"
rm ./.tmp


