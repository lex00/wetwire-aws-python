"""PropertyTypes for AWS::Glue::SchemaVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Schema(PropertyType):
    registry_name: DslValue[str] | None = None
    schema_arn: DslValue[str] | None = None
    schema_name: DslValue[str] | None = None
