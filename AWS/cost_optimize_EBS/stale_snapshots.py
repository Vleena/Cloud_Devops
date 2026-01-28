import boto3

EC2 = boto3.client('ec2')

volume_list = []
#list the EBS volumes
vol = EC2.describe_volumes()
for v in vol['Volumes']:
	volume_list.append(v['VolumeId'])

#list the snapshots and check if the snapshot attached to the volume if no delete it

snapshots = EC2.describe_snapshots(OwnerIds=['self'])
for snap in snapshots['Snapshots']:
	if snap['SnapshotId'] not in volume_list:
		print("Deleting snapshot:",snap['SnapshotId'])
		EC2.delete_snapshot(SnapshotId=snap['SnapshotId'])

print("cleaned the stale snapshots successfully")
