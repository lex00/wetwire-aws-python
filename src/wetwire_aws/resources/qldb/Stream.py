"""PropertyTypes for AWS::QLDB::Stream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class KinesisConfiguration(PropertyType):
    aggregation_enabled: DslValue[bool] | None = None
    stream_arn: DslValue[str] | None = None
