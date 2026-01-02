"""PropertyTypes for AWS::EC2::TransitGatewayVpcAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Options(PropertyType):
    appliance_mode_support: str | None = None
    dns_support: str | None = None
    ipv6_support: str | None = None
    security_group_referencing_support: str | None = None
