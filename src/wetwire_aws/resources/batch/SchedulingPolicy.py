"""PropertyTypes for AWS::Batch::SchedulingPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FairsharePolicy(PropertyType):
    compute_reservation: float | None = None
    share_decay_seconds: float | None = None
    share_distribution: list[ShareAttributes] = field(default_factory=list)


@dataclass
class ShareAttributes(PropertyType):
    share_identifier: str | None = None
    weight_factor: float | None = None
