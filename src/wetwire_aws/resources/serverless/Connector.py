"""PropertyTypes for AWS::Serverless::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectorDestination(PropertyType):
    arn: str | None = None
    id: str | None = None
    type_: str | None = None


@dataclass
class ConnectorSource(PropertyType):
    id: str | None = None
    arn: str | None = None
    role_name: str | None = None
    type_: str | None = None
