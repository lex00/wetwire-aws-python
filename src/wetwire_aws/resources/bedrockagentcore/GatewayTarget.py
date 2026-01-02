"""PropertyTypes for AWS::BedrockAgentCore::GatewayTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApiKeyCredentialProvider(PropertyType):
    provider_arn: str | None = None
    credential_location: str | None = None
    credential_parameter_name: str | None = None
    credential_prefix: str | None = None


@dataclass
class ApiSchemaConfiguration(PropertyType):
    inline_payload: str | None = None
    s3: S3Configuration | None = None


@dataclass
class CredentialProvider(PropertyType):
    api_key_credential_provider: ApiKeyCredentialProvider | None = None
    oauth_credential_provider: OAuthCredentialProvider | None = None


@dataclass
class CredentialProviderConfiguration(PropertyType):
    credential_provider_type: str | None = None
    credential_provider: CredentialProvider | None = None


@dataclass
class McpLambdaTargetConfiguration(PropertyType):
    lambda_arn: str | None = None
    tool_schema: ToolSchema | None = None


@dataclass
class McpServerTargetConfiguration(PropertyType):
    endpoint: str | None = None


@dataclass
class McpTargetConfiguration(PropertyType):
    lambda_: McpLambdaTargetConfiguration | None = None
    mcp_server: McpServerTargetConfiguration | None = None
    open_api_schema: ApiSchemaConfiguration | None = None
    smithy_model: ApiSchemaConfiguration | None = None


@dataclass
class OAuthCredentialProvider(PropertyType):
    provider_arn: str | None = None
    scopes: list[String] = field(default_factory=list)
    custom_parameters: dict[str, String] = field(default_factory=dict)
    default_return_url: str | None = None
    grant_type: str | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_owner_account_id: str | None = None
    uri: str | None = None


@dataclass
class SchemaDefinition(PropertyType):
    type_: str | None = None
    description: str | None = None
    items: SchemaDefinition | None = None
    properties: dict[str, SchemaDefinition] = field(default_factory=dict)
    required: list[String] = field(default_factory=list)


@dataclass
class TargetConfiguration(PropertyType):
    mcp: McpTargetConfiguration | None = None


@dataclass
class ToolDefinition(PropertyType):
    description: str | None = None
    input_schema: SchemaDefinition | None = None
    name: str | None = None
    output_schema: SchemaDefinition | None = None


@dataclass
class ToolSchema(PropertyType):
    inline_payload: list[ToolDefinition] = field(default_factory=list)
    s3: S3Configuration | None = None
