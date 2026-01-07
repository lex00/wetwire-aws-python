"""PropertyTypes for AWS::AmplifyUIBuilder::Theme."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ThemeValue(PropertyType):
    children: list[DslValue[ThemeValues]] = field(default_factory=list)
    value: DslValue[str] | None = None


@dataclass
class ThemeValues(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[ThemeValue] | None = None
