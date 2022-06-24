import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0ba700d7ab4e56064').terminate() # put your instance id
