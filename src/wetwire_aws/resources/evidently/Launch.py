"""PropertyTypes for AWS::Evidently::Launch."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ExecutionStatusObject(PropertyType):
    status: str | None = None
    desired_state: str | None = None
    reason: str | None = None


@dataclass
class GroupToWeight(PropertyType):
    group_name: str | None = None
    split_weight: int | None = None


@dataclass
class LaunchGroupObject(PropertyType):
    feature: str | None = None
    group_name: str | None = None
    variation: str | None = None
    description: str | None = None


@dataclass
class MetricDefinitionObject(PropertyType):
    entity_id_key: str | None = None
    metric_name: str | None = None
    value_key: str | None = None
    event_pattern: str | None = None
    unit_label: str | None = None


@dataclass
class SegmentOverride(PropertyType):
    evaluation_order: int | None = None
    segment: str | None = None
    weights: list[GroupToWeight] = field(default_factory=list)


@dataclass
class StepConfig(PropertyType):
    group_weights: list[GroupToWeight] = field(default_factory=list)
    start_time: str | None = None
    segment_overrides: list[SegmentOverride] = field(default_factory=list)
