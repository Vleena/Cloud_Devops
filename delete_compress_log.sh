#!/bin/bash

read -p "Enter the Error log path:" Log_file
read -p "Enter the number days old files:" Days
echo "list the log files in $Log_file which is greater than $Days days"
find "$Log_file" -type f -name "*.log" -mtime +$Days -ls

read -p "delete(d) or compress(c) the log file:" choice

if [ "$choice" = 'd' ]; then
	find "$Log_file" -type f -name "*.log" -mtime +$Days -delete
	echo "Deleted Successfully"
elif [ "$choice" = 'c' ];then
	find "$Log_file" -type f -name "*.log" -mtime +$Days -exec gzip {} \;
	echo "Compressed Successfully"
else
	echo "no Action"
fi
	


