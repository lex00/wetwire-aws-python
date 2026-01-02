"""PropertyTypes for AWS::IoTWireless::WirelessDeviceImportTask."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Sidewalk(PropertyType):
    device_creation_file: str | None = None
    device_creation_file_list: list[String] = field(default_factory=list)
    role: str | None = None
    sidewalk_manufacturing_sn: str | None = None
