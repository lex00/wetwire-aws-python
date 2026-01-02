"""PropertyTypes for AWS::ImageBuilder::ImagePipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoDisablePolicy(PropertyType):
    failure_count: int | None = None


@dataclass
class EcrConfiguration(PropertyType):
    container_tags: list[String] = field(default_factory=list)
    repository_name: str | None = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    ecr_configuration: EcrConfiguration | None = None
    image_scanning_enabled: bool | None = None


@dataclass
class ImageTestsConfiguration(PropertyType):
    image_tests_enabled: bool | None = None
    timeout_minutes: int | None = None


@dataclass
class PipelineLoggingConfiguration(PropertyType):
    image_log_group_name: str | None = None
    pipeline_log_group_name: str | None = None


@dataclass
class Schedule(PropertyType):
    auto_disable_policy: AutoDisablePolicy | None = None
    pipeline_execution_start_condition: str | None = None
    schedule_expression: str | None = None


@dataclass
class WorkflowConfiguration(PropertyType):
    on_failure: str | None = None
    parallel_group: str | None = None
    parameters: list[WorkflowParameter] = field(default_factory=list)
    workflow_arn: str | None = None


@dataclass
class WorkflowParameter(PropertyType):
    name: str | None = None
    value: list[String] = field(default_factory=list)
