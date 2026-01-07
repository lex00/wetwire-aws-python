"""PropertyTypes for AWS::Bedrock::FlowAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FlowAliasConcurrencyConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    max_concurrency: DslValue[float] | None = None


@dataclass
class FlowAliasRoutingConfigurationListItem(PropertyType):
    flow_version: DslValue[str] | None = None
