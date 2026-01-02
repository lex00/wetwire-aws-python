"""PropertyTypes for AWS::SageMaker::EndpointConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AsyncInferenceClientConfig(PropertyType):
    max_concurrent_invocations_per_instance: int | None = None


@dataclass
class AsyncInferenceConfig(PropertyType):
    output_config: AsyncInferenceOutputConfig | None = None
    client_config: AsyncInferenceClientConfig | None = None


@dataclass
class AsyncInferenceNotificationConfig(PropertyType):
    error_topic: str | None = None
    include_inference_response_in: list[String] = field(default_factory=list)
    success_topic: str | None = None


@dataclass
class AsyncInferenceOutputConfig(PropertyType):
    kms_key_id: str | None = None
    notification_config: AsyncInferenceNotificationConfig | None = None
    s3_failure_path: str | None = None
    s3_output_path: str | None = None


@dataclass
class CapacityReservationConfig(PropertyType):
    capacity_reservation_preference: str | None = None
    ml_reservation_arn: str | None = None


@dataclass
class CaptureContentTypeHeader(PropertyType):
    csv_content_types: list[String] = field(default_factory=list)
    json_content_types: list[String] = field(default_factory=list)


@dataclass
class CaptureOption(PropertyType):
    capture_mode: str | None = None


@dataclass
class ClarifyExplainerConfig(PropertyType):
    shap_config: ClarifyShapConfig | None = None
    enable_explanations: str | None = None
    inference_config: ClarifyInferenceConfig | None = None


@dataclass
class ClarifyFeatureType(PropertyType):
    pass


@dataclass
class ClarifyHeader(PropertyType):
    pass


@dataclass
class ClarifyInferenceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_payload_in_mb": "MaxPayloadInMB",
    }

    content_template: str | None = None
    feature_headers: list[ClarifyHeader] = field(default_factory=list)
    feature_types: list[ClarifyFeatureType] = field(default_factory=list)
    features_attribute: str | None = None
    label_attribute: str | None = None
    label_headers: list[ClarifyHeader] = field(default_factory=list)
    label_index: int | None = None
    max_payload_in_mb: int | None = None
    max_record_count: int | None = None
    probability_attribute: str | None = None
    probability_index: int | None = None


@dataclass
class ClarifyShapBaselineConfig(PropertyType):
    mime_type: str | None = None
    shap_baseline: str | None = None
    shap_baseline_uri: str | None = None


@dataclass
class ClarifyShapConfig(PropertyType):
    shap_baseline_config: ClarifyShapBaselineConfig | None = None
    number_of_samples: int | None = None
    seed: int | None = None
    text_config: ClarifyTextConfig | None = None
    use_logit: bool | None = None


@dataclass
class ClarifyTextConfig(PropertyType):
    granularity: str | None = None
    language: str | None = None


@dataclass
class DataCaptureConfig(PropertyType):
    capture_options: list[CaptureOption] = field(default_factory=list)
    destination_s3_uri: str | None = None
    initial_sampling_percentage: int | None = None
    capture_content_type_header: CaptureContentTypeHeader | None = None
    enable_capture: bool | None = None
    kms_key_id: str | None = None


@dataclass
class ExplainerConfig(PropertyType):
    clarify_explainer_config: ClarifyExplainerConfig | None = None


@dataclass
class ManagedInstanceScaling(PropertyType):
    max_instance_count: int | None = None
    min_instance_count: int | None = None
    status: str | None = None


@dataclass
class ProductionVariant(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_ssm_access": "EnableSSMAccess",
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    variant_name: str | None = None
    capacity_reservation_config: CapacityReservationConfig | None = None
    container_startup_health_check_timeout_in_seconds: int | None = None
    enable_ssm_access: bool | None = None
    inference_ami_version: str | None = None
    initial_instance_count: int | None = None
    initial_variant_weight: float | None = None
    instance_type: str | None = None
    managed_instance_scaling: ManagedInstanceScaling | None = None
    model_data_download_timeout_in_seconds: int | None = None
    model_name: str | None = None
    routing_config: RoutingConfig | None = None
    serverless_config: ServerlessConfig | None = None
    volume_size_in_gb: int | None = None


@dataclass
class RoutingConfig(PropertyType):
    routing_strategy: str | None = None


@dataclass
class ServerlessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_size_in_mb": "MemorySizeInMB",
    }

    max_concurrency: int | None = None
    memory_size_in_mb: int | None = None
    provisioned_concurrency: int | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
