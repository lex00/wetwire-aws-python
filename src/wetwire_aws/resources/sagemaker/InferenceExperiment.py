"""PropertyTypes for AWS::SageMaker::InferenceExperiment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CaptureContentTypeHeader(PropertyType):
    csv_content_types: list[DslValue[str]] = field(default_factory=list)
    json_content_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataStorageConfig(PropertyType):
    destination: DslValue[str] | None = None
    content_type: DslValue[CaptureContentTypeHeader] | None = None
    kms_key: DslValue[str] | None = None


@dataclass
class EndpointMetadata(PropertyType):
    endpoint_name: DslValue[str] | None = None
    endpoint_config_name: DslValue[str] | None = None
    endpoint_status: DslValue[str] | None = None


@dataclass
class InferenceExperimentSchedule(PropertyType):
    end_time: DslValue[str] | None = None
    start_time: DslValue[str] | None = None


@dataclass
class ModelInfrastructureConfig(PropertyType):
    infrastructure_type: DslValue[str] | None = None
    real_time_inference_config: DslValue[RealTimeInferenceConfig] | None = None


@dataclass
class ModelVariantConfig(PropertyType):
    infrastructure_config: DslValue[ModelInfrastructureConfig] | None = None
    model_name: DslValue[str] | None = None
    variant_name: DslValue[str] | None = None


@dataclass
class RealTimeInferenceConfig(PropertyType):
    instance_count: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None


@dataclass
class ShadowModeConfig(PropertyType):
    shadow_model_variants: list[DslValue[ShadowModelVariantConfig]] = field(
        default_factory=list
    )
    source_model_variant_name: DslValue[str] | None = None


@dataclass
class ShadowModelVariantConfig(PropertyType):
    sampling_percentage: DslValue[int] | None = None
    shadow_model_variant_name: DslValue[str] | None = None
