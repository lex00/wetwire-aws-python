"""PropertyTypes for AWS::Pipes::Pipe."""

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
class BatchArrayProperties(PropertyType):
    size: int | None = None


@dataclass
class BatchContainerOverrides(PropertyType):
    command: list[String] = field(default_factory=list)
    environment: list[BatchEnvironmentVariable] = field(default_factory=list)
    instance_type: str | None = None
    resource_requirements: list[BatchResourceRequirement] = field(default_factory=list)


@dataclass
class BatchEnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class BatchJobDependency(PropertyType):
    job_id: str | None = None
    type_: str | None = None


@dataclass
class BatchResourceRequirement(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class BatchRetryStrategy(PropertyType):
    attempts: int | None = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    capacity_provider: str | None = None
    base: int | None = None
    weight: int | None = None


@dataclass
class CloudwatchLogsLogDestination(PropertyType):
    log_group_arn: str | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    arn: str | None = None


@dataclass
class DimensionMapping(PropertyType):
    dimension_name: str | None = None
    dimension_value: str | None = None
    dimension_value_type: str | None = None


@dataclass
class EcsContainerOverride(PropertyType):
    command: list[String] = field(default_factory=list)
    cpu: int | None = None
    environment: list[EcsEnvironmentVariable] = field(default_factory=list)
    environment_files: list[EcsEnvironmentFile] = field(default_factory=list)
    memory: int | None = None
    memory_reservation: int | None = None
    name: str | None = None
    resource_requirements: list[EcsResourceRequirement] = field(default_factory=list)


@dataclass
class EcsEnvironmentFile(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class EcsEnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class EcsEphemeralStorage(PropertyType):
    size_in_gi_b: int | None = None


@dataclass
class EcsInferenceAcceleratorOverride(PropertyType):
    device_name: str | None = None
    device_type: str | None = None


@dataclass
class EcsResourceRequirement(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class EcsTaskOverride(PropertyType):
    container_overrides: list[EcsContainerOverride] = field(default_factory=list)
    cpu: str | None = None
    ephemeral_storage: EcsEphemeralStorage | None = None
    execution_role_arn: str | None = None
    inference_accelerator_overrides: list[EcsInferenceAcceleratorOverride] = field(
        default_factory=list
    )
    memory: str | None = None
    task_role_arn: str | None = None


@dataclass
class Filter(PropertyType):
    pattern: str | None = None


@dataclass
class FilterCriteria(PropertyType):
    filters: list[Filter] = field(default_factory=list)


@dataclass
class FirehoseLogDestination(PropertyType):
    delivery_stream_arn: str | None = None


@dataclass
class MQBrokerAccessCredentials(PropertyType):
    basic_auth: str | None = None


@dataclass
class MSKAccessCredentials(PropertyType):
    client_certificate_tls_auth: str | None = None
    sasl_scram512_auth: str | None = None


@dataclass
class MultiMeasureAttributeMapping(PropertyType):
    measure_value: str | None = None
    measure_value_type: str | None = None
    multi_measure_attribute_name: str | None = None


@dataclass
class MultiMeasureMapping(PropertyType):
    multi_measure_attribute_mappings: list[MultiMeasureAttributeMapping] = field(
        default_factory=list
    )
    multi_measure_name: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    awsvpc_configuration: AwsVpcConfiguration | None = None


@dataclass
class PipeEnrichmentHttpParameters(PropertyType):
    header_parameters: dict[str, String] = field(default_factory=dict)
    path_parameter_values: list[String] = field(default_factory=list)
    query_string_parameters: dict[str, String] = field(default_factory=dict)


@dataclass
class PipeEnrichmentParameters(PropertyType):
    http_parameters: PipeEnrichmentHttpParameters | None = None
    input_template: str | None = None


@dataclass
class PipeLogConfiguration(PropertyType):
    cloudwatch_logs_log_destination: CloudwatchLogsLogDestination | None = None
    firehose_log_destination: FirehoseLogDestination | None = None
    include_execution_data: list[String] = field(default_factory=list)
    level: str | None = None
    s3_log_destination: S3LogDestination | None = None


@dataclass
class PipeSourceActiveMQBrokerParameters(PropertyType):
    credentials: MQBrokerAccessCredentials | None = None
    queue_name: str | None = None
    batch_size: int | None = None
    maximum_batching_window_in_seconds: int | None = None


@dataclass
class PipeSourceDynamoDBStreamParameters(PropertyType):
    starting_position: str | None = None
    batch_size: int | None = None
    dead_letter_config: DeadLetterConfig | None = None
    maximum_batching_window_in_seconds: int | None = None
    maximum_record_age_in_seconds: int | None = None
    maximum_retry_attempts: int | None = None
    on_partial_batch_item_failure: str | None = None
    parallelization_factor: int | None = None


@dataclass
class PipeSourceKinesisStreamParameters(PropertyType):
    starting_position: str | None = None
    batch_size: int | None = None
    dead_letter_config: DeadLetterConfig | None = None
    maximum_batching_window_in_seconds: int | None = None
    maximum_record_age_in_seconds: int | None = None
    maximum_retry_attempts: int | None = None
    on_partial_batch_item_failure: str | None = None
    parallelization_factor: int | None = None
    starting_position_timestamp: str | None = None


@dataclass
class PipeSourceManagedStreamingKafkaParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupID",
    }

    topic_name: str | None = None
    batch_size: int | None = None
    consumer_group_id: str | None = None
    credentials: MSKAccessCredentials | None = None
    maximum_batching_window_in_seconds: int | None = None
    starting_position: str | None = None


@dataclass
class PipeSourceParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "active_mq_broker_parameters": "ActiveMQBrokerParameters",
        "dynamo_db_stream_parameters": "DynamoDBStreamParameters",
        "rabbit_mq_broker_parameters": "RabbitMQBrokerParameters",
    }

    active_mq_broker_parameters: PipeSourceActiveMQBrokerParameters | None = None
    dynamo_db_stream_parameters: PipeSourceDynamoDBStreamParameters | None = None
    filter_criteria: FilterCriteria | None = None
    kinesis_stream_parameters: PipeSourceKinesisStreamParameters | None = None
    managed_streaming_kafka_parameters: (
        PipeSourceManagedStreamingKafkaParameters | None
    ) = None
    rabbit_mq_broker_parameters: PipeSourceRabbitMQBrokerParameters | None = None
    self_managed_kafka_parameters: PipeSourceSelfManagedKafkaParameters | None = None
    sqs_queue_parameters: PipeSourceSqsQueueParameters | None = None


@dataclass
class PipeSourceRabbitMQBrokerParameters(PropertyType):
    credentials: MQBrokerAccessCredentials | None = None
    queue_name: str | None = None
    batch_size: int | None = None
    maximum_batching_window_in_seconds: int | None = None
    virtual_host: str | None = None


@dataclass
class PipeSourceSelfManagedKafkaParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupID",
    }

    topic_name: str | None = None
    additional_bootstrap_servers: list[String] = field(default_factory=list)
    batch_size: int | None = None
    consumer_group_id: str | None = None
    credentials: SelfManagedKafkaAccessConfigurationCredentials | None = None
    maximum_batching_window_in_seconds: int | None = None
    server_root_ca_certificate: str | None = None
    starting_position: str | None = None
    vpc: SelfManagedKafkaAccessConfigurationVpc | None = None


