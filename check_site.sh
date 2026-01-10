#!/bin/bash

###########################################
#Author:- Vleena
#Description:- check the website is up or not
#Version:- V1
#############################################

site_URL="https://dm-us.informaticacloud.com/identity-service/home"

#curl only to get the status code
#-s silent mode hides the progress bar
#-o /dell/null discard the website content
# -w print only the specific data that we want
response=$(curl -s -o /dev/null -w ${http_code} ${site_URL})

echo $response
