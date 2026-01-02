"""PropertyTypes for AWS::Events::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EndpointEventBus(PropertyType):
    event_bus_arn: str | None = None


@dataclass
class FailoverConfig(PropertyType):
    primary: Primary | None = None
    secondary: Secondary | None = None


@dataclass
class Primary(PropertyType):
    health_check: str | None = None


@dataclass
class ReplicationConfig(PropertyType):
    state: str | None = None


@dataclass
class RoutingConfig(PropertyType):
    failover_config: FailoverConfig | None = None


@dataclass
class Secondary(PropertyType):
    route: str | None = None
