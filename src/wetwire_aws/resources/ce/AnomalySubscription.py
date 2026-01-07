"""PropertyTypes for AWS::CE::AnomalySubscription."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResourceTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Subscriber(PropertyType):
    address: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    status: DslValue[str] | None = None
