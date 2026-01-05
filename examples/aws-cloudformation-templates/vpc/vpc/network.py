"""Network resources: VPC, PublicSubnet1, InternetGateway, PrivateSubnet1RouteTable, PrivateSubnet2RouteTable, PublicSubnet2RouteTable, VPCGW, PublicSubnet2DefaultRoute, PublicSubnet2EIP, PublicSubnet2, PublicSubnet2RouteTableAssociation, PublicSubnet2NATGateway, PrivateSubnet2DefaultRoute, PrivateSubnet2Subnet, PrivateSubnet2RouteTableAssociation, PublicSubnet1RouteTable, PrivateSubnet1Subnet, PublicSubnet1RouteTableAssociation, PublicSubnet1EIP, PublicSubnet1DefaultRoute, PublicSubnet1NATGateway, PrivateSubnet1DefaultRoute, PrivateSubnet1RouteTableAssociation."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


class PublicSubnet1(ec2.Subnet):
    availability_zone = Select(0, GetAZs())
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = VPC


class InternetGateway(ec2.InternetGateway):
    pass


class PrivateSubnet1RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PrivateSubnet2RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PublicSubnet2RouteTable(ec2.RouteTable):
    vpc_id = VPC


class VPCGW(ec2.VPCGatewayAttachment):
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class PublicSubnet2DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicSubnet2RouteTable
    depends_on = [VPCGW]


class PublicSubnet2EIP(ec2.EIP):
    domain = 'vpc'


class PublicSubnet2(ec2.Subnet):
    availability_zone = Select(1, GetAZs())
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = VPC


class PublicSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicSubnet2RouteTable
    subnet_id = PublicSubnet2


class PublicSubnet2NATGateway(ec2.NatGateway):
    allocation_id = PublicSubnet2EIP.AllocationId
    subnet_id = PublicSubnet2
    depends_on = [PublicSubnet2DefaultRoute, PublicSubnet2RouteTableAssociation]


class PrivateSubnet2DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = PublicSubnet2NATGateway
    route_table_id = PrivateSubnet2RouteTable


class PrivateSubnet2Subnet(ec2.Subnet):
    availability_zone = Select(1, GetAZs())
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = VPC


class PrivateSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateSubnet2RouteTable
    subnet_id = PrivateSubnet2Subnet


class PublicSubnet1RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PrivateSubnet1Subnet(ec2.Subnet):
    availability_zone = Select(0, GetAZs())
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = VPC


class PublicSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicSubnet1RouteTable
    subnet_id = PublicSubnet1


class PublicSubnet1EIP(ec2.EIP):
    domain = 'vpc'


class PublicSubnet1DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicSubnet1RouteTable
    depends_on = [VPCGW]


class PublicSubnet1NATGateway(ec2.NatGateway):
    allocation_id = PublicSubnet1EIP.AllocationId
    subnet_id = PublicSubnet1
    depends_on = [PublicSubnet1DefaultRoute, PublicSubnet1RouteTableAssociation]


class PrivateSubnet1DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = PublicSubnet1NATGateway
    route_table_id = PrivateSubnet1RouteTable


class PrivateSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateSubnet1RouteTable
    subnet_id = PrivateSubnet1Subnet
