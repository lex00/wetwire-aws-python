"""PropertyTypes for AWS::Neptune::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DBClusterRole(PropertyType):
    role_arn: str | None = None
    feature_name: str | None = None


@dataclass
class ServerlessScalingConfiguration(PropertyType):
    max_capacity: float | None = None
    min_capacity: float | None = None
