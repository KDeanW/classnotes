#!/bin/bash
echo "date:" $(date)
echo "user info:"
echo "user:" whoami
echo "login:" 
echo "network info:"
iwgetid>store.txt
echo "network name"
python info.py 2
echo "ip"
hostname -i
ifconfig | grep 'broadcast'>store.txt
echo "netmask"
python info.py 1
echo "broadcast ip"
python info.py 3
ip route |grep default>store.txt
echo "gatway ip"
python info.py 4
ifconfig | grep 'ether'>store.txt
echo "MAC address"
python info.py 5
