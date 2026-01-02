"""PropertyTypes for AWS::BedrockAgentCore::Runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AgentRuntimeArtifact(PropertyType):
    code_configuration: CodeConfiguration | None = None
    container_configuration: ContainerConfiguration | None = None


@dataclass
class AuthorizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_jwt_authorizer": "CustomJWTAuthorizer",
    }

    custom_jwt_authorizer: CustomJWTAuthorizerConfiguration | None = None


@dataclass
class Code(PropertyType):
    s3: S3Location | None = None


@dataclass
class CodeConfiguration(PropertyType):
    code: Code | None = None
    entry_point: list[String] = field(default_factory=list)
    runtime: str | None = None


@dataclass
class ContainerConfiguration(PropertyType):
    container_uri: str | None = None


@dataclass
class CustomJWTAuthorizerConfiguration(PropertyType):
    discovery_url: str | None = None
    allowed_audience: list[String] = field(default_factory=list)
    allowed_clients: list[String] = field(default_factory=list)


@dataclass
class LifecycleConfiguration(PropertyType):
    idle_runtime_session_timeout: int | None = None
    max_lifetime: int | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    network_mode: str | None = None
    network_mode_config: VpcConfig | None = None


@dataclass
class RequestHeaderConfiguration(PropertyType):
    request_header_allowlist: list[String] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    prefix: str | None = None
    version_id: str | None = None


@dataclass
class VpcConfig(PropertyType):
    security_groups: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)


@dataclass
class WorkloadIdentityDetails(PropertyType):
    workload_identity_arn: str | None = None
