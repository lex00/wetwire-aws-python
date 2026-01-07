"""PropertyTypes for AWS::ApiGatewayV2::Authorizer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class JWTConfiguration(PropertyType):
    audience: list[DslValue[str]] = field(default_factory=list)
    issuer: DslValue[str] | None = None
