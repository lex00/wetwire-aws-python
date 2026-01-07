"""Network resources: VPC, PrivateRouteTable2, PublicSubnet2, InternetGateway, InternetGatewayAttachment, NatGateway2EIP, NatGateway2, PrivateSubnet2, PublicRouteTable, PublicSubnet2RouteTableAssociation, PrivateRouteTable1, PrivateSubnet1, PrivateSubnet1RouteTableAssociation, PublicSubnet1, NatGateway1EIP, NatGateway1, PrivateSubnet2RouteTableAssociation, PublicSubnet1RouteTableAssociation, DefaultPublicRoute, DefaultPrivateRoute2, DefaultPrivateRoute1, NoIngressSecurityGroup."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    resource: ec2.VPC
    cidr_block = VpcCIDR
    enable_dns_support = True
    enable_dns_hostnames = True


class PrivateRouteTable2(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet2(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet2CIDR
    map_public_ip_on_launch = True


class InternetGateway(ec2.InternetGateway):
    resource: ec2.InternetGateway


class InternetGatewayAttachment(ec2.VPCGatewayAttachment):
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class NatGateway2EIP(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class NatGateway2(ec2.NatGateway):
    resource: ec2.NatGateway
    allocation_id = NatGateway2EIP.AllocationId
    subnet_id = PublicSubnet2


class PrivateSubnet2(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet2CIDR
    map_public_ip_on_launch = False


class PublicRouteTable(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PrivateRouteTable1(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC


class PrivateSubnet1(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PrivateSubnet1CIDR
    map_public_ip_on_launch = False


class PrivateSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1


class PublicSubnet1(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = PublicSubnet1CIDR
    map_public_ip_on_launch = True


class NatGateway1EIP(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [InternetGatewayAttachment]


class NatGateway1(ec2.NatGateway):
    resource: ec2.NatGateway
    allocation_id = NatGateway1EIP.AllocationId
    subnet_id = PublicSubnet1


class PrivateSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class PublicSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class DefaultPublicRoute(ec2.Route):
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [InternetGatewayAttachment]


class DefaultPrivateRoute2(ec2.Route):
    resource: ec2.Route
    route_table_id = PrivateRouteTable2
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway2


class DefaultPrivateRoute1(ec2.Route):
    resource: ec2.Route
    route_table_id = PrivateRouteTable1
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGateway1


class NoIngressSecurityGroup(ec2.SecurityGroup):
    resource: ec2.SecurityGroup
    group_name = 'no-ingress-sg'
    group_description = 'Security group with no ingress rule'
    vpc_id = VPC
