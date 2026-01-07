"""PropertyTypes for AWS::IoTWireless::WirelessGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoRaWANGateway(PropertyType):
    gateway_eui: DslValue[str] | None = None
    rf_region: DslValue[str] | None = None
