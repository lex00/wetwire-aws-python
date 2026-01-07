"""PropertyTypes for AWS::ServiceDiscovery::PublicDnsNamespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Properties(PropertyType):
    dns_properties: DslValue[PublicDnsPropertiesMutable] | None = None


@dataclass
class PublicDnsPropertiesMutable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "soa": "SOA",
    }

    soa: DslValue[SOA] | None = None


@dataclass
class SOA(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ttl": "TTL",
    }

    ttl: DslValue[float] | None = None
