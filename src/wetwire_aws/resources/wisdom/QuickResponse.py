"""PropertyTypes for AWS::Wisdom::QuickResponse."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GroupingConfiguration(PropertyType):
    criteria: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class QuickResponseContentProvider(PropertyType):
    content: DslValue[str] | None = None


@dataclass
class QuickResponseContents(PropertyType):
    markdown: DslValue[QuickResponseContentProvider] | None = None
    plain_text: DslValue[QuickResponseContentProvider] | None = None
