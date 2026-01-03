"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance:
    resource: ec2.Instance
    instance_type = InstanceType
    subnet_id = Select(0, Subnets)
    security_group_ids = [InstanceSecurityGroup.GroupId]
    key_name = KeyName
    image_id = LatestAmiId
