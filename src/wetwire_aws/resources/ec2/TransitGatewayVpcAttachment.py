"""PropertyTypes for AWS::EC2::TransitGatewayVpcAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Options(PropertyType):
    appliance_mode_support: DslValue[str] | None = None
    dns_support: DslValue[str] | None = None
    ipv6_support: DslValue[str] | None = None
    security_group_referencing_support: DslValue[str] | None = None
