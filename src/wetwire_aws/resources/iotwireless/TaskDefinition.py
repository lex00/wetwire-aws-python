"""PropertyTypes for AWS::IoTWireless::TaskDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoRaWANGatewayVersion(PropertyType):
    model: str | None = None
    package_version: str | None = None
    station: str | None = None


@dataclass
class LoRaWANUpdateGatewayTaskCreate(PropertyType):
    current_version: LoRaWANGatewayVersion | None = None
    sig_key_crc: int | None = None
    update_signature: str | None = None
    update_version: LoRaWANGatewayVersion | None = None


@dataclass
class LoRaWANUpdateGatewayTaskEntry(PropertyType):
    current_version: LoRaWANGatewayVersion | None = None
    update_version: LoRaWANGatewayVersion | None = None


@dataclass
class UpdateWirelessGatewayTaskCreate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lo_ra_wan": "LoRaWAN",
    }

    lo_ra_wan: LoRaWANUpdateGatewayTaskCreate | None = None
    update_data_role: str | None = None
    update_data_source: str | None = None
