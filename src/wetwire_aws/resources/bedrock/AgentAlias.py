"""PropertyTypes for AWS::Bedrock::AgentAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AgentAliasHistoryEvent(PropertyType):
    end_date: DslValue[str] | None = None
    routing_configuration: list[DslValue[AgentAliasRoutingConfigurationListItem]] = (
        field(default_factory=list)
    )
    start_date: DslValue[str] | None = None


@dataclass
class AgentAliasRoutingConfigurationListItem(PropertyType):
    agent_version: DslValue[str] | None = None
