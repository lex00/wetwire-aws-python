"""PropertyTypes for AWS::SageMaker::ModelPackage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdditionalInferenceSpecificationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_response_mime_types": "SupportedResponseMIMETypes",
    }

    containers: list[ModelPackageContainerDefinition] = field(default_factory=list)
    name: str | None = None
    description: str | None = None
    supported_content_types: list[String] = field(default_factory=list)
    supported_realtime_inference_instance_types: list[String] = field(
        default_factory=list
    )
    supported_response_mime_types: list[String] = field(default_factory=list)
    supported_transform_instance_types: list[String] = field(default_factory=list)


@dataclass
class Bias(PropertyType):
    post_training_report: MetricsSource | None = None
    pre_training_report: MetricsSource | None = None
    report: MetricsSource | None = None


@dataclass
class DataSource(PropertyType):
    s3_data_source: S3DataSource | None = None


@dataclass
class DriftCheckBaselines(PropertyType):
    bias: DriftCheckBias | None = None
    explainability: DriftCheckExplainability | None = None
    model_data_quality: DriftCheckModelDataQuality | None = None
    model_quality: DriftCheckModelQuality | None = None


@dataclass
class DriftCheckBias(PropertyType):
    config_file: FileSource | None = None
    post_training_constraints: MetricsSource | None = None
    pre_training_constraints: MetricsSource | None = None


@dataclass
class DriftCheckExplainability(PropertyType):
    config_file: FileSource | None = None
    constraints: MetricsSource | None = None


@dataclass
class DriftCheckModelDataQuality(PropertyType):
    constraints: MetricsSource | None = None
    statistics: MetricsSource | None = None


@dataclass
class DriftCheckModelQuality(PropertyType):
    constraints: MetricsSource | None = None
    statistics: MetricsSource | None = None


@dataclass
class Explainability(PropertyType):
    report: MetricsSource | None = None


@dataclass
class FileSource(PropertyType):
    s3_uri: str | None = None
    content_digest: str | None = None
    content_type: str | None = None


@dataclass
class InferenceSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_response_mime_types": "SupportedResponseMIMETypes",
    }

    containers: list[ModelPackageContainerDefinition] = field(default_factory=list)
    supported_content_types: list[String] = field(default_factory=list)
    supported_response_mime_types: list[String] = field(default_factory=list)
    supported_realtime_inference_instance_types: list[String] = field(
        default_factory=list
    )
    supported_transform_instance_types: list[String] = field(default_factory=list)


@dataclass
class MetadataProperties(PropertyType):
    commit_id: str | None = None
    generated_by: str | None = None
    project_id: str | None = None
    repository: str | None = None


@dataclass
class MetricsSource(PropertyType):
    content_type: str | None = None
    s3_uri: str | None = None
    content_digest: str | None = None


@dataclass
class ModelAccessConfig(PropertyType):
    accept_eula: bool | None = None


@dataclass
class ModelCard(PropertyType):
    model_card_content: str | None = None
    model_card_status: str | None = None


@dataclass
class ModelDataQuality(PropertyType):
    constraints: MetricsSource | None = None
    statistics: MetricsSource | None = None


@dataclass
class ModelDataSource(PropertyType):
    s3_data_source: S3ModelDataSource | None = None


@dataclass
class ModelInput(PropertyType):
    data_input_config: str | None = None


@dataclass
class ModelMetrics(PropertyType):
    bias: Bias | None = None
    explainability: Explainability | None = None
    model_data_quality: ModelDataQuality | None = None
    model_quality: ModelQuality | None = None


@dataclass
class ModelPackageContainerDefinition(PropertyType):
    image: str | None = None
    container_hostname: str | None = None
    environment: dict[str, String] = field(default_factory=dict)
    framework: str | None = None
    framework_version: str | None = None
    image_digest: str | None = None
    model_data_source: ModelDataSource | None = None
    model_data_url: str | None = None
    model_input: ModelInput | None = None
    nearest_model_name: str | None = None


@dataclass
class ModelPackageStatusDetails(PropertyType):
    validation_statuses: list[ModelPackageStatusItem] = field(default_factory=list)


@dataclass
class ModelPackageStatusItem(PropertyType):
    name: str | None = None
    status: str | None = None
    failure_reason: str | None = None


@dataclass
class ModelQuality(PropertyType):
    constraints: MetricsSource | None = None
    statistics: MetricsSource | None = None


@dataclass
class S3DataSource(PropertyType):
    s3_data_type: str | None = None
    s3_uri: str | None = None


@dataclass
class S3ModelDataSource(PropertyType):
    compression_type: str | None = None
    s3_data_type: str | None = None
    s3_uri: str | None = None
    model_access_config: ModelAccessConfig | None = None


@dataclass
class SecurityConfig(PropertyType):
    kms_key_id: str | None = None


@dataclass
class SourceAlgorithm(PropertyType):
    algorithm_name: str | None = None
    model_data_url: str | None = None


@dataclass
class SourceAlgorithmSpecification(PropertyType):
    source_algorithms: list[SourceAlgorithm] = field(default_factory=list)


@dataclass
class TransformInput(PropertyType):
    data_source: DataSource | None = None
    compression_type: str | None = None
    content_type: str | None = None
    split_type: str | None = None


@dataclass
class TransformJobDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_payload_in_mb": "MaxPayloadInMB",
    }

    transform_input: TransformInput | None = None
    transform_output: TransformOutput | None = None
    transform_resources: TransformResources | None = None
    batch_strategy: str | None = None
    environment: dict[str, String] = field(default_factory=dict)
    max_concurrent_transforms: int | None = None
    max_payload_in_mb: int | None = None


@dataclass
class TransformOutput(PropertyType):
    s3_output_path: str | None = None
    accept: str | None = None
    assemble_with: str | None = None
    kms_key_id: str | None = None


@dataclass
class TransformResources(PropertyType):
    instance_count: int | None = None
    instance_type: str | None = None
    volume_kms_key_id: str | None = None


@dataclass
class ValidationProfile(PropertyType):
    profile_name: str | None = None
    transform_job_definition: TransformJobDefinition | None = None


@dataclass
class ValidationSpecification(PropertyType):
    validation_profiles: list[ValidationProfile] = field(default_factory=list)
    validation_role: str | None = None
