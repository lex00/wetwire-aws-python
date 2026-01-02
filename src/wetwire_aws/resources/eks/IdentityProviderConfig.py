"""PropertyTypes for AWS::EKS::IdentityProviderConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OidcIdentityProviderConfig(PropertyType):
    client_id: str | None = None
    issuer_url: str | None = None
    groups_claim: str | None = None
    groups_prefix: str | None = None
    required_claims: list[RequiredClaim] = field(default_factory=list)
    username_claim: str | None = None
    username_prefix: str | None = None


@dataclass
class RequiredClaim(PropertyType):
    key: str | None = None
    value: str | None = None
