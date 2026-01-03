"""Network resources: VPC, DBSubnet1, InternetGateway, DBSubnet2, AuroraSecurityGroup, DMSSecurityGroup, RouteTable, AttachGateway, Route, SubnetRouteTableAssociation, SubnetRouteTableAssociation1."""

from . import *  # noqa: F403


class VPCAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


class VPCAssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = AWS_STACK_NAME


class VPC:
    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    tags = [VPCAssociationParameter, VPCAssociationParameter1]


class DBSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


class DBSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    cidr_block = '10.0.0.0/26'
    availability_zone = Select(0, GetAZs())
    tags = [DBSubnet1AssociationParameter]


class InternetGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


class InternetGateway:
    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter]


class DBSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


class DBSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    cidr_block = '10.0.0.64/26'
    availability_zone = Select(1, GetAZs())
    tags = [DBSubnet2AssociationParameter]


class AuroraSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '3306'
    to_port = '3306'
    cidr_ip = ClientIP


class AuroraSecurityGroupEgress1:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '3306'
    to_port = '3306'
    cidr_ip = '10.0.0.0/24'


class AuroraSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Security group for Aurora SampleDB DB Instance'
    group_name = 'Aurora SampleDB Security Group'
    vpc_id = VPC
    security_group_ingress = [AuroraSecurityGroupEgress, AuroraSecurityGroupEgress1]


class DMSSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Security group for DMS Instance'
    group_name = 'DMS Demo Security Group'
    vpc_id = VPC


class RouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


class RouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [RouteTableAssociationParameter]


class AttachGateway:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class Route:
    resource: ec2.Route
    route_table_id = RouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [AttachGateway]


class SubnetRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = DBSubnet1
    route_table_id = RouteTable


class SubnetRouteTableAssociation1:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = DBSubnet2
    route_table_id = RouteTable
