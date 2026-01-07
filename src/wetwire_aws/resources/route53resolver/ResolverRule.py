"""PropertyTypes for AWS::Route53Resolver::ResolverRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class TargetAddress(PropertyType):
    ip: DslValue[str] | None = None
    ipv6: DslValue[str] | None = None
    port: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    server_name_indication: DslValue[str] | None = None
