"""PropertyTypes for AWS::QLDB::Stream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class KinesisConfiguration(PropertyType):
    aggregation_enabled: bool | None = None
    stream_arn: str | None = None
