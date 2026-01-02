"""PropertyTypes for AWS::ResilienceHub::ResiliencyPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FailurePolicy(PropertyType):
    rpo_in_secs: int | None = None
    rto_in_secs: int | None = None


@dataclass
class PolicyMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "az": "AZ",
    }

    az: FailurePolicy | None = None
    hardware: FailurePolicy | None = None
    software: FailurePolicy | None = None
    region: FailurePolicy | None = None
