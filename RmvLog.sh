#!/bin/bash
logger="-/home/pi/Rmvr.log"

if [ $# -eq "0" ] ; then
	echo"Usage $0 list of files/directories">&2
	exit 1
fi
silent=false
if [ $1 == "-s" ] ; then
	echo"silent working"
	echo"$(date): $USER: removed: $FILE" >> $logger
	
	silent=true
else
	echo"$(date): $USER: removed: $FILE" >> $logger
	echo"$(date): $USER: removed: $FILE"
fi
if [ silent == "true" ] ; then
	#echo"$(date): $USER: removed: $FILE" >> $logger
	/usr/bin/rm "$2"
else
	/usr/bin/rm "$2"
fi
