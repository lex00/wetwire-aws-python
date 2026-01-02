"""PropertyTypes for AWS::ManagedBlockchain::Member."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApprovalThresholdPolicy(PropertyType):
    proposal_duration_in_hours: int | None = None
    threshold_comparator: str | None = None
    threshold_percentage: int | None = None


@dataclass
class MemberConfiguration(PropertyType):
    name: str | None = None
    description: str | None = None
    member_framework_configuration: MemberFrameworkConfiguration | None = None


@dataclass
class MemberFabricConfiguration(PropertyType):
    admin_password: str | None = None
    admin_username: str | None = None


@dataclass
class MemberFrameworkConfiguration(PropertyType):
    member_fabric_configuration: MemberFabricConfiguration | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    framework: str | None = None
    framework_version: str | None = None
    name: str | None = None
    voting_policy: VotingPolicy | None = None
    description: str | None = None
    network_framework_configuration: NetworkFrameworkConfiguration | None = None


@dataclass
class NetworkFabricConfiguration(PropertyType):
    edition: str | None = None


@dataclass
class NetworkFrameworkConfiguration(PropertyType):
    network_fabric_configuration: NetworkFabricConfiguration | None = None


@dataclass
class VotingPolicy(PropertyType):
    approval_threshold_policy: ApprovalThresholdPolicy | None = None
