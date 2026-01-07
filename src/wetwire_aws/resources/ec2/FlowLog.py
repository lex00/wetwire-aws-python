"""PropertyTypes for AWS::EC2::FlowLog."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationOptions(PropertyType):
    file_format: DslValue[str] | None = None
    hive_compatible_partitions: DslValue[bool] | None = None
    per_hour_partition: DslValue[bool] | None = None
