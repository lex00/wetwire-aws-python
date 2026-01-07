"""PropertyTypes for AWS::Route53Resolver::ResolverEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IpAddressRequest(PropertyType):
    subnet_id: DslValue[str] | None = None
    ip: DslValue[str] | None = None
    ipv6: DslValue[str] | None = None
