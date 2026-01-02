"""PropertyTypes for AWS::AmplifyUIBuilder::Theme."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ThemeValue(PropertyType):
    children: list[ThemeValues] = field(default_factory=list)
    value: str | None = None


@dataclass
class ThemeValues(PropertyType):
    key: str | None = None
    value: ThemeValue | None = None
