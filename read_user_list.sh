#!/bin/bash

####################################
#Author:-Vleena
#Description:- Display the list of users associated with a given repo
#version:- v1

########################################

REPO_OWNER=$1
REPO_NAME=$2

#PAT which is securely communicate with the Github
TOKEN=$token

#-H is the extra info. to the destination server; -s curl with silent mode
response=$(curl -s -H "Authorization: token $TOKEN"  https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/collaborators)  
#all users and permission list
echo "The users list with read access to the ${REPO_OWNER}/${REPO_NAME} is:"
echo $response | jq -r '.[] | select(.permissions.pull==true) | .login'
