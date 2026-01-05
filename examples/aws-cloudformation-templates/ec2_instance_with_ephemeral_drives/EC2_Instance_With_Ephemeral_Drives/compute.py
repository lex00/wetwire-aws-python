"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2InstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sdc'
    virtual_name = 'ephemeral0'


class EC2Instance(ec2.Instance):
    instance_type = InstanceType
    subnet_id = Select(0, Subnets)
    security_groups = [EC2SecurityGroup]
    key_name = KeyName
    image_id = LatestAmiId
    block_device_mappings = [EC2InstanceBlockDeviceMapping]
