"""PropertyTypes for AWS::ImageBuilder::ImagePipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoDisablePolicy(PropertyType):
    failure_count: DslValue[int] | None = None


@dataclass
class EcrConfiguration(PropertyType):
    container_tags: list[DslValue[str]] = field(default_factory=list)
    repository_name: DslValue[str] | None = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    ecr_configuration: DslValue[EcrConfiguration] | None = None
    image_scanning_enabled: DslValue[bool] | None = None


@dataclass
class ImageTestsConfiguration(PropertyType):
    image_tests_enabled: DslValue[bool] | None = None
    timeout_minutes: DslValue[int] | None = None


@dataclass
class PipelineLoggingConfiguration(PropertyType):
    image_log_group_name: DslValue[str] | None = None
    pipeline_log_group_name: DslValue[str] | None = None


@dataclass
class Schedule(PropertyType):
    auto_disable_policy: DslValue[AutoDisablePolicy] | None = None
    pipeline_execution_start_condition: DslValue[str] | None = None
    schedule_expression: DslValue[str] | None = None


@dataclass
class WorkflowConfiguration(PropertyType):
    on_failure: DslValue[str] | None = None
    parallel_group: DslValue[str] | None = None
    parameters: list[DslValue[WorkflowParameter]] = field(default_factory=list)
    workflow_arn: DslValue[str] | None = None


@dataclass
class WorkflowParameter(PropertyType):
    name: DslValue[str] | None = None
    value: list[DslValue[str]] = field(default_factory=list)
