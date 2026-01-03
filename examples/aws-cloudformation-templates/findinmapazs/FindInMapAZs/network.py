"""Network resources: VPC, PublicSubnet1, PublicRouteTable, PublicSubnet1RouteTableAssociation, PrivateRouteTable1, InternetGateway, InternetGatewayAttachment, DefaultPublicRoute, PublicSubnet2, NatGateway2EIP, NatGateway2, PrivateRouteTable2, DefaultPrivateRoute2, NatGateway1EIP, NatGateway1, DefaultPrivateRoute1, NoIngressSecurityGroup, PublicSubnet2RouteTableAssociation, PrivateSubnet2, PrivateSubnet2RouteTableAssociation, PrivateSubnet1, PrivateSubnet1RouteTableAssociation."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    cidr_block = VpcCIDR
    enable_dns_support = True
    enable_dns_hostnames = True


class PublicSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet1CIDR
    map_public_ip_on_launch = True


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class PrivateRouteTable1:
    resource: ec2.RouteTable
    vpc_id = VPC


class InternetGateway:
    resource: ec2.InternetGateway


class InternetGatewayAttachment:
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class DefaultPublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [InternetGatewayAttachment]


class PublicSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet2CIDR
    map_public_ip_on_launch = True


class NatGateway2EIP:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class NatGateway2:
    resource: ec2.NatGateway
    allocation_id = NatGateway2EIP.AllocationId
    subnet_id = PublicSubnet2


class PrivateRouteTable2:
    resource: ec2.RouteTable
    vpc_id = VPC


class DefaultPrivateRoute2:
    resource: ec2.Route
    route_table_id = PrivateRouteTable2
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway2


class NatGateway1EIP:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class NatGateway1:
    resource: ec2.NatGateway
    allocation_id = NatGateway1EIP.AllocationId
    subnet_id = PublicSubnet1


class DefaultPrivateRoute1:
    resource: ec2.Route
    route_table_id = PrivateRouteTable1
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway1


class NoIngressSecurityGroup:
    resource: ec2.SecurityGroup
    group_name = 'no-ingress-sg'
    group_description = 'Security group with no ingress rule'
    vpc_id = VPC


class PublicSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PrivateSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet2CIDR
    map_public_ip_on_launch = False


class PrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class PrivateSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet1CIDR
    map_public_ip_on_launch = False


class PrivateSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1
