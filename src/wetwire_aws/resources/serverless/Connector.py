"""PropertyTypes for AWS::Serverless::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectorDestination(PropertyType):
    arn: DslValue[str] | None = None
    id: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ConnectorSource(PropertyType):
    id: DslValue[str] | None = None
    arn: DslValue[str] | None = None
    role_name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
