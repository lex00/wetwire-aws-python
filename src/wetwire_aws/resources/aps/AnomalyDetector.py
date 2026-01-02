"""PropertyTypes for AWS::APS::AnomalyDetector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnomalyDetectorConfiguration(PropertyType):
    random_cut_forest: RandomCutForestConfiguration | None = None


@dataclass
class IgnoreNearExpected(PropertyType):
    amount: float | None = None
    ratio: float | None = None


@dataclass
class Label(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class MissingDataAction(PropertyType):
    mark_as_anomaly: bool | None = None
    skip: bool | None = None


@dataclass
class RandomCutForestConfiguration(PropertyType):
    query: str | None = None
    ignore_near_expected_from_above: IgnoreNearExpected | None = None
    ignore_near_expected_from_below: IgnoreNearExpected | None = None
    sample_size: int | None = None
    shingle_size: int | None = None
