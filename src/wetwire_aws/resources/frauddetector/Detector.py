"""PropertyTypes for AWS::FraudDetector::Detector."""

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
class EventType(PropertyType):
    arn: str | None = None
    created_time: str | None = None
    description: str | None = None
    entity_types: list[EntityType] = field(default_factory=list)
    event_variables: list[EventVariable] = field(default_factory=list)
    inline: bool | None = None
    labels: list[Label] = field(default_factory=list)
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


@dataclass
class Model(PropertyType):
    arn: str | None = None


@dataclass
class Outcome(PropertyType):
    arn: str | None = None
    created_time: str | None = None
    description: str | None = None
    inline: bool | None = None
    last_updated_time: str | None = None
    name: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    arn: str | None = None
    created_time: str | None = None
    description: str | None = None
    detector_id: str | None = None
    expression: str | None = None
    language: str | None = None
    last_updated_time: str | None = None
    outcomes: list[Outcome] = field(default_factory=list)
    rule_id: str | None = None
    rule_version: str | None = None
    tags: list[Tag] = field(default_factory=list)
