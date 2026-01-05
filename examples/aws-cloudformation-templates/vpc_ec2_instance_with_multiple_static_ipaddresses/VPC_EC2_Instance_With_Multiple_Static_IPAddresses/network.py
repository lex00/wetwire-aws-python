"""Network resources: SSHSecurityGroup, EIP1, Eth0, EIPAssoc1."""

from . import *  # noqa: F403


class SSHSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class SSHSecurityGroup(ec2.SecurityGroup):
    vpc_id = VpcId
    group_description = 'Enable SSH access via port 22'
    security_group_ingress = [SSHSecurityGroupEgress]


class EIP1(ec2.EIP):
    domain = 'vpc'


class Eth0PrivateIpAddressSpecification:
    resource: ec2.Instance.PrivateIpAddressSpecification
    private_ip_address = PrimaryIPAddress
    primary = 'true'


class Eth0PrivateIpAddressSpecification1:
    resource: ec2.Instance.PrivateIpAddressSpecification
    private_ip_address = SecondaryIPAddress
    primary = 'false'


class Eth0AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'Interface 0'


class Eth0AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'Interface'
    value = 'eth0'


class Eth0(ec2.NetworkInterface):
    description = 'eth0'
    group_set = [SSHSecurityGroup]
    private_ip_addresses = [Eth0PrivateIpAddressSpecification, Eth0PrivateIpAddressSpecification1]
    source_dest_check = 'true'
    subnet_id = SubnetId
    tags = [Eth0AssociationParameter, Eth0AssociationParameter1]


class EIPAssoc1(ec2.EIPAssociation):
    network_interface_id = Eth0
    allocation_id = EIP1.AllocationId
