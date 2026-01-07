"""PropertyTypes for AWS::Evidently::Launch."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ExecutionStatusObject(PropertyType):
    status: DslValue[str] | None = None
    desired_state: DslValue[str] | None = None
    reason: DslValue[str] | None = None


@dataclass
class GroupToWeight(PropertyType):
    group_name: DslValue[str] | None = None
    split_weight: DslValue[int] | None = None


@dataclass
class LaunchGroupObject(PropertyType):
    feature: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    variation: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class MetricDefinitionObject(PropertyType):
    entity_id_key: DslValue[str] | None = None
    metric_name: DslValue[str] | None = None
    value_key: DslValue[str] | None = None
    event_pattern: DslValue[str] | None = None
    unit_label: DslValue[str] | None = None


@dataclass
class SegmentOverride(PropertyType):
    evaluation_order: DslValue[int] | None = None
    segment: DslValue[str] | None = None
    weights: list[DslValue[GroupToWeight]] = field(default_factory=list)


@dataclass
class StepConfig(PropertyType):
    group_weights: list[DslValue[GroupToWeight]] = field(default_factory=list)
    start_time: DslValue[str] | None = None
    segment_overrides: list[DslValue[SegmentOverride]] = field(default_factory=list)
