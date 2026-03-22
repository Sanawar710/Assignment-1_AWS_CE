import boto3
import botocore.exceptions

ec2_client = boto3.client('ec2')


ec2_client.describe_availability_zones(
    "all_availability_zones": true
)
