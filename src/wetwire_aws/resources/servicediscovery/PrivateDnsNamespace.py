"""PropertyTypes for AWS::ServiceDiscovery::PrivateDnsNamespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PrivateDnsPropertiesMutable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "soa": "SOA",
    }

    soa: SOA | None = None


@dataclass
class Properties(PropertyType):
    dns_properties: PrivateDnsPropertiesMutable | None = None


@dataclass
class SOA(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ttl": "TTL",
    }

    ttl: float | None = None
