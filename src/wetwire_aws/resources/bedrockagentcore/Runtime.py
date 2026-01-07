"""PropertyTypes for AWS::BedrockAgentCore::Runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AgentRuntimeArtifact(PropertyType):
    code_configuration: DslValue[CodeConfiguration] | None = None
    container_configuration: DslValue[ContainerConfiguration] | None = None


@dataclass
class AuthorizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_jwt_authorizer": "CustomJWTAuthorizer",
    }

    custom_jwt_authorizer: DslValue[CustomJWTAuthorizerConfiguration] | None = None


@dataclass
class Code(PropertyType):
    s3: DslValue[S3Location] | None = None


@dataclass
class CodeConfiguration(PropertyType):
    code: DslValue[Code] | None = None
    entry_point: list[DslValue[str]] = field(default_factory=list)
    runtime: DslValue[str] | None = None


@dataclass
class ContainerConfiguration(PropertyType):
    container_uri: DslValue[str] | None = None


@dataclass
class CustomJWTAuthorizerConfiguration(PropertyType):
    discovery_url: DslValue[str] | None = None
    allowed_audience: list[DslValue[str]] = field(default_factory=list)
    allowed_clients: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LifecycleConfiguration(PropertyType):
    idle_runtime_session_timeout: DslValue[int] | None = None
    max_lifetime: DslValue[int] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    network_mode: DslValue[str] | None = None
    network_mode_config: DslValue[VpcConfig] | None = None


@dataclass
class RequestHeaderConfiguration(PropertyType):
    request_header_allowlist: list[DslValue[str]] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    version_id: DslValue[str] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_groups: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)


@dataclass
class WorkloadIdentityDetails(PropertyType):
    workload_identity_arn: DslValue[str] | None = None
