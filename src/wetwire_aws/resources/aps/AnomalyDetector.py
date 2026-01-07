"""PropertyTypes for AWS::APS::AnomalyDetector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnomalyDetectorConfiguration(PropertyType):
    random_cut_forest: DslValue[RandomCutForestConfiguration] | None = None


@dataclass
class IgnoreNearExpected(PropertyType):
    amount: DslValue[float] | None = None
    ratio: DslValue[float] | None = None


@dataclass
class Label(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class MissingDataAction(PropertyType):
    mark_as_anomaly: DslValue[bool] | None = None
    skip: DslValue[bool] | None = None


@dataclass
class RandomCutForestConfiguration(PropertyType):
    query: DslValue[str] | None = None
    ignore_near_expected_from_above: DslValue[IgnoreNearExpected] | None = None
    ignore_near_expected_from_below: DslValue[IgnoreNearExpected] | None = None
    sample_size: DslValue[int] | None = None
    shingle_size: DslValue[int] | None = None
