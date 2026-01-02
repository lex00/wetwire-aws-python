"""PropertyTypes for AWS::Backup::RestoreTestingSelection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class KeyValue(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class ProtectedResourceConditions(PropertyType):
    string_equals: list[KeyValue] = field(default_factory=list)
    string_not_equals: list[KeyValue] = field(default_factory=list)
