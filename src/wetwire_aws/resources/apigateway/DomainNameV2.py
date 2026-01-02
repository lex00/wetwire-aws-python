"""PropertyTypes for AWS::ApiGateway::DomainNameV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EndpointConfiguration(PropertyType):
    ip_address_type: str | None = None
    types: list[String] = field(default_factory=list)
