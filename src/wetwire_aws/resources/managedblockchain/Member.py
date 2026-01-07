"""PropertyTypes for AWS::ManagedBlockchain::Member."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApprovalThresholdPolicy(PropertyType):
    proposal_duration_in_hours: DslValue[int] | None = None
    threshold_comparator: DslValue[str] | None = None
    threshold_percentage: DslValue[int] | None = None


@dataclass
class MemberConfiguration(PropertyType):
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    member_framework_configuration: DslValue[MemberFrameworkConfiguration] | None = None


@dataclass
class MemberFabricConfiguration(PropertyType):
    admin_password: DslValue[str] | None = None
    admin_username: DslValue[str] | None = None


@dataclass
class MemberFrameworkConfiguration(PropertyType):
    member_fabric_configuration: DslValue[MemberFabricConfiguration] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    framework: DslValue[str] | None = None
    framework_version: DslValue[str] | None = None
    name: DslValue[str] | None = None
    voting_policy: DslValue[VotingPolicy] | None = None
    description: DslValue[str] | None = None
    network_framework_configuration: DslValue[NetworkFrameworkConfiguration] | None = (
        None
    )


@dataclass
class NetworkFabricConfiguration(PropertyType):
    edition: DslValue[str] | None = None


@dataclass
class NetworkFrameworkConfiguration(PropertyType):
    network_fabric_configuration: DslValue[NetworkFabricConfiguration] | None = None


@dataclass
class VotingPolicy(PropertyType):
    approval_threshold_policy: DslValue[ApprovalThresholdPolicy] | None = None
