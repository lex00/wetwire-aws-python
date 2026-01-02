"""PropertyTypes for AWS::Route53Resolver::ResolverEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IpAddressRequest(PropertyType):
    subnet_id: str | None = None
    ip: str | None = None
    ipv6: str | None = None
