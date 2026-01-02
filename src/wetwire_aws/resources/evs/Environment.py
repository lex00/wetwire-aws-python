"""PropertyTypes for AWS::EVS::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Check(PropertyType):
    result: str | None = None
    type_: str | None = None
    impaired_since: str | None = None


@dataclass
class ConnectivityInfo(PropertyType):
    private_route_server_peerings: list[String] = field(default_factory=list)


@dataclass
class HostInfoForCreate(PropertyType):
    host_name: str | None = None
    instance_type: str | None = None
    key_name: str | None = None
    dedicated_host_id: str | None = None
    placement_group_id: str | None = None


@dataclass
class InitialVlanInfo(PropertyType):
    cidr: str | None = None


@dataclass
class InitialVlans(PropertyType):
    edge_v_tep: InitialVlanInfo | None = None
    expansion_vlan1: InitialVlanInfo | None = None
    expansion_vlan2: InitialVlanInfo | None = None
    hcx: InitialVlanInfo | None = None
    nsx_up_link: InitialVlanInfo | None = None
    v_motion: InitialVlanInfo | None = None
    v_san: InitialVlanInfo | None = None
    v_tep: InitialVlanInfo | None = None
    vm_management: InitialVlanInfo | None = None
    vmk_management: InitialVlanInfo | None = None
    hcx_network_acl_id: str | None = None
    is_hcx_public: bool | None = None


@dataclass
class LicenseInfo(PropertyType):
    solution_key: str | None = None
    vsan_key: str | None = None


@dataclass
class Secret(PropertyType):
    secret_arn: str | None = None


@dataclass
class ServiceAccessSecurityGroups(PropertyType):
    security_groups: list[String] = field(default_factory=list)


@dataclass
class VcfHostnames(PropertyType):
    cloud_builder: str | None = None
    nsx: str | None = None
    nsx_edge1: str | None = None
    nsx_edge2: str | None = None
    nsx_manager1: str | None = None
    nsx_manager2: str | None = None
    nsx_manager3: str | None = None
    sddc_manager: str | None = None
    v_center: str | None = None
