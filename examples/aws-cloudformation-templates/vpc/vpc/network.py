"""Network resources: VPC, InternetGateway, VPCGW, PublicSubnet1, PrivateSubnet2RouteTable, PublicSubnet1RouteTable, PublicSubnet1DefaultRoute, PublicSubnet1RouteTableAssociation, PublicSubnet1EIP, PublicSubnet1NATGateway, PrivateSubnet1RouteTable, PrivateSubnet1DefaultRoute, PrivateSubnet2Subnet, PublicSubnet2RouteTable, PublicSubnet2, PublicSubnet2RouteTableAssociation, PrivateSubnet1Subnet, PrivateSubnet1RouteTableAssociation, PublicSubnet2EIP, PublicSubnet2DefaultRoute, PublicSubnet2NATGateway, PrivateSubnet2RouteTableAssociation, PrivateSubnet2DefaultRoute."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


class InternetGateway(ec2.InternetGateway):
    pass


class VPCGW(ec2.VPCGatewayAttachment):
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class PublicSubnet1(ec2.Subnet):
    availability_zone = Select(0, GetAZs())
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = VPC


class PrivateSubnet2RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PublicSubnet1RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PublicSubnet1DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicSubnet1RouteTable
    depends_on = [VPCGW]


class PublicSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicSubnet1RouteTable
    subnet_id = PublicSubnet1


class PublicSubnet1EIP(ec2.EIP):
    domain = 'vpc'


class PublicSubnet1NATGateway(ec2.NatGateway):
    allocation_id = PublicSubnet1EIP.AllocationId
    subnet_id = PublicSubnet1
    depends_on = [PublicSubnet1DefaultRoute, PublicSubnet1RouteTableAssociation]


class PrivateSubnet1RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PrivateSubnet1DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = PublicSubnet1NATGateway
    route_table_id = PrivateSubnet1RouteTable


class PrivateSubnet2Subnet(ec2.Subnet):
    availability_zone = Select(1, GetAZs())
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = VPC


class PublicSubnet2RouteTable(ec2.RouteTable):
    vpc_id = VPC


class PublicSubnet2(ec2.Subnet):
    availability_zone = Select(1, GetAZs())
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = VPC


class PublicSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicSubnet2RouteTable
    subnet_id = PublicSubnet2


class PrivateSubnet1Subnet(ec2.Subnet):
    availability_zone = Select(0, GetAZs())
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = VPC


class PrivateSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateSubnet1RouteTable
    subnet_id = PrivateSubnet1Subnet


class PublicSubnet2EIP(ec2.EIP):
    domain = 'vpc'


class PublicSubnet2DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    route_table_id = PublicSubnet2RouteTable
    depends_on = [VPCGW]


class PublicSubnet2NATGateway(ec2.NatGateway):
    allocation_id = PublicSubnet2EIP.AllocationId
    subnet_id = PublicSubnet2
    depends_on = [PublicSubnet2DefaultRoute, PublicSubnet2RouteTableAssociation]


class PrivateSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateSubnet2RouteTable
    subnet_id = PrivateSubnet2Subnet


class PrivateSubnet2DefaultRoute(ec2.Route):
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = PublicSubnet2NATGateway
    route_table_id = PrivateSubnet2RouteTable
