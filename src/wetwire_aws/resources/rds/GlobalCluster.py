"""PropertyTypes for AWS::RDS::GlobalCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GlobalEndpoint(PropertyType):
    address: DslValue[str] | None = None
