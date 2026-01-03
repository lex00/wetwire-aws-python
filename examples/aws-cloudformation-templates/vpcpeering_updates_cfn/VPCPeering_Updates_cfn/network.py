"""Network resources: PeerIngressRule2, PeerRoute3, PeerRoute4, PeerIngressRule1, PeerRoute1, PeerRoute5, PeerIngressRule6, PeerIngressRule5, PeerRoute6, PeerIngressRule3, PeerRoute2, PeerIngressRule4."""

from . import *  # noqa: F403


class PeerIngressRule2:
    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer CIDR, ${PeerName}')
    group_id = Select(1, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '2SecurityGroupCondition'


class PeerRoute3:
    resource: ec2.Route
    route_table_id = Select(2, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '3RouteTableCondition'


class PeerRoute4:
    resource: ec2.Route
    route_table_id = Select(3, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '4RouteTableCondition'


class PeerIngressRule1:
    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(0, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR


class PeerRoute1:
    resource: ec2.Route
    route_table_id = Select(0, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId


class PeerRoute5:
    resource: ec2.Route
    route_table_id = Select(4, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '5RouteTableCondition'


class PeerIngressRule6:
    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(5, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '6SecurityGroupCondition'


class PeerIngressRule5:
    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(4, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '5SecurityGroupCondition'


class PeerRoute6:
    resource: ec2.Route
    route_table_id = Select(5, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '6RouteTableCondition'


class PeerIngressRule3:
    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(2, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '3SecurityGroupCondition'


class PeerRoute2:
    resource: ec2.Route
    route_table_id = Select(1, Split(',', RouteTableIds))
    destination_cidr_block = PeerVPCCIDR
    vpc_peering_connection_id = VPCPeeringConnectionId
    condition = '2RouteTableCondition'


class PeerIngressRule4:
    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(3, SecurityGroupIds)
    cidr_ip = PeerVPCCIDR
    condition = '4SecurityGroupCondition'
