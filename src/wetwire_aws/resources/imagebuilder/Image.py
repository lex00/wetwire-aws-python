"""PropertyTypes for AWS::ImageBuilder::Image."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeletionSettings(PropertyType):
    execution_role: DslValue[str] | None = None


@dataclass
class EcrConfiguration(PropertyType):
    container_tags: list[DslValue[str]] = field(default_factory=list)
    repository_name: DslValue[str] | None = None


@dataclass
class ImageLoggingConfiguration(PropertyType):
    log_group_name: DslValue[str] | None = None


@dataclass
class ImagePipelineExecutionSettings(PropertyType):
    deployment_id: DslValue[str] | None = None
    on_update: DslValue[bool] | None = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    ecr_configuration: DslValue[EcrConfiguration] | None = None
    image_scanning_enabled: DslValue[bool] | None = None


@dataclass
class ImageTestsConfiguration(PropertyType):
    image_tests_enabled: DslValue[bool] | None = None
    timeout_minutes: DslValue[int] | None = None


@dataclass
class LatestVersion(PropertyType):
    arn: DslValue[str] | None = None
    major: DslValue[str] | None = None
    minor: DslValue[str] | None = None
    patch: DslValue[str] | None = None


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
