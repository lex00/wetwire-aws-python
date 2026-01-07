"""PropertyTypes for AWS::Batch::SchedulingPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FairsharePolicy(PropertyType):
    compute_reservation: DslValue[float] | None = None
    share_decay_seconds: DslValue[float] | None = None
    share_distribution: list[DslValue[ShareAttributes]] = field(default_factory=list)


@dataclass
class ShareAttributes(PropertyType):
    share_identifier: DslValue[str] | None = None
    weight_factor: DslValue[float] | None = None
