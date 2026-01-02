"""PropertyTypes for AWS::QBusiness::Plugin."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class APISchema(PropertyType):
    payload: str | None = None
    s3: S3 | None = None


@dataclass
class BasicAuthConfiguration(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class CustomPluginConfiguration(PropertyType):
    api_schema: APISchema | None = None
    api_schema_type: str | None = None
    description: str | None = None


@dataclass
class OAuth2ClientCredentialConfiguration(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None
    authorization_url: str | None = None
    token_url: str | None = None


@dataclass
class PluginAuthConfiguration(PropertyType):
    basic_auth_configuration: BasicAuthConfiguration | None = None
    no_auth_configuration: dict[str, Any] | None = None
    o_auth2_client_credential_configuration: (
        OAuth2ClientCredentialConfiguration | None
    ) = None


@dataclass
class S3(PropertyType):
    bucket: str | None = None
    key: str | None = None
