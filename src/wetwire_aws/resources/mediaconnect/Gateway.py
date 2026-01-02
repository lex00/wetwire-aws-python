"""PropertyTypes for AWS::MediaConnect::Gateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GatewayNetwork(PropertyType):
    cidr_block: str | None = None
    name: str | None = None
