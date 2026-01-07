"""PropertyTypes for AWS::AppRunner::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthenticationConfiguration(PropertyType):
    access_role_arn: DslValue[str] | None = None
    connection_arn: DslValue[str] | None = None


@dataclass
class CodeConfiguration(PropertyType):
    configuration_source: DslValue[str] | None = None
    code_configuration_values: DslValue[CodeConfigurationValues] | None = None


@dataclass
class CodeConfigurationValues(PropertyType):
    runtime: DslValue[str] | None = None
    build_command: DslValue[str] | None = None
    port: DslValue[str] | None = None
    runtime_environment_secrets: list[DslValue[KeyValuePair]] = field(
        default_factory=list
    )
    runtime_environment_variables: list[DslValue[KeyValuePair]] = field(
        default_factory=list
    )
    start_command: DslValue[str] | None = None


@dataclass
class CodeRepository(PropertyType):
    repository_url: DslValue[str] | None = None
    source_code_version: DslValue[SourceCodeVersion] | None = None
    code_configuration: DslValue[CodeConfiguration] | None = None
    source_directory: DslValue[str] | None = None


@dataclass
class EgressConfiguration(PropertyType):
    egress_type: DslValue[str] | None = None
    vpc_connector_arn: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key: DslValue[str] | None = None


@dataclass
class HealthCheckConfiguration(PropertyType):
    healthy_threshold: DslValue[int] | None = None
    interval: DslValue[int] | None = None
    path: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    timeout: DslValue[int] | None = None
    unhealthy_threshold: DslValue[int] | None = None


@dataclass
class ImageConfiguration(PropertyType):
    port: DslValue[str] | None = None
    runtime_environment_secrets: list[DslValue[KeyValuePair]] = field(
        default_factory=list
    )
    runtime_environment_variables: list[DslValue[KeyValuePair]] = field(
        default_factory=list
    )
    start_command: DslValue[str] | None = None


@dataclass
class ImageRepository(PropertyType):
    image_identifier: DslValue[str] | None = None
    image_repository_type: DslValue[str] | None = None
    image_configuration: DslValue[ImageConfiguration] | None = None


@dataclass
class IngressConfiguration(PropertyType):
    is_publicly_accessible: DslValue[bool] | None = None


@dataclass
class InstanceConfiguration(PropertyType):
    cpu: DslValue[str] | None = None
    instance_role_arn: DslValue[str] | None = None
    memory: DslValue[str] | None = None


@dataclass
class KeyValuePair(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    egress_configuration: DslValue[EgressConfiguration] | None = None
    ingress_configuration: DslValue[IngressConfiguration] | None = None
    ip_address_type: DslValue[str] | None = None


@dataclass
class ServiceObservabilityConfiguration(PropertyType):
    observability_enabled: DslValue[bool] | None = None
    observability_configuration_arn: DslValue[str] | None = None


@dataclass
class SourceCodeVersion(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SourceConfiguration(PropertyType):
    authentication_configuration: DslValue[AuthenticationConfiguration] | None = None
    auto_deployments_enabled: DslValue[bool] | None = None
    code_repository: DslValue[CodeRepository] | None = None
    image_repository: DslValue[ImageRepository] | None = None
