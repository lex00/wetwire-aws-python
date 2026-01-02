"""PropertyTypes for AWS::FraudDetector::EventType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EntityType(PropertyType):
    arn: str | None = None
    created_time: str | None = None
    description: str | None = None
    inline: bool | None = None
    last_updated_time: str | None = None
    name: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class EventVariable(PropertyType):
    arn: str | None = None
    created_time: str | None = None
    data_source: str | None = None
    data_type: str | None = None
    default_value: str | None = None
    description: str | None = None
    inline: bool | None = None
    last_updated_time: str | None = None
    name: str | None = None
    tags: list[Tag] = field(default_factory=list)
    variable_type: str | None = None


@dataclass
class Label(PropertyType):
    arn: str | None = None
    created_time: str | None = None
    description: str | None = None
    inline: bool | None = None
    last_updated_time: str | None = None
    name: str | None = None
    tags: list[Tag] = field(default_factory=list)