@dataclass
class PipeSourceSqsQueueParameters(PropertyType):
    batch_size: int | None = None
    maximum_batching_window_in_seconds: int | None = None


@dataclass
class PipeTargetBatchJobParameters(PropertyType):
    job_definition: str | None = None
    job_name: str | None = None
    array_properties: BatchArrayProperties | None = None
    container_overrides: BatchContainerOverrides | None = None
    depends_on: list[BatchJobDependency] = field(default_factory=list)
    parameters: dict[str, String] = field(default_factory=dict)
    retry_strategy: BatchRetryStrategy | None = None


@dataclass
class PipeTargetCloudWatchLogsParameters(PropertyType):
    log_stream_name: str | None = None
    timestamp: str | None = None


@dataclass
class PipeTargetEcsTaskParameters(PropertyType):
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
    overrides: EcsTaskOverride | None = None
    placement_constraints: list[PlacementConstraint] = field(default_factory=list)
    placement_strategy: list[PlacementStrategy] = field(default_factory=list)
    platform_version: str | None = None
    propagate_tags: str | None = None
    reference_id: str | None = None
    tags: list[Tag] = field(default_factory=list)
    task_count: int | None = None


@dataclass
class PipeTargetEventBridgeEventBusParameters(PropertyType):
    detail_type: str | None = None
    endpoint_id: str | None = None
    resources: list[String] = field(default_factory=list)
    source: str | None = None
    time: str | None = None


