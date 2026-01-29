import boto3

ec2 = boto3.client('ec2')
snapshots = ec2.describe_snapshots(OwnerIds=['self'])

for i in snapshots['Snapshots']:
	print(i['SnapshotId'])
