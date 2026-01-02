"""PropertyTypes for AWS::Wisdom::QuickResponse."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GroupingConfiguration(PropertyType):
    criteria: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class QuickResponseContentProvider(PropertyType):
    content: str | None = None


@dataclass
class QuickResponseContents(PropertyType):
    markdown: QuickResponseContentProvider | None = None
    plain_text: QuickResponseContentProvider | None = None
