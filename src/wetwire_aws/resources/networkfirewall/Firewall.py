"""PropertyTypes for AWS::NetworkFirewall::Firewall."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AvailabilityZoneMapping(PropertyType):
    availability_zone: DslValue[str] | None = None


@dataclass
class SubnetMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IPAddressType",
    }

    subnet_id: DslValue[str] | None = None
    ip_address_type: DslValue[str] | None = None
