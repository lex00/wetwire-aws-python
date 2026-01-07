"""PropertyTypes for AWS::RDS::DBProxyTargetGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionPoolConfigurationInfoFormat(PropertyType):
    connection_borrow_timeout: DslValue[int] | None = None
    init_query: DslValue[str] | None = None
    max_connections_percent: DslValue[int] | None = None
    max_idle_connections_percent: DslValue[int] | None = None
    session_pinning_filters: list[DslValue[str]] = field(default_factory=list)
