"""PropertyTypes for AWS::VerifiedPermissions::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CognitoGroupConfiguration(PropertyType):
    group_entity_type: DslValue[str] | None = None


@dataclass
class CognitoUserPoolConfiguration(PropertyType):
    user_pool_arn: DslValue[str] | None = None
    client_ids: list[DslValue[str]] = field(default_factory=list)
    group_configuration: DslValue[CognitoGroupConfiguration] | None = None


@dataclass
class IdentitySourceConfiguration(PropertyType):
    cognito_user_pool_configuration: DslValue[CognitoUserPoolConfiguration] | None = (
        None
    )
    open_id_connect_configuration: DslValue[OpenIdConnectConfiguration] | None = None


@dataclass
class OpenIdConnectAccessTokenConfiguration(PropertyType):
    audiences: list[DslValue[str]] = field(default_factory=list)
    principal_id_claim: DslValue[str] | None = None


@dataclass
class OpenIdConnectConfiguration(PropertyType):
    issuer: DslValue[str] | None = None
    token_selection: DslValue[OpenIdConnectTokenSelection] | None = None
    entity_id_prefix: DslValue[str] | None = None
    group_configuration: DslValue[OpenIdConnectGroupConfiguration] | None = None


@dataclass
class OpenIdConnectGroupConfiguration(PropertyType):
    group_claim: DslValue[str] | None = None
    group_entity_type: DslValue[str] | None = None


@dataclass
class OpenIdConnectIdentityTokenConfiguration(PropertyType):
    client_ids: list[DslValue[str]] = field(default_factory=list)
    principal_id_claim: DslValue[str] | None = None


@dataclass
class OpenIdConnectTokenSelection(PropertyType):
    access_token_only: DslValue[OpenIdConnectAccessTokenConfiguration] | None = None
    identity_token_only: DslValue[OpenIdConnectIdentityTokenConfiguration] | None = None
