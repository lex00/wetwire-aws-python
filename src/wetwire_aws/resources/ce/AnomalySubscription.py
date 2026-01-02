"""PropertyTypes for AWS::CE::AnomalySubscription."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Subscriber(PropertyType):
    address: str | None = None
    type_: str | None = None
    status: str | None = None
