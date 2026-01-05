"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2InstanceInstanceNetworkInterfaceSpecification:
    resource: ec2.SpotFleet.InstanceNetworkInterfaceSpecification
    network_interface_id = Eth0
    device_index = '0'


class EC2InstanceAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'myInstance'


class EC2Instance(ec2.Instance):
    image_id = LatestAMI
    instance_type = InstanceType
    key_name = KeyName
    network_interfaces = [EC2InstanceInstanceNetworkInterfaceSpecification]
    tags = [EC2InstanceAssociationParameter]
