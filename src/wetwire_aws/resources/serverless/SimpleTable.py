"""PropertyTypes for AWS::Serverless::SimpleTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PrimaryKey(PropertyType):
    name: str | None = None
    type_: str | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    read_capacity_units: int | None = None
    write_capacity_units: int | None = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
    }

    sse_enabled: bool | None = None
