"""PropertyTypes for AWS::Bedrock::AgentAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AgentAliasHistoryEvent(PropertyType):
    end_date: str | None = None
    routing_configuration: list[AgentAliasRoutingConfigurationListItem] = field(
        default_factory=list
    )
    start_date: str | None = None


@dataclass
class AgentAliasRoutingConfigurationListItem(PropertyType):
    agent_version: str | None = None
