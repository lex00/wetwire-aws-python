"""PropertyTypes for AWS::EC2::TransitGatewayMulticastDomain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Options(PropertyType):
    auto_accept_shared_associations: str | None = None
    igmpv2_support: str | None = None
    static_sources_support: str | None = None
