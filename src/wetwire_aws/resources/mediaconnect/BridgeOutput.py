"""PropertyTypes for AWS::MediaConnect::BridgeOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BridgeNetworkOutput(PropertyType):
    ip_address: str | None = None
    network_name: str | None = None
    port: int | None = None
    protocol: str | None = None
    ttl: int | None = None
