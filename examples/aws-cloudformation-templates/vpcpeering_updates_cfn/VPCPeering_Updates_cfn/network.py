"""Network resources: PeerIngressRule5, PeerIngressRule3, PeerIngressRule6, PeerRoute4, PeerIngressRule2, PeerRoute5, PeerIngressRule4, PeerRoute1, PeerRoute3, PeerIngressRule1, PeerRoute6, PeerRoute2."""

from . import *  # noqa: F403


class PeerIngressRule5(ec2.SecurityGroupIngress):
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(4, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '5SecurityGroupCondition'


class PeerIngressRule3(ec2.SecurityGroupIngress):
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(2, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '3SecurityGroupCondition'


class PeerIngressRule6(ec2.SecurityGroupIngress):
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(5, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '6SecurityGroupCondition'


class PeerRoute4(ec2.Route):
    route_table_id = Select(3, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '4RouteTableCondition'


class PeerIngressRule2(ec2.SecurityGroupIngress):
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer CIDR, ${PeerName}')
    group_id = Select(1, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '2SecurityGroupCondition'


class PeerRoute5(ec2.Route):
    route_table_id = Select(4, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '5RouteTableCondition'


class PeerIngressRule4(ec2.SecurityGroupIngress):
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(3, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '4SecurityGroupCondition'


class PeerRoute1(ec2.Route):
    route_table_id = Select(0, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId


class PeerRoute3(ec2.Route):
    route_table_id = Select(2, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '3RouteTableCondition'


class PeerIngressRule1(ec2.SecurityGroupIngress):
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(0, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR


class PeerRoute6(ec2.Route):
    route_table_id = Select(5, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '6RouteTableCondition'


class PeerRoute2(ec2.Route):
    route_table_id = Select(1, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '2RouteTableCondition'
