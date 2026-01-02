"""PropertyTypes for AWS::SageMaker::ProcessingJob."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppSpecification(PropertyType):
    image_uri: str | None = None
    container_arguments: list[String] = field(default_factory=list)
    container_entrypoint: list[String] = field(default_factory=list)


@dataclass
class AthenaDatasetDefinition(PropertyType):
    catalog: str | None = None
    database: str | None = None
    output_format: str | None = None
    output_s3_uri: str | None = None
    query_string: str | None = None
    kms_key_id: str | None = None
    output_compression: str | None = None
    work_group: str | None = None


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
class DatasetDefinition(PropertyType):
    athena_dataset_definition: AthenaDatasetDefinition | None = None
    data_distribution_type: str | None = None
    input_mode: str | None = None
    local_path: str | None = None
    redshift_dataset_definition: RedshiftDatasetDefinition | None = None


@dataclass
class ExperimentConfig(PropertyType):
    experiment_name: str | None = None
    run_name: str | None = None
    trial_component_display_name: str | None = None
    trial_name: str | None = None


@dataclass
class FeatureStoreOutput(PropertyType):
    feature_group_name: str | None = None


@dataclass
class NetworkConfig(PropertyType):
    enable_inter_container_traffic_encryption: bool | None = None
    enable_network_isolation: bool | None = None
    vpc_config: VpcConfig | None = None


@dataclass
class ProcessingInputsObject(PropertyType):
    input_name: str | None = None
    app_managed: bool | None = None
    dataset_definition: DatasetDefinition | None = None
    s3_input: S3Input | None = None


@dataclass
class ProcessingOutputConfig(PropertyType):
    outputs: list[ProcessingOutputsObject] = field(default_factory=list)
    kms_key_id: str | None = None


@dataclass
class ProcessingOutputsObject(PropertyType):
    output_name: str | None = None
    app_managed: bool | None = None
    feature_store_output: FeatureStoreOutput | None = None
    s3_output: S3Output | None = None


@dataclass
class ProcessingResources(PropertyType):
    cluster_config: ClusterConfig | None = None


@dataclass
class RedshiftDatasetDefinition(PropertyType):
    cluster_id: str | None = None
    cluster_role_arn: str | None = None
    database: str | None = None
    db_user: str | None = None
    output_format: str | None = None
    output_s3_uri: str | None = None
    query_string: str | None = None
    kms_key_id: str | None = None
    output_compression: str | None = None


@dataclass
class S3Input(PropertyType):
    s3_data_type: str | None = None
    s3_uri: str | None = None
    local_path: str | None = None
    s3_compression_type: str | None = None
    s3_data_distribution_type: str | None = None
    s3_input_mode: str | None = None


@dataclass
class S3Output(PropertyType):
    s3_upload_mode: str | None = None
    s3_uri: str | None = None
    local_path: str | None = None


@dataclass
class StoppingCondition(PropertyType):
    max_runtime_in_seconds: int | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
