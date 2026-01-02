"""PropertyTypes for AWS::IoTSiteWise::Gateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GatewayCapabilitySummary(PropertyType):
    capability_namespace: str | None = None
    capability_configuration: str | None = None


@dataclass
class GatewayPlatform(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "siemens_ie": "SiemensIE",
    }

    greengrass_v2: GreengrassV2 | None = None
    siemens_ie: SiemensIE | None = None


@dataclass
class GreengrassV2(PropertyType):
    core_device_thing_name: str | None = None
    core_device_operating_system: str | None = None


@dataclass
class SiemensIE(PropertyType):
    iot_core_thing_name: str | None = None
