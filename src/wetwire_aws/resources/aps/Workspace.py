"""PropertyTypes for AWS::APS::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogDestination(PropertyType):
    log_group_arn: str | None = None


@dataclass
class Label(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class LimitsPerLabelSet(PropertyType):
    label_set: list[Label] = field(default_factory=list)
    limits: LimitsPerLabelSetEntry | None = None


@dataclass
class LimitsPerLabelSetEntry(PropertyType):
    max_series: int | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    log_group_arn: str | None = None


@dataclass
class LoggingDestination(PropertyType):
    cloud_watch_logs: CloudWatchLogDestination | None = None
    filters: LoggingFilter | None = None


@dataclass
class LoggingFilter(PropertyType):
    qsp_threshold: int | None = None


@dataclass
class QueryLoggingConfiguration(PropertyType):
    destinations: list[LoggingDestination] = field(default_factory=list)


@dataclass
class WorkspaceConfiguration(PropertyType):
    limits_per_label_sets: list[LimitsPerLabelSet] = field(default_factory=list)
    retention_period_in_days: int | None = None
