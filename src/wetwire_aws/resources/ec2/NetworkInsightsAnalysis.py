"""PropertyTypes for AWS::EC2::NetworkInsightsAnalysis."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdditionalDetail(PropertyType):
    additional_detail_type: DslValue[str] | None = None
    component: DslValue[AnalysisComponent] | None = None
    load_balancers: list[DslValue[AnalysisComponent]] = field(default_factory=list)
    service_name: DslValue[str] | None = None


@dataclass
class AlternatePathHint(PropertyType):
    component_arn: DslValue[str] | None = None
    component_id: DslValue[str] | None = None


@dataclass
class AnalysisAclRule(PropertyType):
    cidr: DslValue[str] | None = None
    egress: DslValue[bool] | None = None
    port_range: DslValue[PortRange] | None = None
    protocol: DslValue[str] | None = None
    rule_action: DslValue[str] | None = None
    rule_number: DslValue[int] | None = None


@dataclass
class AnalysisComponent(PropertyType):
    arn: DslValue[str] | None = None
    id: DslValue[str] | None = None


@dataclass
class AnalysisLoadBalancerListener(PropertyType):
    instance_port: DslValue[int] | None = None
    load_balancer_port: DslValue[int] | None = None


@dataclass
class AnalysisLoadBalancerTarget(PropertyType):
    address: DslValue[str] | None = None
    availability_zone: DslValue[str] | None = None
    instance: DslValue[AnalysisComponent] | None = None
    port: DslValue[int] | None = None


@dataclass
class AnalysisPacketHeader(PropertyType):
    destination_addresses: list[DslValue[str]] = field(default_factory=list)
    destination_port_ranges: list[DslValue[PortRange]] = field(default_factory=list)
    protocol: DslValue[str] | None = None
    source_addresses: list[DslValue[str]] = field(default_factory=list)
    source_port_ranges: list[DslValue[PortRange]] = field(default_factory=list)


@dataclass
class AnalysisRouteTableRoute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_cidr": "destinationCidr",
        "destination_prefix_list_id": "destinationPrefixListId",
        "egress_only_internet_gateway_id": "egressOnlyInternetGatewayId",
        "gateway_id": "gatewayId",
        "instance_id": "instanceId",
    }

    destination_cidr: DslValue[str] | None = None
    destination_prefix_list_id: DslValue[str] | None = None
    egress_only_internet_gateway_id: DslValue[str] | None = None
    gateway_id: DslValue[str] | None = None
    instance_id: DslValue[str] | None = None
    nat_gateway_id: DslValue[str] | None = None
    network_interface_id: DslValue[str] | None = None
    origin: DslValue[str] | None = None
    state: DslValue[str] | None = None
    transit_gateway_id: DslValue[str] | None = None
    vpc_peering_connection_id: DslValue[str] | None = None


@dataclass
class AnalysisSecurityGroupRule(PropertyType):
    cidr: DslValue[str] | None = None
    direction: DslValue[str] | None = None
    port_range: DslValue[PortRange] | None = None
    prefix_list_id: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    security_group_id: DslValue[str] | None = None


@dataclass
class Explanation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_endpoint": "vpcEndpoint",
    }

    acl: DslValue[AnalysisComponent] | None = None
    acl_rule: DslValue[AnalysisAclRule] | None = None
    address: DslValue[str] | None = None
    addresses: list[DslValue[str]] = field(default_factory=list)
    attached_to: DslValue[AnalysisComponent] | None = None
    availability_zones: list[DslValue[str]] = field(default_factory=list)
    cidrs: list[DslValue[str]] = field(default_factory=list)
    classic_load_balancer_listener: DslValue[AnalysisLoadBalancerListener] | None = None
    component: DslValue[AnalysisComponent] | None = None
    component_account: DslValue[str] | None = None
    component_region: DslValue[str] | None = None
    customer_gateway: DslValue[AnalysisComponent] | None = None
    destination: DslValue[AnalysisComponent] | None = None
    destination_vpc: DslValue[AnalysisComponent] | None = None
    direction: DslValue[str] | None = None
    elastic_load_balancer_listener: DslValue[AnalysisComponent] | None = None
    explanation_code: DslValue[str] | None = None
    ingress_route_table: DslValue[AnalysisComponent] | None = None
    internet_gateway: DslValue[AnalysisComponent] | None = None
    load_balancer_arn: DslValue[str] | None = None
    load_balancer_listener_port: DslValue[int] | None = None
    load_balancer_target: DslValue[AnalysisLoadBalancerTarget] | None = None
    load_balancer_target_group: DslValue[AnalysisComponent] | None = None
    load_balancer_target_groups: list[DslValue[AnalysisComponent]] = field(
        default_factory=list
    )
    load_balancer_target_port: DslValue[int] | None = None
    missing_component: DslValue[str] | None = None
    nat_gateway: DslValue[AnalysisComponent] | None = None
    network_interface: DslValue[AnalysisComponent] | None = None
    packet_field: DslValue[str] | None = None
    port: DslValue[int] | None = None
    port_ranges: list[DslValue[PortRange]] = field(default_factory=list)
    prefix_list: DslValue[AnalysisComponent] | None = None
    protocols: list[DslValue[str]] = field(default_factory=list)
    route_table: DslValue[AnalysisComponent] | None = None
    route_table_route: DslValue[AnalysisRouteTableRoute] | None = None
    security_group: DslValue[AnalysisComponent] | None = None
    security_group_rule: DslValue[AnalysisSecurityGroupRule] | None = None
    security_groups: list[DslValue[AnalysisComponent]] = field(default_factory=list)
    source_vpc: DslValue[AnalysisComponent] | None = None
    state: DslValue[str] | None = None
    subnet: DslValue[AnalysisComponent] | None = None
    subnet_route_table: DslValue[AnalysisComponent] | None = None
    transit_gateway: DslValue[AnalysisComponent] | None = None
    transit_gateway_attachment: DslValue[AnalysisComponent] | None = None
    transit_gateway_route_table: DslValue[AnalysisComponent] | None = None
    transit_gateway_route_table_route: (
        DslValue[TransitGatewayRouteTableRoute] | None
    ) = None
    vpc: DslValue[AnalysisComponent] | None = None
    vpc_endpoint: DslValue[AnalysisComponent] | None = None
    vpc_peering_connection: DslValue[AnalysisComponent] | None = None
    vpn_connection: DslValue[AnalysisComponent] | None = None
    vpn_gateway: DslValue[AnalysisComponent] | None = None


@dataclass
class PathComponent(PropertyType):
    acl_rule: DslValue[AnalysisAclRule] | None = None
    additional_details: list[DslValue[AdditionalDetail]] = field(default_factory=list)
    component: DslValue[AnalysisComponent] | None = None
    destination_vpc: DslValue[AnalysisComponent] | None = None
    elastic_load_balancer_listener: DslValue[AnalysisComponent] | None = None
    explanations: list[DslValue[Explanation]] = field(default_factory=list)
    inbound_header: DslValue[AnalysisPacketHeader] | None = None
    outbound_header: DslValue[AnalysisPacketHeader] | None = None
    route_table_route: DslValue[AnalysisRouteTableRoute] | None = None
    security_group_rule: DslValue[AnalysisSecurityGroupRule] | None = None
    sequence_number: DslValue[int] | None = None
    service_name: DslValue[str] | None = None
    source_vpc: DslValue[AnalysisComponent] | None = None
    subnet: DslValue[AnalysisComponent] | None = None
    transit_gateway: DslValue[AnalysisComponent] | None = None
    transit_gateway_route_table_route: (
        DslValue[TransitGatewayRouteTableRoute] | None
    ) = None
    vpc: DslValue[AnalysisComponent] | None = None


@dataclass
class PortRange(PropertyType):
    from_: DslValue[int] | None = None
    to: DslValue[int] | None = None


@dataclass
class TransitGatewayRouteTableRoute(PropertyType):
    attachment_id: DslValue[str] | None = None
    destination_cidr: DslValue[str] | None = None
    prefix_list_id: DslValue[str] | None = None
    resource_id: DslValue[str] | None = None
    resource_type: DslValue[str] | None = None
    route_origin: DslValue[str] | None = None
    state: DslValue[str] | None = None
