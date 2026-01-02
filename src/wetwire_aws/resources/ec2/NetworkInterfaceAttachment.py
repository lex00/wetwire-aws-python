"""PropertyTypes for AWS::EC2::NetworkInterfaceAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EnaSrdSpecification(PropertyType):
    ena_srd_enabled: bool | None = None
    ena_srd_udp_specification: EnaSrdUdpSpecification | None = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    ena_srd_udp_enabled: bool | None = None
