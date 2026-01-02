"""PropertyTypes for AWS::SageMaker::InferenceExperiment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CaptureContentTypeHeader(PropertyType):
    csv_content_types: list[String] = field(default_factory=list)
    json_content_types: list[String] = field(default_factory=list)


@dataclass
class DataStorageConfig(PropertyType):
    destination: str | None = None
    content_type: CaptureContentTypeHeader | None = None
    kms_key: str | None = None


@dataclass
class EndpointMetadata(PropertyType):
    endpoint_name: str | None = None
    endpoint_config_name: str | None = None
    endpoint_status: str | None = None


@dataclass
class InferenceExperimentSchedule(PropertyType):
    end_time: str | None = None
    start_time: str | None = None


@dataclass
class ModelInfrastructureConfig(PropertyType):
    infrastructure_type: str | None = None
    real_time_inference_config: RealTimeInferenceConfig | None = None


@dataclass
class ModelVariantConfig(PropertyType):
    infrastructure_config: ModelInfrastructureConfig | None = None
    model_name: str | None = None
    variant_name: str | None = None


@dataclass
class RealTimeInferenceConfig(PropertyType):
    instance_count: int | None = None
    instance_type: str | None = None


@dataclass
class ShadowModeConfig(PropertyType):
    shadow_model_variants: list[ShadowModelVariantConfig] = field(default_factory=list)
    source_model_variant_name: str | None = None


@dataclass
class ShadowModelVariantConfig(PropertyType):
    sampling_percentage: int | None = None
    shadow_model_variant_name: str | None = None
