"""PropertyTypes for AWS::ResilienceHub::ResiliencyPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FailurePolicy(PropertyType):
    rpo_in_secs: DslValue[int] | None = None
    rto_in_secs: DslValue[int] | None = None


@dataclass
class PolicyMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "az": "AZ",
    }

    az: DslValue[FailurePolicy] | None = None
    hardware: DslValue[FailurePolicy] | None = None
    software: DslValue[FailurePolicy] | None = None
    region: DslValue[FailurePolicy] | None = None
