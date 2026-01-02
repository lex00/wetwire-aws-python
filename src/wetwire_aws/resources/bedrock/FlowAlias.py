"""PropertyTypes for AWS::Bedrock::FlowAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FlowAliasConcurrencyConfiguration(PropertyType):
    type_: str | None = None
    max_concurrency: float | None = None


@dataclass
class FlowAliasRoutingConfigurationListItem(PropertyType):
    flow_version: str | None = None
