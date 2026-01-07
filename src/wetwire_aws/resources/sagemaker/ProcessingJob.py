"""PropertyTypes for AWS::SageMaker::ProcessingJob."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppSpecification(PropertyType):
    image_uri: DslValue[str] | None = None
    container_arguments: list[DslValue[str]] = field(default_factory=list)
    container_entrypoint: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AthenaDatasetDefinition(PropertyType):
    catalog: DslValue[str] | None = None
    database: DslValue[str] | None = None
    output_format: DslValue[str] | None = None
    output_s3_uri: DslValue[str] | None = None
    query_string: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    output_compression: DslValue[str] | None = None
    work_group: DslValue[str] | None = None


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
class DatasetDefinition(PropertyType):
    athena_dataset_definition: DslValue[AthenaDatasetDefinition] | None = None
    data_distribution_type: DslValue[str] | None = None
    input_mode: DslValue[str] | None = None
    local_path: DslValue[str] | None = None
    redshift_dataset_definition: DslValue[RedshiftDatasetDefinition] | None = None


@dataclass
class ExperimentConfig(PropertyType):
    experiment_name: DslValue[str] | None = None
    run_name: DslValue[str] | None = None
    trial_component_display_name: DslValue[str] | None = None
    trial_name: DslValue[str] | None = None


@dataclass
class FeatureStoreOutput(PropertyType):
    feature_group_name: DslValue[str] | None = None


@dataclass
class NetworkConfig(PropertyType):
    enable_inter_container_traffic_encryption: DslValue[bool] | None = None
    enable_network_isolation: DslValue[bool] | None = None
    vpc_config: DslValue[VpcConfig] | None = None


@dataclass
class ProcessingInputsObject(PropertyType):
    input_name: DslValue[str] | None = None
    app_managed: DslValue[bool] | None = None
    dataset_definition: DslValue[DatasetDefinition] | None = None
    s3_input: DslValue[S3Input] | None = None


@dataclass
class ProcessingOutputConfig(PropertyType):
    outputs: list[DslValue[ProcessingOutputsObject]] = field(default_factory=list)
    kms_key_id: DslValue[str] | None = None


@dataclass
class ProcessingOutputsObject(PropertyType):
    output_name: DslValue[str] | None = None
    app_managed: DslValue[bool] | None = None
    feature_store_output: DslValue[FeatureStoreOutput] | None = None
    s3_output: DslValue[S3Output] | None = None


@dataclass
class ProcessingResources(PropertyType):
    cluster_config: DslValue[ClusterConfig] | None = None


@dataclass
class RedshiftDatasetDefinition(PropertyType):
    cluster_id: DslValue[str] | None = None
    cluster_role_arn: DslValue[str] | None = None
    database: DslValue[str] | None = None
    db_user: DslValue[str] | None = None
    output_format: DslValue[str] | None = None
    output_s3_uri: DslValue[str] | None = None
    query_string: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    output_compression: DslValue[str] | None = None


@dataclass
class S3Input(PropertyType):
    s3_data_type: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    local_path: DslValue[str] | None = None
    s3_compression_type: DslValue[str] | None = None
    s3_data_distribution_type: DslValue[str] | None = None
    s3_input_mode: DslValue[str] | None = None


@dataclass
class S3Output(PropertyType):
    s3_upload_mode: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    local_path: DslValue[str] | None = None


@dataclass
class StoppingCondition(PropertyType):
    max_runtime_in_seconds: DslValue[int] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
