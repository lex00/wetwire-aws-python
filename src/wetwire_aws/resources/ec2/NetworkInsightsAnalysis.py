"""PropertyTypes for AWS::EC2::NetworkInsightsAnalysis."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdditionalDetail(PropertyType):
    additional_detail_type: str | None = None
    component: AnalysisComponent | None = None
    load_balancers: list[AnalysisComponent] = field(default_factory=list)
    service_name: str | None = None


@dataclass
class AlternatePathHint(PropertyType):
    component_arn: str | None = None
    component_id: str | None = None


@dataclass
class AnalysisAclRule(PropertyType):
    cidr: str | None = None
    egress: bool | None = None
    port_range: PortRange | None = None
    protocol: str | None = None
    rule_action: str | None = None
    rule_number: int | None = None


@dataclass
class AnalysisComponent(PropertyType):
    arn: str | None = None
    id: str | None = None


@dataclass
class AnalysisLoadBalancerListener(PropertyType):
    instance_port: int | None = None
    load_balancer_port: int | None = None


@dataclass
class AnalysisLoadBalancerTarget(PropertyType):
    address: str | None = None
    availability_zone: str | None = None
    instance: AnalysisComponent | None = None
    port: int | None = None


@dataclass
class AnalysisPacketHeader(PropertyType):
    destination_addresses: list[String] = field(default_factory=list)
    destination_port_ranges: list[PortRange] = field(default_factory=list)
    protocol: str | None = None
    source_addresses: list[String] = field(default_factory=list)
    source_port_ranges: list[PortRange] = field(default_factory=list)


@dataclass
class AnalysisRouteTableRoute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_cidr": "destinationCidr",
        "destination_prefix_list_id": "destinationPrefixListId",
        "egress_only_internet_gateway_id": "egressOnlyInternetGatewayId",
        "gateway_id": "gatewayId",
        "instance_id": "instanceId",
    }

    destination_cidr: str | None = None
    destination_prefix_list_id: str | None = None
    egress_only_internet_gateway_id: str | None = None
    gateway_id: str | None = None
    instance_id: str | None = None
    nat_gateway_id: str | None = None
    network_interface_id: str | None = None
    origin: str | None = None
    state: str | None = None
    transit_gateway_id: str | None = None
    vpc_peering_connection_id: str | None = None


@dataclass
class AnalysisSecurityGroupRule(PropertyType):
    cidr: str | None = None
    direction: str | None = None
    port_range: PortRange | None = None
    prefix_list_id: str | None = None
    protocol: str | None = None
    security_group_id: str | None = None


@dataclass
class Explanation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_endpoint": "vpcEndpoint",
    }

    acl: AnalysisComponent | None = None
    acl_rule: AnalysisAclRule | None = None
    address: str | None = None
    addresses: list[String] = field(default_factory=list)
    attached_to: AnalysisComponent | None = None
    availability_zones: list[String] = field(default_factory=list)
    cidrs: list[String] = field(default_factory=list)
    classic_load_balancer_listener: AnalysisLoadBalancerListener | None = None
    component: AnalysisComponent | None = None
    component_account: str | None = None
    component_region: str | None = None
    customer_gateway: AnalysisComponent | None = None
    destination: AnalysisComponent | None = None
    destination_vpc: AnalysisComponent | None = None
    direction: str | None = None
    elastic_load_balancer_listener: AnalysisComponent | None = None
    explanation_code: str | None = None
    ingress_route_table: AnalysisComponent | None = None
    internet_gateway: AnalysisComponent | None = None
    load_balancer_arn: str | None = None
    load_balancer_listener_port: int | None = None
    load_balancer_target: AnalysisLoadBalancerTarget | None = None
    load_balancer_target_group: AnalysisComponent | None = None
    load_balancer_target_groups: list[AnalysisComponent] = field(default_factory=list)
    load_balancer_target_port: int | None = None
    missing_component: str | None = None
    nat_gateway: AnalysisComponent | None = None
    network_interface: AnalysisComponent | None = None
    packet_field: str | None = None
    port: int | None = None
    port_ranges: list[PortRange] = field(default_factory=list)
    prefix_list: AnalysisComponent | None = None
    protocols: list[String] = field(default_factory=list)
    route_table: AnalysisComponent | None = None
    route_table_route: AnalysisRouteTableRoute | None = None
    security_group: AnalysisComponent | None = None
    security_group_rule: AnalysisSecurityGroupRule | None = None
    security_groups: list[AnalysisComponent] = field(default_factory=list)
    source_vpc: AnalysisComponent | None = None
    state: str | None = None
    subnet: AnalysisComponent | None = None
    subnet_route_table: AnalysisComponent | None = None
    transit_gateway: AnalysisComponent | None = None
    transit_gateway_attachment: AnalysisComponent | None = None
    transit_gateway_route_table: AnalysisComponent | None = None
    transit_gateway_route_table_route: TransitGatewayRouteTableRoute | None = None
    vpc: AnalysisComponent | None = None
    vpc_endpoint: AnalysisComponent | None = None
    vpc_peering_connection: AnalysisComponent | None = None
    vpn_connection: AnalysisComponent | None = None
    vpn_gateway: AnalysisComponent | None = None


@dataclass
class PathComponent(PropertyType):
    acl_rule: AnalysisAclRule | None = None
    additional_details: list[AdditionalDetail] = field(default_factory=list)
    component: AnalysisComponent | None = None
    destination_vpc: AnalysisComponent | None = None
    elastic_load_balancer_listener: AnalysisComponent | None = None
    explanations: list[Explanation] = field(default_factory=list)
    inbound_header: AnalysisPacketHeader | None = None
    outbound_header: AnalysisPacketHeader | None = None
    route_table_route: AnalysisRouteTableRoute | None = None
    security_group_rule: AnalysisSecurityGroupRule | None = None
    sequence_number: int | None = None
    service_name: str | None = None
    source_vpc: AnalysisComponent | None = None
    subnet: AnalysisComponent | None = None
    transit_gateway: AnalysisComponent | None = None
    transit_gateway_route_table_route: TransitGatewayRouteTableRoute | None = None
    vpc: AnalysisComponent | None = None


@dataclass
class PortRange(PropertyType):
    from_: int | None = None
    to: int | None = None


@dataclass
class TransitGatewayRouteTableRoute(PropertyType):
    attachment_id: str | None = None
    destination_cidr: str | None = None
    prefix_list_id: str | None = None
    resource_id: str | None = None
    resource_type: str | None = None
    route_origin: str | None = None
    state: str | None = None
