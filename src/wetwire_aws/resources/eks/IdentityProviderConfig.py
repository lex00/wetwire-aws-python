"""PropertyTypes for AWS::EKS::IdentityProviderConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OidcIdentityProviderConfig(PropertyType):
    client_id: DslValue[str] | None = None
    issuer_url: DslValue[str] | None = None
    groups_claim: DslValue[str] | None = None
    groups_prefix: DslValue[str] | None = None
    required_claims: list[DslValue[RequiredClaim]] = field(default_factory=list)
    username_claim: DslValue[str] | None = None
    username_prefix: DslValue[str] | None = None


@dataclass
class RequiredClaim(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
