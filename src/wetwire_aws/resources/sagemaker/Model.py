"""PropertyTypes for AWS::SageMaker::Model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdditionalModelDataSource(PropertyType):
    channel_name: DslValue[str] | None = None
    s3_data_source: DslValue[S3DataSource] | None = None


@dataclass
class ContainerDefinition(PropertyType):
    container_hostname: DslValue[str] | None = None
    environment: DslValue[dict[str, Any]] | None = None
    image: DslValue[str] | None = None
    image_config: DslValue[ImageConfig] | None = None
    inference_specification_name: DslValue[str] | None = None
    mode: DslValue[str] | None = None
    model_data_source: DslValue[ModelDataSource] | None = None
    model_data_url: DslValue[str] | None = None
    model_package_name: DslValue[str] | None = None
    multi_model_config: DslValue[MultiModelConfig] | None = None


@dataclass
class HubAccessConfig(PropertyType):
    hub_content_arn: DslValue[str] | None = None


@dataclass
class ImageConfig(PropertyType):
    repository_access_mode: DslValue[str] | None = None
    repository_auth_config: DslValue[RepositoryAuthConfig] | None = None


@dataclass
class InferenceExecutionConfig(PropertyType):
    mode: DslValue[str] | None = None


@dataclass
class ModelAccessConfig(PropertyType):
    accept_eula: DslValue[bool] | None = None


@dataclass
class ModelDataSource(PropertyType):
    s3_data_source: DslValue[S3DataSource] | None = None


@dataclass
class MultiModelConfig(PropertyType):
    model_cache_setting: DslValue[str] | None = None


@dataclass
class RepositoryAuthConfig(PropertyType):
    repository_credentials_provider_arn: DslValue[str] | None = None


@dataclass
class S3DataSource(PropertyType):
    compression_type: DslValue[str] | None = None
    s3_data_type: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    hub_access_config: DslValue[HubAccessConfig] | None = None
    model_access_config: DslValue[ModelAccessConfig] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
