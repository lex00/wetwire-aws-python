"""PropertyTypes for AWS::IoTWireless::MulticastGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoRaWAN(PropertyType):
    dl_class: str | None = None
    rf_region: str | None = None
    number_of_devices_in_group: int | None = None
    number_of_devices_requested: int | None = None
