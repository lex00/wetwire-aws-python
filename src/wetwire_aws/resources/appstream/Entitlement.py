"""PropertyTypes for AWS::AppStream::Entitlement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Attribute(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
