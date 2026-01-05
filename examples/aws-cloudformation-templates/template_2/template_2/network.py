"""Network resources: VPC, PublicRouteTable, InternetGateway, ControlPlaneSecurityGroup, PrivateSubnet3, AttachGateway, PrivateRouteTable2, EIP2, PublicSubnet2, NATGateway2, PrivateRoute2, PrivateRouteTable3, PublicRouteTableAssociation2, PrivateRouteTable1, PrivateSubnet1, PrivateRouteTableAssociation1, RouteInternetGateway, ControlPlaneSecurityGroupIngress, EIP1, PublicSubnet1, NATGateway1, PrivateRoute1, EIP3, PublicSubnet3, PrivateSubnet2, NATGateway3, PrivateRoute3, PublicRouteTableAssociation1, PrivateRouteTableAssociation3, PublicRouteTableAssociation3, PrivateRouteTableAssociation2."""

from . import *  # noqa: F403


class VPCAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-vpc')


class VPC:
    resource: ec2.VPC
    cidr_block = VPCCidrBlock
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'
    tags = [VPCAssociationParameter]


class PublicRouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-route-table')


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PublicRouteTableAssociationParameter]


class InternetGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-ig')


class InternetGateway:
    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter]


class ControlPlaneSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Communication between the control plane and worker nodegroups'
    vpc_id = VPC
    group_name = Sub('${AWS::StackName}-eks-control-plane-sg')


class PrivateSubnet3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet3')


class PrivateSubnet3:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = PrivateCidrBlock3
    map_public_ip_on_launch = False
    tags = [PrivateSubnet3AssociationParameter]


class AttachGateway:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class PrivateRouteTable2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table2')


class PrivateRouteTable2:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable2AssociationParameter]


class EIP2:
    resource: ec2.EIP
    domain = 'vpc'


class PublicSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet2')


class PublicSubnet2AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


class PublicSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = PublicCidrBlock2
    tags = [PublicSubnet2AssociationParameter, PublicSubnet2AssociationParameter1]


class NATGateway2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw2')


class NATGateway2:
    resource: ec2.NatGateway
    allocation_id = EIP2.AllocationId
    subnet_id = PublicSubnet2
    tags = [NATGateway2AssociationParameter]


class PrivateRoute2:
    resource: ec2.Route
    route_table_id = PrivateRouteTable2
    nat_gateway_id = NATGateway2
    destination_cidr_block = '0.0.0.0/0'


class PrivateRouteTable3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table3')


class PrivateRouteTable3:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable3AssociationParameter]


class PublicRouteTableAssociation2:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PrivateRouteTable1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table1')


class PrivateRouteTable1:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable1AssociationParameter]


class PrivateSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet1')


class PrivateSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = PrivateCidrBlock1
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]


class PrivateRouteTableAssociation1:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1


class RouteInternetGateway:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    gateway_id = InternetGateway
    destination_cidr_block = '0.0.0.0/0'


class ControlPlaneSecurityGroupIngress:
    resource: ec2.SecurityGroupIngress
    group_id = ControlPlaneSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = ControlPlaneSecurityGroup.GroupId
    source_security_group_owner_id = AWS_ACCOUNT_ID


class EIP1:
    resource: ec2.EIP
    domain = 'vpc'


class PublicSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet1')


class PublicSubnet1AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


class PublicSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = PublicCidrBlock1
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1]


class NATGateway1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw1')


class NATGateway1:
    resource: ec2.NatGateway
    allocation_id = EIP1.AllocationId
    subnet_id = PublicSubnet1
    tags = [NATGateway1AssociationParameter]


class PrivateRoute1:
    resource: ec2.Route
    route_table_id = PrivateRouteTable1
    nat_gateway_id = NATGateway1
    destination_cidr_block = '0.0.0.0/0'


class EIP3:
    resource: ec2.EIP
    domain = 'vpc'


class PublicSubnet3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet3')


class PublicSubnet3AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


class PublicSubnet3:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = PublicCidrBlock3
    tags = [PublicSubnet3AssociationParameter, PublicSubnet3AssociationParameter1]


class PrivateSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet2')


class PrivateSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = PrivateCidrBlock2
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]


class NATGateway3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw3')


class NATGateway3:
    resource: ec2.NatGateway
    allocation_id = EIP3.AllocationId
    subnet_id = PublicSubnet3
    tags = [NATGateway3AssociationParameter]


class PrivateRoute3:
    resource: ec2.Route
    route_table_id = PrivateRouteTable3
    nat_gateway_id = NATGateway3
    destination_cidr_block = '0.0.0.0/0'


class PublicRouteTableAssociation1:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class PrivateRouteTableAssociation3:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable3
    subnet_id = PrivateSubnet3


class PublicRouteTableAssociation3:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet3


class PrivateRouteTableAssociation2:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2
