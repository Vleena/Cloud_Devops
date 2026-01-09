#!/bin/bash

######################################
#Author:- Vleena
#Date:- 2/1/2026
#print the number which is divisible by 3 and 5 but not 15
#version:- V1

#####################################

#set -x

for i in $(seq 1 100)
do 
	if ((($i%3==0)) || (($i%5==0)) && (($i%15!=0)));then
		echo $i
	fi
done
