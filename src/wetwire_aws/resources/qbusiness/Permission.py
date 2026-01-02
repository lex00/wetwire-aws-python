"""PropertyTypes for AWS::QBusiness::Permission."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Condition(PropertyType):
    condition_key: str | None = None
    condition_operator: str | None = None
    condition_values: list[String] = field(default_factory=list)
