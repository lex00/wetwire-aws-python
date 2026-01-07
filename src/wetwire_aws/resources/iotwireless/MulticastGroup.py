"""PropertyTypes for AWS::IoTWireless::MulticastGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoRaWAN(PropertyType):
    dl_class: DslValue[str] | None = None
    rf_region: DslValue[str] | None = None
    number_of_devices_in_group: DslValue[int] | None = None
    number_of_devices_requested: DslValue[int] | None = None
