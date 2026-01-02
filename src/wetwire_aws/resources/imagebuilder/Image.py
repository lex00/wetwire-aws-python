"""PropertyTypes for AWS::ImageBuilder::Image."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeletionSettings(PropertyType):
    execution_role: str | None = None


@dataclass
class EcrConfiguration(PropertyType):
    container_tags: list[String] = field(default_factory=list)
    repository_name: str | None = None


@dataclass
class ImageLoggingConfiguration(PropertyType):
    log_group_name: str | None = None


@dataclass
class ImagePipelineExecutionSettings(PropertyType):
    deployment_id: str | None = None
    on_update: bool | None = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    ecr_configuration: EcrConfiguration | None = None
    image_scanning_enabled: bool | None = None


@dataclass
class ImageTestsConfiguration(PropertyType):
    image_tests_enabled: bool | None = None
    timeout_minutes: int | None = None


@dataclass
class LatestVersion(PropertyType):
    arn: str | None = None
    major: str | None = None
    minor: str | None = None
    patch: str | None = None


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
