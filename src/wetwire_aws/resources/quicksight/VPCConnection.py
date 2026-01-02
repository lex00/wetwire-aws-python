"""PropertyTypes for AWS::QuickSight::VPCConnection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NetworkInterface(PropertyType):
    availability_zone: str | None = None
    error_message: str | None = None
    network_interface_id: str | None = None
    status: str | None = None
    subnet_id: str | None = None
