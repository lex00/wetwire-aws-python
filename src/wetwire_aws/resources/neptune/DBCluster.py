"""PropertyTypes for AWS::Neptune::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DBClusterRole(PropertyType):
    role_arn: DslValue[str] | None = None
    feature_name: DslValue[str] | None = None


@dataclass
class ServerlessScalingConfiguration(PropertyType):
    max_capacity: DslValue[float] | None = None
    min_capacity: DslValue[float] | None = None
