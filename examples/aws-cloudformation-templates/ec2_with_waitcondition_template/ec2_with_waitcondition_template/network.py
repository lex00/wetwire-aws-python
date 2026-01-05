"""Network resources: KWOSSecurityGroup."""

from . import *  # noqa: F403


class KWOSSecurityGroupEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


class KWOSSecurityGroupEgress1(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '8888'
    to_port = '8888'
    cidr_ip = '0.0.0.0/0'


class KWOSSecurityGroupEgress2(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '443'
    to_port = '443'
    cidr_ip = '0.0.0.0/0'


class KWOSSecurityGroupEgress3(ec2.SecurityGroup.Egress):
    ip_protocol = 'icmp'
    from_port = '-1'
    to_port = '-1'
    cidr_ip = '0.0.0.0/0'


class KWOSSecurityGroupEgress4(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class KWOSSecurityGroup(ec2.SecurityGroup):
    vpc_id = VpcId
    group_description = 'Enable HTTP access via port 80/22/443 and ICMP access via port *'
    security_group_ingress = [KWOSSecurityGroupEgress, KWOSSecurityGroupEgress1, KWOSSecurityGroupEgress2, KWOSSecurityGroupEgress3, KWOSSecurityGroupEgress4]
