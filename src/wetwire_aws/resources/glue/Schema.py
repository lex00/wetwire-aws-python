"""PropertyTypes for AWS::Glue::Schema."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Registry(PropertyType):
    arn: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class SchemaVersion(PropertyType):
    is_latest: DslValue[bool] | None = None
    version_number: DslValue[int] | None = None
