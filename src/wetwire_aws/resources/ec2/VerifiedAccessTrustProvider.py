"""PropertyTypes for AWS::EC2::VerifiedAccessTrustProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeviceOptions(PropertyType):
    public_signing_key_url: str | None = None
    tenant_id: str | None = None


@dataclass
class NativeApplicationOidcOptions(PropertyType):
    authorization_endpoint: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    issuer: str | None = None
    public_signing_key_endpoint: str | None = None
    scope: str | None = None
    token_endpoint: str | None = None
    user_info_endpoint: str | None = None


@dataclass
class OidcOptions(PropertyType):
    authorization_endpoint: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    issuer: str | None = None
    scope: str | None = None
    token_endpoint: str | None = None
    user_info_endpoint: str | None = None


@dataclass
class SseSpecification(PropertyType):
    customer_managed_key_enabled: bool | None = None
    kms_key_arn: str | None = None
