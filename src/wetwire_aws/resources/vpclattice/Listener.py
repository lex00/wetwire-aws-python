"""PropertyTypes for AWS::VpcLattice::Listener."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DefaultAction(PropertyType):
    fixed_response: DslValue[FixedResponse] | None = None
    forward: DslValue[Forward] | None = None


@dataclass
class FixedResponse(PropertyType):
    status_code: DslValue[int] | None = None


@dataclass
class Forward(PropertyType):
    target_groups: list[DslValue[WeightedTargetGroup]] = field(default_factory=list)


@dataclass
class WeightedTargetGroup(PropertyType):
    target_group_identifier: DslValue[str] | None = None
    weight: DslValue[int] | None = None
