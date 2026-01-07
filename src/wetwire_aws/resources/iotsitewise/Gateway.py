"""PropertyTypes for AWS::IoTSiteWise::Gateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GatewayCapabilitySummary(PropertyType):
    capability_namespace: DslValue[str] | None = None
    capability_configuration: DslValue[str] | None = None


@dataclass
class GatewayPlatform(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "siemens_ie": "SiemensIE",
    }

    greengrass_v2: DslValue[GreengrassV2] | None = None
    siemens_ie: DslValue[SiemensIE] | None = None


@dataclass
class GreengrassV2(PropertyType):
    core_device_thing_name: DslValue[str] | None = None
    core_device_operating_system: DslValue[str] | None = None


@dataclass
class SiemensIE(PropertyType):
    iot_core_thing_name: DslValue[str] | None = None
