"""PropertyTypes for AWS::RDS::GlobalCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GlobalEndpoint(PropertyType):
    address: str | None = None
