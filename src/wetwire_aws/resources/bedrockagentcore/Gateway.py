"""PropertyTypes for AWS::BedrockAgentCore::Gateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthorizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_jwt_authorizer": "CustomJWTAuthorizer",
    }

    custom_jwt_authorizer: DslValue[CustomJWTAuthorizerConfiguration] | None = None


@dataclass
class CustomJWTAuthorizerConfiguration(PropertyType):
    discovery_url: DslValue[str] | None = None
    allowed_audience: list[DslValue[str]] = field(default_factory=list)
    allowed_clients: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GatewayInterceptorConfiguration(PropertyType):
    interception_points: list[DslValue[str]] = field(default_factory=list)
    interceptor: DslValue[InterceptorConfiguration] | None = None
    input_configuration: DslValue[InterceptorInputConfiguration] | None = None


@dataclass
class GatewayProtocolConfiguration(PropertyType):
    mcp: DslValue[MCPGatewayConfiguration] | None = None


@dataclass
class InterceptorConfiguration(PropertyType):
    lambda_: DslValue[LambdaInterceptorConfiguration] | None = None


@dataclass
class InterceptorInputConfiguration(PropertyType):
    pass_request_headers: DslValue[bool] | None = None


@dataclass
class LambdaInterceptorConfiguration(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class MCPGatewayConfiguration(PropertyType):
    instructions: DslValue[str] | None = None
    search_type: DslValue[str] | None = None
    supported_versions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class WorkloadIdentityDetails(PropertyType):
    workload_identity_arn: DslValue[str] | None = None
