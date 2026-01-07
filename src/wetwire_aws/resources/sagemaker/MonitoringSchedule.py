"""PropertyTypes for AWS::SageMaker::MonitoringSchedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BaselineConfig(PropertyType):
    constraints_resource: DslValue[ConstraintsResource] | None = None
    statistics_resource: DslValue[StatisticsResource] | None = None


@dataclass
class BatchTransformInput(PropertyType):
    data_captured_destination_s3_uri: DslValue[str] | None = None
    dataset_format: DslValue[DatasetFormat] | None = None
    local_path: DslValue[str] | None = None
    exclude_features_attribute: DslValue[str] | None = None
    s3_data_distribution_type: DslValue[str] | None = None
    s3_input_mode: DslValue[str] | None = None


@dataclass
class ClusterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    instance_count: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None
    volume_size_in_gb: DslValue[int] | None = None
    volume_kms_key_id: DslValue[str] | None = None


@dataclass
class ConstraintsResource(PropertyType):
    s3_uri: DslValue[str] | None = None


@dataclass
class Csv(PropertyType):
    header: DslValue[bool] | None = None


@dataclass
class DatasetFormat(PropertyType):
    csv: DslValue[Csv] | None = None
    json: DslValue[Json] | None = None
    parquet: DslValue[bool] | None = None


@dataclass
class EndpointInput(PropertyType):
    endpoint_name: DslValue[str] | None = None
    local_path: DslValue[str] | None = None
    exclude_features_attribute: DslValue[str] | None = None
    s3_data_distribution_type: DslValue[str] | None = None
    s3_input_mode: DslValue[str] | None = None


@dataclass
class Json(PropertyType):
    line: DslValue[bool] | None = None


@dataclass
class MonitoringAppSpecification(PropertyType):
    image_uri: DslValue[str] | None = None
    container_arguments: list[DslValue[str]] = field(default_factory=list)
    container_entrypoint: list[DslValue[str]] = field(default_factory=list)
    post_analytics_processor_source_uri: DslValue[str] | None = None
    record_preprocessor_source_uri: DslValue[str] | None = None


@dataclass
class MonitoringExecutionSummary(PropertyType):
    creation_time: DslValue[str] | None = None
    last_modified_time: DslValue[str] | None = None
    monitoring_execution_status: DslValue[str] | None = None
    monitoring_schedule_name: DslValue[str] | None = None
    scheduled_time: DslValue[str] | None = None
    endpoint_name: DslValue[str] | None = None
    failure_reason: DslValue[str] | None = None
    processing_job_arn: DslValue[str] | None = None


@dataclass
class MonitoringInput(PropertyType):
    batch_transform_input: DslValue[BatchTransformInput] | None = None
    endpoint_input: DslValue[EndpointInput] | None = None


@dataclass
class MonitoringJobDefinition(PropertyType):
    monitoring_app_specification: DslValue[MonitoringAppSpecification] | None = None
    monitoring_inputs: list[DslValue[MonitoringInput]] = field(default_factory=list)
    monitoring_output_config: DslValue[MonitoringOutputConfig] | None = None
    monitoring_resources: DslValue[MonitoringResources] | None = None
    role_arn: DslValue[str] | None = None
    baseline_config: DslValue[BaselineConfig] | None = None
    environment: dict[str, DslValue[str]] = field(default_factory=dict)
    network_config: DslValue[NetworkConfig] | None = None
    stopping_condition: DslValue[StoppingCondition] | None = None


@dataclass
class MonitoringOutput(PropertyType):
    s3_output: DslValue[S3Output] | None = None


@dataclass
class MonitoringOutputConfig(PropertyType):
    monitoring_outputs: list[DslValue[MonitoringOutput]] = field(default_factory=list)
    kms_key_id: DslValue[str] | None = None


@dataclass
class MonitoringResources(PropertyType):
    cluster_config: DslValue[ClusterConfig] | None = None


@dataclass
class MonitoringScheduleConfig(PropertyType):
    monitoring_job_definition: DslValue[MonitoringJobDefinition] | None = None
    monitoring_job_definition_name: DslValue[str] | None = None
    monitoring_type: DslValue[str] | None = None
    schedule_config: DslValue[ScheduleConfig] | None = None


@dataclass
class NetworkConfig(PropertyType):
    enable_inter_container_traffic_encryption: DslValue[bool] | None = None
    enable_network_isolation: DslValue[bool] | None = None
    vpc_config: DslValue[VpcConfig] | None = None


@dataclass
class S3Output(PropertyType):
    local_path: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    s3_upload_mode: DslValue[str] | None = None


@dataclass
class ScheduleConfig(PropertyType):
    schedule_expression: DslValue[str] | None = None
    data_analysis_end_time: DslValue[str] | None = None
    data_analysis_start_time: DslValue[str] | None = None


@dataclass
class StatisticsResource(PropertyType):
    s3_uri: DslValue[str] | None = None


@dataclass
class StoppingCondition(PropertyType):
    max_runtime_in_seconds: DslValue[int] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
