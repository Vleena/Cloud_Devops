#!/bin/bash


#########################
#Author:- Vleena
#Description:- server resource usuage like CPU,RAM,top,Disk space
#version:- V1
###########################

echo "#####################################"
date 
echo "#####################################"
echo "-------------------------------------"
echo "The CPU count:" && nproc
echo "------------------------------------"
echo "The RAM usuage:" && free -h
echo "-------------------------------------"
echo "The Disk space usuage:" && df -h ~
echo "-------------------------------------"
#echo "Overall performace:" && top

