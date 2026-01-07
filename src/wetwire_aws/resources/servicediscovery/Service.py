"""PropertyTypes for AWS::ServiceDiscovery::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DnsConfig(PropertyType):
    dns_records: list[DslValue[DnsRecord]] = field(default_factory=list)
    namespace_id: DslValue[str] | None = None
    routing_policy: DslValue[str] | None = None


@dataclass
class DnsRecord(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ttl": "TTL",
    }

    ttl: DslValue[float] | None = None
    type_: DslValue[str] | None = None


@dataclass
class HealthCheckConfig(PropertyType):
    type_: DslValue[str] | None = None
    failure_threshold: DslValue[float] | None = None
    resource_path: DslValue[str] | None = None


@dataclass
class HealthCheckCustomConfig(PropertyType):
    failure_threshold: DslValue[float] | None = None
