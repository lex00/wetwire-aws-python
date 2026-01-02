"""PropertyTypes for AWS::CloudTrail::Dashboard."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Frequency(PropertyType):
    unit: str | None = None
    value: int | None = None


@dataclass
class RefreshSchedule(PropertyType):
    frequency: Frequency | None = None
    status: str | None = None
    time_of_day: str | None = None


@dataclass
class Widget(PropertyType):
    query_statement: str | None = None
    query_parameters: list[String] = field(default_factory=list)
    view_properties: dict[str, String] = field(default_factory=dict)
