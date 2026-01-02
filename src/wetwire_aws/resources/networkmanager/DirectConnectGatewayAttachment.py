"""PropertyTypes for AWS::NetworkManager::DirectConnectGatewayAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ProposedNetworkFunctionGroupChange(PropertyType):
    attachment_policy_rule_number: int | None = None
    network_function_group_name: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class ProposedSegmentChange(PropertyType):
    attachment_policy_rule_number: int | None = None
    segment_name: str | None = None
    tags: list[Tag] = field(default_factory=list)
