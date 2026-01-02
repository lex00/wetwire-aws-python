"""PropertyTypes for AWS::SageMaker::InferenceComponent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Alarm(PropertyType):
    alarm_name: str | None = None


@dataclass
class AutoRollbackConfiguration(PropertyType):
    alarms: list[Alarm] = field(default_factory=list)


@dataclass
class DeployedImage(PropertyType):
    resolution_time: str | None = None
    resolved_image: str | None = None
    specified_image: str | None = None


@dataclass
class InferenceComponentCapacitySize(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class InferenceComponentComputeResourceRequirements(PropertyType):
    max_memory_required_in_mb: int | None = None
    min_memory_required_in_mb: int | None = None
    number_of_accelerator_devices_required: float | None = None
    number_of_cpu_cores_required: float | None = None


@dataclass
class InferenceComponentContainerSpecification(PropertyType):
    artifact_url: str | None = None
    deployed_image: DeployedImage | None = None
    environment: dict[str, String] = field(default_factory=dict)
    image: str | None = None


@dataclass
class InferenceComponentDeploymentConfig(PropertyType):
    auto_rollback_configuration: AutoRollbackConfiguration | None = None
    rolling_update_policy: InferenceComponentRollingUpdatePolicy | None = None


@dataclass
class InferenceComponentRollingUpdatePolicy(PropertyType):
    maximum_batch_size: InferenceComponentCapacitySize | None = None
    maximum_execution_timeout_in_seconds: int | None = None
    rollback_maximum_batch_size: InferenceComponentCapacitySize | None = None
    wait_interval_in_seconds: int | None = None


@dataclass
class InferenceComponentRuntimeConfig(PropertyType):
    copy_count: int | None = None
    current_copy_count: int | None = None
    desired_copy_count: int | None = None


@dataclass
class InferenceComponentSpecification(PropertyType):
    base_inference_component_name: str | None = None
    compute_resource_requirements: (
        InferenceComponentComputeResourceRequirements | None
    ) = None
    container: InferenceComponentContainerSpecification | None = None
    model_name: str | None = None
    startup_parameters: InferenceComponentStartupParameters | None = None


@dataclass
class InferenceComponentStartupParameters(PropertyType):
    container_startup_health_check_timeout_in_seconds: int | None = None
    model_data_download_timeout_in_seconds: int | None = None
