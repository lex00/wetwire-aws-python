"""PropertyTypes for AWS::FraudDetector::EventType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EntityType(PropertyType):
    arn: DslValue[str] | None = None
    created_time: DslValue[str] | None = None
    description: DslValue[str] | None = None
    inline: DslValue[bool] | None = None
    last_updated_time: DslValue[str] | None = None
    name: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class EventVariable(PropertyType):
    arn: DslValue[str] | None = None
    created_time: DslValue[str] | None = None
    data_source: DslValue[str] | None = None
    data_type: DslValue[str] | None = None
    default_value: DslValue[str] | None = None
    description: DslValue[str] | None = None
    inline: DslValue[bool] | None = None
    last_updated_time: DslValue[str] | None = None
    name: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
    variable_type: DslValue[str] | None = None


@dataclass
class Label(PropertyType):
    arn: DslValue[str] | None = None
    created_time: DslValue[str] | None = None
    description: DslValue[str] | None = None
    inline: DslValue[bool] | None = None
    last_updated_time: DslValue[str] | None = None
    name: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
