"""PropertyTypes for AWS::SageMaker::ModelPackage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdditionalInferenceSpecificationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_response_mime_types": "SupportedResponseMIMETypes",
    }

    containers: list[DslValue[ModelPackageContainerDefinition]] = field(
        default_factory=list
    )
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    supported_content_types: list[DslValue[str]] = field(default_factory=list)
    supported_realtime_inference_instance_types: list[DslValue[str]] = field(
        default_factory=list
    )
    supported_response_mime_types: list[DslValue[str]] = field(default_factory=list)
    supported_transform_instance_types: list[DslValue[str]] = field(
        default_factory=list
    )


@dataclass
class Bias(PropertyType):
    post_training_report: DslValue[MetricsSource] | None = None
    pre_training_report: DslValue[MetricsSource] | None = None
    report: DslValue[MetricsSource] | None = None


@dataclass
class DataSource(PropertyType):
    s3_data_source: DslValue[S3DataSource] | None = None


@dataclass
class DriftCheckBaselines(PropertyType):
    bias: DslValue[DriftCheckBias] | None = None
    explainability: DslValue[DriftCheckExplainability] | None = None
    model_data_quality: DslValue[DriftCheckModelDataQuality] | None = None
    model_quality: DslValue[DriftCheckModelQuality] | None = None


@dataclass
class DriftCheckBias(PropertyType):
    config_file: DslValue[FileSource] | None = None
    post_training_constraints: DslValue[MetricsSource] | None = None
    pre_training_constraints: DslValue[MetricsSource] | None = None


@dataclass
class DriftCheckExplainability(PropertyType):
    config_file: DslValue[FileSource] | None = None
    constraints: DslValue[MetricsSource] | None = None


@dataclass
class DriftCheckModelDataQuality(PropertyType):
    constraints: DslValue[MetricsSource] | None = None
    statistics: DslValue[MetricsSource] | None = None


@dataclass
class DriftCheckModelQuality(PropertyType):
    constraints: DslValue[MetricsSource] | None = None
    statistics: DslValue[MetricsSource] | None = None


@dataclass
class Explainability(PropertyType):
    report: DslValue[MetricsSource] | None = None


@dataclass
class FileSource(PropertyType):
    s3_uri: DslValue[str] | None = None
    content_digest: DslValue[str] | None = None
    content_type: DslValue[str] | None = None


@dataclass
class InferenceSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_response_mime_types": "SupportedResponseMIMETypes",
    }

    containers: list[DslValue[ModelPackageContainerDefinition]] = field(
        default_factory=list
    )
    supported_content_types: list[DslValue[str]] = field(default_factory=list)
    supported_response_mime_types: list[DslValue[str]] = field(default_factory=list)
    supported_realtime_inference_instance_types: list[DslValue[str]] = field(
        default_factory=list
    )
    supported_transform_instance_types: list[DslValue[str]] = field(
        default_factory=list
    )


@dataclass
class MetadataProperties(PropertyType):
    commit_id: DslValue[str] | None = None
    generated_by: DslValue[str] | None = None
    project_id: DslValue[str] | None = None
    repository: DslValue[str] | None = None


@dataclass
class MetricsSource(PropertyType):
    content_type: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    content_digest: DslValue[str] | None = None


@dataclass
class ModelAccessConfig(PropertyType):
    accept_eula: DslValue[bool] | None = None


@dataclass
class ModelCard(PropertyType):
    model_card_content: DslValue[str] | None = None
    model_card_status: DslValue[str] | None = None


@dataclass
class ModelDataQuality(PropertyType):
    constraints: DslValue[MetricsSource] | None = None
    statistics: DslValue[MetricsSource] | None = None


@dataclass
class ModelDataSource(PropertyType):
    s3_data_source: DslValue[S3ModelDataSource] | None = None


@dataclass
class ModelInput(PropertyType):
    data_input_config: DslValue[str] | None = None


@dataclass
class ModelMetrics(PropertyType):
    bias: DslValue[Bias] | None = None
    explainability: DslValue[Explainability] | None = None
    model_data_quality: DslValue[ModelDataQuality] | None = None
    model_quality: DslValue[ModelQuality] | None = None


@dataclass
class ModelPackageContainerDefinition(PropertyType):
    image: DslValue[str] | None = None
    container_hostname: DslValue[str] | None = None
    environment: dict[str, DslValue[str]] = field(default_factory=dict)
    framework: DslValue[str] | None = None
    framework_version: DslValue[str] | None = None
    image_digest: DslValue[str] | None = None
    model_data_source: DslValue[ModelDataSource] | None = None
    model_data_url: DslValue[str] | None = None
    model_input: DslValue[ModelInput] | None = None
    nearest_model_name: DslValue[str] | None = None


@dataclass
class ModelPackageStatusDetails(PropertyType):
    validation_statuses: list[DslValue[ModelPackageStatusItem]] = field(
        default_factory=list
    )


@dataclass
class ModelPackageStatusItem(PropertyType):
    name: DslValue[str] | None = None
    status: DslValue[str] | None = None
    failure_reason: DslValue[str] | None = None


@dataclass
class ModelQuality(PropertyType):
    constraints: DslValue[MetricsSource] | None = None
    statistics: DslValue[MetricsSource] | None = None


@dataclass
class S3DataSource(PropertyType):
    s3_data_type: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None


@dataclass
class S3ModelDataSource(PropertyType):
    compression_type: DslValue[str] | None = None
    s3_data_type: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    model_access_config: DslValue[ModelAccessConfig] | None = None


@dataclass
class SecurityConfig(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class SourceAlgorithm(PropertyType):
    algorithm_name: DslValue[str] | None = None
    model_data_url: DslValue[str] | None = None


@dataclass
class SourceAlgorithmSpecification(PropertyType):
    source_algorithms: list[DslValue[SourceAlgorithm]] = field(default_factory=list)


@dataclass
class TransformInput(PropertyType):
    data_source: DslValue[DataSource] | None = None
    compression_type: DslValue[str] | None = None
    content_type: DslValue[str] | None = None
    split_type: DslValue[str] | None = None


@dataclass
class TransformJobDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_payload_in_mb": "MaxPayloadInMB",
    }

    transform_input: DslValue[TransformInput] | None = None
    transform_output: DslValue[TransformOutput] | None = None
    transform_resources: DslValue[TransformResources] | None = None
    batch_strategy: DslValue[str] | None = None
    environment: dict[str, DslValue[str]] = field(default_factory=dict)
    max_concurrent_transforms: DslValue[int] | None = None
    max_payload_in_mb: DslValue[int] | None = None


@dataclass
class TransformOutput(PropertyType):
    s3_output_path: DslValue[str] | None = None
    accept: DslValue[str] | None = None
    assemble_with: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class TransformResources(PropertyType):
    instance_count: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None
    volume_kms_key_id: DslValue[str] | None = None


@dataclass
class ValidationProfile(PropertyType):
    profile_name: DslValue[str] | None = None
    transform_job_definition: DslValue[TransformJobDefinition] | None = None


@dataclass
class ValidationSpecification(PropertyType):
    validation_profiles: list[DslValue[ValidationProfile]] = field(default_factory=list)
    validation_role: DslValue[str] | None = None
