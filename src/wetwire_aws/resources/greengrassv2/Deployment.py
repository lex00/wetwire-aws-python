"""PropertyTypes for AWS::GreengrassV2::Deployment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComponentConfigurationUpdate(PropertyType):
    merge: DslValue[str] | None = None
    reset: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ComponentDeploymentSpecification(PropertyType):
    component_version: DslValue[str] | None = None
    configuration_update: DslValue[ComponentConfigurationUpdate] | None = None
    run_with: DslValue[ComponentRunWith] | None = None


@dataclass
class ComponentRunWith(PropertyType):
    posix_user: DslValue[str] | None = None
    system_resource_limits: DslValue[SystemResourceLimits] | None = None
    windows_user: DslValue[str] | None = None


@dataclass
class DeploymentComponentUpdatePolicy(PropertyType):
    action: DslValue[str] | None = None
    timeout_in_seconds: DslValue[int] | None = None


@dataclass
class DeploymentConfigurationValidationPolicy(PropertyType):
    timeout_in_seconds: DslValue[int] | None = None


@dataclass
class DeploymentIoTJobConfiguration(PropertyType):
    abort_config: DslValue[IoTJobAbortConfig] | None = None
    job_executions_rollout_config: DslValue[IoTJobExecutionsRolloutConfig] | None = None
    timeout_config: DslValue[IoTJobTimeoutConfig] | None = None


@dataclass
class DeploymentPolicies(PropertyType):
    component_update_policy: DslValue[DeploymentComponentUpdatePolicy] | None = None
    configuration_validation_policy: (
        DslValue[DeploymentConfigurationValidationPolicy] | None
    ) = None
    failure_handling_policy: DslValue[str] | None = None


@dataclass
class IoTJobAbortConfig(PropertyType):
    criteria_list: list[DslValue[IoTJobAbortCriteria]] = field(default_factory=list)


@dataclass
class IoTJobAbortCriteria(PropertyType):
    action: DslValue[str] | None = None
    failure_type: DslValue[str] | None = None
    min_number_of_executed_things: DslValue[int] | None = None
    threshold_percentage: DslValue[float] | None = None


@dataclass
class IoTJobExecutionsRolloutConfig(PropertyType):
    exponential_rate: DslValue[IoTJobExponentialRolloutRate] | None = None
    maximum_per_minute: DslValue[int] | None = None


@dataclass
class IoTJobExponentialRolloutRate(PropertyType):
    base_rate_per_minute: DslValue[int] | None = None
    increment_factor: DslValue[float] | None = None
    rate_increase_criteria: DslValue[IoTJobRateIncreaseCriteria] | None = None


@dataclass
class IoTJobRateIncreaseCriteria(PropertyType):
    number_of_notified_things: DslValue[int] | None = None
    number_of_succeeded_things: DslValue[int] | None = None


@dataclass
class IoTJobTimeoutConfig(PropertyType):
    in_progress_timeout_in_minutes: DslValue[int] | None = None


@dataclass
class SystemResourceLimits(PropertyType):
    cpus: DslValue[float] | None = None
    memory: DslValue[int] | None = None
