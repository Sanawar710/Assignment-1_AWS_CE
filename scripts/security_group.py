import boto3
import botocore.exceptions

ec2_client = boto3.client('ec2')


ec2_client.run_instances(
    "max_count": 1,
    "min_count": 1,
    "image_id": "ami-09256c524fab91d36",
    "instance_type": "t3.micro",
    "ebs_optimized": true,
    "network_interfaces": [{"associate_public_ip_address": true, "device_index": 0, "groups": ["sg-preview-1"]}],
    "credit_specification": {"cpu_credits": "unlimited"},
    "tag_specifications": [{"resource_type": "instance", "tags": [{"key": "Name", "value": "unievent-app-server"}]}],
    "metadata_options": {"http_endpoint": "enabled", "http_put_response_hop_limit": 2, "http_tokens": "required"},
    "private_dns_name_options": {"hostname_type": "ip-name", "enable_resource_name_dns_arecord": true, "enable_resource_name_dns_aaaarecord": false}
)


ec2_client.create_security_group(
    "group_name": "launch-wizard-1",
    "description": "launch-wizard-1 created 2026-03-06T17:12:16.120Z",
    "vpc_id": "vpc-040d86c85b09abd0e"
)


ec2_client.authorize_security_group_ingress(
    "group_id": "sg-preview-1",
    "ip_permissions": [{"ip_protocol": "tcp", "from_port": 22, "to_port": 22, "ip_ranges": [{"cidr_ip": "0.0.0.0/0"}]}]
)
