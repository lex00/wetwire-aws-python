"""PropertyTypes for AWS::IoTWireless::WirelessDeviceImportTask."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Sidewalk(PropertyType):
    device_creation_file: DslValue[str] | None = None
    device_creation_file_list: list[DslValue[str]] = field(default_factory=list)
    role: DslValue[str] | None = None
    sidewalk_manufacturing_sn: DslValue[str] | None = None
