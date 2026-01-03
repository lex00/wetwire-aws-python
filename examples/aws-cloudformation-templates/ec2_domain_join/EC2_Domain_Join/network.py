"""Network resources: InstanceSecurityGroup."""

from . import *  # noqa: F403


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '3389'
    to_port = '3389'
    cidr_ip = '0.0.0.0/0'


class InstanceSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Allow http to client host'
    vpc_id = VPC
    security_group_ingress = [InstanceSecurityGroupEgress]
