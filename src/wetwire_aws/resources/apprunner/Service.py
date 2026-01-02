"""PropertyTypes for AWS::AppRunner::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthenticationConfiguration(PropertyType):
    access_role_arn: str | None = None
    connection_arn: str | None = None


@dataclass
class CodeConfiguration(PropertyType):
    configuration_source: str | None = None
    code_configuration_values: CodeConfigurationValues | None = None


@dataclass
class CodeConfigurationValues(PropertyType):
    runtime: str | None = None
    build_command: str | None = None
    port: str | None = None
    runtime_environment_secrets: list[KeyValuePair] = field(default_factory=list)
    runtime_environment_variables: list[KeyValuePair] = field(default_factory=list)
    start_command: str | None = None


@dataclass
class CodeRepository(PropertyType):
    repository_url: str | None = None
    source_code_version: SourceCodeVersion | None = None
    code_configuration: CodeConfiguration | None = None
    source_directory: str | None = None


@dataclass
class EgressConfiguration(PropertyType):
    egress_type: str | None = None
    vpc_connector_arn: str | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key: str | None = None


@dataclass
class HealthCheckConfiguration(PropertyType):
    healthy_threshold: int | None = None
    interval: int | None = None
    path: str | None = None
    protocol: str | None = None
    timeout: int | None = None
    unhealthy_threshold: int | None = None


@dataclass
class ImageConfiguration(PropertyType):
    port: str | None = None
    runtime_environment_secrets: list[KeyValuePair] = field(default_factory=list)
    runtime_environment_variables: list[KeyValuePair] = field(default_factory=list)
    start_command: str | None = None


@dataclass
class ImageRepository(PropertyType):
    image_identifier: str | None = None
    image_repository_type: str | None = None
    image_configuration: ImageConfiguration | None = None


@dataclass
class IngressConfiguration(PropertyType):
    is_publicly_accessible: bool | None = None


@dataclass
class InstanceConfiguration(PropertyType):
    cpu: str | None = None
    instance_role_arn: str | None = None
    memory: str | None = None


@dataclass
class KeyValuePair(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    egress_configuration: EgressConfiguration | None = None
    ingress_configuration: IngressConfiguration | None = None
    ip_address_type: str | None = None


@dataclass
class ServiceObservabilityConfiguration(PropertyType):
    observability_enabled: bool | None = None
    observability_configuration_arn: str | None = None


@dataclass
class SourceCodeVersion(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class SourceConfiguration(PropertyType):
    authentication_configuration: AuthenticationConfiguration | None = None
    auto_deployments_enabled: bool | None = None
    code_repository: CodeRepository | None = None
    image_repository: ImageRepository | None = None
