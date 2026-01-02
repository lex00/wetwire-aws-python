"""PropertyTypes for AWS::Scheduler::Schedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsVpcConfiguration(PropertyType):
    subnets: list[String] = field(default_factory=list)
    assign_public_ip: str | None = None
    security_groups: list[String] = field(default_factory=list)


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    capacity_provider: str | None = None
    base: float | None = None
    weight: float | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    arn: str | None = None


@dataclass
class EcsParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_ecs_managed_tags": "EnableECSManagedTags",
    }

    task_definition_arn: str | None = None
    capacity_provider_strategy: list[CapacityProviderStrategyItem] = field(
        default_factory=list
    )
    enable_ecs_managed_tags: bool | None = None
    enable_execute_command: bool | None = None
    group: str | None = None
    launch_type: str | None = None
    network_configuration: NetworkConfiguration | None = None
    placement_constraints: list[PlacementConstraint] = field(default_factory=list)
    placement_strategy: list[PlacementStrategy] = field(default_factory=list)
    platform_version: str | None = None
    propagate_tags: str | None = None
    reference_id: str | None = None
    tags: dict[str, Any] | None = None
    task_count: float | None = None


@dataclass
class EventBridgeParameters(PropertyType):
    detail_type: str | None = None
    source: str | None = None


@dataclass
class FlexibleTimeWindow(PropertyType):
    mode: str | None = None
    maximum_window_in_minutes: float | None = None


@dataclass
class KinesisParameters(PropertyType):
    partition_key: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    awsvpc_configuration: AwsVpcConfiguration | None = None


@dataclass
class PlacementConstraint(PropertyType):
    expression: str | None = None
    type_: str | None = None


@dataclass
class PlacementStrategy(PropertyType):
    field_: str | None = None
    type_: str | None = None


@dataclass
class RetryPolicy(PropertyType):
    maximum_event_age_in_seconds: float | None = None
    maximum_retry_attempts: float | None = None


@dataclass
class SageMakerPipelineParameter(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class SageMakerPipelineParameters(PropertyType):
    pipeline_parameter_list: list[SageMakerPipelineParameter] = field(
        default_factory=list
    )


@dataclass
class SqsParameters(PropertyType):
    message_group_id: str | None = None


@dataclass
class Target(PropertyType):
    arn: str | None = None
    role_arn: str | None = None
    dead_letter_config: DeadLetterConfig | None = None
    ecs_parameters: EcsParameters | None = None
    event_bridge_parameters: EventBridgeParameters | None = None
    input: str | None = None
    kinesis_parameters: KinesisParameters | None = None
    retry_policy: RetryPolicy | None = None
    sage_maker_pipeline_parameters: SageMakerPipelineParameters | None = None
    sqs_parameters: SqsParameters | None = None
