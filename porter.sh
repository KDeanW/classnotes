#!/bin/bash
netstat -aon | grep 'LISTENING'>store.txt
python porter.py 1
echo "would you like to see a list of all the ports?"
echo "(yes/no)"
python porter.py 2
w
echo "logs"
ls -i /var/log
