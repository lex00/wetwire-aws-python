"""Network resources: VPC, PublicSubnet2, PublicSubnet2RouteTable, PublicSubnet2RouteTableAssociation, PublicSubnet1EIP, PublicSubnet1, PrivateSubnet1RouteTable, PrivateSubnet1Subnet, PrivateSubnet1RouteTableAssociation, InternetGateway, VPCGW, PublicSubnet2EIP, PublicSubnet1RouteTable, PublicSubnet1DefaultRoute, PublicSubnet1RouteTableAssociation, PublicSubnet1NATGateway, PrivateSubnet1DefaultRoute, PublicSubnet2DefaultRoute, PublicSubnet2NATGateway, PrivateSubnet2RouteTable, PrivateSubnet2DefaultRoute, PrivateSubnet2Subnet, PrivateSubnet2RouteTableAssociation."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


class PublicSubnet2:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs())
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = VPC


class PublicSubnet2RouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicSubnet2RouteTable
    subnet_id = PublicSubnet2


class PublicSubnet1EIP:
    resource: ec2.EIP
    domain = 'vpc'


class PublicSubnet1:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs())
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = VPC


class PrivateSubnet1RouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PrivateSubnet1Subnet:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs())
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = VPC


class PrivateSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateSubnet1RouteTable
    subnet_id = PrivateSubnet1Subnet


class InternetGateway:
    resource: ec2.InternetGateway


class VPCGW:
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class PublicSubnet2EIP:
    resource: ec2.EIP
    domain = 'vpc'


class PublicSubnet1RouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet1DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicSubnet1RouteTable
    depends_on = [VPCGW]


class PublicSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicSubnet1RouteTable
    subnet_id = PublicSubnet1


class PublicSubnet1NATGateway:
    resource: ec2.NatGateway
    allocation_id = PublicSubnet1EIP.AllocationId
    subnet_id = PublicSubnet1
    depends_on = [PublicSubnet1DefaultRoute, PublicSubnet1RouteTableAssociation]


class PrivateSubnet1DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = PublicSubnet1NATGateway
    route_table_id = PrivateSubnet1RouteTable


class PublicSubnet2DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicSubnet2RouteTable
    depends_on = [VPCGW]


class PublicSubnet2NATGateway:
    resource: ec2.NatGateway
    allocation_id = PublicSubnet2EIP.AllocationId
    subnet_id = PublicSubnet2
    depends_on = [PublicSubnet2DefaultRoute, PublicSubnet2RouteTableAssociation]


class PrivateSubnet2RouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PrivateSubnet2DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = PublicSubnet2NATGateway
    route_table_id = PrivateSubnet2RouteTable


class PrivateSubnet2Subnet:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs())
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = VPC


class PrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateSubnet2RouteTable
    subnet_id = PrivateSubnet2Subnet
