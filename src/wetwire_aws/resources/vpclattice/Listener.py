"""PropertyTypes for AWS::VpcLattice::Listener."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DefaultAction(PropertyType):
    fixed_response: FixedResponse | None = None
    forward: Forward | None = None


@dataclass
class FixedResponse(PropertyType):
    status_code: int | None = None


@dataclass
class Forward(PropertyType):
    target_groups: list[WeightedTargetGroup] = field(default_factory=list)


@dataclass
class WeightedTargetGroup(PropertyType):
    target_group_identifier: str | None = None
    weight: int | None = None
