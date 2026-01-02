"""PropertyTypes for AWS::SageMaker::Model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdditionalModelDataSource(PropertyType):
    channel_name: str | None = None
    s3_data_source: S3DataSource | None = None


@dataclass
class ContainerDefinition(PropertyType):
    container_hostname: str | None = None
    environment: dict[str, Any] | None = None
    image: str | None = None
    image_config: ImageConfig | None = None
    inference_specification_name: str | None = None
    mode: str | None = None
    model_data_source: ModelDataSource | None = None
    model_data_url: str | None = None
    model_package_name: str | None = None
    multi_model_config: MultiModelConfig | None = None


@dataclass
class HubAccessConfig(PropertyType):
    hub_content_arn: str | None = None


@dataclass
class ImageConfig(PropertyType):
    repository_access_mode: str | None = None
    repository_auth_config: RepositoryAuthConfig | None = None


@dataclass
class InferenceExecutionConfig(PropertyType):
    mode: str | None = None


@dataclass
class ModelAccessConfig(PropertyType):
    accept_eula: bool | None = None


@dataclass
class ModelDataSource(PropertyType):
    s3_data_source: S3DataSource | None = None


@dataclass
class MultiModelConfig(PropertyType):
    model_cache_setting: str | None = None


@dataclass
class RepositoryAuthConfig(PropertyType):
    repository_credentials_provider_arn: str | None = None


@dataclass
class S3DataSource(PropertyType):
    compression_type: str | None = None
    s3_data_type: str | None = None
    s3_uri: str | None = None
    hub_access_config: HubAccessConfig | None = None
    model_access_config: ModelAccessConfig | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
