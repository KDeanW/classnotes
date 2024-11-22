#!/bin/bash
echo " Running "
when= $date
$when>speed.log
speedtest-cli --secure >store.txt
cat store.txt>speed.log
grep 'Testing from' store.txt
grep 'Download' store.txt
grep 'Upload' store.txt
python -u speed.py
