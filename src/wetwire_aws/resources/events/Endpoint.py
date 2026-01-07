"""PropertyTypes for AWS::Events::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EndpointEventBus(PropertyType):
    event_bus_arn: DslValue[str] | None = None


@dataclass
class FailoverConfig(PropertyType):
    primary: DslValue[Primary] | None = None
    secondary: DslValue[Secondary] | None = None


@dataclass
class Primary(PropertyType):
    health_check: DslValue[str] | None = None


@dataclass
class ReplicationConfig(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class RoutingConfig(PropertyType):
    failover_config: DslValue[FailoverConfig] | None = None


@dataclass
class Secondary(PropertyType):
    route: DslValue[str] | None = None
