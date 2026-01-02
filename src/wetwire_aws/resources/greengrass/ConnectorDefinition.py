"""PropertyTypes for AWS::Greengrass::ConnectorDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Connector(PropertyType):
    connector_arn: str | None = None
    id: str | None = None
    parameters: dict[str, Any] | None = None


@dataclass
class ConnectorDefinitionVersion(PropertyType):
    connectors: list[Connector] = field(default_factory=list)
