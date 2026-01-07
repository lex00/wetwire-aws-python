"""PropertyTypes for AWS::ApiGateway::DocumentationPart."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Location(PropertyType):
    method: DslValue[str] | None = None
    name: DslValue[str] | None = None
    path: DslValue[str] | None = None
    status_code: DslValue[str] | None = None
    type_: DslValue[str] | None = None
