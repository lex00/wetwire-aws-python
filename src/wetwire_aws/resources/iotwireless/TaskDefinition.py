"""PropertyTypes for AWS::IoTWireless::TaskDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoRaWANGatewayVersion(PropertyType):
    model: DslValue[str] | None = None
    package_version: DslValue[str] | None = None
    station: DslValue[str] | None = None


@dataclass
class LoRaWANUpdateGatewayTaskCreate(PropertyType):
    current_version: DslValue[LoRaWANGatewayVersion] | None = None
    sig_key_crc: DslValue[int] | None = None
    update_signature: DslValue[str] | None = None
    update_version: DslValue[LoRaWANGatewayVersion] | None = None


@dataclass
class LoRaWANUpdateGatewayTaskEntry(PropertyType):
    current_version: DslValue[LoRaWANGatewayVersion] | None = None
    update_version: DslValue[LoRaWANGatewayVersion] | None = None


@dataclass
class UpdateWirelessGatewayTaskCreate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lo_ra_wan": "LoRaWAN",
    }

    lo_ra_wan: DslValue[LoRaWANUpdateGatewayTaskCreate] | None = None
    update_data_role: DslValue[str] | None = None
    update_data_source: DslValue[str] | None = None
