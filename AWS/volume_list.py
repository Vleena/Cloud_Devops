import boto3

ec2 = boto3.client('ec2')
vol = ec2.describe_volumes()
#print(vol)

volume_id = []
for volume in vol['Volumes']:
	volume_id.append(volume['VolumeId'])

print(volume_id)

