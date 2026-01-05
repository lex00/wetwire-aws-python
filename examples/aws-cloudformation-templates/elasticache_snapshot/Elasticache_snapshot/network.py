"""Network resources: VPC, PublicInternetRouteTable, PublicSubnetA, PublicSubnetARouteTableAssociation, InternetGateway, VPCGatewayAttachment, PublicSubnetB, RedisSecurityGroup, PublicInternetRoute, PublicSubnetBRouteTableAssociation."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    cidr_block = '10.0.0.0/24'


class PublicInternetRouteTable(ec2.RouteTable):
    vpc_id = VPC


class PublicSubnetA(ec2.Subnet):
    availability_zone = FindInMap("AWSRegion2AZ", AWS_REGION, 'A')
    cidr_block = '10.0.0.0/25'
    vpc_id = VPC


class PublicSubnetARouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicInternetRouteTable
    subnet_id = PublicSubnetA


class InternetGateway(ec2.InternetGateway):
    pass


class VPCGatewayAttachment(ec2.VPCGatewayAttachment):
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class PublicSubnetB(ec2.Subnet):
    availability_zone = FindInMap("AWSRegion2AZ", AWS_REGION, 'B')
    cidr_block = '10.0.0.128/25'
    vpc_id = VPC


class RedisSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '6379'
    to_port = '6379'
    cidr_ip = '192.168.1.0/32'


class RedisSecurityGroup(ec2.SecurityGroup):
    group_description = 'RedisSecurityGroup'
    vpc_id = VPC
    security_group_ingress = [RedisSecurityGroupEgress]


class PublicInternetRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicInternetRouteTable
    depends_on = [InternetGateway, PublicInternetRouteTable]


class PublicSubnetBRouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicInternetRouteTable
    subnet_id = PublicSubnetB
