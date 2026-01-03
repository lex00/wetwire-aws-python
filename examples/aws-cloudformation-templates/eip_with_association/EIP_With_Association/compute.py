"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance:
    resource: ec2.Instance
    user_data = Base64(Join('', [
    'IPAddress=',
    IPAddress,
]))
    instance_type = InstanceType
    subnet_id = Select(0, Subnets)
    security_groups = [InstanceSecurityGroup]
    key_name = KeyName
    image_id = LatestAmiId
