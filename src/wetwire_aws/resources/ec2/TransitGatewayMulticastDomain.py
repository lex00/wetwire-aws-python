"""PropertyTypes for AWS::EC2::TransitGatewayMulticastDomain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Options(PropertyType):
    auto_accept_shared_associations: DslValue[str] | None = None
    igmpv2_support: DslValue[str] | None = None
    static_sources_support: DslValue[str] | None = None
