"""PropertyTypes for AWS::MediaConnect::BridgeOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BridgeNetworkOutput(PropertyType):
    ip_address: DslValue[str] | None = None
    network_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    ttl: DslValue[int] | None = None
