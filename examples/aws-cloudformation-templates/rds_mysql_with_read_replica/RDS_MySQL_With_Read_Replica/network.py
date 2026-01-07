"""Network resources: DBEC2SecurityGroup."""

from . import *  # noqa: F403


class DBEC2SecurityGroupIngress(ec2.SecurityGroup.Ingress):
    ip_protocol = 'tcp'
    from_port = '3306'
    to_port = '3306'
    source_security_group_name = EC2SecurityGroup


class DBEC2SecurityGroup(ec2.SecurityGroup):
    resource: ec2.SecurityGroup
    group_description = 'Open database for access'
    security_group_ingress = [DBEC2SecurityGroupIngress]
    condition = 'IsEC2VPC'
