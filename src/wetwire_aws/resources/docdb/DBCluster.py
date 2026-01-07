"""PropertyTypes for AWS::DocDB::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ServerlessV2ScalingConfiguration(PropertyType):
    max_capacity: DslValue[float] | None = None
    min_capacity: DslValue[float] | None = None
