"""PropertyTypes for AWS::BedrockAgentCore::GatewayTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApiKeyCredentialProvider(PropertyType):
    provider_arn: DslValue[str] | None = None
    credential_location: DslValue[str] | None = None
    credential_parameter_name: DslValue[str] | None = None
    credential_prefix: DslValue[str] | None = None


@dataclass
class ApiSchemaConfiguration(PropertyType):
    inline_payload: DslValue[str] | None = None
    s3: DslValue[S3Configuration] | None = None


@dataclass
class CredentialProvider(PropertyType):
    api_key_credential_provider: DslValue[ApiKeyCredentialProvider] | None = None
    oauth_credential_provider: DslValue[OAuthCredentialProvider] | None = None


@dataclass
class CredentialProviderConfiguration(PropertyType):
    credential_provider_type: DslValue[str] | None = None
    credential_provider: DslValue[CredentialProvider] | None = None


@dataclass
class McpLambdaTargetConfiguration(PropertyType):
    lambda_arn: DslValue[str] | None = None
    tool_schema: DslValue[ToolSchema] | None = None


@dataclass
class McpServerTargetConfiguration(PropertyType):
    endpoint: DslValue[str] | None = None


@dataclass
class McpTargetConfiguration(PropertyType):
    lambda_: DslValue[McpLambdaTargetConfiguration] | None = None
    mcp_server: DslValue[McpServerTargetConfiguration] | None = None
    open_api_schema: DslValue[ApiSchemaConfiguration] | None = None
    smithy_model: DslValue[ApiSchemaConfiguration] | None = None


@dataclass
class OAuthCredentialProvider(PropertyType):
    provider_arn: DslValue[str] | None = None
    scopes: list[DslValue[str]] = field(default_factory=list)
    custom_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    default_return_url: DslValue[str] | None = None
    grant_type: DslValue[str] | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_owner_account_id: DslValue[str] | None = None
    uri: DslValue[str] | None = None


@dataclass
class SchemaDefinition(PropertyType):
    type_: DslValue[str] | None = None
    description: DslValue[str] | None = None
    items: DslValue[SchemaDefinition] | None = None
    properties: dict[str, DslValue[SchemaDefinition]] = field(default_factory=dict)
    required: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TargetConfiguration(PropertyType):
    mcp: DslValue[McpTargetConfiguration] | None = None


@dataclass
class ToolDefinition(PropertyType):
    description: DslValue[str] | None = None
    input_schema: DslValue[SchemaDefinition] | None = None
    name: DslValue[str] | None = None
    output_schema: DslValue[SchemaDefinition] | None = None


@dataclass
class ToolSchema(PropertyType):
    inline_payload: list[DslValue[ToolDefinition]] = field(default_factory=list)
    s3: DslValue[S3Configuration] | None = None
