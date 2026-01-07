"""PropertyTypes for AWS::EC2::NetworkInterfaceAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EnaSrdSpecification(PropertyType):
    ena_srd_enabled: DslValue[bool] | None = None
    ena_srd_udp_specification: DslValue[EnaSrdUdpSpecification] | None = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    ena_srd_udp_enabled: DslValue[bool] | None = None
