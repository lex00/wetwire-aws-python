"""PropertyTypes for AWS::Scheduler::Schedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsVpcConfiguration(PropertyType):
    subnets: list[DslValue[str]] = field(default_factory=list)
    assign_public_ip: DslValue[str] | None = None
    security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    capacity_provider: DslValue[str] | None = None
    base: DslValue[float] | None = None
    weight: DslValue[float] | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class EcsParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_ecs_managed_tags": "EnableECSManagedTags",
    }

    task_definition_arn: DslValue[str] | None = None
    capacity_provider_strategy: list[DslValue[CapacityProviderStrategyItem]] = field(
        default_factory=list
    )
    enable_ecs_managed_tags: DslValue[bool] | None = None
    enable_execute_command: DslValue[bool] | None = None
    group: DslValue[str] | None = None
    launch_type: DslValue[str] | None = None
    network_configuration: DslValue[NetworkConfiguration] | None = None
    placement_constraints: list[DslValue[PlacementConstraint]] = field(
        default_factory=list
    )
    placement_strategy: list[DslValue[PlacementStrategy]] = field(default_factory=list)
    platform_version: DslValue[str] | None = None
    propagate_tags: DslValue[str] | None = None
    reference_id: DslValue[str] | None = None
    tags: DslValue[dict[str, Any]] | None = None
    task_count: DslValue[float] | None = None


@dataclass
class EventBridgeParameters(PropertyType):
    detail_type: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class FlexibleTimeWindow(PropertyType):
    mode: DslValue[str] | None = None
    maximum_window_in_minutes: DslValue[float] | None = None


@dataclass
class KinesisParameters(PropertyType):
    partition_key: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    awsvpc_configuration: DslValue[AwsVpcConfiguration] | None = None


@dataclass
class PlacementConstraint(PropertyType):
    expression: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class PlacementStrategy(PropertyType):
    field_: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class RetryPolicy(PropertyType):
    maximum_event_age_in_seconds: DslValue[float] | None = None
    maximum_retry_attempts: DslValue[float] | None = None


@dataclass
class SageMakerPipelineParameter(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SageMakerPipelineParameters(PropertyType):
    pipeline_parameter_list: list[DslValue[SageMakerPipelineParameter]] = field(
        default_factory=list
    )


@dataclass
class SqsParameters(PropertyType):
    message_group_id: DslValue[str] | None = None


@dataclass
class Target(PropertyType):
    arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    dead_letter_config: DslValue[DeadLetterConfig] | None = None
    ecs_parameters: DslValue[EcsParameters] | None = None
    event_bridge_parameters: DslValue[EventBridgeParameters] | None = None
    input: DslValue[str] | None = None
    kinesis_parameters: DslValue[KinesisParameters] | None = None
    retry_policy: DslValue[RetryPolicy] | None = None
    sage_maker_pipeline_parameters: DslValue[SageMakerPipelineParameters] | None = None
    sqs_parameters: DslValue[SqsParameters] | None = None
