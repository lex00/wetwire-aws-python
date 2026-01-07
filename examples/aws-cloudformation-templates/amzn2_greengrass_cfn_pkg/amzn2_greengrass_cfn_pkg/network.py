"""Network resources: VPC, InstanceSecurityGroup, RouteTablePublic, InternetGateway, VPCGatewayAttachment, RouteTablePublicInternetRoute."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    resource: ec2.VPC
    cidr_block = '172.31.0.0/24'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


class InstanceSecurityGroupEgress(ec2.SecurityGroup.Egress):
    cidr_ip = SecurityAccessCIDR
    from_port = 22
    ip_protocol = 'tcp'
    to_port = 22


class InstanceSecurityGroup(ec2.SecurityGroup):
    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    security_group_ingress = [InstanceSecurityGroupEgress]
    vpc_id = VPC


class RouteTablePublic(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC


class InternetGateway(ec2.InternetGateway):
    resource: ec2.InternetGateway


class VPCGatewayAttachment(ec2.VPCGatewayAttachment):
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class RouteTablePublicInternetRoute(ec2.Route):
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = RouteTablePublic
    depends_on = [VPCGatewayAttachment]
