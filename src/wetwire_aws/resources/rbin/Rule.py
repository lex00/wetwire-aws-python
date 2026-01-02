"""PropertyTypes for AWS::Rbin::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceTag(PropertyType):
    resource_tag_key: str | None = None
    resource_tag_value: str | None = None


@dataclass
class RetentionPeriod(PropertyType):
    retention_period_unit: str | None = None
    retention_period_value: int | None = None


@dataclass
class UnlockDelay(PropertyType):
    unlock_delay_unit: str | None = None
    unlock_delay_value: int | None = None
