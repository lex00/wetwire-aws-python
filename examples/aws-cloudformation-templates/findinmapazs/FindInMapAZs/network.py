"""Network resources: VPC, PrivateRouteTable2, InternetGateway, InternetGatewayAttachment, NatGateway2EIP, PublicSubnet2, NatGateway2, DefaultPrivateRoute2, PrivateRouteTable1, NatGateway1EIP, PublicSubnet1, NatGateway1, DefaultPrivateRoute1, PrivateSubnet2, PublicRouteTable, DefaultPublicRoute, PublicSubnet2RouteTableAssociation, PrivateSubnet2RouteTableAssociation, NoIngressSecurityGroup, PublicSubnet1RouteTableAssociation, PrivateSubnet1, PrivateSubnet1RouteTableAssociation."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    cidr_block = VpcCIDR
    enable_dns_support = True
    enable_dns_hostnames = True


class PrivateRouteTable2(ec2.RouteTable):
    vpc_id = VPC


class InternetGateway(ec2.InternetGateway):
    pass


class InternetGatewayAttachment(ec2.VPCGatewayAttachment):
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class NatGateway2EIP(ec2.EIP):
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class PublicSubnet2(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet2CIDR
    map_public_ip_on_launch = True


class NatGateway2(ec2.NatGateway):
    allocation_id = NatGateway2EIP.AllocationId
    subnet_id = PublicSubnet2


class DefaultPrivateRoute2(ec2.Route):
    route_table_id = PrivateRouteTable2
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway2


class PrivateRouteTable1(ec2.RouteTable):
    vpc_id = VPC


class NatGateway1EIP(ec2.EIP):
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class PublicSubnet1(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet1CIDR
    map_public_ip_on_launch = True


class NatGateway1(ec2.NatGateway):
    allocation_id = NatGateway1EIP.AllocationId
    subnet_id = PublicSubnet1


class DefaultPrivateRoute1(ec2.Route):
    route_table_id = PrivateRouteTable1
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway1


class PrivateSubnet2(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet2CIDR
    map_public_ip_on_launch = False


class PublicRouteTable(ec2.RouteTable):
    vpc_id = VPC


class DefaultPublicRoute(ec2.Route):
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [InternetGatewayAttachment]


class PublicSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PrivateSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class NoIngressSecurityGroup(ec2.SecurityGroup):
    group_name = 'no-ingress-sg'
    group_description = 'Security group with no ingress rule'
    vpc_id = VPC


class PublicSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class PrivateSubnet1(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet1CIDR
    map_public_ip_on_launch = False


class PrivateSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1
