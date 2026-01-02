"""PropertyTypes for AWS::MemoryDB::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Endpoint(PropertyType):
    address: str | None = None
    port: int | None = None
