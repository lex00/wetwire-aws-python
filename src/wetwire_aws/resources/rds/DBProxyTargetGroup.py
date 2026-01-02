"""PropertyTypes for AWS::RDS::DBProxyTargetGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectionPoolConfigurationInfoFormat(PropertyType):
    connection_borrow_timeout: int | None = None
    init_query: str | None = None
    max_connections_percent: int | None = None
    max_idle_connections_percent: int | None = None
    session_pinning_filters: list[String] = field(default_factory=list)
