"""Network resources: IPAddress, InstanceSecurityGroup."""

from . import *  # noqa: F403


class IPAddress(ec2.EIP):
    pass


class InstanceSecurityGroupEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class InstanceSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable SSH access'
    security_group_ingress = [InstanceSecurityGroupEgress]
