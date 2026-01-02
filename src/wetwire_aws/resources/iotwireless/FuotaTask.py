"""PropertyTypes for AWS::IoTWireless::FuotaTask."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoRaWAN(PropertyType):
    rf_region: str | None = None
    start_time: str | None = None
