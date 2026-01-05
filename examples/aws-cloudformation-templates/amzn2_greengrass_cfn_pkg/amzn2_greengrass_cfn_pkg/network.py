"""Network resources: VPC, RouteTablePublic, InternetGateway, VPCGatewayAttachment, RouteTablePublicInternetRoute, InstanceSecurityGroup, RouteTableAssociationAPublic."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    cidr_block = '172.31.0.0/24'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


class RouteTablePublic:
    resource: ec2.RouteTable
    vpc_id = VPC


class InternetGateway:
    resource: ec2.InternetGateway


class VPCGatewayAttachment:
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class RouteTablePublicInternetRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = RouteTablePublic
    depends_on = [VPCGatewayAttachment]


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    cidr_ip = SecurityAccessCIDR
    from_port = 22
    ip_protocol = 'tcp'
    to_port = 22


class InstanceSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    security_group_ingress = [InstanceSecurityGroupEgress]
    vpc_id = VPC


class RouteTableAssociationAPublic:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = RouteTablePublic
    subnet_id = SubnetAPublic
