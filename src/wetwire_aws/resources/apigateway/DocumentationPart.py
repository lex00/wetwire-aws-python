"""PropertyTypes for AWS::ApiGateway::DocumentationPart."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Location(PropertyType):
    method: str | None = None
    name: str | None = None
    path: str | None = None
    status_code: str | None = None
    type_: str | None = None
