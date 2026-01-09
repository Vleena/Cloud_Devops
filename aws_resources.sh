#!/bin/bash

###########################
# Author:- Vleena
# Description:- AWS resource usuage report
# Version:- V1
###########################

echo "#############################"
date
echo "#############################"

set -x

#---- list the aws S3 buckets
aws s3 ls

# list the aws EC2 instances
aws ec2 describe-instances|jq '.Reservations[].Instances[].InstanceId'

#list the lambda functions
#aws lambda list-functions

#list the IAM users
aws iam list-users |jq '.Users[].UserName'
