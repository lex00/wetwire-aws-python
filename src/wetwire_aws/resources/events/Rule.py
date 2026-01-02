"""PropertyTypes for AWS::Events::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppSyncParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "graph_ql_operation": "GraphQLOperation",
    }

    graph_ql_operation: str | None = None


@dataclass
class AwsVpcConfiguration(PropertyType):
    subnets: list[String] = field(default_factory=list)
    assign_public_ip: str | None = None
    security_groups: list[String] = field(default_factory=list)


@dataclass
class BatchArrayProperties(PropertyType):
    size: int | None = None


@dataclass
class BatchParameters(PropertyType):
    job_definition: str | None = None
    job_name: str | None = None
    array_properties: BatchArrayProperties | None = None
    retry_strategy: BatchRetryStrategy | None = None


@dataclass
class BatchRetryStrategy(PropertyType):
    attempts: int | None = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    capacity_provider: str | None = None
    base: int | None = None
    weight: int | None = None


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
    placement_strategies: list[PlacementStrategy] = field(default_factory=list)
    platform_version: str | None = None
    propagate_tags: str | None = None
    reference_id: str | None = None
    tag_list: list[Tag] = field(default_factory=list)
    task_count: int | None = None


@dataclass
class HttpParameters(PropertyType):
    header_parameters: dict[str, String] = field(default_factory=dict)
    path_parameter_values: list[String] = field(default_factory=list)
    query_string_parameters: dict[str, String] = field(default_factory=dict)


@dataclass
class InputTransformer(PropertyType):
    input_template: str | None = None
    input_paths_map: dict[str, String] = field(default_factory=dict)


@dataclass
class KinesisParameters(PropertyType):
    partition_key_path: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    aws_vpc_configuration: AwsVpcConfiguration | None = None


@dataclass
class PlacementConstraint(PropertyType):
    expression: str | None = None
    type_: str | None = None


@dataclass
class PlacementStrategy(PropertyType):
    field_: str | None = None
    type_: str | None = None


@dataclass
class RedshiftDataParameters(PropertyType):
    database: str | None = None
    db_user: str | None = None
    secret_manager_arn: str | None = None
    sql: str | None = None
    sqls: list[String] = field(default_factory=list)
    statement_name: str | None = None
    with_event: bool | None = None


@dataclass
class RetryPolicy(PropertyType):
    maximum_event_age_in_seconds: int | None = None
    maximum_retry_attempts: int | None = None


@dataclass
class RunCommandParameters(PropertyType):
    run_command_targets: list[RunCommandTarget] = field(default_factory=list)


@dataclass
class RunCommandTarget(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)


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
    id: str | None = None
    app_sync_parameters: AppSyncParameters | None = None
    batch_parameters: BatchParameters | None = None
    dead_letter_config: DeadLetterConfig | None = None
    ecs_parameters: EcsParameters | None = None
    http_parameters: HttpParameters | None = None
    input: str | None = None
    input_path: str | None = None
    input_transformer: InputTransformer | None = None
    kinesis_parameters: KinesisParameters | None = None
    redshift_data_parameters: RedshiftDataParameters | None = None
    retry_policy: RetryPolicy | None = None
    role_arn: str | None = None
    run_command_parameters: RunCommandParameters | None = None
    sage_maker_pipeline_parameters: SageMakerPipelineParameters | None = None
    sqs_parameters: SqsParameters | None = None
