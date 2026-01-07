"""PropertyTypes for AWS::Events::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppSyncParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "graph_ql_operation": "GraphQLOperation",
    }

    graph_ql_operation: DslValue[str] | None = None


@dataclass
class AwsVpcConfiguration(PropertyType):
    subnets: list[DslValue[str]] = field(default_factory=list)
    assign_public_ip: DslValue[str] | None = None
    security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class BatchArrayProperties(PropertyType):
    size: DslValue[int] | None = None


@dataclass
class BatchParameters(PropertyType):
    job_definition: DslValue[str] | None = None
    job_name: DslValue[str] | None = None
    array_properties: DslValue[BatchArrayProperties] | None = None
    retry_strategy: DslValue[BatchRetryStrategy] | None = None


@dataclass
class BatchRetryStrategy(PropertyType):
    attempts: DslValue[int] | None = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    capacity_provider: DslValue[str] | None = None
    base: DslValue[int] | None = None
    weight: DslValue[int] | None = None


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
    placement_strategies: list[DslValue[PlacementStrategy]] = field(
        default_factory=list
    )
    platform_version: DslValue[str] | None = None
    propagate_tags: DslValue[str] | None = None
    reference_id: DslValue[str] | None = None
    tag_list: list[DslValue[Tag]] = field(default_factory=list)
    task_count: DslValue[int] | None = None


@dataclass
class HttpParameters(PropertyType):
    header_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    path_parameter_values: list[DslValue[str]] = field(default_factory=list)
    query_string_parameters: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class InputTransformer(PropertyType):
    input_template: DslValue[str] | None = None
    input_paths_map: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class KinesisParameters(PropertyType):
    partition_key_path: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    aws_vpc_configuration: DslValue[AwsVpcConfiguration] | None = None


@dataclass
class PlacementConstraint(PropertyType):
    expression: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class PlacementStrategy(PropertyType):
    field_: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class RedshiftDataParameters(PropertyType):
    database: DslValue[str] | None = None
    db_user: DslValue[str] | None = None
    secret_manager_arn: DslValue[str] | None = None
    sql: DslValue[str] | None = None
    sqls: list[DslValue[str]] = field(default_factory=list)
    statement_name: DslValue[str] | None = None
    with_event: DslValue[bool] | None = None


@dataclass
class RetryPolicy(PropertyType):
    maximum_event_age_in_seconds: DslValue[int] | None = None
    maximum_retry_attempts: DslValue[int] | None = None


@dataclass
class RunCommandParameters(PropertyType):
    run_command_targets: list[DslValue[RunCommandTarget]] = field(default_factory=list)


@dataclass
class RunCommandTarget(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


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
    id: DslValue[str] | None = None
    app_sync_parameters: DslValue[AppSyncParameters] | None = None
    batch_parameters: DslValue[BatchParameters] | None = None
    dead_letter_config: DslValue[DeadLetterConfig] | None = None
    ecs_parameters: DslValue[EcsParameters] | None = None
    http_parameters: DslValue[HttpParameters] | None = None
    input: DslValue[str] | None = None
    input_path: DslValue[str] | None = None
    input_transformer: DslValue[InputTransformer] | None = None
    kinesis_parameters: DslValue[KinesisParameters] | None = None
    redshift_data_parameters: DslValue[RedshiftDataParameters] | None = None
    retry_policy: DslValue[RetryPolicy] | None = None
    role_arn: DslValue[str] | None = None
    run_command_parameters: DslValue[RunCommandParameters] | None = None
    sage_maker_pipeline_parameters: DslValue[SageMakerPipelineParameters] | None = None
    sqs_parameters: DslValue[SqsParameters] | None = None
