#!/bin/bash


##########################
#Author:- Vleena
#Date:- 2/1/2026
#Description:- count the number of s in given word "mississippi"
#version:- V1
########################

w="mississippi"
grep -o 's' <<< $w | wc -l

