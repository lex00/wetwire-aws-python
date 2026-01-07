"""PropertyTypes for AWS::FIS::ExperimentTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchDashboard(PropertyType):
    dashboard_identifier: DslValue[str] | None = None


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class DataSources(PropertyType):
    cloud_watch_dashboards: list[DslValue[CloudWatchDashboard]] = field(
        default_factory=list
    )


@dataclass
class ExperimentReportS3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class ExperimentTemplateAction(PropertyType):
    action_id: DslValue[str] | None = None
    description: DslValue[str] | None = None
    parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    start_after: list[DslValue[str]] = field(default_factory=list)
    targets: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class ExperimentTemplateExperimentOptions(PropertyType):
    account_targeting: DslValue[str] | None = None
    empty_target_resolution_mode: DslValue[str] | None = None


@dataclass
class ExperimentTemplateExperimentReportConfiguration(PropertyType):
    outputs: DslValue[Outputs] | None = None
    data_sources: DslValue[DataSources] | None = None
    post_experiment_duration: DslValue[str] | None = None
    pre_experiment_duration: DslValue[str] | None = None


@dataclass
class ExperimentTemplateLogConfiguration(PropertyType):
    log_schema_version: DslValue[int] | None = None
    cloud_watch_logs_configuration: DslValue[CloudWatchLogsConfiguration] | None = None
    s3_configuration: DslValue[S3Configuration] | None = None


@dataclass
class ExperimentTemplateStopCondition(PropertyType):
    source: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ExperimentTemplateTarget(PropertyType):
    resource_type: DslValue[str] | None = None
    selection_mode: DslValue[str] | None = None
    filters: list[DslValue[ExperimentTemplateTargetFilter]] = field(
        default_factory=list
    )
    parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    resource_arns: list[DslValue[str]] = field(default_factory=list)
    resource_tags: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class ExperimentTemplateTargetFilter(PropertyType):
    path: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Outputs(PropertyType):
    experiment_report_s3_configuration: (
        DslValue[ExperimentReportS3Configuration] | None
    ) = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
