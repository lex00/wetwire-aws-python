"""PropertyTypes for AWS::MemoryDB::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Endpoint(PropertyType):
    address: DslValue[str] | None = None
    port: DslValue[int] | None = None
