#!/bin/sh

# script to resize and crop

FILES="$@"
for k in $FILES
do
    h=`identify -format "%h" $k`
    w=`identify -format "%w" $k`
    #echo "$k, w:$w, h:$h"
    #If landscape
    if [ $w -ge $h ]
    then
	convert $k -resize x800 -crop 800x800+0+0  r.$k
    else
	convert $k -resize 800x -crop 800x800+0+0 r.$k
    fi
done