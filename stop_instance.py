# # Libraries
import os
import time
import boto3
import logging

# # Default Values
instance_id = os.environ['InstanceId']
logging.basicConfig(level=logging.INFO)
ec2 = boto3.client('ec2', region_name='us-east-1')

# # Lambda Function
def handler(event, context):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    return str(response)