"""PropertyTypes for AWS::FMS::Policy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IEMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "account": "ACCOUNT",
        "orgunit": "ORGUNIT",
    }

    account: list[String] = field(default_factory=list)
    orgunit: list[String] = field(default_factory=list)


@dataclass
class IcmpTypeCode(PropertyType):
    code: int | None = None
    type_: int | None = None


@dataclass
class NetworkAclCommonPolicy(PropertyType):
    network_acl_entry_set: NetworkAclEntrySet | None = None


@dataclass
class NetworkAclEntry(PropertyType):
    egress: bool | None = None
    protocol: str | None = None
    rule_action: str | None = None
    cidr_block: str | None = None
    icmp_type_code: IcmpTypeCode | None = None
    ipv6_cidr_block: str | None = None
    port_range: PortRange | None = None


@dataclass
class NetworkAclEntrySet(PropertyType):
    force_remediate_for_first_entries: bool | None = None
    force_remediate_for_last_entries: bool | None = None
    first_entries: list[NetworkAclEntry] = field(default_factory=list)
    last_entries: list[NetworkAclEntry] = field(default_factory=list)


@dataclass
class NetworkFirewallPolicy(PropertyType):
    firewall_deployment_model: str | None = None


@dataclass
class PolicyOption(PropertyType):
    network_acl_common_policy: NetworkAclCommonPolicy | None = None
    network_firewall_policy: NetworkFirewallPolicy | None = None
    third_party_firewall_policy: ThirdPartyFirewallPolicy | None = None


@dataclass
class PolicyTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class PortRange(PropertyType):
    from_: int | None = None
    to: int | None = None


@dataclass
class ResourceTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class SecurityServicePolicyData(PropertyType):
    type_: str | None = None
    managed_service_data: str | None = None
    policy_option: PolicyOption | None = None


@dataclass
class ThirdPartyFirewallPolicy(PropertyType):
    firewall_deployment_model: str | None = None
