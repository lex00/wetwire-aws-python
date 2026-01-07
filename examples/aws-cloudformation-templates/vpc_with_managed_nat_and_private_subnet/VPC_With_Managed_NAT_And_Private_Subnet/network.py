"""Network resources: InternetGateway, VPC, PrivateRouteTable0, PublicSubnet0, ElasticIP0, NATGateway0, PrivateRouteToInternet0, PublicNetworkAcl, InboundHTTPPublicNetworkAclEntry, OutboundPublicNetworkAclEntry, PublicSubnet1, PublicSubnetNetworkAclAssociation1, GatewayToInternet, PublicRouteTable, PublicSubnetRouteTableAssociation0, PublicSubnetNetworkAclAssociation0, PrivateSubnet1, PrivateRouteTable1, ElasticIP1, NATGateway1, PrivateRouteToInternet1, PublicSubnetRouteTableAssociation1, PrivateSubnet0, PrivateSubnetRouteTableAssociation0, PublicRoute, PrivateSubnetRouteTableAssociation1."""

from . import *  # noqa: F403


class InternetGatewayAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class InternetGatewayAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Public'


class InternetGatewayAssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-IGW',
])


class InternetGateway(ec2.InternetGateway):
    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter, InternetGatewayAssociationParameter1, InternetGatewayAssociationParameter2]


class VPCAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class VPCAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Public'


class VPCAssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = VPCName


class VPC(ec2.VPC):
    resource: ec2.VPC
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')
    tags = [VPCAssociationParameter, VPCAssociationParameter1, VPCAssociationParameter2]


class PrivateRouteTable0AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-private-route-table-0',
])


class PrivateRouteTable0(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable0AssociationParameter]


class PublicSubnet0AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class PublicSubnet0AssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Public'


class PublicSubnet0AssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-public-',
    Select(0, GetAZs()),
])


class PublicSubnet0(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public0', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet0AssociationParameter, PublicSubnet0AssociationParameter1, PublicSubnet0AssociationParameter2]


class ElasticIP0(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'


class NATGateway0(ec2.NatGateway):
    resource: ec2.NatGateway
    allocation_id = ElasticIP0.AllocationId
    subnet_id = PublicSubnet0


class PrivateRouteToInternet0(ec2.Route):
    resource: ec2.Route
    route_table_id = PrivateRouteTable0
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NATGateway0


class PublicNetworkAclAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class PublicNetworkAclAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Public'


class PublicNetworkAclAssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-public-nacl',
])


class PublicNetworkAcl(ec2.NetworkAcl):
    resource: ec2.NetworkAcl
    vpc_id = VPC
    tags = [PublicNetworkAclAssociationParameter, PublicNetworkAclAssociationParameter1, PublicNetworkAclAssociationParameter2]


class InboundHTTPPublicNetworkAclEntryPortRange(ec2.NetworkAclEntry.PortRange):
    from_ = '0'
    to = '65535'


class InboundHTTPPublicNetworkAclEntry(ec2.NetworkAclEntry):
    resource: ec2.NetworkAclEntry
    network_acl_id = PublicNetworkAcl
    rule_number = '100'
    protocol = '-1'
    rule_action = 'allow'
    egress = 'false'
    cidr_block = '0.0.0.0/0'
    port_range = InboundHTTPPublicNetworkAclEntryPortRange


class OutboundPublicNetworkAclEntryPortRange(ec2.NetworkAclEntry.PortRange):
    from_ = '0'
    to = '65535'


class OutboundPublicNetworkAclEntry(ec2.NetworkAclEntry):
    resource: ec2.NetworkAclEntry
    network_acl_id = PublicNetworkAcl
    rule_number = '100'
    protocol = '-1'
    rule_action = 'allow'
    egress = 'true'
    cidr_block = '0.0.0.0/0'
    port_range = OutboundPublicNetworkAclEntryPortRange


class PublicSubnet1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class PublicSubnet1AssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Public'


class PublicSubnet1AssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-public-',
    Select(1, GetAZs()),
])


class PublicSubnet1(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public1', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1, PublicSubnet1AssociationParameter2]


class PublicSubnetNetworkAclAssociation1(ec2.SubnetNetworkAclAssociation):
    resource: ec2.SubnetNetworkAclAssociation
    subnet_id = PublicSubnet1
    network_acl_id = PublicNetworkAcl


class GatewayToInternet(ec2.VPCGatewayAttachment):
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class PublicRouteTableAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class PublicRouteTableAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Public'


class PublicRouteTableAssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-public-route-table',
])


class PublicRouteTable(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PublicRouteTableAssociationParameter, PublicRouteTableAssociationParameter1, PublicRouteTableAssociationParameter2]


class PublicSubnetRouteTableAssociation0(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnet0
    route_table_id = PublicRouteTable


class PublicSubnetNetworkAclAssociation0(ec2.SubnetNetworkAclAssociation):
    resource: ec2.SubnetNetworkAclAssociation
    subnet_id = PublicSubnet0
    network_acl_id = PublicNetworkAcl


class PrivateSubnet1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class PrivateSubnet1AssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Private'


class PrivateSubnet1AssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-private-',
    Select(1, GetAZs()),
])


class PrivateSubnet1(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Private1', 'CIDR')
    tags = [PrivateSubnet1AssociationParameter, PrivateSubnet1AssociationParameter1, PrivateSubnet1AssociationParameter2]


class PrivateRouteTable1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-private-route-table-1',
])


class PrivateRouteTable1(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable1AssociationParameter]


class ElasticIP1(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'


class NATGateway1(ec2.NatGateway):
    resource: ec2.NatGateway
    allocation_id = ElasticIP1.AllocationId
    subnet_id = PublicSubnet1


class PrivateRouteToInternet1(ec2.Route):
    resource: ec2.Route
    route_table_id = PrivateRouteTable1
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NATGateway1


class PublicSubnetRouteTableAssociation1(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnet1
    route_table_id = PublicRouteTable


class PrivateSubnet0AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Application'
    value = AWS_STACK_NAME


class PrivateSubnet0AssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Network'
    value = 'Private'


class PrivateSubnet0AssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('', [
    VPCName,
    '-private-',
    Select(0, GetAZs()),
])


class PrivateSubnet0(ec2.Subnet):
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Private0', 'CIDR')
    tags = [PrivateSubnet0AssociationParameter, PrivateSubnet0AssociationParameter1, PrivateSubnet0AssociationParameter2]


class PrivateSubnetRouteTableAssociation0(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PrivateSubnet0
    route_table_id = PrivateRouteTable0


class PublicRoute(ec2.Route):
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayToInternet]


class PrivateSubnetRouteTableAssociation1(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PrivateSubnet1
    route_table_id = PrivateRouteTable1
