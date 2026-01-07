"""PropertyTypes for AWS::SageMaker::EndpointConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AsyncInferenceClientConfig(PropertyType):
    max_concurrent_invocations_per_instance: DslValue[int] | None = None


@dataclass
class AsyncInferenceConfig(PropertyType):
    output_config: DslValue[AsyncInferenceOutputConfig] | None = None
    client_config: DslValue[AsyncInferenceClientConfig] | None = None


@dataclass
class AsyncInferenceNotificationConfig(PropertyType):
    error_topic: DslValue[str] | None = None
    include_inference_response_in: list[DslValue[str]] = field(default_factory=list)
    success_topic: DslValue[str] | None = None


@dataclass
class AsyncInferenceOutputConfig(PropertyType):
    kms_key_id: DslValue[str] | None = None
    notification_config: DslValue[AsyncInferenceNotificationConfig] | None = None
    s3_failure_path: DslValue[str] | None = None
    s3_output_path: DslValue[str] | None = None


@dataclass
class CapacityReservationConfig(PropertyType):
    capacity_reservation_preference: DslValue[str] | None = None
    ml_reservation_arn: DslValue[str] | None = None


@dataclass
class CaptureContentTypeHeader(PropertyType):
    csv_content_types: list[DslValue[str]] = field(default_factory=list)
    json_content_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CaptureOption(PropertyType):
    capture_mode: DslValue[str] | None = None


@dataclass
class ClarifyExplainerConfig(PropertyType):
    shap_config: DslValue[ClarifyShapConfig] | None = None
    enable_explanations: DslValue[str] | None = None
    inference_config: DslValue[ClarifyInferenceConfig] | None = None


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

    content_template: DslValue[str] | None = None
    feature_headers: list[DslValue[ClarifyHeader]] = field(default_factory=list)
    feature_types: list[DslValue[ClarifyFeatureType]] = field(default_factory=list)
    features_attribute: DslValue[str] | None = None
    label_attribute: DslValue[str] | None = None
    label_headers: list[DslValue[ClarifyHeader]] = field(default_factory=list)
    label_index: DslValue[int] | None = None
    max_payload_in_mb: DslValue[int] | None = None
    max_record_count: DslValue[int] | None = None
    probability_attribute: DslValue[str] | None = None
    probability_index: DslValue[int] | None = None


@dataclass
class ClarifyShapBaselineConfig(PropertyType):
    mime_type: DslValue[str] | None = None
    shap_baseline: DslValue[str] | None = None
    shap_baseline_uri: DslValue[str] | None = None


@dataclass
class ClarifyShapConfig(PropertyType):
    shap_baseline_config: DslValue[ClarifyShapBaselineConfig] | None = None
    number_of_samples: DslValue[int] | None = None
    seed: DslValue[int] | None = None
    text_config: DslValue[ClarifyTextConfig] | None = None
    use_logit: DslValue[bool] | None = None


@dataclass
class ClarifyTextConfig(PropertyType):
    granularity: DslValue[str] | None = None
    language: DslValue[str] | None = None


@dataclass
class DataCaptureConfig(PropertyType):
    capture_options: list[DslValue[CaptureOption]] = field(default_factory=list)
    destination_s3_uri: DslValue[str] | None = None
    initial_sampling_percentage: DslValue[int] | None = None
    capture_content_type_header: DslValue[CaptureContentTypeHeader] | None = None
    enable_capture: DslValue[bool] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class ExplainerConfig(PropertyType):
    clarify_explainer_config: DslValue[ClarifyExplainerConfig] | None = None


@dataclass
class ManagedInstanceScaling(PropertyType):
    max_instance_count: DslValue[int] | None = None
    min_instance_count: DslValue[int] | None = None
    status: DslValue[str] | None = None


@dataclass
class ProductionVariant(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_ssm_access": "EnableSSMAccess",
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    variant_name: DslValue[str] | None = None
    capacity_reservation_config: DslValue[CapacityReservationConfig] | None = None
    container_startup_health_check_timeout_in_seconds: DslValue[int] | None = None
    enable_ssm_access: DslValue[bool] | None = None
    inference_ami_version: DslValue[str] | None = None
    initial_instance_count: DslValue[int] | None = None
    initial_variant_weight: DslValue[float] | None = None
    instance_type: DslValue[str] | None = None
    managed_instance_scaling: DslValue[ManagedInstanceScaling] | None = None
    model_data_download_timeout_in_seconds: DslValue[int] | None = None
    model_name: DslValue[str] | None = None
    routing_config: DslValue[RoutingConfig] | None = None
    serverless_config: DslValue[ServerlessConfig] | None = None
    volume_size_in_gb: DslValue[int] | None = None


@dataclass
class RoutingConfig(PropertyType):
    routing_strategy: DslValue[str] | None = None


@dataclass
class ServerlessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_size_in_mb": "MemorySizeInMB",
    }

    max_concurrency: DslValue[int] | None = None
    memory_size_in_mb: DslValue[int] | None = None
    provisioned_concurrency: DslValue[int] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
