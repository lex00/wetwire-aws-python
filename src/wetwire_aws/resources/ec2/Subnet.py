"""PropertyTypes for AWS::EC2::Subnet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BlockPublicAccessStates(PropertyType):
    internet_gateway_block_mode: str | None = None


@dataclass
class PrivateDnsNameOptionsOnLaunch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: bool | None = None
    enable_resource_name_dns_aaaa_record: bool | None = None
    hostname_type: str | None = None
