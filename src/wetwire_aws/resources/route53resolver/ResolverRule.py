"""PropertyTypes for AWS::Route53Resolver::ResolverRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TargetAddress(PropertyType):
    ip: str | None = None
    ipv6: str | None = None
    port: str | None = None
    protocol: str | None = None
    server_name_indication: str | None = None
