"""PropertyTypes for AWS::EC2::FlowLog."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DestinationOptions(PropertyType):
    file_format: str | None = None
    hive_compatible_partitions: bool | None = None
    per_hour_partition: bool | None = None
