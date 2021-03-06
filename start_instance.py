# # Libraries
import os
import time
import json
import boto3
import logging

# # Default Values
instance_id = os.environ['InstanceId']
logging.basicConfig(level=logging.INFO)
ec2 = boto3.client('ec2', region_name='us-east-1')

# # Lambda Function
def handler(event, context):
    ec2.start_instances(InstanceIds=[instance_id])
    time.sleep(5)
    reservations = ec2.describe_instances(InstanceIds=[instance_id]).get("Reservations")
    for reservation in reservations:
        for instance in reservation['Instances']:
            # print(instance.get("PublicIpAddress"))
            logging.info(instance.get("PublicIpAddress"))
            ip = instance.get("PublicIpAddress")
    # return str(ip)
    return {
        'statusCode': 200,
        'body': json.dumps(ip)
    }