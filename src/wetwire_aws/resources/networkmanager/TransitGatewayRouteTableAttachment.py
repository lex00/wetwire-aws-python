"""PropertyTypes for AWS::NetworkManager::TransitGatewayRouteTableAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ProposedNetworkFunctionGroupChange(PropertyType):
    attachment_policy_rule_number: DslValue[int] | None = None
    network_function_group_name: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class ProposedSegmentChange(PropertyType):
    attachment_policy_rule_number: DslValue[int] | None = None
    segment_name: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
