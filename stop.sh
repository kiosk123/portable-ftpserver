#!/bin/bash

PORT=$(grep -E "^(p|P)(o|O)(r|R)(t|T)=[0-9]*" ./config.py | sed -E 's/(p|P)(o|O)(r|R)(t|T)=//g')

if [ $(netstat -ntlp | grep $PORT | grep -v grep | wc -l) -gt 0 ] ; then
	kill -9 $(netstat -ntlp | grep $PORT | grep -v grep | awk '{ print $7}' | sed 's/\/python[0-9]*//g')
	echo "ftpserver shutdown is sucess"
else 
	echo "no server to down"
fi