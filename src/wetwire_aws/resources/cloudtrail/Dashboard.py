"""PropertyTypes for AWS::CloudTrail::Dashboard."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Frequency(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class RefreshSchedule(PropertyType):
    frequency: DslValue[Frequency] | None = None
    status: DslValue[str] | None = None
    time_of_day: DslValue[str] | None = None


@dataclass
class Widget(PropertyType):
    query_statement: DslValue[str] | None = None
    query_parameters: list[DslValue[str]] = field(default_factory=list)
    view_properties: dict[str, DslValue[str]] = field(default_factory=dict)
