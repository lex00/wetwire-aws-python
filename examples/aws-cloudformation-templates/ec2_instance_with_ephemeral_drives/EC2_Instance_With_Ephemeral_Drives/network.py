"""Network resources: EC2SecurityGroup."""

from . import *  # noqa: F403


class EC2SecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class EC2SecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'SSH access'
    security_group_ingress = [EC2SecurityGroupEgress]
