"""PropertyTypes for AWS::ApiGateway::DomainNameV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EndpointConfiguration(PropertyType):
    ip_address_type: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)
