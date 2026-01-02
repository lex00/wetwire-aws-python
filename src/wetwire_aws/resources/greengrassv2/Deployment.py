"""PropertyTypes for AWS::GreengrassV2::Deployment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComponentConfigurationUpdate(PropertyType):
    merge: str | None = None
    reset: list[String] = field(default_factory=list)


@dataclass
class ComponentDeploymentSpecification(PropertyType):
    component_version: str | None = None
    configuration_update: ComponentConfigurationUpdate | None = None
    run_with: ComponentRunWith | None = None


@dataclass
class ComponentRunWith(PropertyType):
    posix_user: str | None = None
    system_resource_limits: SystemResourceLimits | None = None
    windows_user: str | None = None


@dataclass
class DeploymentComponentUpdatePolicy(PropertyType):
    action: str | None = None
    timeout_in_seconds: int | None = None


@dataclass
class DeploymentConfigurationValidationPolicy(PropertyType):
    timeout_in_seconds: int | None = None


@dataclass
class DeploymentIoTJobConfiguration(PropertyType):
    abort_config: IoTJobAbortConfig | None = None
    job_executions_rollout_config: IoTJobExecutionsRolloutConfig | None = None
    timeout_config: IoTJobTimeoutConfig | None = None


@dataclass
class DeploymentPolicies(PropertyType):
    component_update_policy: DeploymentComponentUpdatePolicy | None = None
    configuration_validation_policy: DeploymentConfigurationValidationPolicy | None = (
        None
    )
    failure_handling_policy: str | None = None


@dataclass
class IoTJobAbortConfig(PropertyType):
    criteria_list: list[IoTJobAbortCriteria] = field(default_factory=list)


@dataclass
class IoTJobAbortCriteria(PropertyType):
    action: str | None = None
    failure_type: str | None = None
    min_number_of_executed_things: int | None = None
    threshold_percentage: float | None = None


@dataclass
class IoTJobExecutionsRolloutConfig(PropertyType):
    exponential_rate: IoTJobExponentialRolloutRate | None = None
    maximum_per_minute: int | None = None


@dataclass
class IoTJobExponentialRolloutRate(PropertyType):
    base_rate_per_minute: int | None = None
    increment_factor: float | None = None
    rate_increase_criteria: IoTJobRateIncreaseCriteria | None = None


@dataclass
class IoTJobRateIncreaseCriteria(PropertyType):
    number_of_notified_things: int | None = None
    number_of_succeeded_things: int | None = None


@dataclass
class IoTJobTimeoutConfig(PropertyType):
    in_progress_timeout_in_minutes: int | None = None


@dataclass
class SystemResourceLimits(PropertyType):
    cpus: float | None = None
    memory: int | None = None