@dataclass
class PipeTargetHttpParameters(PropertyType):
    header_parameters: dict[str, String] = field(default_factory=dict)
    path_parameter_values: list[String] = field(default_factory=list)
    query_string_parameters: dict[str, String] = field(default_factory=dict)


@dataclass
class PipeTargetKinesisStreamParameters(PropertyType):
    partition_key: str | None = None


@dataclass
class PipeTargetLambdaFunctionParameters(PropertyType):
    invocation_type: str | None = None


@dataclass
class PipeTargetParameters(PropertyType):
    batch_job_parameters: PipeTargetBatchJobParameters | None = None
    cloud_watch_logs_parameters: PipeTargetCloudWatchLogsParameters | None = None
    ecs_task_parameters: PipeTargetEcsTaskParameters | None = None
    event_bridge_event_bus_parameters: (
        PipeTargetEventBridgeEventBusParameters | None
    ) = None
    http_parameters: PipeTargetHttpParameters | None = None
    input_template: str | None = None
    kinesis_stream_parameters: PipeTargetKinesisStreamParameters | None = None
    lambda_function_parameters: PipeTargetLambdaFunctionParameters | None = None
    redshift_data_parameters: PipeTargetRedshiftDataParameters | None = None
    sage_maker_pipeline_parameters: PipeTargetSageMakerPipelineParameters | None = None
    sqs_queue_parameters: PipeTargetSqsQueueParameters | None = None
    step_function_state_machine_parameters: PipeTargetStateMachineParameters | None = (
        None
    )
    timestream_parameters: PipeTargetTimestreamParameters | None = None


@dataclass
class PipeTargetRedshiftDataParameters(PropertyType):
    database: str | None = None
    sqls: list[String] = field(default_factory=list)
    db_user: str | None = None
    secret_manager_arn: str | None = None
    statement_name: str | None = None
    with_event: bool | None = None


@dataclass
class PipeTargetSageMakerPipelineParameters(PropertyType):
    pipeline_parameter_list: list[SageMakerPipelineParameter] = field(
        default_factory=list
    )


@dataclass
class PipeTargetSqsQueueParameters(PropertyType):
    message_deduplication_id: str | None = None
    message_group_id: str | None = None


@dataclass
class PipeTargetStateMachineParameters(PropertyType):
    invocation_type: str | None = None


@dataclass
class PipeTargetTimestreamParameters(PropertyType):
    dimension_mappings: list[DimensionMapping] = field(default_factory=list)
    time_value: str | None = None
    version_value: str | None = None
    epoch_time_unit: str | None = None
    multi_measure_mappings: list[MultiMeasureMapping] = field(default_factory=list)
    single_measure_mappings: list[SingleMeasureMapping] = field(default_factory=list)
    time_field_type: str | None = None
    timestamp_format: str | None = None


@dataclass
class PlacementConstraint(PropertyType):
    expression: str | None = None
    type_: str | None = None


@dataclass
class PlacementStrategy(PropertyType):
    field_: str | None = None
    type_: str | None = None


@dataclass
class S3LogDestination(PropertyType):
    bucket_name: str | None = None
    bucket_owner: str | None = None
    output_format: str | None = None
    prefix: str | None = None


@dataclass
class SageMakerPipelineParameter(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class SelfManagedKafkaAccessConfigurationCredentials(PropertyType):
    basic_auth: str | None = None
    client_certificate_tls_auth: str | None = None
    sasl_scram256_auth: str | None = None
    sasl_scram512_auth: str | None = None


@dataclass
class SelfManagedKafkaAccessConfigurationVpc(PropertyType):
    security_group: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)


@dataclass
class SingleMeasureMapping(PropertyType):
    measure_name: str | None = None
    measure_value: str | None = None
    measure_value_type: str | None = None
