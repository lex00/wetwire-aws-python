"""PropertyTypes for AWS::EVS::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Check(PropertyType):
    result: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    impaired_since: DslValue[str] | None = None


@dataclass
class ConnectivityInfo(PropertyType):
    private_route_server_peerings: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HostInfoForCreate(PropertyType):
    host_name: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
    key_name: DslValue[str] | None = None
    dedicated_host_id: DslValue[str] | None = None
    placement_group_id: DslValue[str] | None = None


@dataclass
class InitialVlanInfo(PropertyType):
    cidr: DslValue[str] | None = None


@dataclass
class InitialVlans(PropertyType):
    edge_v_tep: DslValue[InitialVlanInfo] | None = None
    expansion_vlan1: DslValue[InitialVlanInfo] | None = None
    expansion_vlan2: DslValue[InitialVlanInfo] | None = None
    hcx: DslValue[InitialVlanInfo] | None = None
    nsx_up_link: DslValue[InitialVlanInfo] | None = None
    v_motion: DslValue[InitialVlanInfo] | None = None
    v_san: DslValue[InitialVlanInfo] | None = None
    v_tep: DslValue[InitialVlanInfo] | None = None
    vm_management: DslValue[InitialVlanInfo] | None = None
    vmk_management: DslValue[InitialVlanInfo] | None = None
    hcx_network_acl_id: DslValue[str] | None = None
    is_hcx_public: DslValue[bool] | None = None


@dataclass
class LicenseInfo(PropertyType):
    solution_key: DslValue[str] | None = None
    vsan_key: DslValue[str] | None = None


@dataclass
class Secret(PropertyType):
    secret_arn: DslValue[str] | None = None


@dataclass
class ServiceAccessSecurityGroups(PropertyType):
    security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VcfHostnames(PropertyType):
    cloud_builder: DslValue[str] | None = None
    nsx: DslValue[str] | None = None
    nsx_edge1: DslValue[str] | None = None
    nsx_edge2: DslValue[str] | None = None
    nsx_manager1: DslValue[str] | None = None
    nsx_manager2: DslValue[str] | None = None
    nsx_manager3: DslValue[str] | None = None
    sddc_manager: DslValue[str] | None = None
    v_center: DslValue[str] | None = None
