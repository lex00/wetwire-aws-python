"""Network resources: VPC, PublicRouteTable, InternetGateway, RouteInternetGateway, PrivateSubnet3, PublicSubnet1, EIP1, EIP3, ControlPlaneSecurityGroup, PrivateSubnet1, PublicSubnet3, PrivateSubnet2, PublicSubnet2, NATGateway1, PublicRouteTableAssociation2, AttachGateway, NATGateway3, PrivateRouteTable3, PrivateRoute3, PrivateRouteTable1, ControlPlaneSecurityGroupIngress, PrivateRouteTable2, PrivateRouteTableAssociation2, PublicRouteTableAssociation3, EIP2, PrivateRouteTableAssociation1, NATGateway2, PrivateRoute2, PublicRouteTableAssociation1, PrivateRoute1, PrivateRouteTableAssociation3."""

from . import *  # noqa: F403


class VPCAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-vpc')


class VPC(ec2.VPC):
    cidr_block = VPCCidrBlock
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'
    tags = [VPCAssociationParameter]


class PublicRouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-route-table')


class PublicRouteTable(ec2.RouteTable):
    vpc_id = VPC
    tags = [PublicRouteTableAssociationParameter]


class InternetGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-ig')


class InternetGateway(ec2.InternetGateway):
    tags = [InternetGatewayAssociationParameter]


class RouteInternetGateway(ec2.Route):
    route_table_id = PublicRouteTable
    gateway_id = InternetGateway
    destination_cidr_block = '0.0.0.0/0'


class PrivateSubnet3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet3')


class PrivateSubnet3(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = PrivateCidrBlock3
    map_public_ip_on_launch = False
    tags = [PrivateSubnet3AssociationParameter]


class PublicSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet1')


class PublicSubnet1AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


class PublicSubnet1(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = PublicCidrBlock1
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1]


class EIP1(ec2.EIP):
    domain = 'vpc'


class EIP3(ec2.EIP):
    domain = 'vpc'


class ControlPlaneSecurityGroup(ec2.SecurityGroup):
    group_description = 'Communication between the control plane and worker nodegroups'
    vpc_id = VPC
    group_name = Sub('${AWS::StackName}-eks-control-plane-sg')


class PrivateSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet1')


class PrivateSubnet1(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = PrivateCidrBlock1
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]


class PublicSubnet3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet3')


class PublicSubnet3AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


class PublicSubnet3(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = PublicCidrBlock3
    tags = [PublicSubnet3AssociationParameter, PublicSubnet3AssociationParameter1]


class PrivateSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet2')


class PrivateSubnet2(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = PrivateCidrBlock2
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]


class PublicSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet2')


class PublicSubnet2AssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


class PublicSubnet2(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = PublicCidrBlock2
    tags = [PublicSubnet2AssociationParameter, PublicSubnet2AssociationParameter1]


class NATGateway1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw1')


class NATGateway1(ec2.NatGateway):
    allocation_id = EIP1.AllocationId
    subnet_id = PublicSubnet1
    tags = [NATGateway1AssociationParameter]


class PublicRouteTableAssociation2(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class AttachGateway(ec2.VPCGatewayAttachment):
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class NATGateway3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw3')


class NATGateway3(ec2.NatGateway):
    allocation_id = EIP3.AllocationId
    subnet_id = PublicSubnet3
    tags = [NATGateway3AssociationParameter]


class PrivateRouteTable3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table3')


class PrivateRouteTable3(ec2.RouteTable):
    vpc_id = VPC
    tags = [PrivateRouteTable3AssociationParameter]


class PrivateRoute3(ec2.Route):
    route_table_id = PrivateRouteTable3
    nat_gateway_id = NATGateway3
    destination_cidr_block = '0.0.0.0/0'


class PrivateRouteTable1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table1')


class PrivateRouteTable1(ec2.RouteTable):
    vpc_id = VPC
    tags = [PrivateRouteTable1AssociationParameter]


class ControlPlaneSecurityGroupIngress(ec2.SecurityGroupIngress):
    group_id = ControlPlaneSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = ControlPlaneSecurityGroup.GroupId
    source_security_group_owner_id = AWS_ACCOUNT_ID


class PrivateRouteTable2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table2')


class PrivateRouteTable2(ec2.RouteTable):
    vpc_id = VPC
    tags = [PrivateRouteTable2AssociationParameter]


class PrivateRouteTableAssociation2(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class PublicRouteTableAssociation3(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet3


class EIP2(ec2.EIP):
    domain = 'vpc'


class PrivateRouteTableAssociation1(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1


class NATGateway2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw2')


class NATGateway2(ec2.NatGateway):
    allocation_id = EIP2.AllocationId
    subnet_id = PublicSubnet2
    tags = [NATGateway2AssociationParameter]


class PrivateRoute2(ec2.Route):
    route_table_id = PrivateRouteTable2
    nat_gateway_id = NATGateway2
    destination_cidr_block = '0.0.0.0/0'


class PublicRouteTableAssociation1(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class PrivateRoute1(ec2.Route):
    route_table_id = PrivateRouteTable1
    nat_gateway_id = NATGateway1
    destination_cidr_block = '0.0.0.0/0'


class PrivateRouteTableAssociation3(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable3
    subnet_id = PrivateSubnet3
