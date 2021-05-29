import time
import json
import boto3
import logging
logging.basicConfig(level=logging.INFO)
ec2 = boto3.client('ec2', region_name='us-east-1')

def handler(event, context):
    ec2.start_instances(InstanceIds=[''])
    time.sleep(5)
    reservations = ec2.describe_instances(InstanceIds=['']).get("Reservations")
    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
            logging.info(instance.get("PublicIpAddress"))
            ip = instance.get("PublicIpAddress")
    return str(ip)
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(ip)
    # }

# if __name__=="__main__":
#     lambda_handler()