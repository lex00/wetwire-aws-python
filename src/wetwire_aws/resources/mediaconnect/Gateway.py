"""PropertyTypes for AWS::MediaConnect::Gateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GatewayNetwork(PropertyType):
    cidr_block: DslValue[str] | None = None
    name: DslValue[str] | None = None
