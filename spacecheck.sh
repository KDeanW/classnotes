#!/bin/bash
	
df|awk '{print $5}'|grep '%'|grep -v 'U' >store.txt
store=store.txt
cat store.txt
python spacereader.py
