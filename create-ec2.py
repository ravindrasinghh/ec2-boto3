import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
      ImageId='ami-0e6329e222e662a52',
      MinCount=1,
      MaxCount=1,
      InstanceType='t2.micro',
    )
