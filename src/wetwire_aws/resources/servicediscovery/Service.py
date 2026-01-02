"""PropertyTypes for AWS::ServiceDiscovery::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DnsConfig(PropertyType):
    dns_records: list[DnsRecord] = field(default_factory=list)
    namespace_id: str | None = None
    routing_policy: str | None = None


@dataclass
class DnsRecord(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ttl": "TTL",
    }

    ttl: float | None = None
    type_: str | None = None


@dataclass
class HealthCheckConfig(PropertyType):
    type_: str | None = None
    failure_threshold: float | None = None
    resource_path: str | None = None


@dataclass
class HealthCheckCustomConfig(PropertyType):
    failure_threshold: float | None = None
