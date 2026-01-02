"""PropertyTypes for AWS::Evidently::Experiment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MetricGoalObject(PropertyType):
    desired_change: str | None = None
    entity_id_key: str | None = None
    metric_name: str | None = None
    value_key: str | None = None
    event_pattern: str | None = None
    unit_label: str | None = None


@dataclass
class OnlineAbConfigObject(PropertyType):
    control_treatment_name: str | None = None
    treatment_weights: list[TreatmentToWeight] = field(default_factory=list)


@dataclass
class RunningStatusObject(PropertyType):
    status: str | None = None
    analysis_complete_time: str | None = None
    desired_state: str | None = None
    reason: str | None = None


@dataclass
class TreatmentObject(PropertyType):
    feature: str | None = None
    treatment_name: str | None = None
    variation: str | None = None
    description: str | None = None


@dataclass
class TreatmentToWeight(PropertyType):
    split_weight: int | None = None
    treatment: str | None = None
