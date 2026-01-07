"""PropertyTypes for AWS::Backup::RestoreTestingSelection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class KeyValue(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ProtectedResourceConditions(PropertyType):
    string_equals: list[DslValue[KeyValue]] = field(default_factory=list)
    string_not_equals: list[DslValue[KeyValue]] = field(default_factory=list)
