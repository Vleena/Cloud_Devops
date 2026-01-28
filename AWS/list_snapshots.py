import boto3


EC2 = boto3.client('ec2')
snapshots = EC2.describe_snapshots(OwnerIds=['self'])
print(snapshots)
