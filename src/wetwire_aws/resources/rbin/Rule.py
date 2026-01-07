"""PropertyTypes for AWS::Rbin::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResourceTag(PropertyType):
    resource_tag_key: DslValue[str] | None = None
    resource_tag_value: DslValue[str] | None = None


@dataclass
class RetentionPeriod(PropertyType):
    retention_period_unit: DslValue[str] | None = None
    retention_period_value: DslValue[int] | None = None


@dataclass
class UnlockDelay(PropertyType):
    unlock_delay_unit: DslValue[str] | None = None
    unlock_delay_value: DslValue[int] | None = None
