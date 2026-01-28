import boto3

Ec2 = boto3.client('ec2')

vol_id = []
snapshots = Ec2.describe_snapshots(OwnerIds=['self'])
volumes = Ec2.describe_volumes()

for vol in volumes['Volumes']:
	vol_id.append(vol['VolumeId'])

for snap in snapshots['Snapshots']:
	if snap['VolumeId'] not in vol_id:
		print("stale snapshot is:", snap['SnapshotId'])


