"""Compute resources: BastionInstance."""

from . import *  # noqa: F403


class BastionInstanceAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'Bastion'


class BastionInstance:
    resource: ec2.Instance
    key_name = KeyName
    instance_type = 't2.micro'
    security_group_ids = [BastionSG]
    subnet_id = PublicSubnet1
    image_id = LinuxAMI
    iam_instance_profile = BastionProfile
    tags = [BastionInstanceAssociationParameter]
