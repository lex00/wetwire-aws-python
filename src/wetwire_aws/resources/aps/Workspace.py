"""PropertyTypes for AWS::APS::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogDestination(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class Label(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class LimitsPerLabelSet(PropertyType):
    label_set: list[DslValue[Label]] = field(default_factory=list)
    limits: DslValue[LimitsPerLabelSetEntry] | None = None


@dataclass
class LimitsPerLabelSetEntry(PropertyType):
    max_series: DslValue[int] | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class LoggingDestination(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogDestination] | None = None
    filters: DslValue[LoggingFilter] | None = None


@dataclass
class LoggingFilter(PropertyType):
    qsp_threshold: DslValue[int] | None = None


@dataclass
class QueryLoggingConfiguration(PropertyType):
    destinations: list[DslValue[LoggingDestination]] = field(default_factory=list)


@dataclass
class WorkspaceConfiguration(PropertyType):
    limits_per_label_sets: list[DslValue[LimitsPerLabelSet]] = field(
        default_factory=list
    )
    retention_period_in_days: DslValue[int] | None = None
