import boto3
import botocore.exceptions

ec2_client = boto3.client('ec2')


ec2_client.describe_availability_zones(
    "all_availability_zones": true
)


ec2_client.create_vpc(
    "amazon_provided_ipv6cidr_block": false,
    "instance_tenancy": "default",
    "vpc_encryption_control": {"mode": "enforce", "internet_gateway_exclusion": "enable", "egress_only_internet_gateway_exclusion": "enable", "nat_gateway_exclusion": "enable", "virtual_private_gateway_exclusion": "enable", "vpc_peering_exclusion": "enable", "lambda_exclusion": "enable", "vpc_lattice_exclusion": "enable", "elastic_file_system_exclusion": "enable"},
    "cidr_block": "10.0.0.0/16",
    "tag_specifications": [{"resource_type": "vpc", "tags": [{"key": "Name", "value": "assignment1_Cloud"}]}]
)
