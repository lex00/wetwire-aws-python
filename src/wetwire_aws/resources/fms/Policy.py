"""PropertyTypes for AWS::FMS::Policy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IEMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "account": "ACCOUNT",
        "orgunit": "ORGUNIT",
    }

    account: list[DslValue[str]] = field(default_factory=list)
    orgunit: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IcmpTypeCode(PropertyType):
    code: DslValue[int] | None = None
    type_: DslValue[int] | None = None


@dataclass
class NetworkAclCommonPolicy(PropertyType):
    network_acl_entry_set: DslValue[NetworkAclEntrySet] | None = None


@dataclass
class NetworkAclEntry(PropertyType):
    egress: DslValue[bool] | None = None
    protocol: DslValue[str] | None = None
    rule_action: DslValue[str] | None = None
    cidr_block: DslValue[str] | None = None
    icmp_type_code: DslValue[IcmpTypeCode] | None = None
    ipv6_cidr_block: DslValue[str] | None = None
    port_range: DslValue[PortRange] | None = None


@dataclass
class NetworkAclEntrySet(PropertyType):
    force_remediate_for_first_entries: DslValue[bool] | None = None
    force_remediate_for_last_entries: DslValue[bool] | None = None
    first_entries: list[DslValue[NetworkAclEntry]] = field(default_factory=list)
    last_entries: list[DslValue[NetworkAclEntry]] = field(default_factory=list)


@dataclass
class NetworkFirewallPolicy(PropertyType):
    firewall_deployment_model: DslValue[str] | None = None


@dataclass
class PolicyOption(PropertyType):
    network_acl_common_policy: DslValue[NetworkAclCommonPolicy] | None = None
    network_firewall_policy: DslValue[NetworkFirewallPolicy] | None = None
    third_party_firewall_policy: DslValue[ThirdPartyFirewallPolicy] | None = None


@dataclass
class PolicyTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class PortRange(PropertyType):
    from_: DslValue[int] | None = None
    to: DslValue[int] | None = None


@dataclass
class ResourceTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SecurityServicePolicyData(PropertyType):
    type_: DslValue[str] | None = None
    managed_service_data: DslValue[str] | None = None
    policy_option: DslValue[PolicyOption] | None = None


@dataclass
class ThirdPartyFirewallPolicy(PropertyType):
    firewall_deployment_model: DslValue[str] | None = None
