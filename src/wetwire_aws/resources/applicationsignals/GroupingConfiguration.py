"""PropertyTypes for AWS::ApplicationSignals::GroupingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GroupingAttributeDefinition(PropertyType):
    grouping_name: str | None = None
    grouping_source_keys: list[String] = field(default_factory=list)
    default_grouping_value: str | None = None
