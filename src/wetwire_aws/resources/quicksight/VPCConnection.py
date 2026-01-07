"""PropertyTypes for AWS::QuickSight::VPCConnection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NetworkInterface(PropertyType):
    availability_zone: DslValue[str] | None = None
    error_message: DslValue[str] | None = None
    network_interface_id: DslValue[str] | None = None
    status: DslValue[str] | None = None
    subnet_id: DslValue[str] | None = None
