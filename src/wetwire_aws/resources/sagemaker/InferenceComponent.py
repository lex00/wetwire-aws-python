"""PropertyTypes for AWS::SageMaker::InferenceComponent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Alarm(PropertyType):
    alarm_name: DslValue[str] | None = None


@dataclass
class AutoRollbackConfiguration(PropertyType):
    alarms: list[DslValue[Alarm]] = field(default_factory=list)


@dataclass
class DeployedImage(PropertyType):
    resolution_time: DslValue[str] | None = None
    resolved_image: DslValue[str] | None = None
    specified_image: DslValue[str] | None = None


@dataclass
class InferenceComponentCapacitySize(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class InferenceComponentComputeResourceRequirements(PropertyType):
    max_memory_required_in_mb: DslValue[int] | None = None
    min_memory_required_in_mb: DslValue[int] | None = None
    number_of_accelerator_devices_required: DslValue[float] | None = None
    number_of_cpu_cores_required: DslValue[float] | None = None


@dataclass
class InferenceComponentContainerSpecification(PropertyType):
    artifact_url: DslValue[str] | None = None
    deployed_image: DslValue[DeployedImage] | None = None
    environment: dict[str, DslValue[str]] = field(default_factory=dict)
    image: DslValue[str] | None = None


@dataclass
class InferenceComponentDeploymentConfig(PropertyType):
    auto_rollback_configuration: DslValue[AutoRollbackConfiguration] | None = None
    rolling_update_policy: DslValue[InferenceComponentRollingUpdatePolicy] | None = None


@dataclass
class InferenceComponentRollingUpdatePolicy(PropertyType):
    maximum_batch_size: DslValue[InferenceComponentCapacitySize] | None = None
    maximum_execution_timeout_in_seconds: DslValue[int] | None = None
    rollback_maximum_batch_size: DslValue[InferenceComponentCapacitySize] | None = None
    wait_interval_in_seconds: DslValue[int] | None = None


@dataclass
class InferenceComponentRuntimeConfig(PropertyType):
    copy_count: DslValue[int] | None = None
    current_copy_count: DslValue[int] | None = None
    desired_copy_count: DslValue[int] | None = None


@dataclass
class InferenceComponentSpecification(PropertyType):
    base_inference_component_name: DslValue[str] | None = None
    compute_resource_requirements: (
        DslValue[InferenceComponentComputeResourceRequirements] | None
    ) = None
    container: DslValue[InferenceComponentContainerSpecification] | None = None
    model_name: DslValue[str] | None = None
    startup_parameters: DslValue[InferenceComponentStartupParameters] | None = None


@dataclass
class InferenceComponentStartupParameters(PropertyType):
    container_startup_health_check_timeout_in_seconds: DslValue[int] | None = None
    model_data_download_timeout_in_seconds: DslValue[int] | None = None
