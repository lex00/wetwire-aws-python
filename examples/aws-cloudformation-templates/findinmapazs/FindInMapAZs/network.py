"""Network resources: InternetGateway, VPC, InternetGatewayAttachment, NatGateway2EIP, NatGateway1EIP, PublicRouteTable, PublicSubnet2, PublicSubnet2RouteTableAssociation, PrivateRouteTable2, PublicSubnet1, NatGateway1, PublicSubnet1RouteTableAssociation, NatGateway2, DefaultPrivateRoute2, PrivateSubnet2, DefaultPublicRoute, PrivateRouteTable1, PrivateSubnet1, PrivateSubnet1RouteTableAssociation, DefaultPrivateRoute1, PrivateSubnet2RouteTableAssociation, NoIngressSecurityGroup."""

from . import *  # noqa: F403


class InternetGateway:
    resource: ec2.InternetGateway


class VPC:
    resource: ec2.VPC
    cidr_block = VpcCIDR
    enable_dns_support = True
    enable_dns_hostnames = True


class InternetGatewayAttachment:
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class NatGateway2EIP:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class NatGateway1EIP:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet2CIDR
    map_public_ip_on_launch = True


class PublicSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PrivateRouteTable2:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet1CIDR
    map_public_ip_on_launch = True


class NatGateway1:
    resource: ec2.NatGateway
    allocation_id = NatGateway1EIP.AllocationId
    subnet_id = PublicSubnet1


class PublicSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class NatGateway2:
    resource: ec2.NatGateway
    allocation_id = NatGateway2EIP.AllocationId
    subnet_id = PublicSubnet2


class DefaultPrivateRoute2:
    resource: ec2.Route
    route_table_id = PrivateRouteTable2
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway2


class PrivateSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet2CIDR
    map_public_ip_on_launch = False


class DefaultPublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [InternetGatewayAttachment]


class PrivateRouteTable1:
    resource: ec2.RouteTable
    vpc_id = VPC


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


class DefaultPrivateRoute1:
    resource: ec2.Route
    route_table_id = PrivateRouteTable1
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway1


class PrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class NoIngressSecurityGroup:
    resource: ec2.SecurityGroup
    group_name = 'no-ingress-sg'
    group_description = 'Security group with no ingress rule'
    vpc_id = VPC
