"""PropertyTypes for AWS::ApplicationSignals::GroupingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GroupingAttributeDefinition(PropertyType):
    grouping_name: DslValue[str] | None = None
    grouping_source_keys: list[DslValue[str]] = field(default_factory=list)
    default_grouping_value: DslValue[str] | None = None
