"""PropertyTypes for AWS::IoTWireless::WirelessGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoRaWANGateway(PropertyType):
    gateway_eui: str | None = None
    rf_region: str | None = None
