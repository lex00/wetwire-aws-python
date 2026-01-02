"""PropertyTypes for AWS::Glue::SchemaVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Schema(PropertyType):
    registry_name: str | None = None
    schema_arn: str | None = None
    schema_name: str | None = None
