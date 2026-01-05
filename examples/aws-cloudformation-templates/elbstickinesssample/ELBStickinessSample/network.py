"""Network resources: InstanceSecurityGroup."""

from . import *  # noqa: F403


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class InstanceSecurityGroupEgress1:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


class InstanceSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable SSH access and HTTP access on the inbound port'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupEgress1]
