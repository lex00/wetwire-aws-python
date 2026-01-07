"""PropertyTypes for AWS::EC2::VerifiedAccessTrustProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeviceOptions(PropertyType):
    public_signing_key_url: DslValue[str] | None = None
    tenant_id: DslValue[str] | None = None


@dataclass
class NativeApplicationOidcOptions(PropertyType):
    authorization_endpoint: DslValue[str] | None = None
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    issuer: DslValue[str] | None = None
    public_signing_key_endpoint: DslValue[str] | None = None
    scope: DslValue[str] | None = None
    token_endpoint: DslValue[str] | None = None
    user_info_endpoint: DslValue[str] | None = None


@dataclass
class OidcOptions(PropertyType):
    authorization_endpoint: DslValue[str] | None = None
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    issuer: DslValue[str] | None = None
    scope: DslValue[str] | None = None
    token_endpoint: DslValue[str] | None = None
    user_info_endpoint: DslValue[str] | None = None


@dataclass
class SseSpecification(PropertyType):
    customer_managed_key_enabled: DslValue[bool] | None = None
    kms_key_arn: DslValue[str] | None = None
