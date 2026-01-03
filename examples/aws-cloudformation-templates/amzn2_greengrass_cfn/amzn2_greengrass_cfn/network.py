"""Network resources: VPC, InstanceSecurityGroup, InternetGateway, VPCGatewayAttachment, RouteTablePublic, RouteTablePublicInternetRoute."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    cidr_block = '172.31.0.0/24'
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = SecurityAccessCIDR


class InstanceSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    vpc_id = VPC
    security_group_ingress = [InstanceSecurityGroupEgress]


class InternetGateway:
    resource: ec2.InternetGateway


class VPCGatewayAttachment:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class RouteTablePublic:
    resource: ec2.RouteTable
    vpc_id = VPC


class RouteTablePublicInternetRoute:
    resource: ec2.Route
    route_table_id = RouteTablePublic
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [VPCGatewayAttachment]
