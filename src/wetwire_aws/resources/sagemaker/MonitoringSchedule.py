"""PropertyTypes for AWS::SageMaker::MonitoringSchedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BaselineConfig(PropertyType):
    constraints_resource: ConstraintsResource | None = None
    statistics_resource: StatisticsResource | None = None


@dataclass
class BatchTransformInput(PropertyType):
    data_captured_destination_s3_uri: str | None = None
    dataset_format: DatasetFormat | None = None
    local_path: str | None = None
    exclude_features_attribute: str | None = None
    s3_data_distribution_type: str | None = None
    s3_input_mode: str | None = None


@dataclass
class ClusterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    instance_count: int | None = None
    instance_type: str | None = None
    volume_size_in_gb: int | None = None
    volume_kms_key_id: str | None = None


@dataclass
class ConstraintsResource(PropertyType):
    s3_uri: str | None = None


@dataclass
class Csv(PropertyType):
    header: bool | None = None


@dataclass
class DatasetFormat(PropertyType):
    csv: Csv | None = None
    json: Json | None = None
    parquet: bool | None = None


@dataclass
class EndpointInput(PropertyType):
    endpoint_name: str | None = None
    local_path: str | None = None
    exclude_features_attribute: str | None = None
    s3_data_distribution_type: str | None = None
    s3_input_mode: str | None = None


@dataclass
class Json(PropertyType):
    line: bool | None = None


@dataclass
class MonitoringAppSpecification(PropertyType):
    image_uri: str | None = None
    container_arguments: list[String] = field(default_factory=list)
    container_entrypoint: list[String] = field(default_factory=list)
    post_analytics_processor_source_uri: str | None = None
    record_preprocessor_source_uri: str | None = None


@dataclass
class MonitoringExecutionSummary(PropertyType):
    creation_time: str | None = None
    last_modified_time: str | None = None
    monitoring_execution_status: str | None = None
    monitoring_schedule_name: str | None = None
    scheduled_time: str | None = None
    endpoint_name: str | None = None
    failure_reason: str | None = None
    processing_job_arn: str | None = None


@dataclass
class MonitoringInput(PropertyType):
    batch_transform_input: BatchTransformInput | None = None
    endpoint_input: EndpointInput | None = None


@dataclass
class MonitoringJobDefinition(PropertyType):
    monitoring_app_specification: MonitoringAppSpecification | None = None
    monitoring_inputs: list[MonitoringInput] = field(default_factory=list)
    monitoring_output_config: MonitoringOutputConfig | None = None
    monitoring_resources: MonitoringResources | None = None
    role_arn: str | None = None
    baseline_config: BaselineConfig | None = None
    environment: dict[str, String] = field(default_factory=dict)
    network_config: NetworkConfig | None = None
    stopping_condition: StoppingCondition | None = None


@dataclass
class MonitoringOutput(PropertyType):
    s3_output: S3Output | None = None


@dataclass
class MonitoringOutputConfig(PropertyType):
    monitoring_outputs: list[MonitoringOutput] = field(default_factory=list)
    kms_key_id: str | None = None


@dataclass
class MonitoringResources(PropertyType):
    cluster_config: ClusterConfig | None = None


@dataclass
class MonitoringScheduleConfig(PropertyType):
    monitoring_job_definition: MonitoringJobDefinition | None = None
    monitoring_job_definition_name: str | None = None
    monitoring_type: str | None = None
    schedule_config: ScheduleConfig | None = None


@dataclass
class NetworkConfig(PropertyType):
    enable_inter_container_traffic_encryption: bool | None = None
    enable_network_isolation: bool | None = None
    vpc_config: VpcConfig | None = None


@dataclass
class S3Output(PropertyType):
    local_path: str | None = None
    s3_uri: str | None = None
    s3_upload_mode: str | None = None


@dataclass
class ScheduleConfig(PropertyType):
    schedule_expression: str | None = None
    data_analysis_end_time: str | None = None
    data_analysis_start_time: str | None = None


@dataclass
class StatisticsResource(PropertyType):
    s3_uri: str | None = None


@dataclass
class StoppingCondition(PropertyType):
    max_runtime_in_seconds: int | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
