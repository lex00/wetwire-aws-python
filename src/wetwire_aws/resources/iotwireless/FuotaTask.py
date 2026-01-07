"""PropertyTypes for AWS::IoTWireless::FuotaTask."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoRaWAN(PropertyType):
    rf_region: DslValue[str] | None = None
    start_time: DslValue[str] | None = None
