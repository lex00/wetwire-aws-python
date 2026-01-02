"""PropertyTypes for AWS::BedrockAgentCore::Gateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthorizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_jwt_authorizer": "CustomJWTAuthorizer",
    }

    custom_jwt_authorizer: CustomJWTAuthorizerConfiguration | None = None


@dataclass
class CustomJWTAuthorizerConfiguration(PropertyType):
    discovery_url: str | None = None
    allowed_audience: list[String] = field(default_factory=list)
    allowed_clients: list[String] = field(default_factory=list)


@dataclass
class GatewayInterceptorConfiguration(PropertyType):
    interception_points: list[String] = field(default_factory=list)
    interceptor: InterceptorConfiguration | None = None
    input_configuration: InterceptorInputConfiguration | None = None


@dataclass
class GatewayProtocolConfiguration(PropertyType):
    mcp: MCPGatewayConfiguration | None = None


@dataclass
class InterceptorConfiguration(PropertyType):
    lambda_: LambdaInterceptorConfiguration | None = None


@dataclass
class InterceptorInputConfiguration(PropertyType):
    pass_request_headers: bool | None = None


@dataclass
class LambdaInterceptorConfiguration(PropertyType):
    arn: str | None = None


@dataclass
class MCPGatewayConfiguration(PropertyType):
    instructions: str | None = None
    search_type: str | None = None
    supported_versions: list[String] = field(default_factory=list)


@dataclass
class WorkloadIdentityDetails(PropertyType):
    workload_identity_arn: str | None = None
