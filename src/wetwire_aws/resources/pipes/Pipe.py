"""PropertyTypes for AWS::Pipes::Pipe."""

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
class BatchArrayProperties(PropertyType):
    size: DslValue[int] | None = None


@dataclass
class BatchContainerOverrides(PropertyType):
    command: list[DslValue[str]] = field(default_factory=list)
    environment: list[DslValue[BatchEnvironmentVariable]] = field(default_factory=list)
    instance_type: DslValue[str] | None = None
    resource_requirements: list[DslValue[BatchResourceRequirement]] = field(
        default_factory=list
    )


@dataclass
class BatchEnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class BatchJobDependency(PropertyType):
    job_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class BatchResourceRequirement(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class BatchRetryStrategy(PropertyType):
    attempts: DslValue[int] | None = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    capacity_provider: DslValue[str] | None = None
    base: DslValue[int] | None = None
    weight: DslValue[int] | None = None


@dataclass
class CloudwatchLogsLogDestination(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class DimensionMapping(PropertyType):
    dimension_name: DslValue[str] | None = None
    dimension_value: DslValue[str] | None = None
    dimension_value_type: DslValue[str] | None = None


@dataclass
class EcsContainerOverride(PropertyType):
    command: list[DslValue[str]] = field(default_factory=list)
    cpu: DslValue[int] | None = None
    environment: list[DslValue[EcsEnvironmentVariable]] = field(default_factory=list)
    environment_files: list[DslValue[EcsEnvironmentFile]] = field(default_factory=list)
    memory: DslValue[int] | None = None
    memory_reservation: DslValue[int] | None = None
    name: DslValue[str] | None = None
    resource_requirements: list[DslValue[EcsResourceRequirement]] = field(
        default_factory=list
    )


@dataclass
class EcsEnvironmentFile(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EcsEnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EcsEphemeralStorage(PropertyType):
    size_in_gi_b: DslValue[int] | None = None


@dataclass
class EcsInferenceAcceleratorOverride(PropertyType):
    device_name: DslValue[str] | None = None
    device_type: DslValue[str] | None = None


@dataclass
class EcsResourceRequirement(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EcsTaskOverride(PropertyType):
    container_overrides: list[DslValue[EcsContainerOverride]] = field(
        default_factory=list
    )
    cpu: DslValue[str] | None = None
    ephemeral_storage: DslValue[EcsEphemeralStorage] | None = None
    execution_role_arn: DslValue[str] | None = None
    inference_accelerator_overrides: list[DslValue[EcsInferenceAcceleratorOverride]] = (
        field(default_factory=list)
    )
    memory: DslValue[str] | None = None
    task_role_arn: DslValue[str] | None = None


@dataclass
class Filter(PropertyType):
    pattern: DslValue[str] | None = None


@dataclass
class FilterCriteria(PropertyType):
    filters: list[DslValue[Filter]] = field(default_factory=list)


@dataclass
class FirehoseLogDestination(PropertyType):
    delivery_stream_arn: DslValue[str] | None = None


@dataclass
class MQBrokerAccessCredentials(PropertyType):
    basic_auth: DslValue[str] | None = None


@dataclass
class MSKAccessCredentials(PropertyType):
    client_certificate_tls_auth: DslValue[str] | None = None
    sasl_scram512_auth: DslValue[str] | None = None


@dataclass
class MultiMeasureAttributeMapping(PropertyType):
    measure_value: DslValue[str] | None = None
    measure_value_type: DslValue[str] | None = None
    multi_measure_attribute_name: DslValue[str] | None = None


@dataclass
class MultiMeasureMapping(PropertyType):
    multi_measure_attribute_mappings: list[DslValue[MultiMeasureAttributeMapping]] = (
        field(default_factory=list)
    )
    multi_measure_name: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    awsvpc_configuration: DslValue[AwsVpcConfiguration] | None = None


@dataclass
class PipeEnrichmentHttpParameters(PropertyType):
    header_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    path_parameter_values: list[DslValue[str]] = field(default_factory=list)
    query_string_parameters: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class PipeEnrichmentParameters(PropertyType):
    http_parameters: DslValue[PipeEnrichmentHttpParameters] | None = None
    input_template: DslValue[str] | None = None


@dataclass
class PipeLogConfiguration(PropertyType):
    cloudwatch_logs_log_destination: DslValue[CloudwatchLogsLogDestination] | None = (
        None
    )
    firehose_log_destination: DslValue[FirehoseLogDestination] | None = None
    include_execution_data: list[DslValue[str]] = field(default_factory=list)
    level: DslValue[str] | None = None
    s3_log_destination: DslValue[S3LogDestination] | None = None


@dataclass
class PipeSourceActiveMQBrokerParameters(PropertyType):
    credentials: DslValue[MQBrokerAccessCredentials] | None = None
    queue_name: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None


@dataclass
class PipeSourceDynamoDBStreamParameters(PropertyType):
    starting_position: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    dead_letter_config: DslValue[DeadLetterConfig] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None
    maximum_record_age_in_seconds: DslValue[int] | None = None
    maximum_retry_attempts: DslValue[int] | None = None
    on_partial_batch_item_failure: DslValue[str] | None = None
    parallelization_factor: DslValue[int] | None = None


@dataclass
class PipeSourceKinesisStreamParameters(PropertyType):
    starting_position: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    dead_letter_config: DslValue[DeadLetterConfig] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None
    maximum_record_age_in_seconds: DslValue[int] | None = None
    maximum_retry_attempts: DslValue[int] | None = None
    on_partial_batch_item_failure: DslValue[str] | None = None
    parallelization_factor: DslValue[int] | None = None
    starting_position_timestamp: DslValue[str] | None = None


@dataclass
class PipeSourceManagedStreamingKafkaParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupID",
    }

    topic_name: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    consumer_group_id: DslValue[str] | None = None
    credentials: DslValue[MSKAccessCredentials] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None
    starting_position: DslValue[str] | None = None


@dataclass
class PipeSourceParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "active_mq_broker_parameters": "ActiveMQBrokerParameters",
        "dynamo_db_stream_parameters": "DynamoDBStreamParameters",
        "rabbit_mq_broker_parameters": "RabbitMQBrokerParameters",
    }

    active_mq_broker_parameters: DslValue[PipeSourceActiveMQBrokerParameters] | None = (
        None
    )
    dynamo_db_stream_parameters: DslValue[PipeSourceDynamoDBStreamParameters] | None = (
        None
    )
    filter_criteria: DslValue[FilterCriteria] | None = None
    kinesis_stream_parameters: DslValue[PipeSourceKinesisStreamParameters] | None = None
    managed_streaming_kafka_parameters: (
        DslValue[PipeSourceManagedStreamingKafkaParameters] | None
    ) = None
    rabbit_mq_broker_parameters: DslValue[PipeSourceRabbitMQBrokerParameters] | None = (
        None
    )
    self_managed_kafka_parameters: (
        DslValue[PipeSourceSelfManagedKafkaParameters] | None
    ) = None
    sqs_queue_parameters: DslValue[PipeSourceSqsQueueParameters] | None = None


@dataclass
class PipeSourceRabbitMQBrokerParameters(PropertyType):
    credentials: DslValue[MQBrokerAccessCredentials] | None = None
    queue_name: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None
    virtual_host: DslValue[str] | None = None


@dataclass
class PipeSourceSelfManagedKafkaParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupID",
    }

    topic_name: DslValue[str] | None = None
    additional_bootstrap_servers: list[DslValue[str]] = field(default_factory=list)
    batch_size: DslValue[int] | None = None
    consumer_group_id: DslValue[str] | None = None
    credentials: DslValue[SelfManagedKafkaAccessConfigurationCredentials] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None
    server_root_ca_certificate: DslValue[str] | None = None
    starting_position: DslValue[str] | None = None
    vpc: DslValue[SelfManagedKafkaAccessConfigurationVpc] | None = None


@dataclass
class PipeSourceSqsQueueParameters(PropertyType):
    batch_size: DslValue[int] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None


@dataclass
class PipeTargetBatchJobParameters(PropertyType):
    job_definition: DslValue[str] | None = None
    job_name: DslValue[str] | None = None
    array_properties: DslValue[BatchArrayProperties] | None = None
    container_overrides: DslValue[BatchContainerOverrides] | None = None
    depends_on: list[DslValue[BatchJobDependency]] = field(default_factory=list)
    parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    retry_strategy: DslValue[BatchRetryStrategy] | None = None


@dataclass
class PipeTargetCloudWatchLogsParameters(PropertyType):
    log_stream_name: DslValue[str] | None = None
    timestamp: DslValue[str] | None = None


@dataclass
class PipeTargetEcsTaskParameters(PropertyType):
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
    overrides: DslValue[EcsTaskOverride] | None = None
    placement_constraints: list[DslValue[PlacementConstraint]] = field(
        default_factory=list
    )
    placement_strategy: list[DslValue[PlacementStrategy]] = field(default_factory=list)
    platform_version: DslValue[str] | None = None
    propagate_tags: DslValue[str] | None = None
    reference_id: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
    task_count: DslValue[int] | None = None


@dataclass
class PipeTargetEventBridgeEventBusParameters(PropertyType):
    detail_type: DslValue[str] | None = None
    endpoint_id: DslValue[str] | None = None
    resources: list[DslValue[str]] = field(default_factory=list)
    source: DslValue[str] | None = None
    time: DslValue[str] | None = None


@dataclass
class PipeTargetHttpParameters(PropertyType):
    header_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    path_parameter_values: list[DslValue[str]] = field(default_factory=list)
    query_string_parameters: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class PipeTargetKinesisStreamParameters(PropertyType):
    partition_key: DslValue[str] | None = None


@dataclass
class PipeTargetLambdaFunctionParameters(PropertyType):
    invocation_type: DslValue[str] | None = None


@dataclass
class PipeTargetParameters(PropertyType):
    batch_job_parameters: DslValue[PipeTargetBatchJobParameters] | None = None
    cloud_watch_logs_parameters: DslValue[PipeTargetCloudWatchLogsParameters] | None = (
        None
    )
    ecs_task_parameters: DslValue[PipeTargetEcsTaskParameters] | None = None
    event_bridge_event_bus_parameters: (
        DslValue[PipeTargetEventBridgeEventBusParameters] | None
    ) = None
    http_parameters: DslValue[PipeTargetHttpParameters] | None = None
    input_template: DslValue[str] | None = None
    kinesis_stream_parameters: DslValue[PipeTargetKinesisStreamParameters] | None = None
    lambda_function_parameters: DslValue[PipeTargetLambdaFunctionParameters] | None = (
        None
    )
    redshift_data_parameters: DslValue[PipeTargetRedshiftDataParameters] | None = None
    sage_maker_pipeline_parameters: (
        DslValue[PipeTargetSageMakerPipelineParameters] | None
    ) = None
    sqs_queue_parameters: DslValue[PipeTargetSqsQueueParameters] | None = None
    step_function_state_machine_parameters: (
        DslValue[PipeTargetStateMachineParameters] | None
    ) = None
    timestream_parameters: DslValue[PipeTargetTimestreamParameters] | None = None


@dataclass
class PipeTargetRedshiftDataParameters(PropertyType):
    database: DslValue[str] | None = None
    sqls: list[DslValue[str]] = field(default_factory=list)
    db_user: DslValue[str] | None = None
    secret_manager_arn: DslValue[str] | None = None
    statement_name: DslValue[str] | None = None
    with_event: DslValue[bool] | None = None


@dataclass
class PipeTargetSageMakerPipelineParameters(PropertyType):
    pipeline_parameter_list: list[DslValue[SageMakerPipelineParameter]] = field(
        default_factory=list
    )


@dataclass
class PipeTargetSqsQueueParameters(PropertyType):
    message_deduplication_id: DslValue[str] | None = None
    message_group_id: DslValue[str] | None = None


@dataclass
class PipeTargetStateMachineParameters(PropertyType):
    invocation_type: DslValue[str] | None = None


@dataclass
class PipeTargetTimestreamParameters(PropertyType):
    dimension_mappings: list[DslValue[DimensionMapping]] = field(default_factory=list)
    time_value: DslValue[str] | None = None
    version_value: DslValue[str] | None = None
    epoch_time_unit: DslValue[str] | None = None
    multi_measure_mappings: list[DslValue[MultiMeasureMapping]] = field(
        default_factory=list
    )
    single_measure_mappings: list[DslValue[SingleMeasureMapping]] = field(
        default_factory=list
    )
    time_field_type: DslValue[str] | None = None
    timestamp_format: DslValue[str] | None = None


@dataclass
class PlacementConstraint(PropertyType):
    expression: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class PlacementStrategy(PropertyType):
    field_: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class S3LogDestination(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    output_format: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class SageMakerPipelineParameter(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SelfManagedKafkaAccessConfigurationCredentials(PropertyType):
    basic_auth: DslValue[str] | None = None
    client_certificate_tls_auth: DslValue[str] | None = None
    sasl_scram256_auth: DslValue[str] | None = None
    sasl_scram512_auth: DslValue[str] | None = None


@dataclass
class SelfManagedKafkaAccessConfigurationVpc(PropertyType):
    security_group: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SingleMeasureMapping(PropertyType):
    measure_name: DslValue[str] | None = None
    measure_value: DslValue[str] | None = None
    measure_value_type: DslValue[str] | None = None
