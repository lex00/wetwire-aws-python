"""PropertyTypes for AWS::IoTWireless::NetworkAnalyzerConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TraceContent(PropertyType):
    log_level: str | None = None
    wireless_device_frame_info: str | None = None
