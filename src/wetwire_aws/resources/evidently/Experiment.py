"""PropertyTypes for AWS::Evidently::Experiment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MetricGoalObject(PropertyType):
    desired_change: DslValue[str] | None = None
    entity_id_key: DslValue[str] | None = None
    metric_name: DslValue[str] | None = None
    value_key: DslValue[str] | None = None
    event_pattern: DslValue[str] | None = None
    unit_label: DslValue[str] | None = None


@dataclass
class OnlineAbConfigObject(PropertyType):
    control_treatment_name: DslValue[str] | None = None
    treatment_weights: list[DslValue[TreatmentToWeight]] = field(default_factory=list)


@dataclass
class RunningStatusObject(PropertyType):
    status: DslValue[str] | None = None
    analysis_complete_time: DslValue[str] | None = None
    desired_state: DslValue[str] | None = None
    reason: DslValue[str] | None = None


@dataclass
class TreatmentObject(PropertyType):
    feature: DslValue[str] | None = None
    treatment_name: DslValue[str] | None = None
    variation: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class TreatmentToWeight(PropertyType):
    split_weight: DslValue[int] | None = None
    treatment: DslValue[str] | None = None
