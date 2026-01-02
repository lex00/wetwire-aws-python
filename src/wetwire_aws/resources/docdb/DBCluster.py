"""PropertyTypes for AWS::DocDB::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ServerlessV2ScalingConfiguration(PropertyType):
    max_capacity: float | None = None
    min_capacity: float | None = None
