"""PropertyTypes for AWS::FIS::ExperimentTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchDashboard(PropertyType):
    dashboard_identifier: str | None = None


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    log_group_arn: str | None = None


@dataclass
class DataSources(PropertyType):
    cloud_watch_dashboards: list[CloudWatchDashboard] = field(default_factory=list)


@dataclass
class ExperimentReportS3Configuration(PropertyType):
    bucket_name: str | None = None
    prefix: str | None = None


@dataclass
class ExperimentTemplateAction(PropertyType):
    action_id: str | None = None
    description: str | None = None
    parameters: dict[str, String] = field(default_factory=dict)
    start_after: list[String] = field(default_factory=list)
    targets: dict[str, String] = field(default_factory=dict)


@dataclass
class ExperimentTemplateExperimentOptions(PropertyType):
    account_targeting: str | None = None
    empty_target_resolution_mode: str | None = None


@dataclass
class ExperimentTemplateExperimentReportConfiguration(PropertyType):
    outputs: Outputs | None = None
    data_sources: DataSources | None = None
    post_experiment_duration: str | None = None
    pre_experiment_duration: str | None = None


@dataclass
class ExperimentTemplateLogConfiguration(PropertyType):
    log_schema_version: int | None = None
    cloud_watch_logs_configuration: CloudWatchLogsConfiguration | None = None
    s3_configuration: S3Configuration | None = None


@dataclass
class ExperimentTemplateStopCondition(PropertyType):
    source: str | None = None
    value: str | None = None


@dataclass
class ExperimentTemplateTarget(PropertyType):
    resource_type: str | None = None
    selection_mode: str | None = None
    filters: list[ExperimentTemplateTargetFilter] = field(default_factory=list)
    parameters: dict[str, String] = field(default_factory=dict)
    resource_arns: list[String] = field(default_factory=list)
    resource_tags: dict[str, String] = field(default_factory=dict)


@dataclass
class ExperimentTemplateTargetFilter(PropertyType):
    path: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Outputs(PropertyType):
    experiment_report_s3_configuration: ExperimentReportS3Configuration | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: str | None = None
    prefix: str | None = None
