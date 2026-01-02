"""PropertyTypes for AWS::ApiGatewayV2::Authorizer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class JWTConfiguration(PropertyType):
    audience: list[String] = field(default_factory=list)
    issuer: str | None = None
