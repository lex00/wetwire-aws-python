"""PropertyTypes for AWS::QBusiness::Plugin."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class APISchema(PropertyType):
    payload: DslValue[str] | None = None
    s3: DslValue[S3] | None = None


@dataclass
class BasicAuthConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class CustomPluginConfiguration(PropertyType):
    api_schema: DslValue[APISchema] | None = None
    api_schema_type: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class OAuth2ClientCredentialConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
    authorization_url: DslValue[str] | None = None
    token_url: DslValue[str] | None = None


@dataclass
class PluginAuthConfiguration(PropertyType):
    basic_auth_configuration: DslValue[BasicAuthConfiguration] | None = None
    no_auth_configuration: DslValue[dict[str, Any]] | None = None
    o_auth2_client_credential_configuration: (
        DslValue[OAuth2ClientCredentialConfiguration] | None
    ) = None


@dataclass
class S3(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
