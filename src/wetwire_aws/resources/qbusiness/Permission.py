"""PropertyTypes for AWS::QBusiness::Permission."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Condition(PropertyType):
    condition_key: DslValue[str] | None = None
    condition_operator: DslValue[str] | None = None
    condition_values: list[DslValue[str]] = field(default_factory=list)
