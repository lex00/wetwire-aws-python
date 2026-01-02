"""PropertyTypes for AWS::VerifiedPermissions::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CognitoGroupConfiguration(PropertyType):
    group_entity_type: str | None = None


@dataclass
class CognitoUserPoolConfiguration(PropertyType):
    user_pool_arn: str | None = None
    client_ids: list[String] = field(default_factory=list)
    group_configuration: CognitoGroupConfiguration | None = None


@dataclass
class IdentitySourceConfiguration(PropertyType):
    cognito_user_pool_configuration: CognitoUserPoolConfiguration | None = None
    open_id_connect_configuration: OpenIdConnectConfiguration | None = None


@dataclass
class OpenIdConnectAccessTokenConfiguration(PropertyType):
    audiences: list[String] = field(default_factory=list)
    principal_id_claim: str | None = None


@dataclass
class OpenIdConnectConfiguration(PropertyType):
    issuer: str | None = None
    token_selection: OpenIdConnectTokenSelection | None = None
    entity_id_prefix: str | None = None
    group_configuration: OpenIdConnectGroupConfiguration | None = None


@dataclass
class OpenIdConnectGroupConfiguration(PropertyType):
    group_claim: str | None = None
    group_entity_type: str | None = None


@dataclass
class OpenIdConnectIdentityTokenConfiguration(PropertyType):
    client_ids: list[String] = field(default_factory=list)
    principal_id_claim: str | None = None


@dataclass
class OpenIdConnectTokenSelection(PropertyType):
    access_token_only: OpenIdConnectAccessTokenConfiguration | None = None
    identity_token_only: OpenIdConnectIdentityTokenConfiguration | None = None
