"""PropertyTypes for AWS::Serverless::SimpleTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PrimaryKey(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    read_capacity_units: DslValue[int] | None = None
    write_capacity_units: DslValue[int] | None = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
    }

    sse_enabled: DslValue[bool] | None = None
